# Trello Setup Guide

Create the Trello board for the new process. Use `02-board-structure.md` (stages) and `01-card-format.md` (labels) from the process's design files as the spec.

## Persona

**Builder** -- Execute the board creation steps methodically. Record all IDs. Work autonomously -- the design phase was the time for questions. Do not rename stages or labels from what the design specifies.

## Steps

### 1. Create the Board

Use the Trello API to create a board in the project organization:

```python
# Organization ID for Record360 hackathon boards
org_id = '650204b18fc6ade83e759d0f'

# Create board
POST /boards
{
  "name": "<board name from 02-board-structure.md>",
  "defaultLists": "false",
  "idOrganization": org_id
}
```

### 2. Create Lists

Create lists in reverse order (Trello adds to the left, so last-created appears first):

```
Done, <last stage>, ..., <first stage>
```

Each list corresponds to a stage from `02-board-structure.md`.

### 3. Create Labels

Create labels matching the types defined in `01-card-format.md`:

```
POST /boards/{boardId}/labels
{
  "name": "<label name>",
  "color": "<color>"
}
```

Standard colors:
- blue, green, yellow, orange, red, purple, sky, lime, pink, black

### 4. Record IDs

Capture and record all IDs:
- Board ID and URL
- Each list's ID
- Each label's ID

These IDs must be wired into the skill files.

### 5. Wire IDs into Skill

Update the main SKILL.md's Board Configuration section with:
- Board name, ID, URL
- Lists table (stage, list name, list ID)
- Labels table (label, color, ID)

Update each sub-skill SKILL.md with the correct list IDs in their move_card and create_card commands.

## Trello API Script

Use the shared `trello_api.py` for standard operations:

```bash
python3 .claude/skills/trello/scripts/trello_api.py <command> [args]
```

For board/list/label creation (not in the standard script), use direct API calls via Python.
