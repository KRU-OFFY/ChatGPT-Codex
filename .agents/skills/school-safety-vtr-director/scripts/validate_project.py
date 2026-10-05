#!/usr/bin/env python3
"""Validate a school-safety VTR project JSON before rendering."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def resolve(base: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else base / path


def validate(project_path: Path) -> tuple[list[str], list[str], float]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        project = json.loads(project_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Cannot read project JSON: {exc}"], [], 0
    base = project_path.parent
    clips = project.get("clips")
    if not isinstance(clips, list) or not clips:
        errors.append("clips must be a non-empty array")
        clips = []
    total = 0.0
    for index, clip in enumerate(clips):
        label = f"clips[{index}]"
        if not isinstance(clip, dict):
            errors.append(f"{label} must be an object")
            continue
        if not clip.get("path"):
            errors.append(f"{label}.path is required")
        elif not resolve(base, clip["path"]).is_file():
            errors.append(f"{label}.path does not exist: {clip['path']}")
        duration = clip.get("duration")
        if not isinstance(duration, (int, float)) or duration <= 0:
            errors.append(f"{label}.duration must be greater than zero")
        else:
            total += float(duration)
        for key, low, high, default in (
            ("brightness", -1, 1, 0), ("contrast", 0, 2, 1),
            ("saturation", 0, 3, 1), ("volume", 0, 4, 1),
        ):
            value = clip.get(key, default)
            if not isinstance(value, (int, float)) or not low <= value <= high:
                errors.append(f"{label}.{key} must be between {low} and {high}")
        for key in ("start", "fade_in", "fade_out"):
            value = clip.get(key, 0)
            if not isinstance(value, (int, float)) or value < 0:
                errors.append(f"{label}.{key} must be non-negative")
        if isinstance(duration, (int, float)) and clip.get("fade_in", 0) + clip.get("fade_out", 0) > duration:
            errors.append(f"{label} fade durations exceed clip duration")
    max_duration = project.get("max_duration_seconds", 290)
    if not isinstance(max_duration, (int, float)) or not 1 <= max_duration <= 300:
        errors.append("max_duration_seconds must be between 1 and 300")
    elif total > max_duration + 0.001:
        errors.append(f"planned duration {total:.3f}s exceeds maximum {max_duration:.3f}s")
    elif total > max_duration - 5:
        warnings.append("planned duration has less than five seconds of safety margin")
    if not project.get("output"):
        errors.append("output is required")
    for field in ("subtitles",):
        if project.get(field) and not resolve(base, project[field]).is_file():
            errors.append(f"{field} does not exist: {project[field]}")
    for field in ("logo", "voiceover", "music"):
        value = project.get(field)
        if value:
            if not isinstance(value, dict) or not value.get("path"):
                errors.append(f"{field}.path is required")
            elif not resolve(base, value["path"]).is_file():
                errors.append(f"{field}.path does not exist: {value['path']}")
    if project.get("logo", {}).get("position", "top-right") not in {"top-left", "top-right", "bottom-left", "bottom-right"}:
        errors.append("logo.position is invalid")
    return errors, warnings, total


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    args = parser.parse_args()
    errors, warnings, total = validate(Path(args.project).resolve())
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"OK: project is valid; planned duration {total:.3f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

