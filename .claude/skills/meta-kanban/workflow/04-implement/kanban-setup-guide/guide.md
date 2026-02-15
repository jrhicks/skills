# Kanban Setup Guide

Create the local kanban folder structure for the new process. Use `02-board-structure.md` from the process's design files as the spec.

## Persona

**Builder** -- Create the folder structure exactly as designed. Work autonomously. Do not add folders or files beyond what the design specifies.

## Steps

### 1. Create Root Folder

```bash
mkdir -p .kanban/<board-name-kebab>/
```

Use the kebab-case version of the board name (e.g., "Android InspectPro Review" becomes `android-inspectpro-review`).

### 2. Create Stage Folders

Create a folder for each stage, including Done:

```bash
mkdir -p .kanban/<board-name>/01_<stage>/
mkdir -p .kanban/<board-name>/02_<stage>/
# ... for each stage
mkdir -p .kanban/<board-name>/NN_done/
```

Folder naming convention: `NN_<stage-name-in-past-or-gerund>` matching `02-board-structure.md`.

### 3. Add .gitkeep Files

Each stage folder needs a `.gitkeep` so git tracks empty directories:

```bash
touch .kanban/<board-name>/01_<stage>/.gitkeep
# ... for each stage folder
```

### 4. Create discussion.md (if applicable)

If the design calls for cross-topic discussion, create:

```bash
# .kanban/<board-name>/discussion.md
```

Content:
```markdown
# <Board Name> -- Cross-Topic Discussion

Aha moments and insights that span multiple <items>. Append new entries; don't rewrite old ones.

```

### 5. Verify

List the created structure:
```bash
find .kanban/<board-name>/ -type f
```

Expected:
```
.kanban/<board-name>/discussion.md
.kanban/<board-name>/01_<stage>/.gitkeep
.kanban/<board-name>/02_<stage>/.gitkeep
...
.kanban/<board-name>/NN_done/.gitkeep
```

## Reference Examples

Study these annotated kanban trees from existing processes to compare your output against:

- **`ref-android-inspectpro-review-kanban.md`** -- Simple flat structure with 5 stage folders, cross-topic discussion.md, and .gitkeep convention
- **`ref-sdui-and-mob-kanban.md`** -- 6 stage folders with PascalCase item folders, deliverable accumulation, and 26+ items in specifying stage
