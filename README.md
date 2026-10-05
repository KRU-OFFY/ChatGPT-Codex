# TOFFY Cloud Skills

Repository: https://github.com/KRU-OFFY/ChatGPT-Codex (public)

เก็บ source ต้นฉบับ 26 แพ็กเกจ: อีก 25 สกิลจาก ZIP ที่ตรวจ checksum ครบ พร้อม TOFFY System Orchestrator 5 ไฟล์จาก verified backup ทุกไฟล์คัดลอกตาม bytes เดิม ไม่ reconstruction หรือ repair และไม่ยกระดับคุณภาพ

## Source locations

- `.agents/skills/` เป็น repo skill source สำหรับ Work cloud / Codex tasks ที่ checkout repository นี้
- `plugins/toffy-orchestrator/skills/` เป็น portable plugin copy ของ TOFFY
- `plugins/other-chat-skills/skills/` เป็น portable plugin copies ของอีก 25 สกิล
- `.agents/plugins/marketplace.json` แสดง plugin แบบ AVAILABLE เท่านั้น ไม่ auto-install

สอง source views จำเป็นสำหรับ repo skill discovery และ portable plugin packaging; ทุกสำเนามี SHA-256 ตรงกันและตรวจด้วย SOURCE_INDEX.json / SHA256SUMS.txt ไม่ใช้ symlink ที่ขึ้นกับ OS

## Verified versus pending

Source bytes verified; Git storage is not proof of ChatGPT installation or model invocation. Some external connector/runtime dependencies are not bundled. Original catalogue names and source names are recorded separately; plugin namespaces can differ. writing-for-agents references a pointers.md file absent from the supplied snapshot. writing-skills sibling runtime guides are in the full original superpowers plugin, not this export. Keep quality unchanged.

ไม่มี raw audit logs, ZIP attachments, auth/config credentials หรือข้อมูลอื่นนอก package source และ metadata ของ repository นี้ใน commit

อ่าน CLOUD_BINDING_PLAN.md ก่อนติดตั้งหรือเชื่อมต่อแต่ละ runtime

Official references: [Build skills](https://learn.chatgpt.com/docs/build-skills), [Package your plugin](https://developers.openai.com/plugins/build/plugins), [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments)
