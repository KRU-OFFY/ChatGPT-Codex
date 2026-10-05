---
name: designing-pdf-manuals
description: Use when creating or redesigning multi-page PDF manuals, technical guides, field manuals, educational handbooks, infographic-heavy documents, or graphic-realistic manuals from briefs, files, references, or mixed visual assets.
---

# Designing PDF Manuals

## Overview

Build source-grounded, visually coherent PDF manuals through a gated Workflow Agent. Keep AI decisions bounded; use deterministic planning, QA, preflight, approval, and release gates.

## When to Use

Use for technical manuals, field guides, educational handbooks, government/admin manuals, system guides, infographic manuals, and graphic-realistic manuals. Do not use for a trivial text-only PDF or single-page poster.

## Core Workflow

Follow these phases in order.

1. **Intake** — collect brief, files, references, audience, purpose, language, visual direction, evidence needs, and release constraints. Default to **A4** portrait only when unspecified.
2. **Analyze** — extract goals, scope, risks, facts vs assumptions, gaps, and claims needing verification.
3. **Page Map** — define each page's purpose, content blocks, archetype, asset needs, source, and acceptance criteria before page production.
4. **Research / Assets** — ground project facts in supplied files first; use current authoritative research when needed; prepare screenshots, photos, diagrams, or generated visuals.
5. **Write** — create structured prose, captions, labels, tables, warnings, and references suitable for layout.
6. **Image / Diagram** — use **image generation** when original diagrams, realistic virtual illustrations, or explanatory visuals improve understanding. Never present simulated UI as an exact real screenshot.
7. **Layout** — apply the design system: grid, typography, margins, icons, headers/footers, numbering, and consistent hierarchy.
8. **Thai QA** — verify Thai wording, terminology, punctuation, line breaks, and mixed Thai/Latin rendering.
9. **Visual QA** — inspect every rendered page for clipping, overflow, weak hierarchy, irrelevant images, poor crops, inconsistent spacing, and illegible text.
10. **PDF Preflight** — reopen the final artifact; verify page size/count, openability, encryption state, fonts when available, and render every page for final inspection.
11. **Human Approval** — require approval for important, official, safety-critical, regulated, or externally published manuals.
12. **Release** — version the output, record verification/revision notes, and never silently overwrite a verified final.

## Hard Rules

- **No Silent Fallback.** If a requested connector/tool is unavailable, state it. Use another route only when authorized or permitted, and name the actual tool used.
- Prefer read-only / least-privilege access when sufficient.
- Do not invent unseen file content, citations, measurements, or UI details.
- Retry only transient tool failures; do not blindly retry validation, authorization, or schema errors.
- Treat model output as untrusted until validated.
- High-impact write, publish, send, delete, or external-release actions require authorization or Human Approval.
- When Adobe or Adobe Express is explicitly requested and available, use it where helpful; never claim Adobe was used when the connector failed.

## References

Read as needed:
- `references/architecture.md` — states, roles, checkpoints, reliability.
- `references/design-system.md` — page archetypes and visual rules.
- `references/qa-checklist.md` — final verification gates.
- `references/tool-routing.md` — files, web, Adobe, image, PDF, and MCP routing.

Use `templates/` for the project brief, Page Map, and revision log.
