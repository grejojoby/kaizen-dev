---
name: kaizen-dev
description: Use when implementing, debugging, refactoring, or reviewing code. Trace the actual implementation before editing, make the smallest complete change, verify it, and report what was checked.
---

# Kaizen Dev

Make the smallest complete change. Verify it. Keep the evidence visible.

Use this workflow for coding tasks. Adapt the depth of investigation and verification to the task's risk; do not turn a small change into a ceremony.

## Workflow

1. **Look before writing.** Read the repository instructions, inspect the current working-tree changes, and examine the code and tests relevant to the request. Trace the behavior from its entry point or caller to the implementation that actually handles it. Confirm that any nearby pattern you plan to reuse is on this active path and fits the same constraints; a similar name or search hit is not proof. Use targeted, read-only exploration. Do not edit code, tests, configuration, or documentation to discover how the project works. A small, direct task needs a small inspection, not a survey of the whole repository. If the relevant path or expected behavior is still unclear, keep investigating without writes or ask the user when repository evidence cannot resolve it.
2. **Bound the outcome.** Restate the requested behavior in observable terms. Identify constraints and the narrowest affected surface. If a missing decision would materially change behavior, cost, data, or safety, ask before proceeding. Otherwise state a reasonable assumption briefly and continue.
3. **Plan proportionately.** For a one-file, low-risk change, proceed without a ceremony. For broad, ambiguous, or high-risk work, give a short plan before editing. Prefer the smallest change that fully satisfies the request. Avoid speculative features, unnecessary dependencies, and unrelated cleanup.
4. **Implement in the repository's style.** Preserve existing public behavior unless the request changes it. Use clear names and existing abstractions. Add a test for the changed behavior when a relevant test pattern exists. Explain non-obvious business constraints in a comment; do not narrate obvious code.
5. **Verify with evidence.** Discover the project's documented checks. Run the most targeted meaningful test or check first, then broader checks when the change warrants them and time/resources allow. Inspect the actual output. Do not suppress failures, silently change tests to make them pass, or say a command passed unless it ran and passed.
6. **Stop on a real blocker.** If a check fails, determine whether it is caused by the change or was already failing. Fix regressions caused by the change. If a required check cannot run, say why and what remains uncertain. Do not proceed as though a quality gate passed. Ask for approval before destructive, external, production, or otherwise high-impact actions.
7. **Review and report.** Inspect the final diff for scope, correctness, accidental files, secrets, and generated artifacts. Summarize the change and list checks as passed, failed, or not run. State any material limitation or next decision plainly.

## Working rules

- Preserve changes you did not make. Never overwrite or discard user work to obtain a clean diff.
- Follow repository instructions and existing conventions unless they conflict with the user's request or create a safety issue. Explain the conflict instead of silently choosing.
- Do not write first and inspect later. Before the first edit, identify the active implementation path, confirm any local pattern is actually used there, find the relevant tests or verification method, and note project constraints.
- Prefer one small, reversible step over a broad rewrite. Do not add flexibility for hypothetical future requirements.
- A failing test is evidence to investigate, not permission to weaken the test. Establish a baseline when practical and distinguish pre-existing failures from regressions.
- Do not claim that a test, build, review, deployment, or other action happened unless it did.
- Match verification to risk. A documentation typo does not need a full integration suite; a data migration or security-sensitive change deserves more careful checks.
- Do not deploy, publish, delete important data, rotate credentials, or trigger an external side effect without the required user approval.
- Reflection is useful when it produces a concrete improvement. Do not add unrelated cleanup or a mandatory retrospective to every task.

## Completion format

Lead with what changed. Keep the report short and concrete. Include:

- The behavior or files changed.
- The exact checks run and their result.
- Any checks not run, remaining risk, or user decision needed.

Do not call unverified work “done.”
