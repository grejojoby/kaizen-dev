# Public-release checklist

A polished repository improves first-time use, but no structure or launch tactic guarantees stars. Keep the promise clear, make the first try easy, and earn trust with accurate claims and responsive maintenance.

## Before making the repository public

- Confirm the final GitHub owner and repository name. Update the README with the direct one-command install from GitHub, then test it from a clean temporary account or container.
- Set the GitHub description to a short, plain-English promise. Suggested draft: **A portable coding-agent skill: inspect first, make the smallest complete change, verify it, and report evidence.**
- Add relevant GitHub topics such as `agent-skills`, `coding-agents`, `software-engineering`, and `developer-tools`.
- Confirm the MIT license is the intended license. Ensure the code of conduct and security policy point to a private, usable contact method.
- Run `python scripts/validate_repo.py`. Test the documented Claude Code install from a clean profile. Test at least one additional agent before describing that host as verified.
- Make sure the install command selects only this skill. Keep the CLI's confirmation enabled in user-facing commands.
- Review the first screen of the README on GitHub mobile and desktop. Keep the headline, quick install, short demo, and docs links visible before long background material.
- Verify the GitHub Pages source is set to Actions. After a successful deploy, check the public URL, mobile layout, page metadata, and sitemap.
- Do not add a star badge, benchmark result, compatibility claim, logo credit, or performance statistic that cannot be substantiated.

## After publishing

- Create a release only when the install path and docs have been tested. Summarize user-visible changes in `CHANGELOG.md`.
- Invite a small number of developers to try the skill on real tasks. Ask for redacted examples and record both useful behavior and failures in the evaluation set.
- Share a useful demo or lesson in relevant communities, following their rules. Avoid mass-posting identical promotion or asking for stars without a meaningful contribution.
- Respond to issues with reproducible questions and small, reviewable changes. If an installation or supported-host claim changes, update the docs and test the new path.
- Publish evaluation results only with the host, model and version, task setup, number of runs, failures, and limitations disclosed.
