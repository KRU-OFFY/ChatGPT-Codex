# Project dashboard rules

Display a compact dashboard automatically after material intake, issue detection, stage completion, render progress, render failure, QC, or delivery.

## Status vocabulary

| Status | Thai label | Meaning |
|---|---|---|
| `missing` | ขาดข้อมูล | Required input has not been provided |
| `blocked` | ติดขัด | Work cannot advance safely |
| `needs-review` | ต้องตรวจ/ปรับปรุง | Data exists but may be incomplete or inconsistent |
| `pending` | รอดำเนินการ | Waiting for a prior stage |
| `ready` | พร้อม | Inputs are sufficient to begin |
| `in-progress` | กำลังดำเนินการ | Work is active |
| `completed` | เสร็จแล้ว | Stage passed its checks |
| `failed` | ไม่สำเร็จ | A technical or validation failure occurred |
| `not-applicable` | ไม่เกี่ยวข้อง | Excluded from this profile |

## Required dashboard blocks

1. Overall progress and current stage
2. User input report: chat files, connected Drive files, reference links, and input readiness rows
3. Production workflow: script, storyboard, edit plan, editing, subtitles, render, QC, and delivery
4. Missing inputs and inconsistencies, ordered critical → warning → info
5. Render state with progress, attempt, output, and error
6. Connection mode, project update date, and last source check time
7. Next automatic action

## Update rules

- Update image, video, document, and audio rows immediately after inspection.
- Set `consistency` to `needs-review` when names, dates, counts, claims, or evidence conflict.
- Add a concise issue with the exact mismatch and required correction; do not silently choose one value.
- Set downstream stages to `blocked` only when the mismatch materially changes scoring or narration.
- During rendering, update `render_state.status` to `queued`, `rendering`, `completed`, or `failed`, and update progress when available.
- On render failure, retain the error summary and next safe corrective action.
- After successful render, verify streams and duration before marking `render` completed.
- Keep resolved issues for traceability with `status: resolved`; hide them from the compact view unless asked.
- Never label a downloaded standalone HTML or one-time JSON import as real-time. Use `snapshot` until a URL or persistent file handle is successfully polled.
- When a live URL or file handle is connected, poll every two seconds with cache disabled and retain the last valid state if a read fails.

Use `scripts/project_dashboard.py` to generate the dashboard and update deterministic workflow or render fields.
