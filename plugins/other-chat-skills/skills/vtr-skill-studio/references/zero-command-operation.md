# Zero-command operation

Make the project feel like one studio with one entrance. Do not require the user to remember Skill names, workflow stages, file naming, or commands.

## Input router

| New input | Automatic action |
|---|---|
| URL or URLs | Inspect, canonicalize, deduplicate, classify, and add to the correct source registry |
| PDF, DOCX, or long text | Classify as rubric, official guidance, school facts, script, or evidence; summarize and index it |
| Image or logo | Inspect identity, resolution, orientation, privacy, and likely scene use |
| Video | Inspect duration, resolution, aspect ratio, frame rate, streams, exposure, and audio; add to the media inventory |
| Audio or music | Inspect duration, channels, loudness risk, speech/music role, and rights status |
| Several mixed files | Batch-classify first, then report one consolidated intake receipt |
| Correction or replacement | Update the existing record; do not create a competing duplicate |
| “Continue” or equivalent | Resume from the stored project state and perform the next safe stage |
| Complete brief with enough inputs | Advance automatically through mapping, scripting, storyboard, edit plan, render, and QC as far as evidence permits |

## Automatic stage progression

1. **Intake** — capture and classify inputs.
2. **Evidence readiness** — map rubric/objectives to verified evidence.
3. **Content design** — create narrative, script, storyboard, shot list, and timeline.
4. **Media preparation** — inspect, trim, correct, and organize source media.
5. **Assembly** — create edit project, captions, graphics, narration, and audio mix.
6. **Render** — produce a preview or final MP4 when inputs are sufficient.
7. **Quality control** — run technical and topic-specific review; fix safe issues automatically.
8. **Delivery** — provide final outputs and a short record of unresolved limitations.

Advance to the next stage without asking for permission when the action is reversible, within project scope, and supported by evidence. Pause only for a material blocker such as a missing authoritative rubric, ambiguous school identity, missing required evidence, privacy risk, unclear media rights, or a choice that would substantially change the result.

## Minimal response format

After intake, reply with a compact status card. After any material production change, also show or refresh the project dashboard with missing inputs, inconsistencies, workflow progress, render state, QC, and next automatic action.

```text
รับข้อมูลแล้ว: [new count/type]
รายการซ้ำ: [count]
สถานะโครงการ: [stage]
ดำเนินการอัตโนมัติ: [action completed]
ต้องการจากผู้ใช้: [only material blockers, or “ไม่มี”]
```

Do not narrate internal tools, repositories, commits, or synchronization. Do not repeat the entire source list unless asked.

For school-safety work, generate the dashboard from `school-safety-vtr-director` using `scripts/project_dashboard.py show`. Update render state automatically when queued, rendering, completed, or failed.

## Defaults that avoid questions

- Language: Thai
- Landscape VTR: 1920x1080, 16:9, 30 fps, H.264/AAC MP4
- School-safety hard limit: 300 seconds; target 280–290 seconds
- Style: formal, evidence-led, restrained motion, readable Thai text
- Editing: FFmpeg core; Remotion only when motion graphics materially help
- Output progression: draft assets first, preview render when ready, final after QC
- Facts: use only verified project data; mark unknown fields instead of guessing
