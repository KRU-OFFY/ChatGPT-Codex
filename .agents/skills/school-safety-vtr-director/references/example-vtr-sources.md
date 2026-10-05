# Example VTR and official sources

Use `source-registry.json` as the canonical source list. It stores official guidance, rubrics, user-selected examples, discovered comparisons, verification status, and check dates without duplicating URLs in this file.

## Authority order

1. Current assessment rubric issued to the school by its district or committee
2. Current official Department of Labour Protection and Welfare guidance
3. School records and verified evidence
4. Example VTRs, used only for creative and structural study

Never treat a public example as proof of compliance with the user's district rubric. A user-selected example has creative priority but does not gain factual authority.

## Automatic intake

When the user pastes links:

1. Inspect public metadata with web search or page access.
2. Normalize YouTube URLs and remove tracking parameters.
3. Run `scripts/manage_sources.py add` once per source.
4. Use `pending-verification` when the title, publisher, or availability cannot be verified; never guess missing metadata.
5. Skip duplicates by canonical URL or YouTube video ID.
6. Record whether the source was selected by the user or discovered through research.
7. Validate and save the updated Skill.

Example:

```bash
python3 scripts/manage_sources.py add 'https://youtu.be/VIDEO_ID?si=tracking' \
  --title 'Verified title' \
  --category example-vtr \
  --selected-by-user \
  --status verified
```

## Analysis worksheet

For every example reviewed, capture identity, duration, opening, structure, visible evidence, narration, picture quality, graphics, audio, accessibility, compliance, reusable patterns, and weaknesses to avoid.

Compare at least two examples before recommending a style. Build a new storyboard from the user's rubric and evidence; do not recreate another school's scene order or reuse its claims, footage, music, or personal data.
