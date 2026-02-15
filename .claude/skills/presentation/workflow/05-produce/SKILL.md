# /presentation produce <presentation-name>

Build the presentation artifacts.

## Persona

**Producer** -- Build artifacts from the spec. Delegate to skills for specialized work. Report progress.

**Mode: Execute** -- Build, don't facilitate. The spec is the blueprint; follow it.

**Do NOT:** Redesign. Over-create manually instead of delegating. Re-open shape/outline/spec decisions.

### Persona Refinements

**Image creation steps:** Shift to **Illustrator** -- visual metaphors, symbols, pictograms, chalkboard sequences. Think in images, not words. Propose visual concepts before generating.

**Deck assembly steps:** Stay as Producer -- delegate to the **pptx** skill for file creation.

## Mode Detection

Find the presentation folder in `.kanban/presentation/*/presentation-name/` and read `card.md`.

**Start Mode:**
- Presentation is in `04_specified/` with `done: true`
- Action: Move to `05_produced/`, mark undone

**Resume Mode:**
- Presentation is already in `05_produced/` with `done` absent or false
- Action: Check what assets exist in `produce/`, resume from where we left off

**Error cases:**
- Not found: "presentation-name not found."
- Spec not done: "Spec is not complete. Finish specifying first."

## Start Mode Process

### 1. Move Local Folder

```bash
mv .kanban/presentation/04_specified/presentation-name/ .kanban/presentation/05_produced/presentation-name/
```

### 2. Update card.md

- Set `done: false`

### 3. Move Trello Card

```bash
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5e2f14b6a82e828fa8
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

### 4. Read Spec

Read `05-spec.md`. This is the blueprint for production.

### 5. Produce

Read `produce-guide.md` for the production steps. Follow them in order.

## Complete Stage

After all artifacts are built:

```bash
python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
```

Update `card.md`: set `done: true`.

Move to done:
```bash
mv .kanban/presentation/05_produced/presentation-name/ .kanban/presentation/06_done/presentation-name/
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5e50014d602d1a4e6e
```

### Report

```
Produced: Presentation Title [label]
Stage: 05_produced (Done) --> moved to 06_done
Card: <card_url>
Artifacts: produce/presentation.pptx, produce/presentation.pdf
```
