from __future__ import annotations

import json
import textwrap
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError
from urllib.request import Request, urlopen


OWNER = "CodexDLC"
OUTPUT_PATH = Path("docs/updates/_generated/releases.md")


@dataclass(frozen=True)
class Library:
    repo: str
    docs_url: str
    summary: str


LIBRARIES: list[Library] = [
    Library("codex-core", "https://codexdlc.github.io/codex-core/latest/", "Foundation layer for DTOs, settings, utilities, and shared runtime primitives."),
    Library("codex-platform", "https://codexdlc.github.io/codex-platform/latest/", "Infrastructure layer for workers, Redis integrations, streams, and platform plumbing."),
    Library("codex-ai", "https://codexdlc.github.io/codex-ai/latest/", "Provider-agnostic AI abstraction layer for model integrations and AI-facing interfaces."),
    Library("codex-services", "https://codexdlc.github.io/codex-services/latest/", "Service-level business logic and higher-level application workflows."),
    Library("codex-django", "https://codexdlc.github.io/codex-django/latest/", "Django runtime modules and reusable integrations for Codex projects."),
    Library("codex-django-cli", "https://codexdlc.github.io/codex-django-cli/latest/", "CLI scaffolding, blueprints, and project bootstrap tooling."),
    Library("codex-bot", "https://codexdlc.github.io/codex-bot/", "Bot framework and automation-oriented runtime for Codex products."),
]


@dataclass
class UpdateEntry:
    repo: str
    date: datetime
    kind: str
    version: str
    title: str
    summary: str
    docs_url: str
    repo_url: str
    source_url: str


def github_get(path: str) -> Any:
    request = Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "codex-docs-updates-generator",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def parse_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def cleanup_release_body(body: str | None) -> str:
    if not body:
        return ""
    cleaned = body.strip().replace("\r\n", "\n")
    first_block = cleaned.split("\n\n", 1)[0].strip()
    first_line = " ".join(line.strip() for line in first_block.splitlines() if line.strip())
    return textwrap.shorten(first_line, width=220, placeholder="...")


def fetch_latest_release(library: Library) -> UpdateEntry | None:
    try:
        payload = github_get(f"/repos/{OWNER}/{library.repo}/releases/latest")
    except HTTPError as exc:
        if exc.code == 404:
            return None
        raise

    published_at = payload.get("published_at") or payload.get("created_at")
    version = payload.get("tag_name") or payload.get("name") or "release"
    summary = cleanup_release_body(payload.get("body"))
    if not summary:
        summary = "Latest GitHub release is available for this library."

    return UpdateEntry(
        repo=library.repo,
        date=parse_datetime(published_at),
        kind="release",
        version=version,
        title=payload.get("name") or version,
        summary=summary,
        docs_url=library.docs_url,
        repo_url=f"https://github.com/{OWNER}/{library.repo}",
        source_url=payload["html_url"],
    )


def fetch_latest_tag(library: Library) -> UpdateEntry:
    tags = github_get(f"/repos/{OWNER}/{library.repo}/tags?per_page=1")
    if not tags:
        raise RuntimeError(f"No tags found for {library.repo}")

    tag = tags[0]
    commit = github_get(f"/repos/{OWNER}/{library.repo}/commits/{tag['commit']['sha']}")
    commit_date = commit["commit"]["committer"]["date"]

    return UpdateEntry(
        repo=library.repo,
        date=parse_datetime(commit_date),
        kind="tag",
        version=tag["name"],
        title=tag["name"],
        summary="Latest published reference is currently represented by a git tag. A formal GitHub Release has not been published yet.",
        docs_url=library.docs_url,
        repo_url=f"https://github.com/{OWNER}/{library.repo}",
        source_url=f"https://github.com/{OWNER}/{library.repo}/releases/tag/{tag['name']}",
    )


def fetch_entry(library: Library) -> UpdateEntry:
    release = fetch_latest_release(library)
    if release is not None:
        return release
    return fetch_latest_tag(library)


def render_entry(entry: UpdateEntry, summary_lookup: dict[str, str]) -> str:
    date_label = entry.date.date().isoformat()
    repo_summary = summary_lookup[entry.repo]
    return "\n".join(
        [
            f"### {date_label} · {entry.repo} · {entry.kind}",
            "",
            f"**{entry.title}**",
            "",
            f"{repo_summary} {entry.summary}",
            "",
            f"- Version: `{entry.version}`",
            f"- Documentation: [Open docs]({entry.docs_url})",
            f"- Repository: [Open repo]({entry.repo_url})",
            f"- Source: [View on GitHub]({entry.source_url})",
            "",
        ]
    )


def render(entries: list[UpdateEntry]) -> str:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    summary_lookup = {library.repo: library.summary for library in LIBRARIES}

    lines = [
        f"_Generated from GitHub release data with tag fallback on {generated_at}._",
        "",
    ]
    for entry in entries:
        lines.append(render_entry(entry, summary_lookup))
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    entries = [fetch_entry(library) for library in LIBRARIES]
    entries.sort(key=lambda item: item.date, reverse=True)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render(entries), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
