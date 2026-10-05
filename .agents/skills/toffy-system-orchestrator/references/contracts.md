# Lane contracts

Use these fields as a structured command and report template. Never populate unknown fields with invented values.

## Ownership register
Lane | Owner | Allowed write paths/resources | Read dependencies | Shared-resource owner | Baseline/version | Lock/state | Handoff prerequisite

Check disjoint writes, schema/API compatibility, lock ownership and exact upstream artifacts before starting. Pause a conflicting writer until ownership is resolved; do not let two lanes independently repair the same shared resource.

## Lane command
- Command ID, revision, timestamp/timezone, main-lane authority
- Objective and expected behavior
- Canonical target and exact source revision/hash
- Operation mode; allowed writes and forbidden targets/actions
- Required connected tools, actual preflight evidence and quota constraints
- Owner, lock, upstream prerequisites and downstream contract
- Acceptance criteria including error/negative paths
- Required evidence and artifact format
- Cleanup, rollback and STOP conditions
- Prompt Perfect input/output reference and main-lane review result

Do not dispatch if mandatory fields, ownership, prerequisite or required tool readiness are missing. Keep a useful draft with missing fields OPEN.

## Lane result
- Command revision, source revision/hash, artifact revision/hash and diff
- Actual tools/runtime and commands with exit codes
- Expected versus actual for each acceptance criterion
- Raw evidence references; label synthetic versus live results
- Persistent mutations, temporary state and verified cleanup/baseline
- Passed scope, failures, unknowns, blockers and exact next action

## Main acceptance
Record independent reviewer/tool, inspected raw evidence, accepted scope, rejected criteria, integration prerequisites, combined test evidence and decision authority. Never mark project closure from isolated lane results alone.

## Readiness and review scope

For each tool record mandatory/optional, needed capability, reason selected, verified connection/permission/quota and evidence timestamp. Mark project PARTIAL when some scope passed; separately mark a blocked step BLOCKED. Define integrated test names, environment, expected results and applicability authority before dispatch.

Require an evaluator with clean task-local context and no producer conclusions; provide original requirements and raw artifacts. Record independence and inspected versions. Define synthetic fixtures, student-data exclusions, secret redaction, retention and cleanup in each school-system contract.

Resolve specialist skills by frontmatter: matt-skills-curated:skill-conductor, matt-skills-curated:writing-for-agents, superpowers:writing-skills, and skill-creator. If a mandatory specialist is unavailable, report the blocked authoring step rather than claiming it was applied.
