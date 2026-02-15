# /presentation outline <presentation-name>

Design the talk architecture and media plan.

## Persona

**Architect** -- Draft the outline from the locked-in shape. Dispatch to label-specific guide for type-dependent content. Re-anchor context at each step with a running summary.

**Mode: Facilitate** -- You propose structure, the user reacts. Lead with drafts, not questions.

**Do NOT:** Start from blank. Skip reading the shape compilation. Re-open shape decisions.

## Mode Detection

Find the presentation folder in `.kanban/presentation/*/presentation-name/` and read `card.md`.

**Start Mode:**
- Presentation is in `02_shaped/` with `done: true`
- Action: Move to `03_outlined/`, mark undone

**Resume Mode:**
- Presentation is already in `03_outlined/` with `done` absent or false
- Action: Check which brainstorm files exist, resume from where we left off

**Error cases:**
- Not found: "presentation-name not found."
- In a later stage: "presentation-name is already in <stage>."
- In `02_shaped/` without done: "Shape is not complete. Finish shaping first."

## Start Mode Process

### 1. Move Local Folder

```bash
mv .kanban/presentation/02_shaped/presentation-name/ .kanban/presentation/03_outlined/presentation-name/
```

### 2. Update card.md

- Set `done: false`

### 3. Move Trello Card

```bash
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5e68ba37a10e8a221e
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

### 4. Read Shape Compilation

Read `03-shape.md` (the compilation, NOT the brainstorm files). This is your source material for outlining.

### 5. Route by Label

Read `label` from `card.md`:

- **inform** --> Read `outline-guide/guide.md` then `outline-guide/inform-guide.md`
- **expose** or **persuade** --> Read `outline-guide/guide.md` then `outline-guide/expose-persuade-guide.md`

Follow the instructions in the guide files. They specify which brainstorm files to create.

## Brainstorm Files

**inform:**
- `04-outline/01-sections.md` -- section outline + board vs slides per section
- `04-outline/02-delivery.md` -- cycling plan, hooks, props, start/stop

**expose / persuade:**
- `04-outline/01-vision.md` -- vision statement
- `04-outline/02-done-something.md` -- steps enumerated
- `04-outline/03-contributions.md` -- what you accomplished
- `04-outline/04-sections.md` -- section outline + slides vs board per section
- `04-outline/05-delivery.md` -- cycling plan, hooks, props, start/stop

## Lock-In

After all brainstorm files are written, synthesize into `04-outline.md` -- the locked-in outline. Present for user approval.

## Complete Stage

After user approves `04-outline.md`:

```bash
python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
```

Update `card.md`: set `done: true`.

Move to next stage:
```bash
mv .kanban/presentation/03_outlined/presentation-name/ .kanban/presentation/04_specified/presentation-name/
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5e8a5ca1785c4c5114
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

Update `card.md`: set `done: false`.

### Report

```
Outlined: Presentation Title [label]
Stage: 03_outlined (Done) --> moved to 04_specified
Card: <card_url>
Ready for: /presentation specify presentation-name
```
