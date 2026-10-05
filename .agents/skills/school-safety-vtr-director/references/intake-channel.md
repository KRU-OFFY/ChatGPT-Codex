# Teacher upload channel

Use this channel for evidence supplied by school staff. The live IDs and deployment status are in `project-state.json` under `intake_channel`.

## Intake contract

- The Google Sheet tab `ทะเบียนหลักฐาน` is the internal source of truth.
- Accept production media only after its status is `พร้อมใช้ตัดต่อ`.
- Treat `รับไฟล์แล้ว` and `กำลังตรวจ` as queued, not approved.
- Surface `ขาดข้อมูล`, `ไฟล์ซ้ำ`, `ไม่ตรงเกณฑ์`, and `ต้องตรวจข้อมูลส่วนบุคคล` as user-input issues.
- Never delete possible duplicates automatically.
- Never expose uploader names, private Drive URLs, or file names through a public Dashboard API. Aggregate counts only.
- Large videos use a shared Google Drive link; the web uploader limits direct uploads to 20 MB per file and 30 MB per submission.

## Deployment boundary

The Drive folder, category folders, registry Sheet, and Apps Script package may be created automatically. Google requires the account owner to authorize the script and deploy the Web app once. Do not label the channel live until `web_app_url` and `dashboard_api_url` are recorded and successfully polled.
