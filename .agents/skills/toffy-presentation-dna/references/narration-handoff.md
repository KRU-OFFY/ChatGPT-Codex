# Narration handoff contract

When a deck needs narration, emit one block per slide:

- slide_id
- canonical_script
- speaking_goal
- tone
- pronunciation_sensitive_terms
- target_start_or_sequence
- transition_note
- timing_status: PLANNED | RENDERED_UNVERIFIED | VERIFIED

Select voice direction from the current audience, user brief, and speaking goal; do not impose one voice across projects. The following is an optional PA-style example only:

> ผู้พูดคนเดียว เสียงผู้ชายภาษาไทยมาตรฐาน น้ำเสียงสุภาพ เป็นทางการ และมั่นใจ อ่านชัดถ้อยชัดคำ เว้นจังหวะสั้นตามวรรคตอน รักษาระดับเสียงสม่ำเสมอ และอ่านชื่อเฉพาะ/ตัวเลขตามข้อความโดยไม่แต่งเติม

Generate or edit audio only when the host exposes an authorized audio capability. Otherwise return the handoff without claiming audio exists.

For per-slide audio, verify actual rendered duration before replacing an earlier timeline. A planned start time is not evidence that the generated clip fits that window.
