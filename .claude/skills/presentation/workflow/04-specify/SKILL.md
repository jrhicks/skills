# /presentation specify <presentation-name>

Create the slide-by-slide blueprint.

## Persona

**Editor** -- Draft the spec from the outline compilation. Build, don't facilitate. Present the full spec for user feedback and iterate. This is execution mode -- the intellectual design is done, now we're deciding exactly how to say it.

**Mode: Execute** -- You draft, the user reviews. Quick iteration cycles.

**Do NOT:** Redesign the talk. Re-open shape or outline decisions. Facilitate brainstorms.

## Mode Detection

Find the presentation folder in `.kanban/presentation/*/presentation-name/` and read `card.md`.

**Start Mode:**
- Presentation is in `03_outlined/` with `done: true`
- Action: Move to `04_specified/`, mark undone

**Resume Mode:**
- Presentation is already in `04_specified/` with `done` absent or false
- Action: Read existing `05-spec.md` if it exists, continue editing

**Error cases:**
- Not found: "presentation-name not found."
- In a later stage: "presentation-name is already in <stage>."
- Outline not done: "Outline is not complete. Finish outlining first."

## Start Mode Process

### 1. Move Local Folder

```bash
mv .kanban/presentation/03_outlined/presentation-name/ .kanban/presentation/04_specified/presentation-name/
```

### 2. Update card.md

- Set `done: false`

### 3. Move Trello Card

```bash
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5e8a5ca1785c4c5114
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

### 4. Read Outline Compilation

Read `04-outline.md` (the compilation, NOT the brainstorm files). This is your source material.

### 5. Draft Spec

Read `specify-guide.md` for the spec format and slide crime audit checklist. Draft `05-spec.md`.

Present the full spec to the user. Iterate until approved.

## Complete Stage

After user approves `05-spec.md`:

```bash
python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
```

Update `card.md`: set `done: true`.

Move to next stage:
```bash
mv .kanban/presentation/04_specified/presentation-name/ .kanban/presentation/05_produced/presentation-name/
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5e2f14b6a82e828fa8
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

Update `card.md`: set `done: false`.

### Report

```
Specified: Presentation Title [label]
Stage: 04_specified (Done) --> moved to 05_produced
Card: <card_url>
Ready for: /presentation produce presentation-name
```
