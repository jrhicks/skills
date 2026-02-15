---
name: trello
description: |
  Manage Trello boards, lists, and cards via the Trello REST API.
  Supports listing boards, creating/updating/moving/archiving cards,
  managing lists, and setting active boards/workspaces.
  Triggers: "trello", "create trello card", "list my boards",
  "move card", "update trello", "archive card".
user-invocable: true
model-invocable: true
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - AskUserQuestion
---

# Trello Skill

Manage Trello boards, lists, and cards via REST API.

## Prerequisites

Environment variables must be set: `TRELLO_API_KEY`, `TRELLO_TOKEN`

## Active Board

**Board:** Q1 Prototyping
**Board ID:** `698cc371e8291dcffe3895a8`
**URL:** https://trello.com/b/EvSGgNkE/q1-prototyping

**Lists:**

| List | ID |
|------|----|
| Noticing | `698cc371e8291dcffe389602` |
| Research & Shaping | `698cc42c02e9d172b5ca992d` |
| Prototyping | `698cc43ceabdfb11364da724` |
| Integrating | `698cc48f36088d0a4ea370be` |
| Distilling | `698cc4f1a18354e5ab82db1d` |

When the user says "trello" without specifying a board, use this board by default.

## Scripts

Python helpers in `scripts/` for reliable API access (avoids curl shell-escaping issues on writes).

**`scripts/trello_api.py`** -- General Trello operations:
```bash
python3 .claude/skills/trello/scripts/trello_api.py update_card <card_id> --name "title" --desc "desc"
python3 .claude/skills/trello/scripts/trello_api.py get_card <card_id>
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> <list_id>
python3 .claude/skills/trello/scripts/trello_api.py add_comment <card_id> "text"
python3 .claude/skills/trello/scripts/trello_api.py search "query"
python3 .claude/skills/trello/scripts/trello_api.py list_cards <list_id>
python3 .claude/skills/trello/scripts/trello_api.py create_card <list_id> --name "title" [--desc "desc"] [--labels "id1,id2"]
python3 .claude/skills/trello/scripts/trello_api.py add_label <card_id> <label_id>
python3 .claude/skills/trello/scripts/trello_api.py remove_label <card_id> <label_id>
```

**`scripts/sync_ears.py`** -- Sync card description to Trello:
```bash
# Push from trello.md (preferred -- reads card_id from frontmatter)
python3 .claude/skills/trello/scripts/sync_ears.py _project/management/03_plans/OPS-061-local-s3-simulation/trello.md

# Preview without pushing
python3 .claude/skills/trello/scripts/sync_ears.py --preview <path>/trello.md

# Bootstrap from raw EARS (auto-extract, then refine in trello.md)
python3 .claude/skills/trello/scripts/sync_ears.py --ears --preview <ears_file> [<ears_file>...]
python3 .claude/skills/trello/scripts/sync_ears.py --ears <card_id> <ears_file> [<ears_file>...]
```

## Card Format

See `card-format.md` for the standard Trello card description convention (Notice/Idea/Requirements/References).

## Read Operations (curl)

For read-only operations, curl is fine:

```bash
# List boards
curl -s "https://api.trello.com/1/members/me/boards?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN&fields=name,url,shortUrl" | python3 -m json.tool

# Get lists on a board
curl -s "https://api.trello.com/1/boards/{boardId}/lists?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN&fields=name,id" | python3 -m json.tool

# Get cards on a list
curl -s "https://api.trello.com/1/lists/{listId}/cards?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN&fields=name,desc,due,labels,shortUrl" | python3 -m json.tool

# Search cards on active board
curl -s "https://api.trello.com/1/search?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN&query={searchQuery}&modelTypes=cards&card_fields=name,desc,shortUrl,idList&idBoards=698cc371e8291dcffe3895a8" | python3 -m json.tool
```
