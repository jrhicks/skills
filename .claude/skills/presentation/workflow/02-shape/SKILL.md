# /presentation shape <presentation-name>

Define audience, extract core idea, build Star elements.

## Persona

**Shaper** -- Work through 3 brainstorm sessions then lock in. Lead with proposals drawn from the brain-dump. Present drafts for the user to react to and refine -- don't ask open questions that leave them alone with the work.

**Mode: Facilitate** -- You propose, the user reacts. Re-anchor context with a running summary between sessions.

**Do NOT:** Answer for the user. Skip brainstorms. Start from blank instead of proposing from brain-dump.

## Mode Detection

Find the presentation folder in `~/.kanban/presentation/*/presentation-name/` and read `card.md`.

**Start Mode:**
- Presentation is in `01_brain-dumped/` with `done: true`
- Action: Move to `02_shaped/`, mark undone

**Resume Mode:**
- Presentation is already in `02_shaped/` with `done` absent or false
- Action: Check which brainstorm files exist, resume from where we left off

**Error cases:**
- Not found: "presentation-name not found. Use `/presentation brain-dump` first."
- In a later stage: "presentation-name is already in <stage>. Cannot move backward."

## Start Mode Process

### 1. Move Local Folder

```bash
mv ~/.kanban/presentation/01_brain-dumped/presentation-name/ ~/.kanban/presentation/02_shaped/presentation-name/
```

### 2. Update card.md

- Set `done: false`

### 3. Move Trello Card

```bash
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5fbb3e86083ea67469
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

### 4. Begin Shaping

Read `01-brain-dump.md` and any content in `02-brain-dump/`. Then proceed to the brainstorm sessions.

## Brainstorm Sessions

Read `shape-guide.md` for detailed instructions on each session. Work through them in order:

1. **Grounding** (audience, situating, fencing) --> `03-shape/01-grounding.md`
2. **Core** (salient idea, story, surprise) --> `03-shape/02-core.md`
3. **Packaging** (symbol, slogan, empowerment promise) --> `03-shape/03-packaging.md`

After each session, write the brainstorm file. Re-anchor context before starting the next.

## Lock-in

After all 3 brainstorms, synthesize into `03-shape.md` -- the locked-in shape. This is the compilation that downstream stages read. Present it for user approval.

The locked-in shape should include:
- **Audience** -- who, what they know, what they need
- **Situating** -- context that frames the talk
- **Fencing** -- what this is NOT about
- **Salient idea** -- the one thing that sticks out
- **Story** -- the narrative arc
- **Surprise** -- the unexpected element
- **Symbol** -- visual handle (may be TBD)
- **Slogan** -- verbal handle (may be TBD)
- **Empowerment promise** -- what they'll know/be able to do after

## Complete Stage

After user approves `03-shape.md`:

```bash
python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
```

Update `card.md`: set `done: true`.

Move to next stage:
```bash
mv ~/.kanban/presentation/02_shaped/presentation-name/ ~/.kanban/presentation/03_outlined/presentation-name/
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5e68ba37a10e8a221e
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

Update `card.md`: set `done: false`.

### Report

```
Shaped: Presentation Title [label]
Stage: 02_shaped (Done) --> moved to 03_outlined
Card: <card_url>
Ready for: /presentation outline presentation-name
```
