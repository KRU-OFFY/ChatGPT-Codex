#!/usr/bin/env python3
"""Build a self-contained dashboard snapshot without claiming a live connection."""

from __future__ import annotations

import argparse
import base64
import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATE = ROOT / "assets" / "vtr-dashboard.html"
DEFAULT_STATE = ROOT / "references" / "project-state.json"
DEFAULT_LOGO = ROOT / "assets" / "school-logo.png"


def build(template: Path, state_path: Path, logo_path: Path, output: Path) -> None:
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if not isinstance(state.get("workflow"), dict) or not isinstance(state.get("render_state"), dict):
        raise ValueError("State file is missing workflow or render_state")

    html = template.read_text(encoding="utf-8")
    state_json = json.dumps(state, ensure_ascii=False, separators=(",", ":"))
    html, replacements = re.subn(
        r"/\*__STATE_START__\*/.*?/\*__STATE_END__\*/",
        f"/*__STATE_START__*/{state_json}/*__STATE_END__*/",
        html,
        count=1,
        flags=re.DOTALL,
    )
    if replacements != 1:
        raise ValueError("Could not replace embedded dashboard state")

    mime = "image/png" if logo_path.suffix.lower() == ".png" else "image/jpeg"
    logo_data = base64.b64encode(logo_path.read_bytes()).decode("ascii")
    html, replacements = re.subn(
        r'src="school-logo\.(?:png|jpe?g)"',
        f'src="data:{mime};base64,{logo_data}"',
        html,
        count=1,
    )
    if replacements != 1:
        raise ValueError("Could not embed school logo")

    built_at = datetime.now().astimezone().isoformat(timespec="seconds")
    html = html.replace("<body>", f'<body data-built-at="{built_at}">', 1)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE))
    parser.add_argument("--state", default=str(DEFAULT_STATE))
    parser.add_argument("--logo", default=str(DEFAULT_LOGO))
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    build(Path(args.template), Path(args.state), Path(args.logo), Path(args.output))
    print(f"OK: wrote standalone dashboard to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
