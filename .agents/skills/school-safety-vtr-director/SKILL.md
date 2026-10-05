---
name: school-safety-vtr-director
description: Plan, assemble, edit, and quality-check Thai school-safety assessment VTRs under five minutes. Use when Codex must analyze an uploaded district rubric, map evidence to scoring criteria, audit school photos/videos/audio, write Thai narration and storyboards, create an FFmpeg-ready project, render an MP4, add logos/subtitles/music, simulate a committee review, automatically ingest pasted VTR, YouTube, PDF, rubric, and official-guidance links, or operate connected desktop video, audio, file-management, browser, and upload workflows through an available computer-control tool.
---

# School Safety VTR Director

Produce an evidence-led VTR. Treat the current district rubric supplied by the user as authoritative. Never substitute a generic safety checklist when a local rubric exists.

Operate in zero-command mode. Do not require the user to name this Skill, choose a workflow stage, or repeat known school information. Read `references/project-state.json` at the start of each school-safety task and update it after material intake or stage completion. Read `references/dashboard-rules.md` and regenerate the compact dashboard whenever readiness, issues, editing, render, or QC status changes.

## Workflow

1. Read `references/project-state.json`; resume the next unfinished stage automatically.
2. When the user supplies source links, inspect their metadata and run `scripts/manage_sources.py add` for each canonical source. For connected Google Drive folders, list children recursively, register unique file IDs in `references/drive-source-registry.json`, and classify relevance without downloading large media unnecessarily. Do this automatically without requesting a second instruction.
3. When the user supplies files or media, classify and inspect them immediately; do not ask what they are for when the project context makes it clear.
4. When `intake_channel` exists in `references/project-state.json`, read its Google Sheet registry as the teacher-upload queue. Treat rows with `พร้อมใช้ตัดต่อ` as approved production inputs; surface `ขาดข้อมูล`, `ไฟล์ซ้ำ`, `ไม่ตรงเกณฑ์`, and `ต้องตรวจข้อมูลส่วนบุคคล` in the dashboard before using those files. Never expose uploader names in a public dashboard payload.
5. Inventory the rubric, school facts, media, brand assets, narration, music, and consent status in `references/media-inventory.json`. Register each uploaded file automatically with its hash, technical findings, intended use, and approval status.
6. Read `references/project-facts.json`, `references/rubric-workflow.md`, and `references/rubric-evidence-matrix.md`. Create or update the criterion-to-evidence matrix before scripting; user-confirmed facts override inconsistent legacy document text.
7. Read `references/example-vtr-sources.md`, `references/source-registry.json`, and `references/drive-source-registry.json` when studying references, connected evidence, or proposing a creative direction. Analyze patterns; never copy claims, footage, music, or school-specific content.
8. Run `scripts/inspect_media.py` on candidate media. Flag unreadable, portrait, low-resolution, silent, clipped, or unusually short files.
9. Identify missing evidence. Ask only for missing inputs that materially block an accurate or compliant result, with at most three short questions at once.
10. Write a Thai narration script, storyboard, shot list, and timeline. Target 4:40–4:50; never plan exactly 5:00.
11. Read `references/editorial-standards.md`. Apply privacy, copyright, factual accuracy, legibility, and audio rules.
12. Create `project.json` from `references/project-schema.md`. Use relative paths where practical.
13. Run `scripts/validate_project.py project.json`. Resolve every safe, deterministic error before rendering.
14. Run `scripts/render_vtr.py project.json` when required inputs are sufficient. Do not ask for confirmation merely to create a reversible preview render.
15. Inspect the rendered duration and streams with `scripts/inspect_media.py` and conduct the committee-style review in `references/quality-check.md`. Fix safe technical defects automatically.
16. Update `references/project-state.json` and deliver the MP4 plus script, storyboard, evidence matrix, subtitles, and quality report when ready.
17. Run `scripts/project_dashboard.py show` after every material state change. Present the compact dashboard automatically; do not require the user to request it.
18. For a visual live view, run `scripts/serve_dashboard.py` and use `assets/vtr-dashboard.html`. It polls `references/project-state.json` every two seconds. The page separates user-provided inputs from the production workflow. When opened as a standalone file, it must label embedded or manually imported data as a snapshot; only label it live after a URL or persistent file handle is connected.
19. When the user requests a downloadable single-file dashboard, run `scripts/build_standalone_dashboard.py --output <safe-path>.html`. It embeds the current state and school logo while preserving the honest connection labels and one-click live file connection.
20. When a compatible computer-control tool is connected and the user asks for hands-on setup or editing, read `references/computer-control.md`. Use the tool for reversible in-scope desktop actions, report the active app and result, and pause for the user at passwords, passkeys, OTP, CAPTCHA, consent, account authorization, publishing, sharing, deletion, or other consequential confirmation screens.

## Editing policy

- Preserve original aspect ratio; scale and pad instead of stretching.
- Prefer straight cuts and short fades. Use effects only to clarify structure or evidence.
- Keep narration intelligible. Reduce background music under speech and prevent clipping.
- Do not invent dates, statistics, activities, awards, participants, or outcomes.
- Do not expose student surnames, health data, phone numbers, IDs, or sensitive incident details unless necessary, authorized, and explicitly requested.
- Use only media and music the school may lawfully use.
- Stop before rendering if the rubric, required evidence, or essential identity assets are missing and guessing would change the assessment outcome.
- After intake, respond with only: received items, duplicates, current stage, automatic action completed, and material blockers. Do not repeat operating instructions unless asked.

## Script usage

All scripts require Python 3.10+, FFmpeg, and ffprobe on `PATH`.

```bash
python3 scripts/inspect_media.py media/
python3 scripts/manage_sources.py list
python3 scripts/project_dashboard.py show
python3 scripts/serve_dashboard.py
python3 scripts/build_standalone_dashboard.py --output VTR-Dashboard.html
python3 scripts/validate_project.py project.json
python3 scripts/render_vtr.py project.json
```

The renderer updates the dashboard state during rendering. Pass `--state path/to/project-state.json` only when using a non-default state file. It supports clip trimming, scaling/padding, brightness, contrast, saturation, clip volume, fades, logo overlay, burned subtitles, voice-over, background music, audio ducking, and H.264/AAC MP4 output. Keep advanced motion graphics in a separate Remotion project; read `references/remotion-extension.md` only when the user requests animated infographics or a reusable visual template.
