---
name: vtr-skill-studio
description: Design, create, test, and update reusable Skills for video editing, VTR production, audio correction, motion graphics, production-status dashboards, and committee-ready school presentations. Use when the user wants this project to act as a video-skill studio; asks to build or improve a video-editing Skill; needs an FFmpeg, Remotion, caption, narration, brightness, effects, audio, missing-input, inconsistency, editing-progress, render-progress, or QC workflow; wants to adapt the school-safety VTR system to another topic; or pastes VTR, YouTube, PDF, rubric, tutorial, music, or reference links that should be ingested automatically into the project source library.
---

# VTR Skill Studio

Treat this project as a dedicated studio for creating and improving video-editing Skills. Use `school-safety-vtr-director` as the reference implementation, not as the boundary of supported topics.

Operate in zero-command mode. The user should be able to paste text, links, files, images, audio, or video without naming a Skill or explaining the next step. Read `references/zero-command-operation.md` before routing new inputs.

## Studio model

Separate every solution into two layers:

1. **Production core** — media inspection, trimming, picture correction, audio mixing, captions, branding, rendering, and technical QC.
2. **Topic profile** — purpose, audience, rubric, duration, evidence, narrative structure, visual identity, terminology, privacy, and acceptance rules.

Keep the production core reusable. Put topic-specific requirements in references or profile data so a new VTR does not require rewriting the editor.

## Workflow

1. Classify every new input using `references/zero-command-operation.md`; do not ask the user to choose a Skill.
2. If the user supplies source links, read `references/automatic-source-intake.md` and ingest them without requiring an additional command.
3. Classify the production capability using `references/capability-matrix.md`.
4. Read `references/studio-defaults.md` and apply its defaults unless the user overrides them.
5. For school-safety assessment work, read `references/school-safety-profile.md` and require the current district rubric before final scoring or rendering.
6. For another topic, create a profile from `references/topic-profile-template.md`.
7. Decide the Skill form:
   - instruction-only for analysis, scripting, or handoff;
   - script-backed FFmpeg for deterministic editing and audio work;
   - Remotion-backed for reusable motion graphics;
   - hybrid for complete VTR production.
8. Use the installed `skill-creator` workflow to initialize, edit, validate, test, and save each new or updated Skill.
9. Reuse tested scripts from `school-safety-vtr-director` when their behavior matches. Do not duplicate scripts merely to rename them.
10. Test every added editing script on representative video with and without audio. Verify the rendered streams and duration.
11. Run the gates in `references/studio-quality-gates.md` before declaring the Skill complete.

## Default deliverables

Create only deliverables needed for the chosen profile:

- source and evidence inventory
- rubric or objective mapping
- narration script
- storyboard and shot list
- edit decision list or `project.json`
- captions
- rendered MP4
- media inspection report
- technical and committee-style quality report

## Guardrails

- Never infer that attractive editing satisfies an assessment criterion.
- Never fabricate evidence, activities, outcomes, dates, awards, or participants.
- Protect student privacy and verify media/music rights.
- Preserve original logos and names.
- Plan below the hard duration limit.
- Do not claim full-cycle editing unless a render was actually produced and inspected.
- Keep each created Skill scoped to one repeatable job; use profiles to add topic variants.
- Never reply only with “What would you like me to do?” when the input type and project purpose make the next safe action inferable.
- Ask at most three short questions in one turn, and only when answers materially unblock the next production stage.
