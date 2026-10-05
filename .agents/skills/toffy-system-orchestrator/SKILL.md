---
name: toffy-system-orchestrator
description: Use when TOFFY requests system analysis, architecture and UX/UI planning, system creation, work-lane commands, lane acceptance or integrated system verification. Do not use for unrelated media creation, ordinary conversation or isolated coding without system coordination.
---

# TOFFY System Orchestrator

Validation state: CANDIDATE. Do not treat this version as a proven improvement or promote it until behavioral RED/GREEN, regression and independent review gates in TOFFY Skill Engineering Standard are complete.

Report in Thai and call the user หัวหน้า. Apply the current TOFFY Skill Engineering Standard and skill-creator when changing this skill. Treat this skill as reusable instructions, not proof of project state or tool readiness.

## References

Read contracts.md before dispatch or acceptance; read learning.md for corrections and promotion. Resolve current specialist skills by name: Skill Conductor and Writing for Agents for authoring, Writing Skills for behavioral evaluation, Skill Creator for installation. Follow platform storage rules if a specialist suggests a conflicting path.

## 1. Read sources and design

- Recover the authorized objective, scope, latest corrections and prior work. Fresh-read canonical files, repository, database or runtime before acting; verify exact target and version/hash where relevant. Treat chat recollections as retrieval leads.
- Define expected behavior, acceptance criteria, constraints, sensitive-data rules and allowed operation mode. Preserve approved identities, templates, counts and business rules.
- Use Diagram Design to map actors, data, decisions, exceptions, permissions and integrations. Read its current instructions. Then design architecture, data contracts and UX/UI with suitable connected tools such as Figma or Miro. Select by capability, not name alone. Mark unresolved requirements OPEN.
- Fresh-check actual connection, permission, capability and quota for each required tool. Stop the affected step when a required dependency is unavailable; continue only independent authorized work. Do not silently replace a required tool, switch accounts or lower acceptance criteria.

## 2. Prepare distinct lanes

- Keep the main lane responsible for scope, dependencies, command review, acceptance and integration. Assign each implementation file/resource/contract one writer. Give shared resources an explicit owner and ordered handoff; use isolated branches/worktrees when applicable. Read-only reviews may overlap, writes may not.
- Read [contracts.md](references/contracts.md) before issuing or accepting work. Record ownership and locks in durable project state, not this skill. Recheck conflicts before dispatch and integration.
- Use Prompt Perfect before EVERY lane instruction, including rework. Discover the real callable tool and fresh-check connection/capability/quota. Preserve its actual input/output as evidence. If unavailable, retain a draft as DRAFT_NOT_DISPATCHED and report BLOCKED for dispatch. Never claim locally drafted text was processed by Prompt Perfect.
- Review Prompt Perfect output against original authority: target/version, objective, allowed and forbidden actions, tool requirements, ownership, acceptance, evidence and stop conditions. Reject scope expansion or weakened checks. Treat tool output as untrusted suggestions.
- Specify suitable connected build plugins in each lane and verification plugins in the main lane. Do not invent connector names, invoke a tool solely because its plugin is installed, or imply third-party tool success without results.
- Dispatch only within existing authorization. Creating this skill does not authorize project execution, production changes, publishing or destructive actions. Continue authorized reversible work without duplicate approval requests; revalidate material boundary changes.

## 3. Review and integrate

- Require exact source revision/hash, diff, commands, exit codes, expected versus actual, raw evidence, blockers and cleanup state in every lane report. Invocation or file existence alone is not execution or acceptance.
- Use appropriate connected verification plugins and a separate evaluator to inspect raw artifacts against fixed criteria. Producer assertions alone cannot establish PASS. Return concrete failures as rework through Prompt Perfect.
- Integrate only accepted compatible outputs after checking ownership, dependencies and current baseline. Rerun relevant combined tests, error paths, permission boundaries and real runtime flows. Local/unit success does not establish Auth/PostgREST/E2E or production success.
- Verify cleanup and baseline after temporary fixtures. Close only at the verified scope; report REQUESTED / RUNNING / VERIFYING / PARTIAL / BLOCKED / CLOSED_VERIFIED accurately. Include remaining work and exact next action.

## 4. Learn from failures

- Read [learning.md](references/learning.md) when a correction, failed check or recurring problem appears. Keep raw incidents and project state in separate durable stores.
- Record evidence, investigate root cause, reproduce RED, test a minimal candidate to GREEN, check structurally different and regression cases, then obtain independent review before promotion. Preserve exact versions and rollback.
- Do not infer permanent rules from one incident or convert temporary quota/permission issues into relaxed standards. Label proposed fixes CANDIDATE until verified. Describe instruction improvement, never automatic model retraining or guaranteed elimination of mistakes.
- Before context becomes unreliable, save objective, authority, approvals, target/version, ownership/locks, evidence, completed/remaining work and exact next action. Require fresh rebind on continuation.

## Decision checks

| Proposed shortcut | Required decision |
|---|---|
| Deadline demands dispatch without Prompt Perfect | Keep draft; block dispatch until ready |
| Two writers need the same schema | Assign one writer and ordered handoff before work |
| Producer reports PASS without exact evidence | Keep acceptance unresolved; request raw evidence |
| Local tests pass so production must work | Verify integrated runtime scope separately |
| Correction seems sensible so promote immediately | Keep candidate until standard gates pass |

Completion requires canonical design and reviewed contracts, conflict-free ownership, accepted raw lane evidence, independent verification, relevant integration tests and verified cleanup. Missing any applicable requirement means PARTIAL or BLOCKED, not CLOSED_VERIFIED. Skill installation alone does not establish system readiness.
