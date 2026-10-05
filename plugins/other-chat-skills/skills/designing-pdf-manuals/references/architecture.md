# Architecture Reference

## Operating Model

The skill is the policy/control layer. Tools are execution adapters. Keep orchestration decisions, checkpoints, and release gates explicit even when individual creative steps are agentic.

## State Model

| State | Meaning | Allowed next states |
|---|---|---|
| `INTAKE` | Brief and source context received | `ANALYZED`, `NEEDS_ATTENTION` |
| `ANALYZED` | Goals, scope, facts, risks extracted | `PLANNED`, `NEEDS_ATTENTION` |
| `PLANNED` | Section map and Page Map complete | `ASSETS_READY`, `NEEDS_ATTENTION` |
| `ASSETS_READY` | Required source/generated assets prepared | `CONTENT_READY`, `NEEDS_ATTENTION` |
| `CONTENT_READY` | Structured copy blocks complete | `LAYOUT_READY`, `NEEDS_ATTENTION` |
| `LAYOUT_READY` | Pages assembled | `QA_PASSED`, `QA_FAILED` |
| `QA_FAILED` | Content/text/visual gate failed | `LAYOUT_READY`, `CONTENT_READY`, `NEEDS_ATTENTION` |
| `QA_PASSED` | Content, Thai, and visual gates passed | `PREFLIGHT_PASSED`, `PREFLIGHT_FAILED` |
| `PREFLIGHT_FAILED` | PDF technical/final-render verification failed | `LAYOUT_READY`, `NEEDS_ATTENTION` |
| `PREFLIGHT_PASSED` | PDF verified | `AWAITING_APPROVAL`, `RELEASED` |
| `AWAITING_APPROVAL` | Human review required | `RELEASED`, `NEEDS_ATTENTION` |
| `RELEASED` | Versioned final released | terminal |
| `NEEDS_ATTENTION` | Safe automation cannot continue | resume only after issue resolved |

Never release from a state earlier than `PREFLIGHT_PASSED`.

## Agent Responsibilities

- **Orchestrator:** state, sequence, checkpointing, stop conditions, retries, approvals.
- **Analyze Agent:** purpose, audience, scope, constraints, evidence gaps, risk.
- **Planning Agent:** section map, Page Map, archetypes, asset plan, acceptance criteria.
- **Writer Agent:** structured prose, captions, labels, tables, warnings.
- **Image Agent:** image brief, generation/edit routing, real-vs-virtual visual choice.
- **Layout Agent:** page composition and design-system conformance.
- **Evaluator Agent:** completeness, factual consistency, terminology, acceptance criteria.
- **Thai QA:** Thai wording and Thai/Latin typography/rendering.
- **Visual QA:** rendered-page legibility and consistency.
- **PDF Preflight:** technical inspection and final artifact reopen.

## Checkpoints

Create a checkpoint after:
1. analysis,
2. Page Map,
3. assets,
4. layout,
5. QA,
6. preflight,
7. release.

## Failure Classification

- **Transient:** timeout, temporary service capacity, retriable network failure. Retry with a bounded budget.
- **Validation:** malformed input, unsupported format, failed acceptance criterion. Fix input; do not blind retry.
- **Authorization:** permission/authentication failure. Stop and request the needed authorization path.
- **Business/policy:** release blocked by approval or policy. Stop at the gate.
- **Partial side effect:** external write may have succeeded. Use stable operation IDs and verify before repeating.

## Safety and Governance

- Read-only first when sufficient.
- Keep secrets and unnecessary personal data out of prompts, logs, and history.
- Separate read tools from write tools where possible.
- Treat generated claims, citations, measurements, screenshots, and UI labels as untrusted until verified.
