# The Kaizen Dev workflow

The skill is a loop, not a rigid checklist. Use more investigation and stronger verification when the risk is higher. A typo fix should stay small; a permission change, migration, or security boundary needs more care.

## 1. Trace the real path before writing

Start with read-only reconnaissance. Read the repository's agent instructions and inspect the current working-tree changes. Locate the relevant entry point, then follow callers to the implementation that actually handles the requested behavior. Check nearby tests, fixtures, and established patterns. Before reusing a similar helper, verify that the active code path calls it and that it has the same constraints; the first matching filename or search result may be legacy, test-only, or irrelevant. Find the actual test and build commands in project documentation or configuration.

Do not edit code, tests, or documentation just to discover how the project is structured. Keep the inspection focused: a one-line text change does not require reading the entire repository. Before the first write, the agent should be able to name the active implementation path, the behavior it intends to change, the relevant local pattern, and the most useful verification step. If it cannot, it should keep investigating without writes or ask the user when the repository does not answer the question.

## 2. Define a bounded outcome

Translate the request into a result someone can observe. For example: “A user without projects sees the existing empty-state message and a link to create one.” Identify what is in scope and what is not.

Ask a question only when an unanswered choice would materially affect behavior, compatibility, user data, cost, or safety. For routine details, state a reasonable assumption and continue.

## 3. Make the smallest complete change

Follow existing patterns. Add only the code, test, documentation, or migration needed for the requested behavior. Avoid speculative configuration, new dependencies, and unrelated refactoring. “Smallest” must still be complete: do not omit error handling or accessibility when they are part of the requirement, and do add tests when they protect meaningful behavior or risk.

Choose tests for the assurance they provide—not to execute every line or chase 100% coverage. Prefer assertions about observable behavior, meaningful contracts, edge cases, and regressions at the layer where users or integrations encounter them. If an obvious one-line utility has no separate contract and its callers already have useful coverage, a duplicate direct unit test may add no value. Conversely, short code still merits a test when it carries a business rule, boundary, or meaningful failure mode. When you add no test, briefly explain the decision and run the most relevant existing check.

## 4. Verify in a useful order

Start with the narrowest relevant check, such as a behavior-focused unit or integration test or a linter for changed files. Then run broader checks when the risk and runtime justify them. For behavior that depends on a running application, use the project's documented manual or integration verification too. A useful test should fail for a meaningful regression—not merely prove that a trivial function was called.

When something fails, inspect the failure. Compare with a baseline if practical. A known pre-existing failure is still important to report, but it is not automatically a regression caused by the change.

## 5. Review the result

Inspect the final diff. Confirm that it is limited to the intended work, that tests cover the new or changed behavior, and that no credentials, generated files, debug code, or unrelated edits slipped in.

## 6. Report what happened

State what changed and what you actually verified. List checks as passed, failed, or not run. Explain any material limitation or remaining risk. Never imply a command succeeded if it was not run.

## Adjust the workflow to risk

- **Low risk:** inspect the direct file and its relevant instructions or pattern, make the direct change, run a focused check, review the diff.
- **Moderate risk:** trace the affected behavior, identify compatibility constraints, plan a few steps, add or update regression tests, run relevant suite(s), inspect the diff.
- **High impact:** clarify requirements, evaluate rollback and data/security consequences, request approval for external or destructive actions, and verify with an appropriate staging or review process.

The agent must not treat “stop the line” as a reason to stop all work on every unrelated failing check. It must stop claiming the current change is verified, investigate whether the check is relevant or pre-existing, and clearly report the result.
