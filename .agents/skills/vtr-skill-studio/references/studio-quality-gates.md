# Studio quality gates

## Skill design

- Name and description trigger on realistic user language.
- The Skill has one repeatable job and clear boundaries.
- Topic rules are separated from reusable production logic.
- Detailed references are loaded only when relevant.

## Implementation

- Skill structure passes `quick_validate.py`.
- Every new script runs successfully on representative inputs.
- Tests include video with audio, video without audio, portrait media, and duration overflow.
- Errors are actionable and do not silently produce partial output.

## Render verification

- Output exists and opens.
- Video and audio streams are present.
- Resolution, frame rate, codecs, and duration match the profile.
- Narration remains intelligible and final audio does not clip.
- Captions, logos, names, and timecodes are correct.

## Editorial compliance

- Every factual claim has evidence.
- Privacy and media rights were reviewed.
- Effects support comprehension.
- The result passes the topic-specific rubric or acceptance checks.
