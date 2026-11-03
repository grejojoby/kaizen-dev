# Kaizen Dev

**The smallest complete change. Verified.**

A portable coding-agent skill: inspect the real project, make the smallest complete change, verify it, and report evidence.

[View the Kaizen Dev landing page](https://grejojoby.github.io/kaizen-dev/) · [Install the skill](#install)

## Install

With Node.js and npm available, install from GitHub for Claude Code:

```bash
npx --yes skills add grejojoby/kaizen-dev --skill kaizen-dev --agent claude-code --global --copy
```

The installer asks you to confirm. Review the skill before use; it runs with your agent's permissions. To choose other supported agents interactively, omit `--agent claude-code --global`. For a local clone, replace `grejojoby/kaizen-dev` with `./`.

Start Claude Code and run `/kaizen-dev`, or ask for a coding task and let the skill activate when relevant. See [all install options](docs/install.md).

## The loop

```text
LOOK → BOUND → CHANGE → VERIFY → REPORT
```

- **Look before writing:** read project instructions, inspect existing changes, trace the relevant code path, and find its tests. Do not edit to discover the codebase.
- **Bound:** define the observable result; ask only when a material choice is unclear.
- **Change:** make the smallest complete fix that follows the project's patterns.
- **Verify:** run relevant checks; investigate failures and never claim a check passed unless it did.
- **Report:** summarize the diff, checks, and any remaining risk.

No speculative features. No unrelated cleanup. No hidden failing tests.

## Handy commands

```bash
# Install to this project, interactively choose agent(s)
npx --yes skills add grejojoby/kaizen-dev --skill kaizen-dev

# See, check, update, or remove the installed skill
npx skills list
npx skills check
npx skills update kaizen-dev
npx skills remove kaizen-dev --agent claude-code --global

# Validate this repository
python scripts/validate_repo.py
```

## Why “Kaizen”?

The skill adapts practices associated with *genchi genbutsu* (inspect the actual situation), *kaizen* (continuous improvement), *jidoka* (make problems visible), and *hansei* (learn from mistakes). The Japanese terms are optional context, not claims about how all Japanese developers work. The software workflow is our adaptation of manufacturing principles, not a claim that software is a factory.

## Try it. Check it.

The [`SKILL.md`](skills/kaizen-dev/SKILL.md) is the whole runtime skill. Read a [worked example](examples/focused-bug-fix.md), try the [behavior-evaluation scenarios](evals/cases.json), and use the [scoring rubric](docs/evaluation.md). No model-performance gain is claimed; results should be measured and reported with failures and setup details.

[Principles](docs/principles.md) · [Workflow](docs/workflow.md) · [Research](docs/research.md) · [Contributing](CONTRIBUTING.md) · [Pages deployment](docs/pages-deployment.md) · [Release checklist](docs/release-checklist.md) · [MIT License](LICENSE)
