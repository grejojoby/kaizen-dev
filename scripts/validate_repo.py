#!/usr/bin/env python3
"""Validate the structure and internal references of the Kaizen Dev repository."""

from __future__ import annotations

import json
import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://grejojoby.github.io/kaizen-dev/"
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
    "docs/pages-deployment.md",
    "examples/focused-bug-fix.md",
    "evals/cases.json",
    ".github/workflows/deploy-pages.yml",
    "site/index.html",
    "site/styles.css",
    "site/app.js",
    "site/404.html",
    "site/robots.txt",
    "site/sitemap.xml",
    "site/.nojekyll",
    "site/assets/mark.svg",
    "site/assets/og-card.png",
    "scripts/social-card.html",
    "scripts/render-social-card.sh",
)
REQUIRED_SKILL_HEADINGS = (
    "## Workflow",
    "## Working rules",
    "## Completion format",
)
LOCAL_LINK = re.compile(r"\]\(([^)]+)\)")


class SiteResourceParser(HTMLParser):
    """Collect local href/src references from the static site HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.resources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        for name in ("href", "src"):
            value = attributes.get(name)
            if value:
                self.resources.append(value)


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


def validate_site(errors: list[str]) -> None:
    site = ROOT / "site"
    index = site / "index.html"
    if not index.is_file():
        return

    html = index.read_text(encoding="utf-8")
    requirements = {
        "canonical URL": f'<link rel="canonical" href="{SITE_URL}">',
        "Open Graph URL": f'<meta property="og:url" content="{SITE_URL}">',
        "Open Graph image": f'<meta property="og:image" content="{SITE_URL}assets/og-card.png">',
        "Twitter card": 'name="twitter:card" content="summary_large_image"',
        "responsive viewport": 'name="viewport" content="width=device-width, initial-scale=1"',
        "skip link": 'class="skip-link" href="#main"',
        "local stylesheet": 'href="styles.css"',
        "local script": 'src="app.js"',
        "favicon": 'href="assets/mark.svg"',
    }
    for label, snippet in requirements.items():
        if snippet not in html:
            errors.append(f"site/index.html is missing {label}")

    title = re.search(r"<title>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if not title or not title.group(1).strip():
        errors.append("site/index.html must have a non-empty title")
    elif not 30 <= len(title.group(1).strip()) <= 60:
        errors.append("site/index.html title should be 30–60 characters")

    description = re.search(
        r'<meta\s+name="description"\s+content="([^"]*)"', html, flags=re.IGNORECASE
    )
    if not description or not 50 <= len(description.group(1)) <= 160:
        errors.append("site/index.html description must be 50–160 characters")

    if len(re.findall(r"<h1\b", html, flags=re.IGNORECASE)) != 1:
        errors.append("site/index.html must contain exactly one h1")

    robots = site / "robots.txt"
    if robots.is_file() and f"Sitemap: {SITE_URL}sitemap.xml" not in robots.read_text(encoding="utf-8"):
        errors.append("site/robots.txt must point to the canonical sitemap")

    sitemap = site / "sitemap.xml"
    if sitemap.is_file() and f"<loc>{SITE_URL}</loc>" not in sitemap.read_text(encoding="utf-8"):
        errors.append("site/sitemap.xml must contain the canonical home URL")

    not_found = site / "404.html"
    if not_found.is_file():
        text = not_found.read_text(encoding="utf-8")
        if 'name="robots" content="noindex"' not in text:
            errors.append("site/404.html must be marked noindex")

    card = site / "assets/og-card.png"
    if card.is_file():
        data = card.read_bytes()
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append("site/assets/og-card.png is not a valid PNG")
        else:
            width, height = struct.unpack(">II", data[16:24])
            if (width, height) != (1200, 630):
                errors.append("site/assets/og-card.png must be 1200×630 pixels")

    workflow = ROOT / ".github/workflows/deploy-pages.yml"
    if workflow.is_file():
        text = workflow.read_text(encoding="utf-8")
        for label, snippet in (
            ("site-only artifact path", "path: site"),
            ("configure-pages action", "actions/configure-pages@v5"),
            ("Pages artifact action", "actions/upload-pages-artifact@v4"),
            ("Pages deployment action", "actions/deploy-pages@v4"),
            ("Pages permission", "pages: write"),
            ("OIDC permission", "id-token: write"),
            ("manual workflow trigger", "workflow_dispatch"),
        ):
            if snippet not in text:
                errors.append(f"Pages workflow is missing {label}")


def validate_site_resources(errors: list[str]) -> None:
    site = ROOT / "site"
    for relative in ("index.html", "404.html"):
        path = site / relative
        if not path.is_file():
            continue
        parser = SiteResourceParser()
        parser.feed(path.read_text(encoding="utf-8"))
        for value in parser.resources:
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or value.startswith("#") or not parsed.path:
                continue
            target = (site / unquote(parsed.path)).resolve()
            if not target.is_relative_to(site.resolve()):
                errors.append(f"Local site resource escapes site/: {relative} -> {value}")
            elif not target.exists():
                errors.append(f"Missing site resource in {relative}: {value}")


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
    validate_site(errors)
    validate_site_resources(errors)
    validate_local_markdown_links(errors)
    if errors:
        for error in errors:
            fail(error)
        print(f"Repository validation failed with {len(errors)} issue(s).")
        return 1
    print(
        "Repository validation passed: required files, skill metadata, eval cases, "
        "static site assets, Pages workflow, and local Markdown links are valid."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
