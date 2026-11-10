"""Converts the owner's "Motion Landscape" style library (a zip) into SYRA's library format (PLAN 6).

  python -X utf8 convert.py <zip> <out-styles-folder> [--only NN] [--no-video] [--jobs N]

Reads the zip only; never writes to it. For each "NN Name/" folder it writes <out>/<id>/:
  DESIGN.md      the info card from "X Tags.txt", then "X Style.md" with its file links pointing at the new names
  sample.mp4     "X Video.mp4" re-encoded: 720p H.264, CRF 30, no audio, faststart (owner, 10 Nov 2026)
  thumbnail.jpg  from "X 00 Cover.jpg", 640 wide
  source/index.html  "X HTML.html", unchanged
  CREDITS.txt    when the folder has one (image licences)
The component images, the prompt, the .ico and desktop.ini are left out (owner, 10 Nov 2026).
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = "Motion Landscape/"

# kind and family for each style, by number (building-blocks.md's families). "primitive" when the style is one building
# block from that list; "mix" when it combines several. A judgment, listed in the report for the owner to change.
CLASSIFY: dict[str, tuple[str, str]] = {
    "01": ("mix", "Data and diagrams"), "02": ("mix", "Screen and digital"), "03": ("mix", "Motion-led"),
    "04": ("mix", "Type-led"), "05": ("mix", "Type-led"), "06": ("mix", "Type-led"),
    "07": ("mix", "Paper and craft"), "08": ("mix", "Depth and 3D"), "09": ("mix", "Depth and 3D"),
    "10": ("mix", "Flat and graphic"), "11": ("primitive", "Flat and graphic"), "12": ("primitive", "Print and texture"),
    "13": ("mix", "Screen and digital"), "14": ("primitive", "Line and hand-drawn"), "15": ("mix", "Depth and 3D"),
    "16": ("primitive", "Screen and digital"), "17": ("primitive", "Print and texture"), "18": ("mix", "Type-led"),
    "19": ("primitive", "Line and hand-drawn"), "20": ("primitive", "Screen and digital"), "21": ("primitive", "Paper and craft"),
    "22": ("mix", "Depth and 3D"), "23": ("primitive", "Depth and 3D"), "24": ("mix", "Depth and 3D"),
    "25": ("mix", "Screen and digital"), "26": ("primitive", "Flat and graphic"), "27": ("primitive", "Print and texture"),
    "28": ("primitive", "Line and hand-drawn"), "29": ("mix", "Data and diagrams"), "30": ("mix", "Screen and digital"),
    "31": ("mix", "Depth and 3D"), "32": ("mix", "Depth and 3D"), "33": ("primitive", "Paper and craft"),
    "34": ("mix", "Data and diagrams"), "35": ("mix", "Flat and graphic"), "36": ("mix", "Data and diagrams"),
    "37": ("mix", "Depth and 3D"), "38": ("mix", "Flat and graphic"), "39": ("mix", "Depth and 3D"),
    "40": ("mix", "Flat and graphic"), "41": ("mix", "Flat and graphic"), "42": ("mix", "Print and texture"),
    "43": ("mix", "Print and texture"), "44": ("mix", "Paper and craft"), "45": ("mix", "Paper and craft"),
    "46": ("mix", "Paper and craft"), "47": ("mix", "Paper and craft"), "48": ("mix", "Line and hand-drawn"),
    "49": ("mix", "Paper and craft"), "50": ("primitive", "Paper and craft"), "51": ("mix", "Print and texture"),
    "52": ("mix", "Line and hand-drawn"), "53": ("mix", "Flat and graphic"), "54": ("mix", "Depth and 3D"),
    "55": ("primitive", "Motion-led"), "56": ("mix", "Flat and graphic"), "57": ("mix", "Depth and 3D"),
    "58": ("mix", "Type-led"), "59": ("mix", "Depth and 3D"), "60": ("mix", "Paper and craft"),
    "61": ("mix", "Type-led"), "62": ("mix", "Paper and craft"), "63": ("mix", "Depth and 3D"), "64": ("mix", "Depth and 3D"),
}

# Ids that would clash with a style already in the library get the style's own longer name.
TAKEN = {"isometric", "paper-cut", "one-line", "flat-vector", "blueprint", "kinetic-type", "pixel-art", "glass-panels",
         "data-charts", "neon-glow", "shape-morphing"}

# Embedded pictures above this many bytes mean the look depends on images, not code alone. Nearly every style embeds one
# shared picture of about 200-260 KB, so the line sits well above that; between 380 and 510 KB are small textures.
IMAGE_BYTES = 600_000

SAFE_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def slug(text: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower().replace("&", " and "))).strip("-")


def field(tags: str, label: str) -> str:
    m = re.search(rf"^{re.escape(label)}\s*(.*?)\s*$", tags, re.M)
    if not m:
        # A label after a run of spaces on a line that starts with its Arabic twin ("المزاج: …        Mood: …").
        m = re.search(rf"\s{{2,}}{re.escape(label)}\s*(.*?)\s*$", tags, re.M)
    return m.group(1).strip() if m else ""


def words(text: str) -> list[str]:
    """A list for the info card: split on English and Arabic commas, nothing that would end the list."""
    parts = re.split(r"[,،]", text)
    return [re.sub(r"[\[\]#]", "", p).strip() for p in parts if re.sub(r"[\[\]#]", "", p).strip()]


def hashtags(line: str) -> list[str]:
    return [t.replace("_", " ") for t in re.findall(r"#([^\s#]+)", line)]


def one_line(text: str) -> str:
    """An info-card value stays on one line, and never looks like an end-of-line comment ("  #")."""
    return re.sub(r"\s+", " ", text).replace(" #", " ").strip()


def embedded_image_bytes(html: str) -> int:
    return sum(len(m) for m in re.findall(r"data:image/(?:png|jpe?g|webp|gif|avif);base64,([A-Za-z0-9+/=]+)", html)) * 3 // 4


def rewrite_body(style: str, prefix: str) -> tuple[str, dict[str, int]]:
    """The owner's text, unchanged in substance; only its links to the folder's files follow the new names."""
    counts: dict[str, int] = {}
    p = re.escape(prefix)

    def sub(pattern: str, repl: str, text: str, key: str, flags: int = 0) -> str:
        new, n = re.subn(pattern, repl, text, flags=flags)
        counts[key] = counts.get(key, 0) + n
        return new

    s = style
    # The cover picture → the thumbnail.
    s = sub(rf"!\[([^\]]*)\]\(<{p} Images/{p} 00 Cover\.jpg>\)", r"![\1](thumbnail.jpg)", s, "cover")
    # The components table: its preview pictures are gone, so its Preview column goes too.
    s = sub(r"^\| # \| Component \| Preview \|\s*$", "| # | Component |", s, "table head", re.M)
    s = sub(r"^\|---\|---\|---\|\s*$", "|---|---|", s, "table rule", re.M)
    s = sub(rf"^(\| [^|\n]* \| [^|\n]* )\| !\[[^\]]*\]\(<{p} Images/[^>]*>\) \|\s*$", r"\1|", s, "component rows", re.M)
    # The files table: rows for what isn't kept go, the others point at the new names.
    s = sub(rf"^\| \[{p} Prompt\.txt\]\(<{p} Prompt\.txt>\) \|.*\n", "", s, "prompt row", re.M)
    s = sub(rf"^\| \[{p} Images\]\(<{p} Images>\) \|.*\n", "", s, "images row", re.M)
    s = sub(rf"^\| \[{p} Tags\.txt\]\(<{p} Tags\.txt>\) \|.*\n",
            "| The info card at the top of this file | Tags & hashtags: what the style expresses, what it suits, search words |\n",
            s, "tags row", re.M)
    s = sub(rf"\[{p} HTML\.html\]\(<{p} HTML\.html>\)", "[source/index.html](source/index.html)", s, "html link")
    s = sub(rf"\[{p} Video\.mp4\]\(<{p} Video\.mp4>\)", "[sample.mp4](sample.mp4)", s, "video link")
    # The same names in running text.
    s = sub(rf"{p} HTML\.html", "source/index.html", s, "html name")
    s = sub(rf"{p} Video\.mp4", "sample.mp4", s, "video name")
    # The component pictures are gone (owner, 10 Nov 2026): the sentences that send the reader to them go too, so the agent
    # isn't sent looking for files that don't exist.
    s = sub(rf"[،,]?\s*والصور في (?:نفس )?فولدر {p} Images", "", s, "arabic images sentence")
    s = sub(rf"\s*(?:,\s*)?and (?:the )?(?:frames|images|pictures) in \"{p} Images\\?\"", "", s, "english images phrase")
    counts["left: prompt mentions"] = len(re.findall(rf"{p} Prompt", s))
    counts["left: images mentions"] = len(re.findall(rf"{p} Images", s))
    return s, counts


def encode(ffmpeg: str, src: Path, out: Path) -> None:
    subprocess.run(
        [ffmpeg, "-y", "-v", "error", "-i", str(src), "-vf", "scale=-2:720", "-c:v", "libx264", "-preset", "medium",
         "-crf", "30", "-pix_fmt", "yuv420p", "-an", "-movflags", "+faststart", "-threads", "4", str(out)],
        check=True,
    )


def thumbnail(ffmpeg: str, src: Path, out: Path) -> None:
    subprocess.run([ffmpeg, "-y", "-v", "error", "-i", str(src), "-vf", "scale=640:-2", "-q:v", "3", str(out)], check=True)


def convert_one(z: zipfile.ZipFile, folder: str, out_root: Path, ffmpeg: str, video: bool, tmp: Path) -> dict:
    number = folder.split(" ", 1)[0]
    entries = [n for n in z.namelist() if n.startswith(f"{ROOT}{folder}/")]
    top = [n for n in entries if n.count("/") == 2]
    tags_file = next(n for n in top if n.endswith(" Tags.txt"))
    prefix = tags_file.rsplit("/", 1)[1][: -len(" Tags.txt")]
    tags = z.read(tags_file).decode("utf-8")
    style = z.read(next(n for n in top if n.endswith(" Style.md"))).decode("utf-8")
    html_name = next(n for n in top if n.endswith(" HTML.html"))
    html = z.read(html_name)

    first = tags.splitlines()[0]
    m = re.match(r"^\S+:\s*(.*?)\s+—\s+(.*?)\s+·\s+Style\s+\d+", first)
    if not m:
        raise ValueError(f"{folder}: can't read the name from {first!r}")
    arabic_name, name = m.group(1).strip(), m.group(2).strip()
    folder_name = folder.split(" ", 1)[1]
    sid = slug(folder_name)
    if sid in TAKEN:
        sid = slug(name)
    if not SAFE_ID.match(sid) or sid in TAKEN:
        raise ValueError(f"{folder}: no usable id ({sid})")

    kind, family = CLASSIFY[number]
    photos = field(tags, "Real photos:")
    images = embedded_image_bytes(html.decode("utf-8", "replace"))
    made_with = "needs-images" if photos.lower().startswith("yes") or images > IMAGE_BYTES else "code"
    english = [t for t in hashtags(field(tags, "#English:"))]
    search = [arabic_name] + hashtags(field(tags, "#عربي:")) + words(field(tags, "كلمات بحث:"))
    search = list(dict.fromkeys(w for w in search if w))

    card = [
        "---",
        f"id: {sid}",
        f"name: {one_line(name)}",
        f"kind: {kind}",
        f"family: {family}",
        f"tags: [{', '.join(english)}]",
        f"search: [{', '.join(one_line(w) for w in search)}]",
        f"look: {one_line(field(tags, 'In one line:'))}",
        f"suits: {one_line(field(tags, 'Best for:'))}",
        f"made_with: {made_with}",
        "mixes: []",
        f"source: Motion Landscape, style {number} ({folder_name})",
        "---",
        "",
    ]
    body, counts = rewrite_body(style, prefix)

    out = out_root / sid
    (out / "source").mkdir(parents=True, exist_ok=True)
    (out / "DESIGN.md").write_text("\n".join(card) + body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    (out / "source" / "index.html").write_bytes(html)
    credits = next((n for n in top if n.endswith("CREDITS.txt")), None)
    if credits:
        (out / "CREDITS.txt").write_bytes(z.read(credits))
    cover = next(n for n in entries if re.search(r" 00 Cover\.jpg$", n))
    work = tmp / sid
    work.mkdir(parents=True, exist_ok=True)
    cover_tmp = work / "cover.jpg"
    cover_tmp.write_bytes(z.read(cover))
    thumbnail(ffmpeg, cover_tmp, out / "thumbnail.jpg")
    if video:
        video_name = next(n for n in top if n.endswith(" Video.mp4"))
        raw = work / "video.mp4"
        with z.open(video_name) as src, open(raw, "wb") as dst:
            shutil.copyfileobj(src, dst, 1 << 20)
        encode(ffmpeg, raw, out / "sample.mp4")
    shutil.rmtree(work, ignore_errors=True)
    return {"number": number, "folder": folder, "id": sid, "name": name, "kind": kind, "family": family,
            "made_with": made_with, "photos": photos, "embedded_image_kb": images // 1024, "credits": bool(credits),
            "links": counts, "tags": len(english), "search": len(search)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("zip")
    ap.add_argument("out")
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--no-video", action="store_true")
    ap.add_argument("--jobs", type=int, default=2)
    a = ap.parse_args()
    ffmpeg = shutil.which("ffmpeg") or sys.exit("ffmpeg not found")
    out_root = Path(a.out)
    out_root.mkdir(parents=True, exist_ok=True)
    z = zipfile.ZipFile(a.zip)
    folders = sorted({n.split("/")[1] for n in z.namelist() if n.startswith(ROOT) and n.count("/") >= 2})
    if a.only:
        folders = [f for f in folders if f.split(" ", 1)[0] in a.only]
    tmp = Path(tempfile.mkdtemp(prefix="convert-", dir=out_root.parent))
    results: list[dict] = []

    def run(folder: str) -> dict:
        # Each worker reads the zip through its own handle.
        with zipfile.ZipFile(a.zip) as own:
            r = convert_one(own, folder, out_root, ffmpeg, not a.no_video, tmp)
        print(f"[done] {folder} -> {r['id']}", flush=True)
        return r

    with ThreadPoolExecutor(max_workers=a.jobs) as pool:
        for r in pool.map(run, folders):
            results.append(r)
    shutil.rmtree(tmp, ignore_errors=True)
    (out_root.parent / "conversion.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"converted {len(results)}")


if __name__ == "__main__":
    main()
