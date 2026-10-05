#!/usr/bin/env python3
"""Maintain a canonical, deduplicated VTR source registry."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

DEFAULT_REGISTRY = Path(__file__).resolve().parent.parent / "references" / "source-registry.json"
VALID_CATEGORIES = {
    "official-guidance", "assessment-rubric", "example-vtr", "editing-tutorial",
    "motion-graphics-reference", "audio-reference", "music-or-sfx",
    "school-evidence", "other",
}
VALID_STATUS = {"verified", "pending-verification", "unavailable"}


def youtube_id(url: str) -> str | None:
    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")
    if host == "youtu.be":
        candidate = parsed.path.strip("/").split("/")[0]
    elif host in {"youtube.com", "m.youtube.com"}:
        if parsed.path == "/watch":
            candidate = parse_qs(parsed.query).get("v", [""])[0]
        elif parsed.path.startswith(("/shorts/", "/embed/")):
            candidate = parsed.path.strip("/").split("/")[1]
        else:
            candidate = ""
    else:
        return None
    return candidate if re.fullmatch(r"[A-Za-z0-9_-]{6,20}", candidate or "") else None


def canonicalize(url: str) -> tuple[str, str]:
    url = url.strip()
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"Invalid HTTP(S) URL: {url}")
    video_id = youtube_id(url)
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}", f"youtube-{video_id}"
    tracking = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "fbclid", "gclid"}
    query = [(k, v) for k, values in parse_qs(parsed.query, keep_blank_values=True).items() for v in values if k not in tracking]
    clean = urlunparse((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path or "/", "", urlencode(query), ""))
    return clean, "web-" + __import__("hashlib").sha256(clean.encode()).hexdigest()[:12]


def load_registry(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "updated_at": str(date.today()), "sources": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("sources"), list):
        raise ValueError("Registry must contain a sources array")
    return data


def save_registry(path: Path, data: dict) -> None:
    data["updated_at"] = str(date.today())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def add_source(args: argparse.Namespace) -> int:
    if args.category not in VALID_CATEGORIES or args.status not in VALID_STATUS:
        raise ValueError("Invalid category or status")
    path = Path(args.registry).resolve()
    data = load_registry(path)
    canonical, source_id = canonicalize(args.url)
    existing = next((item for item in data["sources"] if item.get("id") == source_id or item.get("url") == canonical), None)
    if existing:
        changed = False
        if args.selected_by_user and not existing.get("selected_by_user"):
            existing["selected_by_user"] = True
            existing["priority"] = "user-primary"
            changed = True
        if args.title and (existing.get("status") == "pending-verification" or existing.get("title", "").startswith("รอตรวจสอบ")):
            existing["title"] = args.title
            existing["status"] = args.status
            existing["checked_at"] = args.checked_at
            changed = True
        if changed:
            save_registry(path, data)
            print(f"UPDATED {source_id} {canonical}")
        else:
            print(f"DUPLICATE {source_id} {canonical}")
        return 0
    data["sources"].append({
        "id": source_id,
        "url": canonical,
        "title": args.title or "รอตรวจสอบชื่อจากแหล่งข้อมูล",
        "category": args.category,
        "priority": "user-primary" if args.selected_by_user else args.priority,
        "selected_by_user": bool(args.selected_by_user),
        "status": args.status if args.title else "pending-verification",
        "checked_at": args.checked_at,
    })
    save_registry(path, data)
    print(f"ADDED {source_id} {canonical}")
    return 0


def list_sources(args: argparse.Namespace) -> int:
    data = load_registry(Path(args.registry).resolve())
    items = data["sources"]
    if args.category:
        items = [item for item in items if item.get("category") == args.category]
    if args.status:
        items = [item for item in items if item.get("status") == args.status]
    print(json.dumps({"count": len(items), "sources": items}, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add")
    add.add_argument("url")
    add.add_argument("--title")
    add.add_argument("--category", default="example-vtr")
    add.add_argument("--priority", default="research-comparison")
    add.add_argument("--selected-by-user", action="store_true")
    add.add_argument("--status", default="verified")
    add.add_argument("--checked-at", default=str(date.today()))
    add.set_defaults(func=add_source)
    listing = sub.add_parser("list")
    listing.add_argument("--category")
    listing.add_argument("--status")
    listing.set_defaults(func=list_sources)
    args = parser.parse_args()
    try:
        return args.func(args)
    except (ValueError, json.JSONDecodeError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
