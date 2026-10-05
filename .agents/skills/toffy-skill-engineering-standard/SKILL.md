---
name: toffy-skill-engineering-standard
description: Apply TOFFY's default engineering standard whenever creating or improving a skill. Preserve evidence, separate project state and learning records from reusable instructions, and require reproducible testing and independent review before promoting changes. Use for learning from failures, reviewing TOFFY corrections, preventing repeated work errors, skill evolution, and establishing reusable work standards.
---

# TOFFY Skill Engineering Standard

Apply this as TOFFY's default for future skill creation and revision, unless the user explicitly supplies a different requirement. Compose it with the available skill-creator; do not replace platform installation rules. Call the user หัวหน้า and report in Thai.

## Core workflow

1. Read authoritative current sources and existing skills before creating duplicates. Define objective, authorized scope, expected behavior and acceptance criteria. Treat recalled conversations as retrieval leads, not current project state.
2. Separate three stores: reusable skill instructions/resources; canonical project sources/state; and a durable Learning Sidecar containing raw attempts and derived lessons. Do not rely on chat memory as the evidence store. Never embed secrets or real personal data in a skill or learning record.
3. Observe actual use and record input, attempt, artifact/version, expected versus actual, error, tool/runtime context, and evidence. Mark unknown results UNKNOWN; tool invocation is not proof of execution.
4. Investigate root cause using Observe → Hypothesis → Test → Evidence → Decision. Distinguish instruction defects from permission, quota, connectivity, source, runtime and model failures. Do not change reusable rules merely to hide a temporary tool problem.
5. Reproduce the failure (RED), propose the smallest generalizable candidate fix, and test it (GREEN). Preserve baseline and candidate versions. Record hypothesis, changes and measured outcomes. Do not blindly retry or derive a permanent rule from one incident.
6. Test structurally different cases, negative/error paths, triggering behavior and regression of previously working cases. Keep original acceptance criteria fixed unless an authoritative requirement changes. Label synthetic tests; do not treat them as evidence of live production success.
7. Require an independent reviewer/evaluator with clean context to check raw artifacts against acceptance criteria. Do not let the producer's self-assessment alone establish PASS. If no independent evaluation is available, retain VERIFIED_CANDIDATE or PARTIAL; state exactly what remains.
8. Promote a reusable improvement only after evidence supports generalization, regression passes and required authorization is satisfied. Preserve version history and rollback. Updating authorized personal skill files follows skill-creator's save/verify procedure; production deployment, publishing and risk-boundary changes require their own authorization. Do not infer automatic promotion permission from a learning request.
9. Monitor later use and feed verified failures back into the sidecar. Describe this as improving instructions/resources from evidence, never as automatic retraining of the underlying model or guaranteed autonomous learning.

Read [learning-record.md](references/learning-record.md) when recording a lesson or preparing promotion.

## Reporting and continuity

Use REQUESTED / RUNNING / VERIFYING / PARTIAL / BLOCKED / CLOSED_VERIFIED accurately. State passed checks, unresolved blockers and exact next action. Do not assert improvement without comparative evidence. On context risk, save objective, authority, permissions, exact version, evidence, completed/remaining work and next action before handoff. Rebind current sources on resumption.

## Relationship to system-development skills

Keep system-specific orchestration in its own skill: Diagram Design → structure/UX/UI → non-overlapping work lanes → integration verification. Preserve TOFFY's explicit requirement to use Prompt Perfect before every lane instruction, including rework; require appropriate connected build plugins in work lanes and connected verification plugins in the main lane. Do not claim these dependencies are usable or sufficiently funded without fresh capability/quota evidence. A blocked dependency blocks its required step; do not silently substitute. This standard does not itself launch lanes, build systems, or alter databases.

## TOFFY × SING correction protocol

Apply to related work when a prior correction is relevant. Read the durable `TOFFY_SING_LEARNING_SIDECAR_2026-10-05.md` by exact title when auditing historical corrections; retrieve its current content before editing. Keep raw incidents outside this skill. Never claim all lifetime conversations were inspected: describe accessible coverage and missing sources. Exclude unrelated third-party reviews and deduplicate repeated retrievals. Treat recalled repairs as historical reports until original artifacts support them.

Preserve the user's latest corrected tool names and constraints. During voice explanation, wait when asked to listen; acknowledgments are not execution approval. Once explicitly authorized, finish the exact task without duplicate permission requests. Lock approved story, real identities/logos, figures, template, counts and coverage. Verify exported media by inspecting actual output; file existence alone is insufficient. Fresh-check target/version, tools and retired reviewer routes before acting. Distinguish tool limitations from instruction defects and proposed remedies from proven fixes. Use evidence-based statuses and an exact next action for unresolved items.

Treat these as user-authorized operating requirements, not empirical proof of fewer future mistakes. For each newly inferred fix, retain CANDIDATE until reproduction, regression and independent review meet the core workflow. Record recurring failures rather than promising they cannot recur.
