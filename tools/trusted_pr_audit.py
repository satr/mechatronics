"""Read changed PR source as data in a trusted pull_request_target workflow.

Never check out, import, exec, eval or run a PR's submitted source here.
Only the base branch's policy module and this script should execute.
"""
from __future__ import annotations

import base64
import json
import os
import re
import urllib.request
from pathlib import Path

from check_executable_sources import ROOT, audit_source, audit_notebook_source
from validate_repository import active_markdown_issues, static_svg_issues

API_ROOT = "https://api.github.com/repos/"
MAX_PAGES = 10
MAX_SOURCE_BYTES = 1_000_000
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def is_executable_example(relative: Path) -> bool:
    parts = relative.parts
    return (
        relative.suffix == ".py" and (
            parts[:1] == ("exercises",)
            or parts[:2] == ("ros2", "demo_pkg")
        )
    ) or relative.suffix == ".ipynb"


def is_passive_content_source(relative: Path) -> bool:
    """Audit all submitted Markdown and SVG bytes as data from trusted base."""
    return relative.suffix.lower() in {".md", ".svg"}


def needs_independent_review(relative: Path) -> bool:
    parts = relative.parts
    return (
        parts[:1] in (("tools",), ("tests",), ("web",), ("notebooks",),
                      ("ros2",), (".github",))
        or relative.suffix in {".ipynb", ".sh", ".bash", ".command",
                               ".ps1", ".bat", ".cmd"}
        or relative.name.startswith("Dockerfile")
        or relative in (
            Path("requirements.txt"),
            Path("ros2/Dockerfile"),
            Path("ros2/compose.yaml"),
        )
    )


def inspect_changed_files(changed: list[dict], fetch_blob) -> tuple[list[str], list[str]]:
    """Check submitted source bytes via an injected data fetcher; never execute them."""
    issues, review_notes = [], []
    for item in changed:
        name = item.get("filename")
        status = item.get("status")
        if not isinstance(name, str) or not name or not isinstance(status, str):
            issues.append("Incomplete PR file metadata")
            continue
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or "\\" in name:
            issues.append(f"Invalid PR filename: {name!r}")
            continue
        if needs_independent_review(relative):
            review_notes.append(f"Independent review required: {name!r}")
        if status == "removed":
            continue
        if status not in {"added", "modified", "renamed", "changed", "copied", "unchanged"}:
            issues.append(f"Unknown change status for {name!r}: {status!r}")
            continue
        if not (is_executable_example(relative) or is_passive_content_source(relative)):
            continue
        sha = item.get("sha")
        if not isinstance(sha, str) or SHA_RE.fullmatch(sha) is None:
            issues.append(f"Missing/invalid source blob SHA for {name!r}")
            continue
        try:
            source = fetch_blob(sha)
            encoded = source.encode("utf-8")
            if len(encoded) > MAX_SOURCE_BYTES:
                raise ValueError("Source is too large to audit")
            if relative.suffix == ".ipynb":
                issues.extend(audit_notebook_source(source, ROOT / relative))
            elif relative.suffix.lower() == ".md":
                issues.extend(
                    f"{name}: {reason}" for reason in active_markdown_issues(source)
                )
            elif relative.suffix.lower() == ".svg":
                issues.extend(
                    f"{name}: {reason}" for reason in static_svg_issues(source)
                )
            else:
                issues.extend(audit_source(source, ROOT / relative))
        except (UnicodeError, ValueError, OSError) as exc:
            issues.append(f"Cannot audit source {name!r}: {exc}")
    return issues, review_notes


def api_client(repo: str, token: str):
    if REPO_RE.fullmatch(repo) is None:
        raise ValueError("Invalid GitHub repository selector")
    if not token:
        raise ValueError("Missing read-only GitHub token")

    def request_json(suffix: str):
        # The host is fixed and these are the ONLY two API paths this audit uses.
        # Reject arbitrary URLs, path traversal, query strings and redirects supplied
        # as suffixes by future callers before attaching the read-only token.
        if not (re.fullmatch(r"pulls/[1-9][0-9]*/files[?]per_page=100&page=[1-9][0-9]*", suffix)
                or re.fullmatch(r"git/blobs/[0-9a-f]{40}", suffix)):
            raise ValueError("Unrecognized GitHub API path")
        url = API_ROOT + repo + "/" + suffix
        request = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "mechatronics-trusted-source-audit",
        })
        # Fixed github.com API host, validated repo and allowlisted suffixes.
        # Do not follow redirects with the bearer token: urllib may forward
        # Authorization to a redirected destination.
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                return None

        opener = urllib.request.build_opener(NoRedirect)
        with opener.open(request, timeout=20) as response:  # nosemgrep: python.lang.security.audit.dynamic-urllib-use-detected.dynamic-urllib-use-detected
            return json.load(response)

    return request_json


def pull_request_files(request_json, number: int) -> list[dict]:
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Invalid pull request number")
    changed = []
    for page in range(1, MAX_PAGES + 1):
        batch = request_json(f"pulls/{number}/files?per_page=100&page={page}")
        if not isinstance(batch, list):
            raise ValueError("Invalid PR files response")
        changed.extend(batch)
        if len(batch) < 100:
            return changed
    raise ValueError("PR exceeds the audit file-count limit")


def blob_fetcher(request_json):
    def fetch(sha: str) -> str:
        if SHA_RE.fullmatch(sha) is None:
            raise ValueError("Invalid blob SHA")
        blob = request_json(f"git/blobs/{sha}")
        if not isinstance(blob, dict) or blob.get("encoding") != "base64":
            raise ValueError("Expected base64 Git blob")
        # Reject excessively large blobs before decoding.
        if not isinstance(blob.get("size"), int) or blob["size"] > MAX_SOURCE_BYTES:
            raise ValueError("Source is too large to audit")
        payload = blob.get("content")
        if not isinstance(payload, str):
            raise ValueError("Missing blob contents")
        raw = base64.b64decode(payload, validate=False)
        if len(raw) != blob["size"] or len(raw) > MAX_SOURCE_BYTES:
            raise ValueError("Blob size mismatch")
        return raw.decode("utf-8")

    return fetch


def main() -> int:
    request_json = api_client(
        os.environ["GITHUB_REPOSITORY"],
        os.environ["GITHUB_TOKEN"],
    )
    number = int(os.environ["PR_NUMBER"])
    files = pull_request_files(request_json, number)
    errors, review = inspect_changed_files(files, blob_fetcher(request_json))
    for note in review:
        print("REVIEW:", note)
    for error in errors:
        print("ERROR:", error)
    if errors:
        return 1
    print(f"Trusted base-branch source audit passed for PR #{number} "
          f"({len(files)} changed files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
