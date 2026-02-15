#!/usr/bin/env python3
"""Sync EARS requirements to a Trello card description.

Two modes:

1. **trello.md mode** (preferred): Reads a ticket's trello.md file which contains
   curated summaries, card metadata, and the card description ready to push.

2. **EARS mode** (bootstrap): Reads raw EARS files, auto-extracts requirements,
   and builds a card description. Good for initial sync -- refine in trello.md after.

Usage:
    # Push from trello.md (reads card_id from frontmatter)
    python3 .claude/skills/trello/scripts/sync_ears.py _project/management/03_plans/OPS-061/trello.md

    # Preview from trello.md
    python3 .claude/skills/trello/scripts/sync_ears.py --preview _project/management/03_plans/OPS-061/trello.md

    # Bootstrap from EARS (auto-extract, raw text)
    python3 .claude/skills/trello/scripts/sync_ears.py --ears <card_id> <ears_file> [<ears_file>...]
    python3 .claude/skills/trello/scripts/sync_ears.py --ears --preview <ears_file> [<ears_file>...]

Options:
    --preview    Print the description without pushing to Trello.
    --ears       Use EARS mode instead of trello.md mode.
    --notice     (EARS mode) Override Notice line.
    --idea       (EARS mode) Override Idea line.

Requires TRELLO_API_KEY and TRELLO_TOKEN environment variables (unless --preview).
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import date


API_BASE = "https://api.trello.com/1"
GITHUB_BASE = "https://github.com/Record360/record-paas/blob/main"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))


def get_auth():
    key = os.environ.get("TRELLO_API_KEY")
    token = os.environ.get("TRELLO_TOKEN")
    if not key or not token:
        print("Error: TRELLO_API_KEY and TRELLO_TOKEN must be set", file=sys.stderr)
        sys.exit(1)
    return key, token


# --- trello.md mode ---

def parse_trello_md(filepath):
    """Parse a trello.md file and return (frontmatter, body).

    Body has EARS IDs stripped from requirement lines for clean Trello display.
    Local trello.md keeps full IDs (e.g., SRV-STOR-001:) for cross-referencing.
    """
    abs_path = os.path.join(REPO_ROOT, filepath) if not os.path.isabs(filepath) else filepath
    with open(abs_path, "r") as f:
        content = f.read()

    frontmatter = {}
    body = content
    if content.startswith("---"):
        end = content.index("---", 3)
        for line in content[3:end].strip().split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                frontmatter[k.strip()] = v.strip()
        body = content[end + 4:].strip()

    # Strip EARS IDs from numbered requirements for Trello display
    # e.g., "1. SRV-STOR-001: Single-file..." -> "1. Single-file..."
    body = re.sub(r'^(\d+\.\s+)[A-Z]+-[A-Z]+-\d+:\s+', r'\1', body, flags=re.MULTILINE)

    return frontmatter, body


def update_trello_md_synced(filepath):
    """Update the synced_at field in trello.md frontmatter."""
    abs_path = os.path.join(REPO_ROOT, filepath) if not os.path.isabs(filepath) else filepath
    with open(abs_path, "r") as f:
        content = f.read()

    today = date.today().isoformat()
    content = re.sub(r'synced_at:.*', f'synced_at: {today}', content)
    with open(abs_path, "w") as f:
        f.write(content)


# --- EARS mode ---

def parse_ears_file(filepath):
    """Parse an EARS file and return (frontmatter, requirements)."""
    abs_path = os.path.join(REPO_ROOT, filepath) if not os.path.isabs(filepath) else filepath
    with open(abs_path, "r") as f:
        content = f.read()

    frontmatter = {}
    if content.startswith("---"):
        end = content.index("---", 3)
        for line in content[3:end].strip().split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                frontmatter[k.strip()] = v.strip()
        content = content[end + 3:].strip()

    req_pattern = re.compile(r'^[❔📌💡🧪🔨✅⚠️]\s+\S+-\S+-\d+:\s+(.+?)(?:\n|$)', re.MULTILINE)
    requirements = []
    for match in req_pattern.finditer(content):
        req_text = match.group(1).strip()
        if len(req_text) > 100:
            req_text = req_text[:97] + "..."
        requirements.append(req_text)

    if os.path.isabs(filepath):
        rel_path = os.path.relpath(filepath, REPO_ROOT)
    else:
        rel_path = filepath

    return {
        "frontmatter": frontmatter,
        "requirements": requirements,
        "rel_path": rel_path,
        "filename": os.path.basename(filepath),
    }


def build_description(ears_files, notice=None, idea=None):
    """Build a Trello card description from parsed EARS data."""
    lines = []

    if notice:
        lines.append(f"**Notice:** {notice}")
        lines.append("")
    if idea:
        lines.append(f"**Idea:** {idea}")
        lines.append("")
    if notice or idea:
        lines.append("---")
        lines.append("")

    lines.append("**Requirements**")
    lines.append("")
    req_num = 1
    for ears in ears_files:
        for req in ears["requirements"]:
            lines.append(f"{req_num}. {req}")
            req_num += 1
    lines.append("")
    lines.append("---")
    lines.append("")

    if len(ears_files) == 1:
        ears = ears_files[0]
        github_url = f"{GITHUB_BASE}/{ears['rel_path']}"
        lines.append(f"**References:** [{ears['filename']}]({github_url})")
    else:
        lines.append("**References:**")
        for ears in ears_files:
            github_url = f"{GITHUB_BASE}/{ears['rel_path']}"
            lines.append(f"- [{ears['filename']}]({github_url})")

    return "\n".join(lines)


# --- Trello API ---

def push_to_trello(card_id, desc, title=None):
    """Update a Trello card description and optionally its name."""
    key, token = get_auth()
    url = f"{API_BASE}/cards/{card_id}?key={key}&token={token}"
    payload = {"desc": desc}
    if title:
        payload["name"] = title
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="PUT", headers={"Content-Type": "application/json"})
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())


# --- CLI ---

def main():
    args = sys.argv[1:]
    preview = False
    ears_mode = False
    notice = None
    idea = None
    positional = []

    i = 0
    while i < len(args):
        if args[i] == "--preview":
            preview = True
        elif args[i] == "--ears":
            ears_mode = True
        elif args[i] == "--notice":
            notice = args[i + 1]
            i += 1
        elif args[i] == "--idea":
            idea = args[i + 1]
            i += 1
        else:
            positional.append(args[i])
        i += 1

    if ears_mode:
        # EARS mode: auto-extract from .ears.md files
        if preview:
            ears_paths = positional
            card_id = None
        else:
            if len(positional) < 2:
                print("Usage: sync_ears.py --ears <card_id> <ears_file> [<ears_file>...]")
                sys.exit(1)
            card_id = positional[0]
            ears_paths = positional[1:]

        ears_files = [parse_ears_file(p) for p in ears_paths]
        total_reqs = sum(len(e["requirements"]) for e in ears_files)
        print(f"Parsed {len(ears_files)} EARS file(s), {total_reqs} requirements")
        desc = build_description(ears_files, notice=notice, idea=idea)

    else:
        # trello.md mode (default)
        if not positional:
            print("Usage: sync_ears.py <trello.md>")
            print("       sync_ears.py --ears <card_id> <ears_file> [<ears_file>...]")
            sys.exit(1)

        trello_md_path = positional[0]
        frontmatter, body = parse_trello_md(trello_md_path)
        card_id = frontmatter.get("card_id")
        title = frontmatter.get("title")
        desc = body

        if not card_id and not preview:
            print("Error: card_id not found in trello.md frontmatter", file=sys.stderr)
            sys.exit(1)

        print(f"Read trello.md: card {card_id}, {len(desc)} chars")

    if preview:
        print("\n--- Preview ---\n")
        print(desc)
    else:
        title_to_push = title if not ears_mode else None
        result = push_to_trello(card_id, desc, title=title_to_push)
        print(f"Updated: {result['name']}")
        print(f"URL: {result['shortUrl']}")

        # Update synced_at in trello.md if in trello.md mode
        if not ears_mode:
            update_trello_md_synced(positional[0])
            print(f"Updated synced_at in {positional[0]}")


if __name__ == "__main__":
    main()
