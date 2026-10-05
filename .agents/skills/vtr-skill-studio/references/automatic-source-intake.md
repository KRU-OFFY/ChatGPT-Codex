# Automatic source intake

Treat a message containing only links, or links plus a short label, as an instruction to add those sources to this VTR studio automatically.

## Intake procedure

1. Extract every HTTP or HTTPS URL.
2. Canonicalize YouTube links to `https://www.youtube.com/watch?v=<video-id>` and remove tracking parameters.
3. Search or open each source to obtain the real title, publisher or channel, publication year, source type, and topic.
4. Classify each source as one of:
   - `official-guidance`
   - `assessment-rubric`
   - `example-vtr`
   - `editing-tutorial`
   - `motion-graphics-reference`
   - `audio-reference`
   - `music-or-sfx`
   - `school-evidence`
   - `other`
5. Route school-safety sources to `school-safety-vtr-director`. Route other sources to the relevant topic Skill or create a topic profile when none exists.
6. Deduplicate by canonical URL; for YouTube, deduplicate by video ID.
7. Preserve an inaccessible source as `pending-verification`. Never guess its title, school, date, or authority.
8. Record the date checked and whether the source was selected by the user or discovered by research.
9. Save and validate the updated Skill source registry.
10. Reply with only the new items, duplicates skipped, pending items, and the resulting total.

## Trust rules

- A user-selected example receives higher creative priority, not higher factual authority.
- Official rubrics and current government guidance outrank example videos.
- Do not transfer another school's claims, evidence, music, footage, or personal data into a new production.
- Recheck changing requirements before relying on a stored source for scoring.

## Automatic behavior boundary

Automatic intake occurs when the user sends links in the active conversation. Do not create a recurring web search unless the user specifies a schedule or asks for monitoring.
