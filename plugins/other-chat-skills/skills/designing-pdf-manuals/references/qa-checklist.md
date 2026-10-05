# QA and Preflight Checklist

## Gate A — Content Correctness

- All required sections from the brief are present.
- Facts from supplied files match the source.
- Time-sensitive facts are verified with current authoritative sources when required.
- Assumptions are labeled.
- Units, names, model numbers, page references, and cross-references are consistent.
- Safety, legal, financial, medical, or regulated claims have appropriate source/approval handling.

## Gate B — Thai QA

- Thai spelling and punctuation are correct.
- Technical terminology is consistent throughout the manual.
- Thai line breaks do not create awkward single-character or punctuation artifacts.
- Mixed Thai/Latin text renders correctly.
- English acronyms and product terms are not missing glyphs.
- Numerals, units, and spacing conventions are consistent.

## Gate C — Visual QA

Inspect every rendered page, not only representative samples.

- No text is clipped or outside safe margins.
- No text overlaps another object.
- No broken/missing glyphs.
- Images are relevant to the adjacent instruction.
- Image crops preserve the important subject.
- Warnings are visually stronger than normal notes.
- Tables remain readable at print scale.
- Icon style is consistent.
- Header/footer/page-number position is consistent.
- Visual density is balanced; no page is unintentionally empty or overcrowded.

## Gate D — Image Integrity

- Generated visuals do not fabricate critical readings or labels.
- Simulated UI is identified when exactness matters.
- Photos and diagrams do not contradict the text.
- Before/after or PASS/FAIL pairs are clearly distinguished.
- Resolution is adequate for intended output.

## Gate E — PDF Preflight

- File opens without error.
- Expected page count matches actual page count.
- Page size/orientation matches the brief.
- Encryption state is intentional.
- Embedded fonts are present when the PDF tool exposes font information.
- All pages render successfully.
- Final rendered pages are visually inspected after export.
- No accidental blank pages or duplicated pages.
- Links/bookmarks are verified when they are part of the deliverable.

## Gate F — Artifact Reopen

Reopen the actual final artifact after the last change. Do not rely on an earlier preview or source document.

## Gate G — Human Approval

Required for externally published, official, safety-critical, legal, financial, medical, policy, procurement, or other high-impact documents. Record approver/reviewer and version before Release.

## Release Verdict

Use one of:
- `PASS` — all mandatory gates passed.
- `PASS_WITH_NOTES` — only non-blocking notes remain.
- `FAIL` — a mandatory gate failed.
- `NEEDS_ATTENTION` — automation cannot safely resolve the issue.
