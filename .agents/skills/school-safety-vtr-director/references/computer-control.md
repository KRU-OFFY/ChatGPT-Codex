# Computer-control workflow

Use this reference only when a compatible computer-control tool is actually available in the current session. Configuration in the project state does not create or install a connector.

## Start

1. Detect the connected control surface and its supported actions. Prefer a project-specific connector such as Windows-MCP over generic screen clicking when both are available.
2. Read the current screen or application state before acting. Do not assume a window, file, timeline, or account is active.
3. State the short action being performed. Keep the user informed if work continues longer than one minute.
4. Work only in the VTR project files, applications, and services placed in scope by the user.

## Automatic desktop actions

- Create non-destructive folders and organize copies of project media.
- Open the dashboard, editor, audio tool, file manager, or rendering console.
- Import approved media, set a 1920×1080 timeline, and apply the project frame rate.
- Trim, reorder, adjust brightness/contrast/saturation, normalize levels, duck music, add approved logo/subtitles, preview, save, and export a reversible draft.
- Inspect render status, error dialogs, file duration, dimensions, and audio streams.
- Navigate to setup pages and fill non-sensitive fields from verified project data.

## User takeover and confirmations

Pause and clearly identify the required user action for:

- passwords, passkeys, OTP, CAPTCHA, biometric prompts, recovery codes, and account selection;
- OAuth or Google/Microsoft account authorization;
- publishing, sharing outside the existing project audience, sending messages, or changing permissions;
- deleting or overwriting originals, uninstalling software, purchases, subscriptions, or irreversible operations.

Never read, copy, store, paste, screenshot, or repeat secrets. After user takeover, re-read the visible state and continue only when the expected success screen is confirmed.

## Editing safeguards

- Preserve originals. Use a project copy and incremental saves.
- Never publish or replace the final VTR without explicit confirmation.
- Stop if the selected file does not match the registry, privacy status, or approved evidence category.
- Prefer exact menu or accessibility controls; use coordinate clicks only after confirming window size and target.
- After each major editing step, save and verify the preview before continuing.

## Completion record

Update `project-state.json` with the application used, completed action, timestamp, output path, and any pending user takeover. Do not mark a desktop task completed solely because a click occurred; verify the resulting state.
