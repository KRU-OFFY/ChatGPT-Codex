---
name: toffy-presentation-dna
description: Use when TOFFY requests Presentation DNA, new or continued slide-image sets, Canva presentation conversion, or motion and narration for a presentation. Do not use for ordinary conversation or unrelated media without presentation scope.
---

# TOFFY Presentation DNA

## Core principle

Support any style selected by the user. Establish a project-specific visual contract from the current brief and/or approved reference images, then preserve that contract across the set while adapting composition to each slide's message and evidence.

Do not impose a permanent template, palette, font, ornament, or voice. A new project starts a new contract. Continue an existing contract only when the user requests continuation or explicitly selects it. Do not transfer an older project's colors or graphic treatment into a new set silently.

If the brief defines the style without reference images, use that brief to produce a representative pilot. If neither brief nor reference defines the style, ask one focused style question or propose clearly labeled options; do not default to Banwai. If brief and references conflict, resolve the material conflict before generating the set. Record the source and approval status of the contract.

## Source authority

Before generating anything, bind to the freshest authoritative inputs: the current style brief, approved reference images, canonical text/data, real evidence photos, and official logos. Never invent evidence, people, certificates, statistics, or logos. If source authority is missing or contradictory, report the blocker instead of filling the gap.

When the user explicitly asks to continue the previous TOFFY/Banwai PA 2569 look and no newer approved reference is supplied, load `references/style-profile-banwai-pa-2569.json`. Otherwise derive a new style contract from the supplied approved reference set and do not silently reuse the Banwai preset.

## Engineering and learning contract

Apply the current `toffy-skill-engineering-standard` during presentation production and skill revision; also use Skill Creator when revising this skill. Resolve that personal skill by frontmatter name; do not assume a remembered version is current. Keep reusable rules here, project state in canonical project files, and raw incidents in a durable Learning Sidecar outside this skill. Read [learning-loop.md](references/learning-loop.md) before acting on a correction or revising the workflow.

Treat these workflow gates as user-authorized requirements. Do not claim empirical reduction in mistakes, automatic model retraining, or successful Canva/audio integration from saved instructions alone. Keep inferred improvements CANDIDATE until reproduction, regression and independent evaluation support promotion. Separate skill maintenance from slide production: a request to fix the skill does not authorize regenerating the deck.

## Workflow — ordered gates

Follow `STYLE → CHATGPT IMAGE BUILD → IMAGE REVIEW → CANVA → MAGIC LAYERS → QC → MOTION → VOICE → EXPORT`. Advance only after the preceding required gate passes. Record each stage's artifact/version, Expected vs Actual, evidence and status in project state.

1. **Bind and learn**: identify objective, audience, slide count, canonical facts, approved references and evidence boundaries. Retrieve relevant durable lessons before execution; distinguish prior reported fixes from proven ones. Fresh-check tools, permission, connectivity and quota for the next stage. Stop the blocked stage without silently switching tools or lowering quality.
2. **Freeze STYLE_CONTRACT**: record project/set identity, source brief/reference, approval status, palette roles, layout grammar, title/header treatment, card geometry, icon language, photo framing, footer system, ornament density, typography hierarchy and negative-space behavior. Preserve required invariants and permitted variation. Plan slide roles and map claims to authoritative evidence. Lock approved story, counts, names, figures, photos and logos.
3. **ChatGPT Image Build**: use the host's native ChatGPT image generation to create individual slide images, keeping TEXT, PHOTO, ICON, SHAPE, DECORATION and BACKGROUND separable. Preserve real people's identities and official logo proportions; never substitute generated likenesses for evidence. Generate a representative pilot when style fidelity is uncertain. For the agreed 14-slide workflow, use batches of 7 + 7 and maintain coverage across both. Use the current approved slide count for other projects. If image generation is unavailable, return IMAGE_PROMPTS marked PLANNED/BLOCKED, not IMAGE_SET, and do not advance.
4. **Image Review — hard gate**: inspect every actual generated image for canonical Thai/mixed-script text, numerals, facts, identities, logos, style consistency, clipping, ghost text and evidence visibility. Verify filenames, count, dimensions, aspect ratio and color profile against the current STYLE_CONTRACT from actual files where required. Apply PNG sRGB, 16:9 and 3840×2160 only to a project whose approved brief requires them; record smaller native output and any separately resized derivative accurately. Never label a smaller image native 4K. Obtain the user's image approval before Canva, Magic Layers or final export; reuse approval only for the exact unchanged reviewed version. A contact sheet may support review but does not replace individual-page inputs.
5. **Canva handoff/import**: provide each approved image filename, canonical text, photo intent and semantic-region notes. Import the approved individual PNG/JPG pages; do not substitute a multipage PDF or use Canva image generation for the set, an individual slide, an evidence photo or an official logo. Correct altered evidence with the canonical real source. Fresh-verify actual Canva access and capability; prepare a handoff if unavailable and mark conversion BLOCKED, not completed.
6. **Magic Layers**: use only when actually available in the authorized Canva session. Inspect resulting editable text, shapes and photo regions. A flattened image placed on a slide is not verified layer conversion. Preserve real photos by comparing with canonical source and replacing altered/fragmented evidence from that source when necessary. Use [magic-layers-qc.md](references/magic-layers-qc.md).
7. **QC after conversion**: perform Text Authority Pass against canonical wording, then inspect geometry after every reconstructed-text correction. Check overflow, clipping, duplicates, hierarchy, photo continuity, logo ratio and complete slide coverage. Require these checks before motion.
8. **Motion**: apply the authorized presentation animation to the verified layers. Inspect playback for entrances/exits, transitions, flashing, blank frames and text/evidence obstruction; preserve readability throughout. Mark required motion BLOCKED if capability is unavailable instead of treating static slides as animated.
9. **Voice**: prepare one narration block per slide using [narration-handoff.md](references/narration-handoff.md). For the requested workflow use soft, polite, formal narration with quiet background music, unless the current brief specifies otherwise. Render only through an authorized capability; inspect actual sound, duration, pronunciation, music balance and synchronization with slide/motion timing. A script or timeline alone is not generated audio.
10. **Export**: export the requested formats only after required Image Review, layer/text/geometry QC, motion and voice gates pass. Inspect the actual exported artifact for count, dimensions, editable content where requested, playback, audio and missing content. Do not jump straight to PPTX before the image/Canva workflow. When only still images are requested, end after verified image delivery; motion/voice are required only for a scope that requests them. Distinguish review previews from final exports.
11. **Close and monitor**: report Expected vs Actual separately for planned, generated, image-approved, imported, converted, QC-verified, animated, narrated and exported states. Record corrections and fresh post-fix evidence in the sidecar. Keep unresolved integration checks PARTIAL/BLOCKED and state exact next action; do not call the entire task CLOSED_VERIFIED from a successful stage alone.

## Optional example: Banwai PA 2569

Load this example only when explicitly selected or when continuing the named Banwai set. Never use it as a default for a new project. The packaged profile reports this reference palette: royal blue around `#012E86`, emerald around `#01502D`, warm gold around `#F6D268`, and cream around `#FBFAF7`. Use deep-blue title plaques with gold edging, emerald secondary bars/footer, cream-white cards, restrained gold Thai ornament, gold-framed real-photo evidence, navy body text, and limited accent colors for KPI cards. Keep the overall feel formal, bright, evidence-first, and visually energetic.

The packaged profile reports that its historical 14-image reference set was measured at 1672×941 per image; the source images are not bundled, so this is not a fresh measurement of the current input. Treat 3840×2160 as a downstream production target where required, not as the native source resolution.

## Magic Layers readiness

Use the operational checklist in `references/magic-layers-qc.md`. Treat its font, size, and spacing values as conditional starting points from a prior example, not style requirements. Critical Thai text may start around 48 px at 2160h when container headroom is constrained, then inspect the actual export. Do not assume larger text is safer. After any reconstructed-text correction, geometry QC is mandatory.

## Output contract

Return these sections in order. For still-image-only scope, mark CANVA_HANDOFF and NARRATION_HANDOFF NOT_REQUIRED; do not invoke those stages or add deliverables outside the request:

1. `STYLE_CONTRACT`
2. `SLIDE_PLAN`
3. `IMAGE_SET` or `IMAGE_PROMPTS`
4. `CANVA_HANDOFF`
5. `NARRATION_HANDOFF`
6. `QC_REPORT` with Expected vs Actual, blockers, and exact next action

## Stop conditions

Stop advancement when image approval is missing, real identities are altered, required layers/motion/audio are unverified, or a required tool hits permission/quota/connectivity limits. Preserve a checkpoint and existing approvals; resume from the unresolved gate after fresh verification, without regenerating approved pages.

Stop and report `BLOCKED` or `PARTIAL` when the canonical logo/evidence is unavailable, facts conflict, a reference set is incomplete, output dimensions are unverified, or a host integration cannot be freshly verified. Do not downgrade these gates silently.
