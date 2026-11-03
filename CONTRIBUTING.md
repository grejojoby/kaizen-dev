# Contributing

Thank you for helping make coding-agent work more reliable. Contributions should be useful to a developer, easy to review, and honest about their evidence.

## Before opening an issue or pull request

- Search existing issues and discussions for duplicates.
- For a proposed behavior change, describe the agent behavior you want to observe and the problem it solves.
- Keep one contribution focused. Split unrelated improvements into separate proposals.

## Changes to the skill

- Keep `skills/kaizen-dev/SKILL.md` concise and directly actionable.
- Preserve the core loop: inspect the real project, bound the change, make the smallest complete improvement, verify, review, and report.
- Do not make the skill rigid when risk, project conventions, or task size call for judgment.
- Update [`evals/cases.json`](evals/cases.json) when a change affects expected behavior. Add a case that would catch the failure mode the change is meant to prevent.
- Add tests when they protect observable behavior, a meaningful contract, edge case, or regression—not merely to execute a trivial line or improve a coverage percentage. Skip redundant direct tests when caller-level tests already give useful assurance, and explain why no new test is needed.
- Document the practical principle and its limits in [`docs/principles.md`](docs/principles.md).

## Claims and terminology

- Cite sources for factual claims about Toyota, Japanese concepts, agent behavior, or quantified outcomes.
- Do not turn a concept into a claim about how all Japanese people or developers behave.
- Do not publish performance or quality claims without a reproducible evaluation, setup details, and negative results.
- Keep Japanese terms optional; explain them in plain English and avoid using culture as decoration.

## Validate and submit

Run the repository's dependency-free checks:

```bash
python scripts/validate_repo.py
```

In your pull request, explain the user-facing benefit, files changed, checks run, and any known limitations. See [the pull request template](.github/PULL_REQUEST_TEMPLATE.md).
