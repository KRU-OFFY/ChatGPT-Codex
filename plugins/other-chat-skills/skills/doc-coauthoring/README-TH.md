# doc-coauthoring

Skill สำหรับช่วยผู้ใช้ร่วมเขียนเอกสารอย่างเป็นระบบ 3 ระยะ:

1. Context Gathering — รวบรวมข้อมูลและข้อจำกัด
2. Refinement & Structure — วางโครงสร้าง ร่าง และปรับแก้ทีละส่วน
3. Reader Testing — ทดสอบว่าเอกสารเข้าใจได้สำหรับผู้อ่านใหม่

## ติดตั้งบน Windows

เปิด PowerShell ในโฟลเดอร์นี้ แล้วรัน:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\install.ps1
```

ตำแหน่งติดตั้งเริ่มต้น:

```text
%USERPROFILE%\.agents\skills\doc-coauthoring
```

## ตรวจสอบ

```powershell
.\scripts\validate.ps1
```
