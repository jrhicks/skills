---
name: meta-kanban
description: |
  Design and implement new kanban-based workflows.
  Each card represents a process being designed, progressing from
  noticing through framing, designing, implementing, and done.
  Triggers: "/meta-kanban", "meta-kanban notice", "meta-kanban list".
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

# /meta-kanban

**Global skill.** This skill is installed at `~/.claude/skills/meta-kanban/` and available in every project. Its kanban board lives in the user's home directory at `~/.kanban/meta-kanban/` -- not in any project's `.kanban/` folder. All sub-skills read and write deliverables there.

Design and implement new kanban-based workflows. Processes progress through a 4-stage pipeline from initial recognition to a fully operational skill + board.

## Usage

```
/meta-kanban notice <process-name> --label feeder|direct-output
/meta-kanban frame <process-name>
/meta-kanban design <process-name>
/meta-kanban implement <process-name>
/meta-kanban list
```

## Board Configuration

**Board:** Meta-Kanban
**Board ID:** `6990dbb82caeaef658278ab6`
**URL:** https://trello.com/b/UgU1Xjm9

**Lists:**

| Stage | List Name | List ID |
|-------|-----------|---------|
| 01 | Noticing | `6990dbbaff67775efd5cf00e` |
| 02 | Framing | `6990dbb967427e703c09558b` |
| 03 | Designing | `6990dbb9c95b64da141fe03a` |
| 04 | Implementing | `6990dbb9d52291a2bb89ec62` |
| -- | Done | `6990dbb82caeaef658278bc5` |

**Process Labels:**

| Label | Color | ID |
|-------|-------|----|
| feeder | blue | `6990dbbae8112060ab42c14e` |
| direct-output | green | `6990dbbaff63cfef09c33f8f` |
<!-- | continuous | yellow | `6990dbbbdd19521a5f64b7fd` | -- uncomment when reference implementation exists -->

Every card gets exactly 1 label.

## Trello API

For Trello write operations, delegate to the **trello** skill. It handles all card operations (create, move, update, mark done/undone, list, etc.) and EARS sync.

## Pipeline

| # | Stage | Verb | What Happens | Produces |
|---|-------|------|-------------|----------|
| 01 | Noticing | notice | Recognize need for a new process | card.md |
| 02 | Framing | frame | Answer fundamental questions about purpose, flow, types | framing.md |
| 03 | Designing | design | Identify types, design stages, plan deliverables, design automation + independent review | 01-04 design files |
| 04 | Implementing | implement | Claude extension mastery, then build skill files, Trello board, kanban folders | actual files |
| -- | Done | -- | Process fully created and operational | -- |

## Process Labels

Processes are labeled by type. The label captures the fundamental nature of the workflow:

- **feeder** -- process that generates work items for other boards and improves guides for other processes. Its outputs leave the board.
  - *Reference example:* android-inspectpro-review (`.claude/skills/android-inspectpro-review/`, `.kanban/android-inspectpro-review/`). Analyzes the legacy Android codebase; outputs feed MOB cards and skill guide updates.

- **direct-output** -- process that produces end-products or achieves goals in itself. The board's output is the deliverables themselves.
  - *Reference example:* sdui-and-mob (`.claude/skills/mob/`, `.kanban/sdui-and-mob/`). Each element progresses from Noticed through Distilling and produces EARS requirements, prototype code, native implementations.

<!-- continuous label exists on the Trello board but is not yet supported. Add back when a reference implementation exists. -->

## Done Flow

Done-ness is tracked per-stage via the `done` flag in `card.md` and Trello's `dueComplete`.

1. Process arrives in a stage folder (marked undone) = work in progress
2. Work completes in that stage -- marked done, process stays = "ready to pull"
3. Next stage starts -- folder moves to next stage, marked undone
4. `05_done/` = permanently done

Locally, `card.md` frontmatter tracks this:
```yaml
done: true    # present and true when stage is complete
```

Use `mark_done` / `mark_undone` commands to toggle done state:
```bash
python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
```

## Dispatch

**Workflow stages:**

| Verb | File |
|------|------|
| notice | `workflow/01-notice/SKILL.md` |
| frame | `workflow/02-frame/SKILL.md` |
| design | `workflow/03-design/SKILL.md` |
| implement | `workflow/04-implement/SKILL.md` |

**Utilities:**

| Verb | File |
|------|------|
| list | `utilities/list/SKILL.md` |

Read the SKILL.md for the selected verb and follow its instructions.

## Process Location

Meta-kanban is a global skill. Its board lives at `~/.kanban/meta-kanban/`.

```
~/.kanban/meta-kanban/
├── discussion.md              # Cross-process aha moments
├── 01_noticed/
│   └── android-inspectpro-review/
│       └── card.md
├── 02_framing/
├── 03_designing/
├── 04_implementing/
└── 05_done/
```

**Output scope:** Each process's `card.md` has a `scope` field (`global` or `project`) that determines where the implement stage creates the output skill and kanban board:
- `scope: global` -- output to `~/.claude/skills/` and `~/.kanban/`
- `scope: project` -- output to `.claude/skills/` and `.kanban/`

The `notice` sub-skill asks the user to choose scope when creating a process.

## Process Location (Search)

To find a process, search all stage folders:

```
~/.kanban/meta-kanban/*/process-name/
```

If found, read `card.md` inside it. If not found, the process does not exist yet (only `notice` can create it).

## card.md Format

```yaml
---
card_id: <from Trello>
card_url: <from Trello>
process: Android InspectPro Review
label: feeder
scope: project
done: false
---

Brief description of why this process is needed.
```

The folder location determines the current stage. `done: true` means stage work is complete and the process is ready to pull to the next stage. Resets to `false` on move.

## Deliverable Sequence

Deliverables accumulate in the process folder, roughly numbered by order of creation:

- **Noticing:** `card.md` -- why this process is needed, initial context
- **Framing:** `framing.md` -- answers to all fundamental questions
- **Designing:**
  - `01-card-format.md` -- labels (types), card content, metadata fields
  - `02-board-structure.md` -- board name, stage names, list structure
  - `03-deliverables.md` -- what each stage produces, numbering convention
  - `04-skill-structure.md` -- skill dispatch structure, personas, cross-refs, guide files, ref example placement
- **Implementing:** actual skill files, Trello board, kanban folders

## Cross-Topic Discussion

`discussion.md` at the board root captures aha moments that span multiple processes. Format:

```markdown
## YYYY-MM-DD -- <aha moment title>

<What changed in our thinking and why.>
```

## Examples

```
/meta-kanban notice android-inspectpro-review --label feeder
/meta-kanban notice mob --label direct-output
/meta-kanban frame android-inspectpro-review
/meta-kanban design android-inspectpro-review
/meta-kanban implement android-inspectpro-review
/meta-kanban list
```
