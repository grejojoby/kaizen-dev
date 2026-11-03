# Example: focused bug fix

## Request

“Fix the project list showing a blank page when the API returns no projects.”

## Weak response pattern

The agent assumes the framework and API shape, rewrites the list page, adds an empty-state framework and a new dependency, updates several unrelated components, then says “fixed” without running tests.

## Kaizen Dev response pattern

1. Inspect the repository instructions, project list component, API response handling, existing empty-state examples, tests, and working-tree diff.
2. Confirm how the current code represents an empty result and identify the narrow observable behavior: render the existing empty state instead of a blank page.
3. Add or update a focused test that fails for the blank-page case. Make the smallest change that handles the actual response shape.
4. Run the focused test and any directly relevant type check. If either fails, read the output and distinguish a regression from a baseline failure.
5. Review the diff and report the files changed, exact checks run, and any checks not run.

## What makes this “smallest complete”?

It uses the project's established empty-state design, fixes the observable bug, and tests the empty result because that check would catch the user-visible blank-page regression. It does not add a test merely to call a trivial helper, assume an architecture, redesign unrelated states, or hide an unverified test result.

This is a process example, not a benchmark or a claim about any particular agent's output.
