#!/usr/bin/env python3
"""Render a rubric-led VTR project with FFmpeg."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from validate_project import validate


DEFAULT_STATE = Path(__file__).resolve().parent.parent / "references" / "project-state.json"


def update_dashboard(path: Path, status: str, progress: int, *, output: Path | None = None, error: str | None = None) -> None:
    """Update render state without making rendering depend on the dashboard UI."""
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    render = data.setdefault("render_state", {})
    previous = render.get("status")
    if status == "rendering" and previous not in {"rendering", "queued"}:
        render["attempt"] = int(render.get("attempt", 0)) + 1
        render["started_at"] = datetime.now().isoformat(timespec="seconds")
    render["status"] = status
    render["progress"] = max(0, min(100, int(progress)))
    if output is not None:
        render["output_file"] = str(output)
    if error is not None:
        render["error"] = error
    if status == "completed":
        render["finished_at"] = datetime.now().isoformat(timespec="seconds")
        render["error"] = None
    workflow = data.setdefault("workflow", {})
    row = workflow.setdefault("render", {"label": "Render วิดีโอ"})
    row["status"] = "in-progress" if status in {"queued", "rendering"} else status if status in {"completed", "failed"} else "pending"
    row["progress"] = render["progress"]
    row["note"] = {
        "queued": "อยู่ในคิว Render",
        "rendering": f"กำลัง Render ครั้งที่ {render.get('attempt', 0)}",
        "completed": f"Render สำเร็จ: {render.get('output_file') or '-'}",
        "failed": f"Render ไม่สำเร็จ: {render.get('error') or 'ไม่ทราบสาเหตุ'}",
    }.get(status, "ยังไม่เริ่ม")
    data["current_stage"] = "render"
    data["updated_at"] = datetime.now().date().isoformat()
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(command: list[str]) -> None:
    result = subprocess.run(command)
    if result.returncode:
        raise RuntimeError(f"Command failed with exit code {result.returncode}: {' '.join(command)}")


def has_audio(path: Path) -> bool:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=index", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    return result.returncode == 0 and bool(result.stdout.strip())


def esc_filter_path(path: Path) -> str:
    return str(path).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")


def logo_xy(position: str, margin: int) -> tuple[str, str]:
    return {
        "top-left": (str(margin), str(margin)),
        "top-right": (f"W-w-{margin}", str(margin)),
        "bottom-left": (str(margin), f"H-h-{margin}"),
        "bottom-right": (f"W-w-{margin}", f"H-h-{margin}"),
    }[position]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    parser.add_argument("--keep-work", action="store_true")
    parser.add_argument("--state", default=str(DEFAULT_STATE), help="Dashboard state JSON to update")
    args = parser.parse_args()
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        print("ffmpeg and ffprobe must be available on PATH", file=sys.stderr)
        return 2
    project_path = Path(args.project).resolve()
    errors, warnings, total = validate(project_path)
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    project = json.loads(project_path.read_text(encoding="utf-8"))
    base = project_path.parent
    output = Path(project["output"])
    output = output if output.is_absolute() else base / output
    output.parent.mkdir(parents=True, exist_ok=True)
    state_path = Path(args.state).resolve()
    width, height, fps = int(project.get("width", 1920)), int(project.get("height", 1080)), int(project.get("fps", 30))
    work_ctx = tempfile.TemporaryDirectory(prefix="school-vtr-")
    work = Path(work_ctx.name)
    try:
        update_dashboard(state_path, "rendering", 3, output=output)
        segments: list[Path] = []
        for index, clip in enumerate(project["clips"]):
            source = Path(clip["path"])
            source = source if source.is_absolute() else base / source
            duration = float(clip["duration"])
            video_filters = [
                f"scale={width}:{height}:force_original_aspect_ratio=decrease",
                f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black",
                "setsar=1",
                f"eq=brightness={clip.get('brightness', 0)}:contrast={clip.get('contrast', 1)}:saturation={clip.get('saturation', 1)}",
                f"fps={fps}", "format=yuv420p",
            ]
            fade_in, fade_out = float(clip.get("fade_in", 0)), float(clip.get("fade_out", 0))
            if fade_in:
                video_filters.append(f"fade=t=in:st=0:d={fade_in}")
            if fade_out:
                video_filters.append(f"fade=t=out:st={max(0, duration-fade_out)}:d={fade_out}")
            segment = work / f"segment-{index:04d}.mp4"
            command = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", str(clip.get("start", 0)), "-t", str(duration), "-i", str(source)]
            if has_audio(source):
                command += ["-map", "0:v:0", "-map", "0:a:0", "-vf", ",".join(video_filters), "-af", f"volume={clip.get('volume', 1)},aresample=48000,apad,atrim=0:{duration}"]
            else:
                command += ["-f", "lavfi", "-t", str(duration), "-i", "anullsrc=r=48000:cl=stereo", "-map", "0:v:0", "-map", "1:a:0", "-vf", ",".join(video_filters)]
            command += ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest", str(segment)]
            run(command)
            segments.append(segment)
            update_dashboard(state_path, "rendering", 5 + round(58 * (index + 1) / len(project["clips"])), output=output)
        concat_file = work / "concat.txt"
        concat_file.write_text("".join(f"file '{str(path).replace(chr(39), chr(39)+chr(92)+chr(39)+chr(39))}'\n" for path in segments), encoding="utf-8")
        joined = work / "joined.mp4"
        run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(concat_file), "-c", "copy", str(joined)])
        update_dashboard(state_path, "rendering", 70, output=output)

        inputs = ["-i", str(joined)]
        filter_parts: list[str] = []
        video_label = "0:v"
        next_input = 1
        logo = project.get("logo")
        if logo:
            logo_path = Path(logo["path"]); logo_path = logo_path if logo_path.is_absolute() else base / logo_path
            inputs += ["-i", str(logo_path)]
            filter_parts.append(f"[{next_input}:v]scale={int(logo.get('width', 150))}:-1[logo]")
            x, y = logo_xy(logo.get("position", "top-right"), int(logo.get("margin", 36)))
            filter_parts.append(f"[{video_label}][logo]overlay={x}:{y}[vlogo]")
            video_label = "vlogo"; next_input += 1
        subtitles = project.get("subtitles")
        if subtitles:
            subtitle_path = Path(subtitles); subtitle_path = subtitle_path if subtitle_path.is_absolute() else base / subtitle_path
            filter_parts.append(f"[{video_label}]subtitles='{esc_filter_path(subtitle_path)}'[vsub]")
            video_label = "vsub"

        audio_labels = ["[0:a]"]
        voice = project.get("voiceover")
        if voice:
            path = Path(voice["path"]); path = path if path.is_absolute() else base / path
            inputs += ["-i", str(path)]
            if project.get("music", {}).get("ducking", True):
                filter_parts.append(f"[{next_input}:a]volume={voice.get('volume', 1)},atrim=0:{total},apad,asplit=2[voice][voicesc]")
            else:
                filter_parts.append(f"[{next_input}:a]volume={voice.get('volume', 1)},atrim=0:{total},apad[voice]")
            audio_labels.append("[voice]"); next_input += 1
        music = project.get("music")
        if music:
            path = Path(music["path"]); path = path if path.is_absolute() else base / path
            inputs += ["-stream_loop", "-1", "-i", str(path)]
            filter_parts.append(f"[{next_input}:a]volume={music.get('volume', 0.16)},atrim=0:{total},afade=t=in:st=0:d=1,afade=t=out:st={max(0,total-2)}:d=2[music]")
            if voice and music.get("ducking", True):
                filter_parts.append("[music][voicesc]sidechaincompress=threshold=0.03:ratio=10:attack=20:release=500[ducked]")
                audio_labels.append("[ducked]")
            else:
                audio_labels.append("[music]")
            next_input += 1
        filter_parts.append("".join(audio_labels) + f"amix=inputs={len(audio_labels)}:duration=first:dropout_transition=2,alimiter=limit=0.95[aout]")
        command = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"] + inputs
        if filter_parts:
            command += ["-filter_complex", ";".join(filter_parts)]
        command += ["-map", f"[{video_label}]" if video_label != "0:v" else "0:v", "-map", "[aout]", "-t", str(total), "-c:v", "libx264", "-preset", "medium", "-b:v", project.get("video_bitrate", "8M"), "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", project.get("audio_bitrate", "192k"), "-movflags", "+faststart", str(output)]
        update_dashboard(state_path, "rendering", 82, output=output)
        run(command)
        update_dashboard(state_path, "completed", 100, output=output)
        print(f"OK: rendered {output} ({total:.3f}s planned)")
        if args.keep_work:
            saved = output.parent / f"{output.stem}-work"
            if saved.exists(): shutil.rmtree(saved)
            shutil.copytree(work, saved)
            print(f"Work files: {saved}")
        return 0
    except Exception as exc:
        try:
            update_dashboard(state_path, "failed", 0, output=output, error=str(exc))
        except (OSError, ValueError, json.JSONDecodeError):
            pass
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    finally:
        work_ctx.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
