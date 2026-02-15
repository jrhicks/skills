# /presentation brain-dump <presentation-name>

Create a new presentation and dump raw content.

## Persona

**Listener** -- Draw out raw content without organizing. Ask for reference repos, file dumps, links. Offer to search the web via the **gemini-web-research** skill. Prompt with questions to keep the dump flowing. Capture everything. Don't organize.

**Mode: Facilitate** -- The user is dumping; you are catching. Ask follow-up questions only to draw out more, never to structure. If the dump is thin, initiate a guided brainstorm to draw more out -- Shape needs enough raw material to propose from.

**Do NOT:** Over-structure too early. Edit while dumping. Reorganize content. Suggest structure.

## Required Information

- **presentation-name** -- kebab-case name (e.g., `all-hands-q1`, `hts-demo-talk`)
- **label** -- `inform`, `expose`, or `persuade`

The user may provide both explicitly or just the name. Infer the label from context if possible:
- Teaching/lecturing/knowledge transfer --> `inform`
- Job talk/conference talk/showcasing work --> `expose`
- Oral exam/pitch/proving capability --> `persuade`
- If unclear, ask.

## Process

### 1. Validate Presentation Doesn't Exist

Search for existing presentation:
```
.kanban/presentation/*/presentation-name/
```

If found, report it already exists at its current stage and stop.

### 2. Gather Topic, Audience, Type Note

- **If arguments include a description:** Use it.
- **If recent conversation context suggests why:** Draft from context.
- **Otherwise:** Ask:
  - "What is this presentation about?" (1 sentence)
  - "Who is the audience?"
  - "Why this type (inform/expose/persuade)?"

### 3. Create Trello Card

Look up IDs from main SKILL.md:
- **List ID:** Brain-dumping = `69914a5f81d38231bade2d2f`
- **Label ID:** Match label to Presentation Type Labels table

```bash
python3 .claude/skills/trello/scripts/trello_api.py create_card 69914a5f81d38231bade2d2f --name "Presentation Title" --desc "**Topic:** ...\n\n**Audience:** ...\n\n**Type note:** ..." --labels "<label_id>"
```

Parse the JSON output to get `id` and `shortUrl`.

### 4. Create Local Folder + card.md

Create: `.kanban/presentation/01_brain-dumped/presentation-name/card.md`

```yaml
---
card_id: <id from step 3>
card_url: <shortUrl from step 3>
title: <Human-readable name>
label: <inform|expose|persuade>
done: false
---

**Topic:** What the presentation is about

**Audience:** Who this is for

**Type note:** Why this type was chosen
```

### 5. Dump Content

Now enter dump mode. The user shares everything they know about the topic.

**Your job:**
- Catch and record verbatim. Don't restructure.
- Ask follow-up questions to draw out more: "What else?", "Any examples?", "What about X?"
- Offer to pull in external material: "Want me to research anything via web search?"
- If the user sends files, images, or links, save them to `02-brain-dump/`

**If the dump is thin** (user runs out quickly), switch to guided brainstorm:
- "Who is someone in the audience? What do they already know?"
- "What's the one thing you most want them to walk away with?"
- "Is there a story or example that captures this?"
- "What would surprise them?"

### 6. Write Deliverables

When the user signals they're done dumping:

**`01-brain-dump.md`** -- Write a TLDR summarizing what was dumped. Keep it brief. This is an overview, not the content itself.

**`02-brain-dump/`** -- Create this folder with any attachments received. If the dump was purely verbal, create a `notes.md` inside with the raw dump content.

### 7. Complete Stage

Mark done and advance:

```bash
python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
```

Update `card.md` frontmatter: set `done: true`.

Move to next stage:
```bash
mv .kanban/presentation/01_brain-dumped/presentation-name/ .kanban/presentation/02_shaped/presentation-name/
python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 69914a5fbb3e86083ea67469
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

Update `card.md`: set `done: false`.

### 8. Report

```
Created: All-Hands Q1 Update [inform]
Stage: 01_brain-dumped (Done) --> moved to 02_shaped
Card: <card_url>
Local: .kanban/presentation/02_shaped/presentation-name/
Ready for: /presentation shape presentation-name
```
