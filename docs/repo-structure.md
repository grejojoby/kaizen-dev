# Repository structure

The repository keeps the installable skill separate from the material that explains, tests, and maintains it. The layout is deliberately small; add a directory only when it has a clear purpose and owner.

```text
.
├── .github/                 Issue forms, pull request template, CI
├── docs/                    Principles, workflow, install, research, release checklist
├── evals/                   Machine-readable qualitative agent scenarios
├── examples/                Worked examples for human readers
├── scripts/                 Dependency-free repository validation
├── skills/kaizen-dev/       Canonical Agent Skill
├── AGENTS.md                Instructions for agents editing this repository
├── CONTRIBUTING.md          Contribution workflow
├── LICENSE                  MIT license
└── README.md                User-facing overview and quick install
```

`skills/kaizen-dev/SKILL.md` is the one canonical skill. Do not copy it into multiple agent-specific folders in this repository, where copies can drift. The installation docs explain the Vercel Skills CLI and a manual Claude Code path. Add agent-specific setup only when its instructions are tested, and have it use the same canonical guidance.

When behavior changes, update the skill and the relevant evaluation cases together. Update principles and research documents when the rationale or a source changes. The validator checks the required files, skill metadata, case structure, and local Markdown links. Before publishing, complete the [public-release checklist](release-checklist.md).
