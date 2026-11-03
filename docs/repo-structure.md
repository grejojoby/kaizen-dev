# Repository structure

The repository keeps the installable skill separate from the material that explains, tests, and maintains it. The static product site also has its own directory and deploy workflow. Add a directory only when it has a clear purpose and owner.

```text
.
├── .github/                 Issue forms, PR template, CI, Pages deploy
├── docs/                    Principles, workflow, install, research, Pages, release checklist
├── evals/                   Machine-readable qualitative agent scenarios
├── examples/                Worked examples for human readers
├── scripts/                 Dependency-free checks and social-card source
├── site/                    Static GitHub Pages product landing page
├── skills/kaizen-dev/       Canonical Agent Skill
├── AGENTS.md                Instructions for agents editing this repository
├── CONTRIBUTING.md          Contribution workflow
├── LICENSE                  MIT license
└── README.md                User-facing overview and quick install
```

`skills/kaizen-dev/SKILL.md` is the one canonical skill. Do not copy it into multiple agent-specific folders in this repository, where copies can drift. The installation docs explain the Vercel Skills CLI and a manual Claude Code path. Add agent-specific setup only when its instructions are tested, and have it use the same canonical guidance.

`site/` is the only content published by GitHub Pages. It uses plain HTML, CSS, and a small script; the workflow does not build or publish repository documentation. See the [Pages deployment guide](pages-deployment.md) before changing the site URL or workflow.

When behavior changes, update the skill and the relevant evaluation cases together. Update principles and research documents when the rationale or a source changes. The validator checks required files, skill metadata, evaluation cases, static site assets, deployment wiring, and local Markdown links. Before publishing a repository release, complete the [public-release checklist](release-checklist.md).
