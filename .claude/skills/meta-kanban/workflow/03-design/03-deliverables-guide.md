# Deliverables Guide

Specify what each stage produces. These are the files and artifacts that accumulate in each item's folder as it progresses.

Read `01-card-format.md` and `02-board-structure.md` first -- the types and stage structure constrain what deliverables make sense.

## Persona

**Curriculum Designer** -- Each stage teaches something. Design deliverables that capture what was learned, not just what was produced. Derive from what the framing said about outputs. Do not invent deliverables that have no consumer downstream.

## Questions to Answer

### Per-Stage Deliverables

For each stage, list:
- What files does this stage produce?
- Are files numbered? What prefix convention?
- Do files have a fixed name or a variable name?

### Numbering Convention

How are deliverables numbered?

- Sequential within a stage? (01, 02, 03...)
- Sequential across all stages? (01 in stage 1, 02-03 in stage 2, 04-08 in stage 3...)
- Not numbered?

**Two-level numbering rule:** Root-level deliverables are numbered sequentially across stages. Subfolder deliverables are numbered within each folder starting from 01. When a subfolder directly supports a root file, it shares the same number and name -- this visually pairs the compilation with its supporting material.

*Example:*
```
03-shape.md          # Root compilation (locked-in shape)
03-shape/            # Supporting brainstorms (same number, same name)
  01-grounding.md    # Numbered within folder
  02-core.md
  03-packaging.md
04-outline.md        # Next root compilation
04-outline/          # Supporting brainstorms
  01-sections.md
  02-delivery.md
```

Not every subfolder supports a root file. Some are standalone (e.g., `produce/` is a terminal output folder, not supporting a compilation).

*Other examples:*
- android-inspectpro-review: numbered across all stages (01-inventory in analyzing, 03-07 discussions in synthesizing, 08-09 application artifacts in applying)
- meta-kanban: numbered within the designing stage only (01-04 design files)

### Label-Branched Deliverables

Do different label types produce different deliverables at the same stage?

*Example:* android-inspectpro-review's analyzing stage produces `02-discussion.md` for patterns but `02-research/` (a directory) for functionality topics.

### File Naming

What naming convention for deliverable files?

- `NN-descriptive-name.md` (numbered, kebab-case)
- `descriptive-name.md` (unnumbered, kebab-case)
- Directories for multi-file deliverables?

### Accumulation

Do deliverables accumulate in the folder (stay as items move forward), or does each stage have its own set?

Standard: deliverables accumulate. All files stay in the folder as it moves through stages.

## Deliverable

Produce `03-deliverables.md` in the process folder. Include a stage-by-stage table of deliverables with file names, numbering convention, and any label-branching.
