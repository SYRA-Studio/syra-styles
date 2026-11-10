"""Makes each style's preview.mp4, the small sample the Styles grid plays (owner, 10 Nov 2026), from its sample.mp4.

  python -X utf8 previews.py <styles-folder> [--force] [--jobs N]

360p H.264, CRF 32, no audio, faststart, a keyframe every second so a looping tile restarts cleanly. sample.mp4 stays
as it is, for the large view.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def make(ffmpeg: str, folder: Path, force: bool) -> str:
    sample, preview = folder / "sample.mp4", folder / "preview.mp4"
    if not sample.exists():
        return f"[skip] {folder.name}: no sample.mp4"
    if preview.exists() and not force:
        return f"[kept] {folder.name}"
    part = folder / "preview.part.mp4"
    subprocess.run(
        [ffmpeg, "-y", "-v", "error", "-i", str(sample), "-vf", "scale=-2:360", "-c:v", "libx264", "-preset", "medium",
         "-crf", "32", "-g", "30", "-pix_fmt", "yuv420p", "-an", "-movflags", "+faststart", "-threads", "2", str(part)],
        check=True,
    )
    part.replace(preview)
    return f"[done] {folder.name}: {preview.stat().st_size // 1024} KB"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("styles")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--jobs", type=int, default=3)
    a = ap.parse_args()
    ffmpeg = shutil.which("ffmpeg") or sys.exit("ffmpeg not found")
    folders = sorted(p for p in Path(a.styles).iterdir() if p.is_dir())
    with ThreadPoolExecutor(max_workers=a.jobs) as pool:
        for line in pool.map(lambda f: make(ffmpeg, f, a.force), folders):
            print(line, flush=True)


if __name__ == "__main__":
    main()
