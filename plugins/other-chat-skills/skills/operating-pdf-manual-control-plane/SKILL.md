---
name: operating-pdf-manual-control-plane
description: Use when a PDF manual project must preserve durable stage state, artifact versions, verification evidence, release approval, or publish-result audit while using the designing-pdf-manuals workflow.
---

# Operating PDF Manual Control Plane

## Overview

Use this skill with **designing-pdf-manuals** when the host exposes the `manual_*` MCP tools. The design skill decides how to create the manual; this skill records what stage is authoritative and whether release gates are actually satisfied.

## Required Control Sequence

1. Call `manual_create_project` once for a new project, or `manual_get_project` to resume an existing project.
2. Follow the designing-pdf-manuals workflow and call `manual_advance_stage` only to the immediate next stage. Never skip a stage.
3. After creating a meaningful file or version, call `manual_record_artifact` with a stable artifact id, version, kind, and URI/reference.
4. At `THAI_QA`, `VISUAL_QA`, and `PDF_PREFLIGHT`, perform the real check first, then call `manual_record_verification` with PASS or FAIL plus concrete evidence.
5. Enter `HUMAN_APPROVAL` only after all three verification gates pass. Call `manual_approve_release` only when a human has explicitly approved the release.
6. Advance to `RELEASED`, then call `manual_get_release_manifest` before any external publishing action.
7. If another connector performs publishing, call `manual_record_publish_result` afterward to record SUCCESS or FAILED. This tool records the result; it does not publish.

## Tool Responsibilities

| Tool | Purpose |
|---|---|
| `manual_create_project` | Initialize durable project state |
| `manual_get_project` | Read current state |
| `manual_advance_stage` | Enforce legal stage movement |
| `manual_record_artifact` | Register immutable artifact versions |
| `manual_record_verification` | Store gate evidence |
| `manual_approve_release` | Record explicit human approval |
| `manual_get_release_manifest` | Produce release-ready record |
| `manual_record_publish_result` | Audit an external publish attempt |

## Connector Routing

Read `references/connector-routing.md` before using Adobe, storage, Drive, or publishing connectors. Connector IDs are workspace-specific unless documented as portable. Never invent a connector id or claim a connector action occurred when it was unavailable.

## Hard Rule

**No Silent Fallback.** If the user requires a named connector and it cannot be used, report the block. A local tool may replace it only when the user allowed substitution or the workflow explicitly defines that fallback.
