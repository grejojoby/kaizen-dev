#!/usr/bin/env python3
"""Validate the structure and internal references of the Kaizen Dev repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "LICENSE",
    "CHANGELOG.md",
    "skills/kaizen-dev/SKILL.md",
    "docs/principles.md",
    "docs/workflow.md",
    "docs/install.md",
    "docs/evaluation.md",
    "docs/research.md",
    "docs/repo-structure.md",
    "docs/release-checklist.md",
    "examples/focused-bug-fix.md",
    "evals/cases.json",
)
REQUIRED_SKILL_HEADINGS = (
    "## Workflow",
    "## Working rules",
    "## Completion format",
)
LOCAL_LINK = re.compile(r"\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)


def validate_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Required file is missing: {relative}")


def validate_skill(errors: list[str]) -> None:
    path = ROOT / "skills/kaizen-dev/SKILL.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return
    closing = text.find("\n---\n", 4)
    if closing < 0:
        errors.append("SKILL.md has no closing frontmatter delimiter")
        return
    frontmatter = text[4:closing]
    name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", frontmatter)
    description = re.search(r"(?m)^description:\s*(\S.*)$", frontmatter)
    if not name:
        errors.append("SKILL.md must define a lowercase hyphenated name")
    elif name.group(1) != "kaizen-dev":
        errors.append("SKILL.md name must match the skill folder: kaizen-dev")
    if not description:
        errors.append("SKILL.md must define a non-empty description")
    elif len(description.group(1)) > 1024:
        errors.append("SKILL.md description exceeds the Agent Skills limit of 1024 characters")
    for heading in REQUIRED_SKILL_HEADINGS:
        if heading not in text:
            errors.append(f"SKILL.md is missing required section: {heading}")


def validate_cases(errors: list[str]) -> None:
    path = ROOT / "evals/cases.json"
    if not path.is_file():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"evals/cases.json is invalid JSON: {exc}")
        return
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("evals/cases.json must contain a non-empty cases array")
        return
    seen: set[str] = set()
    for index, case in enumerate(cases):
        label = f"eval case {index + 1}"
        if not isinstance(case, dict):
            errors.append(f"{label} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{label} must have a non-empty id")
        elif case_id in seen:
            errors.append(f"Duplicate evaluation case id: {case_id}")
        else:
            seen.add(case_id)
        for field in ("task", "setup"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"{label} must have a non-empty {field}")
        for field in ("must", "must_not"):
            values = case.get(field)
            if not isinstance(values, list) or not values or not all(
                isinstance(value, str) and value.strip() for value in values
            ):
                errors.append(f"{label} must have a non-empty string array for {field}")


def validate_local_markdown_links(errors: list[str]) -> None:
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw in LOCAL_LINK.findall(text):
            destination = raw.strip().split()[0].strip("<>")
            if not destination or destination.startswith(("#", "https://", "http://", "mailto:", "tel:")):
                continue
            destination = unquote(destination.split("#", 1)[0])
            if not destination:
                continue
            target = (markdown.parent / destination).resolve()
            if not target.exists():
                relative = markdown.relative_to(ROOT)
                errors.append(f"Broken local link in {relative}: {raw}")


def main() -> int:
    errors: list[str] = []
    validate_files(errors)
    validate_skill(errors)
    validate_cases(errors)
    validate_local_markdown_links(errors)
    if errors:
        for error in errors:
            fail(error)
        print(f"Repository validation failed with {len(errors)} issue(s).")
        return 1
    print("Repository validation passed: required files, skill metadata, eval cases, and local Markdown links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
