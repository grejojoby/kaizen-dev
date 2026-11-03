# Install Kaizen Dev

The canonical skill is `skills/kaizen-dev/SKILL.md`. It uses the open Agent Skills format. Host applications may use different discovery paths and may implement skills differently.

## Recommended: Vercel Skills CLI

Install the published skill globally for Claude Code:

```bash
npx --yes skills add grejojoby/kaizen-dev --skill kaizen-dev --agent claude-code --global --copy
```

To install into the current project instead of your personal Claude Code setup, omit `--global`:

```bash
npx --yes skills add grejojoby/kaizen-dev --skill kaizen-dev --agent claude-code --copy
```

To choose among other agents supported by the Skills CLI, omit the `--agent` and scope flags; the installer will offer available destinations:

```bash
npx --yes skills add grejojoby/kaizen-dev --skill kaizen-dev
```

For a local clone, replace `grejojoby/kaizen-dev` with `./`. The local-source path was smoke-tested against this repository in an isolated temporary home directory. The GitHub form will work once this repository is public.

The CLI normally asks you to confirm installation. This repository's user-facing commands do not include the CLI's `-y` flag, which skips that confirmation. Because the command downloads and runs the `skills` CLI from npm, review the installer source and the skill before use. A skill provides instructions to an agent and operates with the permissions that agent has; this repository's skill requests no tools or special permissions.

To inspect, check, update, or remove an installation:

```bash
npx skills list
npx skills check
npx skills update kaizen-dev
npx skills remove kaizen-dev --agent claude-code --global
```

The CLI's agent list and installation paths can change. Basic skills generally use the shared Agent Skills specification, but host support and runtime behavior are not identical. See the [supported-agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) and the destination application's official documentation. See also the [Skills CLI command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

## Claude Code: manual install

For a personal install without the Skills CLI, run from the root of the cloned repository:

```bash
mkdir -p ~/.claude/skills/kaizen-dev
cp skills/kaizen-dev/SKILL.md ~/.claude/skills/kaizen-dev/SKILL.md
```

To share it with one project, copy it to that project's `.claude/skills/kaizen-dev/SKILL.md` and commit the file. Start or restart Claude Code and invoke `/kaizen-dev`.

## Windows PowerShell: manual personal install

Run from the cloned repository root:

```powershell
$target = Join-Path $HOME ".claude/skills/kaizen-dev"
New-Item -ItemType Directory -Force -Path $target | Out-Null
Copy-Item .\skills\kaizen-dev\SKILL.md (Join-Path $target "SKILL.md")
```

## Update or uninstall a manual copy

To update, repeat the copy command. To uninstall the personal copy, remove only the Kaizen Dev skill directory:

```bash
rm -r ~/.claude/skills/kaizen-dev
```

Review the path before running a removal command. For a project install, remove `.claude/skills/kaizen-dev/` from that project instead.

## Other agents

The skill uses the open Agent Skills `SKILL.md` format: a folder with YAML `name` and `description` metadata followed by Markdown instructions. The Skills CLI lists multiple agents that support this format. Other compatible agents may also support it, but their discovery locations and behavior differ. We will add an agent-specific setup only after its instructions have been verified; consult [the Agent Skills specification](https://agentskills.io/specification) and the chosen host's official documentation.
