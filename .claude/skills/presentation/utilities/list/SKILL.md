# /presentation list

List all presentations grouped by their current stage.

## Persona

**Librarian** -- Scan and report. No editorializing.

## Process

### 1. Scan All Stage Folders

Scan these directories for presentation folders (any folder containing `card.md`):

```
~/.kanban/presentation/01_brain-dumped/
~/.kanban/presentation/02_shaped/
~/.kanban/presentation/03_outlined/
~/.kanban/presentation/04_specified/
~/.kanban/presentation/05_produced/
~/.kanban/presentation/06_done/
```

### 2. Read Each card.md

Extract: title, label, done flag, card_url.

### 3. Display

Group presentations by stage folder. Show done status and Trello link:

```
Presentation
================================

01 Brain-dumped (1)
  all-hands-q1 [inform] -- Done  https://trello.com/c/...

02 Shaped (1)
  hts-demo-talk [expose]  https://trello.com/c/...

03 Outlined (0)

04 Specified (0)

05 Produced (0)

06 Done (1)
  onboarding-pitch [persuade]  https://trello.com/c/...

Total: 3 presentations
```

Display rules:
- Show count in parentheses after stage name
- Format: `name [label] -- Done  url` (append "-- Done" only if `done: true`)
- Presentations in `06_done/` are always done, no need to show the flag
- Empty stages show just the header with (0)

### 4. Show Progress for In-Progress Presentations

For presentations not marked done, check what deliverables exist:
- Brain-dumped: does 01-brain-dump.md exist?
- Shaped: which of 03-shape/01-grounding.md, 02-core.md, 03-packaging.md exist? Is 03-shape.md (compilation) written?
- Outlined: which 04-outline/ files exist? Is 04-outline.md (compilation) written?
- Specified: does 05-spec.md exist?
- Produced: what exists in produce/? (assets count, speaker-notes.md, presentation.pptx)

Report as sub-detail under relevant presentations.
