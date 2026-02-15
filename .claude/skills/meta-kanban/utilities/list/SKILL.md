# /meta-kanban list

List all processes grouped by their current stage.

## Persona

**Librarian** -- Report facts impartially. Scan folders, read metadata, display status. Fully autonomous. Do not editorialize, suggest next actions, or comment on process health.

## Process

### 1. Scan All Stage Folders

Scan these directories for process folders (any folder containing `card.md`):

```
~/.kanban/meta-kanban/01_noticed/
~/.kanban/meta-kanban/02_framing/
~/.kanban/meta-kanban/03_designing/
~/.kanban/meta-kanban/04_implementing/
~/.kanban/meta-kanban/05_done/
```

### 2. Read Each card.md

Extract: process name, label, done flag, card_url.

### 3. Display

Group processes by stage folder. Show done status and Trello link:

```
Meta-Kanban
================================

01 Noticed (2)
  android-inspectpro-review [feeder] -- Done  https://trello.com/c/...
  mob [direct-output] -- Done  https://trello.com/c/...

02 Framing (0)

03 Designing (1)
  release-pipeline [direct-output]  https://trello.com/c/...

04 Implementing (0)

05 Done (0)

Total: 3 processes
```

Display rules:
- Show count in parentheses after stage name
- Format: `process-name [label] -- Done  url` (append "-- Done" only if `done: true`)
- Processes in `05_done/` are always done, no need to show the flag
- Empty stages show just the header with (0)

### 4. Show Progress for In-Progress Processes

For processes in `02_framing/` (not done), check if `framing.md` exists.

For processes in `03_designing/` (not done), check which design files exist (01 through 07). Report as sub-detail:
```
03 Designing (1)
  release-pipeline [direct-output]  https://trello.com/c/...
    Design: 01 02 03 _ _ _ _  (3/7 complete)
```

For processes in `04_implementing/` (not done), note which implementation sub-steps appear complete based on whether the new skill/kanban/Trello artifacts exist.
