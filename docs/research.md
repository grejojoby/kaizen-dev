# Research and sources

This project treats Japanese-origin production and improvement concepts as inspirations for engineering practices, not as evidence that one nationality has a single coding style. The mapping from manufacturing to software is an analogy. The agent instructions are designed to be useful even if a reader never uses the Japanese terms.

## What informed the workflow

Toyota's official explanation names jidoka and Just-in-Time as two pillars of the Toyota Production System. It describes jidoka as detecting an abnormality, stopping work to prevent defects from flowing onward, and improving the process so the issue does not recur. It describes Just-in-Time as making what is needed when it is needed and in the amount needed. The software rules about visible checks, investigating failures, and avoiding speculative scope are our adaptation, not Toyota software guidance. [1]

Toyota Europe describes genchi genbutsu as going to the place where a problem exists, confirming the facts, and analyzing root causes. It defines kaizen as continuous improvement and identifies incremental as well as breakthrough improvement. These are company descriptions of Toyota's principles, not evidence that all Japanese developers follow one practice. [2]

Toyota UK's explanation of hansei describes self-reflection as recognizing mistakes and taking action to avoid recurrence. This project adapts it into an optional, lightweight learning step; it does not prescribe a retrospective after every coding task. [3]

The article supplied in the project request discusses kaizen, jidoka, just-in-time scope, clear code, waste, and reflection. It also makes broad claims about Japanese developers and cites anecdotes and numerical comparisons without providing traceable study details in the article text we reviewed. We use it as a prompt for themes only. We do not repeat its performance statistics or generalizations as facts. [4]

Microsoft's VS Code agent guidance recommends starting with a bounded task and observable result, providing relevant files and constraints, reviewing changed files, and running relevant tests. That supports translating principles into explicit steps an agent can follow. It is product guidance, not a controlled trial of this skill. [5]

The Agent Skills specification defines a portable folder containing a `SKILL.md` file, with required `name` and `description` metadata and Markdown instructions. Claude Code documents support for skills in personal and project locations and says Claude Code skills follow the Agent Skills standard. We use the standard metadata and provide Claude Code install steps; other host discovery paths should be verified separately. [6] [7]

Vercel Labs' Skills CLI documents adding skills from a GitHub repository or local directory, selecting one skill and one or more agent targets, and copying or symlinking the skill into host-specific locations. Its supported-agent matrix identifies many destinations. This repository smoke-tested one local installation to Claude Code; it has not validated every host in that matrix. [8] [9]

The two reference repositories illustrate practical distribution choices: a clear one-line benefit, copy-paste setup, and an obvious skill entry point. Their repository pages are design references, not evidence that a particular structure causes popularity. [10] [11]

## Sources

[1] Toyota Motor Corporation, [Toyota Production System](https://global.toyota/en/company/vision-and-philosophy/production-system/).

[2] Toyota Motor Europe, [The Toyota Way](https://www.toyota-europe.com/about-us/toyota-vision-and-philosophy/the-toyota-way).

[3] Toyota (GB) PLC, [Hansei – Toyota Production System guide](https://mag.toyota.co.uk/hansei-toyota-production-system/).

[4] Sohail Saifi, [“Why Japanese Developers Write Code Completely Differently (And Why It Works Better)”](https://medium.com/@sohail_saifi/why-japanese-developers-write-code-completely-differently-and-why-it-works-better-de84d6244fab), Medium, July 17, 2025. The text was provided through the reader URL in the request: https://ekky.dev/app/medium/?url=https%3A%2F%2Fmedium.com%2F%40sohail_saifi%2Fwhy-japanese-developers-write-code-completely-differently-and-why-it-works-better-de84d6244fab.

[5] Microsoft, [Best practices for using AI in VS Code](https://code.visualstudio.com/docs/agents/best-practices).

[6] Agent Skills, [Specification](https://agentskills.io/specification).

[7] Anthropic, [Extend Claude with skills](https://code.claude.com/docs/en/skills).

[8] Vercel Labs, [Skills CLI command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

[9] Vercel Labs, [Skills CLI supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

[10] ayghri, [i-have-adhd](https://github.com/ayghri/i-have-adhd).

[11] Julius Brussee, [caveman](https://github.com/juliusbrussee/caveman).

Sources accessed November 3, 2026. Product documentation can change; check the host documentation before publishing installation paths for additional agents.
