---
name: presentation
description: |
  Create presentations following Patrick Winston's how-to-speak methodology.
  5-stage kanban pipeline from brain-dump through production.
  Triggers: "/presentation", "presentation brain-dump", "presentation list".
user-invocable: true
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# /presentation

Create presentations using Patrick Winston's how-to-speak methodology. Presentations progress through a 5-stage pipeline from raw content dump to finished deck.

**Methodology:** This process is grounded in Winston's MIT "How to Speak" lecture -- a practical framework for communication built on Knowledge + Practice + talent (talent smallest). The full reference lives in `guides/how-to-speak/`. Each stage integrates specific Winston techniques: empowerment promise and Star elements in shaping, cycling and verbal punctuation in outlining, slide crime avoidance in specifying, chalkboard sequences in producing.

## Usage

```
/presentation brain-dump <presentation-name>
/presentation shape <presentation-name>
/presentation outline <presentation-name>
/presentation specify <presentation-name>
/presentation produce <presentation-name>
/presentation list
```

## Board Configuration

**Board:** Presentation
**Board ID:** `69914a5d5dbf39135a9040c4`
**URL:** https://trello.com/b/qzBLV6lo

**Lists:**

| Stage | List Name | List ID |
|-------|-----------|---------|
| 01 | Brain-dumping | `69914a5f81d38231bade2d2f` |
| 02 | Shaping | `69914a5fbb3e86083ea67469` |
| 03 | Outlining | `69914a5e68ba37a10e8a221e` |
| 04 | Specifying | `69914a5e8a5ca1785c4c5114` |
| 05 | Producing | `69914a5e2f14b6a82e828fa8` |
| -- | Done | `69914a5e50014d602d1a4e6e` |

**Presentation Type Labels:**

| Label | Color | ID |
|-------|-------|----|
| inform | blue | `69914a5f9377a80cb6d9f9ec` |
| expose | green | `69914a605ef8c2d9704d1775` |
| persuade | orange | `69914a6076b1c2c2f54f1460` |

Every card gets exactly 1 label.

## Trello API

For Trello write operations, delegate to the **trello** skill. It handles all card operations (create, move, update, mark done/undone, list, etc.).

## Pipeline

| # | Stage | Verb | What Happens | Produces |
|---|-------|------|-------------|----------|
| 01 | Brain-dumping | brain-dump | Raw content dump -- everything you know | card.md, 01-brain-dump.md, 02-brain-dump/ |
| 02 | Shaping | shape | Audience, core extraction, Star elements, fencing | 03-shape/, 03-shape.md |
| 03 | Outlining | outline | Talk architecture, media plan (label-branched) | 04-outline/, 04-outline.md |
| 04 | Specifying | specify | Slide-by-slide blueprint | 05-spec.md |
| 05 | Producing | produce | Build artifacts: images, PPTX, PDF | produce/ |
| -- | Done | -- | Presentation complete and delivered | -- |

## Presentation Type Labels

- **inform** -- Teaching, lecturing. Board-primary. Knowledge transfer. Best tool: the board (speed matches absorption, graphic quality, empathetic mirroring).
- **expose** -- Job talks, conference talks. Slides-primary. Showcasing ideas/accomplishments. Structure: vision + done something + contributions.
- **persuade** -- Oral exams, pitches. Slides-primary. Establishing context and proving capability. Critical: situate your work first.

## Done Flow

Auto-done. Sub-skill marks done and advances to the next stage in one motion. No manual "ready to pull" gate.

Locally, `card.md` frontmatter tracks this:
```yaml
done: true    # set when stage work is complete
```

Use `mark_done` / `mark_undone` commands to toggle done state:
```bash
python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

## Running Instructions (All Stages)

**Capture aha moments.** When a design conversation produces an insight -- about the topic, the audience, the medium -- append it to `discussion.md` in the presentation folder. Format:

```markdown
## YYYY-MM-DD -- <aha moment title>

<What changed in our thinking and why.>
```

Each dated entry is a snapshot. Don't rewrite old entries -- append new ones.

**Compilation files guide next steps.** Each stage produces brainstorm files (supplemental, exploratory) and a compilation file that locks in decisions (`03-shape.md`, `04-outline.md`, `05-spec.md`). The next stage reads the compilation, not the brainstorms. Brainstorms stay as reference but don't drive downstream work.

## Dispatch

**Workflow stages:**

| Verb | File |
|------|------|
| brain-dump | `workflow/01-brain-dump/SKILL.md` |
| shape | `workflow/02-shape/SKILL.md` |
| outline | `workflow/03-outline/SKILL.md` |
| specify | `workflow/04-specify/SKILL.md` |
| produce | `workflow/05-produce/SKILL.md` |

**Utilities:**

| Verb | File |
|------|------|
| list | `utilities/list/SKILL.md` |

Read the SKILL.md for the selected verb and follow its instructions.

## Presentation Location

Presentations are folders inside stage directories under `.kanban/presentation/`. They move between stage folders as work progresses.

```
.kanban/presentation/
├── discussion.md              # Cross-presentation aha moments
├── 01_brain-dumped/
│   └── all-hands-q1/
│       └── card.md
├── 02_shaped/
├── 03_outlined/
├── 04_specified/
├── 05_produced/
└── 06_done/
```

## Presentation Location (Search)

To find a presentation, search all stage folders:

```
.kanban/presentation/*/presentation-name/
```

If found, read `card.md` inside it. If not found, the presentation does not exist yet (only `brain-dump` can create it).

## card.md Format

```yaml
---
card_id: <from Trello>
card_url: <from Trello>
title: <Human-readable name, e.g., "All-Hands Q1 Update">
label: <inform|expose|persuade>
done: false
---

**Topic:** What the presentation is about

**Audience:** Who this is for

**Type note:** Why this type was chosen
```

The folder location determines the current stage. `done: true` means stage work is complete. Resets to `false` on move.

## Deliverable Sequence

Deliverables accumulate in the presentation folder, numbered sequentially across stages:

**Brain-dump:**
- `01-brain-dump.md` -- TLDR of what was dumped
- `02-brain-dump/` -- raw attachments (images, links, notes)

**Shape:**
- `03-shape/` -- brainstorm sessions (01-grounding, 02-core, 03-packaging)
- `03-shape.md` -- locked-in shape merging all brainstorms

**Outline (label-branched):**
- `04-outline/` -- brainstorm sessions (varies by type)
- `04-outline.md` -- locked-in outline

**Specify:**
- `05-spec.md` -- slide-by-slide blueprint

**Produce:**
- `produce/` -- assets, speaker-notes.md, presentation.pptx (.gitignore), presentation.pdf (.gitignore)

## How-to-Speak Reference

Full Winston methodology: `guides/how-to-speak/how-to-speak.md`
Raw transcripts: `guides/how-to-speak/how-to-speak-transcript/`

Stage guides weave in relevant Winston techniques at the point of use.

## Examples

```
/presentation brain-dump all-hands-q1 --label inform
/presentation brain-dump hts-demo-talk --label expose
/presentation shape all-hands-q1
/presentation outline all-hands-q1
/presentation specify all-hands-q1
/presentation produce all-hands-q1
/presentation list
```
