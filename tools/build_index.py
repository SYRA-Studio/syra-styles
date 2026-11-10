"""Writes index.json: the list SYRA Studio reads to find the styles in this repo and their files.

  python -X utf8 tools/build_index.py

For each style folder in styles/ (except those held back in held.txt): its id and every file's path, size and sha256.
SYRA Studio downloads DESIGN.md, thumbnail.jpg, preview.mp4 and CREDITS.txt in the background, and the rest (the full
sample and the source) when someone opens the style. A file whose sha256 changes is downloaded again.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    held = {line.strip() for line in (ROOT / "held.txt").read_text(encoding="utf-8").splitlines() if line.strip()}
    styles = []
    for folder in sorted(p for p in (ROOT / "styles").iterdir() if p.is_dir() and p.name not in held):
        if not (folder / "DESIGN.md").exists():
            raise SystemExit(f"{folder.name} has no DESIGN.md")
        files = {}
        for f in sorted(p for p in folder.rglob("*") if p.is_file() and not p.name.endswith(".part.mp4")):
            files[f.relative_to(folder).as_posix()] = {"size": f.stat().st_size, "sha256": sha256(f)}
        styles.append({"id": folder.name, "files": files})
    index = {"format": 1, "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "styles": styles}
    (ROOT / "index.json").write_text(json.dumps(index, indent=1) + "\n", encoding="utf-8", newline="\n")
    size = sum(f["size"] for s in styles for f in s["files"].values())
    print(f"index.json: {len(styles)} styles, {len(held)} held back, {size / 1e6:.0f} MB")


if __name__ == "__main__":
    main()
