# Instructions for agents working in this repository

## Purpose

This repository publishes one small coding-agent skill and its static product landing page: inspect the real project, make the smallest complete change, verify it, review the diff, and report evidence. Keep the public experience approachable and the internal structure predictable.

## Before editing

Read `README.md` and the files relevant to the requested change. Check `git status` and preserve all existing edits. Treat the skill under `skills/kaizen-dev/SKILL.md` as the canonical runtime instruction; do not maintain a second copy in a platform adapter.

## Structure and ownership

- `skills/kaizen-dev/`: canonical, portable Agent Skill.
- `site/`: static GitHub Pages landing page; publish only this directory.
- `docs/`: rationale, workflow, installation, evaluation, research, Pages deployment, and repository map.
- `examples/`: illustrative task walkthroughs, not performance evidence.
- `evals/`: qualitative behavior scenarios in JSON.
- `scripts/`: dependency-free repository checks and social-card source.
- `.github/`: contribution templates and CI/deploy workflows.

If a change crosses these areas, keep the skill, examples, evaluations, site, and docs consistent. Avoid adding a new top-level directory unless it has a clear owner and purpose.

## Quality bar

Keep the skill concise and executable as instructions. Prefer plain English. Japanese terms must be defined and framed as concepts adapted for software, not stereotypes. Any claim about results or agent performance needs reproducible evidence and disclosed limitations. Tests should protect meaningful behavior and risk, not coverage percentages; add or adjust an evaluation case when expected agent behavior changes.

Keep the landing page static, responsive, accessible, and dependency-free. Do not add tracking or publish private data. Keep canonical and Open Graph URLs, `robots.txt`, and `sitemap.xml` aligned to the current GitHub Pages origin.

Run `python scripts/validate_repo.py` before considering repository work complete. Report the exact checks run and any limitations. Do not claim that model evaluations were run unless they were.

## Safety

Never include secrets, private user code, or personal data in examples or tests. Do not install dependencies or add telemetry for this text-only skill and static site without a clear need and review. Do not publish, release, or change external services without the user's explicit direction.
