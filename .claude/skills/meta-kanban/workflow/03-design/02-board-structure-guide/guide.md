# Board Structure Guide

Design the board's physical structure -- stages, progression rules, and what moves between them.

Read `framing.md` and `01-card-format.md` first. You need to know what types of items flow through the process (from card format) before designing the stages they move through. The framing answers for "Main Steps" and "What Flows Through" drive stage design; the labels and types from card format determine whether stages need branching or type-specific behavior.

## Persona

**Systems Architect** -- Think in stages, flows, and dependencies. The board is a state machine. Draft a board structure from the framing answers and ask for reactions. Do not present blank questions when the framing already provides clear answers.

## Questions to Answer

### Board Name

What should this Trello board be called? Use a clear, descriptive name.

*Examples:* "Android InspectPro Review", "SDUI and MOB", "Meta-Kanban"

### Stage Names

List each stage with:
- **Number prefix** (01, 02, ...) for ordering
- **Stage name** (gerund form for active stages: Noticing, Framing, Analyzing)
- **Folder name** (snake_case: `01_noticed`, `02_framing`)
- **What happens** in this stage (1 sentence)

Include a terminal "Done" stage with no number prefix.

*Examples from existing boards:*

android-inspectpro-review:
| # | Stage | Folder | What Happens |
|---|-------|--------|-------------|
| 01 | Noticing | `01_noticed/` | Recognize topic |
| 02 | Analyzing | `02_analyzing/` | Study source code |
| 03 | Synthesizing | `03_synthesizing/` | Extract value through discussions |
| 04 | Applying | `04_applying/` | Apply findings to other processes |
| -- | Done | `05_done/` | Fully reviewed |

sdui-and-mob:
| # | Stage | Folder | What Happens |
|---|-------|--------|-------------|
| 01 | Noticed | `01_noticed/` | Recognize element |
| 02 | Framing | `02_framing/` | Research behavior |
| 03 | Specifying | `03_specifying/` | Write EARS |
| 04 | Prototyping | `04_prototyping/` | Build interface + component |
| 05 | Nativifying | `05_nativifying/` | Native implementations |
| 06 | Distilling | `06_distilling/` | Final review |

### What Moves Between Stages

What is the unit that progresses through the pipeline? A folder containing files.

- What is it called? (topic, element, process, ticket, item)
- What naming convention? (kebab-case, PascalCase)
- What's the minimum content when created? (just card.md? more?)

### Stage Dependencies

Must stages be strictly sequential, or can some be skipped or run in parallel?

## Reference Examples

Study these annotated kanban trees from existing processes to understand real-world folder structure decisions:

- **`ref-android-inspectpro-review-kanban.md`** -- Simple flat structure with 5 stage folders, cross-topic discussion.md, and .gitkeep convention
- **`ref-sdui-and-mob-kanban.md`** -- 6 stage folders with PascalCase item folders, deliverable accumulation, and 26+ items in specifying stage

## Deliverable

Produce `02-board-structure.md` in the process folder. Include the board name, complete stage table, unit description, and dependency notes.
