# designing-pdf-manuals

Skill-first Workflow Agent for designing and producing high-quality multi-page PDF manuals from briefs, files, references, and visual examples.

## What it is for

Use this skill for technical manuals, field guides, educational handbooks, government/admin manuals, system operation guides, infographic-heavy manuals, and Graphic Realistic manuals.

The skill controls the workflow from source intake through Page Map, writing, images, layout, Thai/visual QA, PDF preflight, Human Approval, and versioned release.

## Install

Copy the `designing-pdf-manuals` directory into the skill directory supported by your runtime. Cross-runtime agent environments commonly recognize a user skills directory such as `~/.agents/skills/`; runtime-specific locations may also be supported.

Keep the folder name unchanged so discovery and internal references remain stable.

## Example trigger prompts

- "สร้างคู่มือ PDF แบบกราฟิกจากไฟล์ที่แนบให้"
- "ออกแบบคู่มือซ่อมบำรุง A4 พร้อมภาพเสมือนจริงและเช็กลิสต์"
- "วิเคราะห์เอกสารนี้แล้วสร้าง Page Map ก่อนทำคู่มือ"
- "ทำคู่มือราชการ PDF และตรวจ Thai QA + PDF Preflight ก่อนส่ง"
- "ใช้ Adobe Express เป็นตัวเลือกหลักในการออกแบบคู่มือนี้"

## Package layout

- `SKILL.md` — core operational instructions
- `references/` — architecture, design system, QA, tool routing
- `templates/` — project brief, Page Map, revision log
- `scripts/validate_skill.py` — static package validator
- `tests/` — contract and validator tests
- `plugin-ready/` — vendor-neutral adapter blueprint for future Plugin/MCP wrapping
- `examples/` — optional generated visual references

## Validation

Run:

```bash
python -m unittest discover -s designing-pdf-manuals/tests -v
python designing-pdf-manuals/scripts/validate_skill.py designing-pdf-manuals
```

Both commands must pass before packaging or deployment.

## Plugin-ready, not plugin-dependent

The core Skill contains the reasoning and quality policy. Adobe, Drive, databases, publishing systems, and other MCP/App integrations should remain adapters. The package in `plugin-ready/` is a design contract only and is not presented as an official plugin manifest.

## Release discipline

A generated PDF is not `FINAL` merely because export succeeded. The workflow requires rendered-page inspection, technical PDF preflight, final artifact reopen, and Human Approval when the document is high impact or externally published.
