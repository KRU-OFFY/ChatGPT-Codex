#!/usr/bin/env python3
"""Inspect media files with ffprobe and emit a compact JSON report."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}
EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi", ".webm", ".m4v", ".mp3", ".wav", ".m4a", ".aac", ".flac"} | IMAGE_EXTENSIONS


def files_from(paths: list[str]) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            found.extend(p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in EXTENSIONS)
        elif path.is_file():
            found.append(path)
    return sorted(set(p.resolve() for p in found))


def probe(path: Path) -> dict:
    command = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size,format_name:stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels",
        "-of", "json", str(path),
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        return {"path": str(path), "ok": False, "error": result.stderr.strip()}
    data = json.loads(result.stdout)
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    audio = next((s for s in streams if s.get("codec_type") == "audio"), None)
    warnings: list[str] = []
    is_image = path.suffix.lower() in IMAGE_EXTENSIONS
    if video:
        width, height = int(video.get("width", 0)), int(video.get("height", 0))
        if height > width:
            warnings.append("portrait-image" if is_image else "portrait-video")
        if is_image:
            if width < 1920 or height < 1080:
                warnings.append("below-full-hd")
        elif width < 1280 or height < 720:
            warnings.append("below-720p")
    if video and not audio and not is_image:
        warnings.append("no-audio-stream")
    return {
        "path": str(path),
        "ok": True,
        "media_type": "image" if is_image else "video" if video else "audio" if audio else "unknown",
        "duration_seconds": None if is_image else round(float(data.get("format", {}).get("duration", 0)), 3),
        "size_bytes": int(data.get("format", {}).get("size", 0)),
        "video": video,
        "audio": audio,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Media files or directories")
    parser.add_argument("--output", help="Write JSON to this file")
    args = parser.parse_args()
    if not shutil.which("ffprobe"):
        print("ffprobe is not available on PATH", file=sys.stderr)
        return 2
    media = files_from(args.paths)
    report = {"file_count": len(media), "files": [probe(path) for path in media]}
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0 if media and all(item["ok"] for item in report["files"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
