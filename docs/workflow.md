# The Kaizen Dev workflow

The skill is a loop, not a rigid checklist. Use more investigation and stronger verification when the risk is higher. A typo fix should stay small; a permission change, migration, or security boundary needs more care.

## 1. Inspect before acting

Read the repository's agent instructions, the relevant code, nearby tests, and the current working-tree changes. Find the project's actual test and build commands in its documentation or configuration. Do not replace discovery with assumptions from another codebase.

Before editing, know what the user asked for and what files are already modified. Preserve unrelated work.

## 2. Define a bounded outcome

Translate the request into a result someone can observe. For example: “A user without projects sees the existing empty-state message and a link to create one.” Identify what is in scope and what is not.

Ask a question only when an unanswered choice would materially affect behavior, compatibility, user data, cost, or safety. For routine details, state a reasonable assumption and continue.

## 3. Make the smallest complete change

Follow existing patterns. Add only the code, test, documentation, or migration needed for the requested behavior. Avoid speculative configuration, new dependencies, and unrelated refactoring. “Smallest” must still be complete: do not omit error handling, accessibility, or tests when they are part of the requirement.

## 4. Verify in a useful order

Start with the narrowest relevant check, such as one unit test or a linter for changed files. Then run broader checks when the risk and runtime justify them. For behavior that depends on a running application, use the project's documented manual or integration verification too.

When something fails, inspect the failure. Compare with a baseline if practical. A known pre-existing failure is still important to report, but it is not automatically a regression caused by the change.

## 5. Review the result

Inspect the final diff. Confirm that it is limited to the intended work, that tests cover the new or changed behavior, and that no credentials, generated files, debug code, or unrelated edits slipped in.

## 6. Report what happened

State what changed and what you actually verified. List checks as passed, failed, or not run. Explain any material limitation or remaining risk. Never imply a command succeeded if it was not run.

## Adjust the workflow to risk

- **Low risk:** inspect nearby code, make the direct change, run a focused check, review the diff.
- **Moderate risk:** identify behavior and compatibility constraints, plan a few steps, add or update regression tests, run relevant suite(s), inspect the diff.
- **High impact:** clarify requirements, evaluate rollback and data/security consequences, request approval for external or destructive actions, and verify with an appropriate staging or review process.

The agent must not treat “stop the line” as a reason to stop all work on every unrelated failing check. It must stop claiming the current change is verified, investigate whether the check is relevant or pre-existing, and clearly report the result.
