#!/usr/bin/env python3
from pathlib import Path
import re
import sys

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "references/architecture.md",
    "references/design-system.md",
    "references/qa-checklist.md",
    "references/tool-routing.md",
    "templates/project-brief.md",
    "templates/page-map.md",
    "templates/revision-log.md",
    "plugin-ready/README.md",
    "plugin-ready/tool-contracts.yaml",
]

REQUIRED_TERMS = [
    "No Silent Fallback",
    "Page Map",
    "Thai QA",
    "Visual QA",
    "PDF Preflight",
    "Human Approval",
    "A4",
    "image generation",
    "Adobe",
]


def validate(root: Path):
    errors = []
    if not root.exists() or not root.is_dir():
        return [f"Skill directory not found: {root}"]

    missing = [p for p in REQUIRED_FILES if not (root / p).exists()]
    if missing:
        errors.append("Missing files: " + ", ".join(missing))

    skill = root / "SKILL.md"
    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter")
        if not re.search(r"(?m)^name:\s*designing-pdf-manuals\s*$", text):
            errors.append("Invalid or missing skill name")
        match = re.search(r"(?m)^description:\s*(.+)$", text)
        if not match or not match.group(1).startswith("Use when "):
            errors.append("Description must start with 'Use when '")
        missing_terms = [term for term in REQUIRED_TERMS if term not in text]
        if missing_terms:
            errors.append("SKILL.md missing terms: " + ", ".join(missing_terms))

    for path in root.rglob("*.md"):
        if "tests" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"\b(TBD|TODO)\b", text):
            errors.append(f"Placeholder found: {path.relative_to(root)}")

    return errors


def main(argv):
    if len(argv) != 2:
        print("INVALID: usage: validate_skill.py <skill-directory>")
        return 2
    root = Path(argv[1]).resolve()
    errors = validate(root)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
