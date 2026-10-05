#!/usr/bin/env python3
"""Show and update the persistent VTR production dashboard."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

DEFAULT_STATE = Path(__file__).resolve().parent.parent / "references" / "project-state.json"
WORKFLOW_STATUSES = {"missing", "blocked", "needs-review", "pending", "ready", "in-progress", "completed", "failed", "not-applicable"}
RENDER_STATUSES = {"not-started", "queued", "rendering", "completed", "failed"}
STATUS_LABELS = {
    "missing": "⛔ ขาดข้อมูล", "blocked": "⛔ ติดขัด", "needs-review": "⚠️ ต้องตรวจ/ปรับปรุง",
    "pending": "⏳ รอดำเนินการ", "ready": "🟦 พร้อม", "in-progress": "🔄 กำลังดำเนินการ",
    "completed": "✅ เสร็จแล้ว", "failed": "❌ ไม่สำเร็จ", "not-applicable": "➖ ไม่เกี่ยวข้อง",
    "not-started": "⏳ ยังไม่เริ่ม", "queued": "🕒 รอ Render", "rendering": "🔄 กำลัง Render",
}
SEVERITY_LABELS = {"critical": "⛔ สำคัญ", "warning": "⚠️ ต้องปรับปรุง", "info": "ℹ️ ข้อมูล"}


def load(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("workflow"), dict) or not isinstance(data.get("render_state"), dict):
        raise ValueError("project-state.json is missing workflow or render_state")
    return data


def save(path: Path, data: dict) -> None:
    data["updated_at"] = str(date.today())
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def overall_progress(data: dict) -> int:
    rows = [row for row in data["workflow"].values() if row.get("status") != "not-applicable"]
    return round(sum(int(row.get("progress", 0)) for row in rows) / len(rows)) if rows else 0


def progress_bar(value: int, width: int = 20) -> str:
    filled = round(width * max(0, min(100, value)) / 100)
    return "█" * filled + "░" * (width - filled)


def dashboard(data: dict) -> str:
    progress = overall_progress(data)
    lines = [
        f"# Dashboard — {data.get('project_name', 'VTR Project')}", "",
        f"**ความคืบหน้ารวม:** `{progress_bar(progress)}` **{progress}%**  ",
        f"**ขั้นปัจจุบัน:** `{data.get('current_stage', '-')}`  ",
        f"**อัปเดต:** `{data.get('updated_at', '-')}`", "",
        "## สถานะการผลิต", "",
        "| งาน | สถานะ | ความคืบหน้า | หมายเหตุ |", "|---|---|---:|---|",
    ]
    for row in data["workflow"].values():
        status = row.get("status", "pending")
        lines.append(f"| {row.get('label', '-')} | {STATUS_LABELS.get(status, status)} | {row.get('progress', 0)}% | {row.get('note', '')} |")
    open_issues = [issue for issue in data.get("issues", []) if issue.get("status") == "open"]
    lines += ["", "## ข้อมูลขาด/ไม่สอดคล้อง", ""]
    if open_issues:
        for issue in sorted(open_issues, key=lambda item: {"critical": 0, "warning": 1, "info": 2}.get(item.get("severity"), 3)):
            lines.append(f"- {SEVERITY_LABELS.get(issue.get('severity'), '•')} **{issue.get('message')}** — {issue.get('required_action')}")
    else:
        lines.append("- ไม่มีประเด็นเปิด")
    render = data["render_state"]
    rstatus = render.get("status", "not-started")
    lines += [
        "", "## Render", "",
        f"- สถานะ: **{STATUS_LABELS.get(rstatus, rstatus)}**",
        f"- ความคืบหน้า: **{render.get('progress', 0)}%**",
        f"- ครั้งที่: **{render.get('attempt', 0)}**",
        f"- ไฟล์: `{render.get('output_file') or '-'}`",
    ]
    if render.get("error"):
        lines.append(f"- ข้อผิดพลาด: `{render['error']}`")
    lines += ["", "## ขั้นตอนถัดไปอัตโนมัติ", "", data.get("next_automatic_action", "-")]
    return "\n".join(lines) + "\n"


def show(args: argparse.Namespace) -> int:
    payload = dashboard(load(Path(args.state).resolve()))
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
        print(f"OK: wrote {args.output}")
    else:
        print(payload, end="")
    return 0


def set_stage(args: argparse.Namespace) -> int:
    if args.status not in WORKFLOW_STATUSES or not 0 <= args.progress <= 100:
        raise ValueError("Invalid workflow status or progress")
    path = Path(args.state).resolve(); data = load(path)
    if args.section not in data["workflow"]:
        raise ValueError(f"Unknown workflow section: {args.section}")
    row = data["workflow"][args.section]
    row["status"] = args.status; row["progress"] = args.progress
    if args.note is not None: row["note"] = args.note
    data["current_stage"] = args.section
    save(path, data)
    print(f"OK: {args.section} = {args.status} ({args.progress}%)")
    return 0


def set_render(args: argparse.Namespace) -> int:
    if args.status not in RENDER_STATUSES or not 0 <= args.progress <= 100:
        raise ValueError("Invalid render status or progress")
    path = Path(args.state).resolve(); data = load(path); render = data["render_state"]
    if args.status == "rendering" and render.get("status") != "rendering":
        render["attempt"] = int(render.get("attempt", 0)) + 1
        render["started_at"] = datetime.now().isoformat(timespec="seconds")
    render["status"] = args.status; render["progress"] = args.progress
    if args.output_file is not None: render["output_file"] = args.output_file
    if args.error is not None: render["error"] = args.error
    if args.status == "completed":
        render["finished_at"] = datetime.now().isoformat(timespec="seconds"); render["error"] = None
    render_row = data["workflow"]["render"]
    render_row["status"] = "in-progress" if args.status in {"queued", "rendering"} else args.status if args.status in {"completed", "failed"} else "pending"
    render_row["progress"] = args.progress
    render_row["note"] = {
        "not-started": "ยังไม่เริ่ม",
        "queued": "อยู่ในคิว Render",
        "rendering": f"กำลัง Render ครั้งที่ {render.get('attempt', 0)}",
        "completed": f"Render สำเร็จ: {render.get('output_file') or '-'}",
        "failed": f"Render ไม่สำเร็จ: {render.get('error') or 'ไม่ทราบสาเหตุ'}",
    }[args.status]
    data["current_stage"] = "render"
    save(path, data)
    print(f"OK: render = {args.status} ({args.progress}%)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", default=str(DEFAULT_STATE))
    sub = parser.add_subparsers(dest="command", required=True)
    show_cmd = sub.add_parser("show"); show_cmd.add_argument("--output"); show_cmd.set_defaults(func=show)
    stage_cmd = sub.add_parser("set")
    stage_cmd.add_argument("section"); stage_cmd.add_argument("status"); stage_cmd.add_argument("--progress", type=int, default=0); stage_cmd.add_argument("--note"); stage_cmd.set_defaults(func=set_stage)
    render_cmd = sub.add_parser("render")
    render_cmd.add_argument("status"); render_cmd.add_argument("--progress", type=int, default=0); render_cmd.add_argument("--output-file"); render_cmd.add_argument("--error"); render_cmd.set_defaults(func=set_render)
    args = parser.parse_args()
    try:
        return args.func(args)
    except (ValueError, json.JSONDecodeError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr); return 1


if __name__ == "__main__":
    raise SystemExit(main())
