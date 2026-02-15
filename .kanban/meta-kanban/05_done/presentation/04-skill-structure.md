# Skill Structure

## Directory Tree

```
.claude/skills/presentation/
├── SKILL.md                              # Main dispatcher
├── workflow/
│   ├── 01-brain-dump/
│   │   └── SKILL.md                      # Raw content dump
│   ├── 02-shape/
│   │   ├── SKILL.md                      # 3 brainstorms + lock-in
│   │   └── shape-guide/                  # Promoted: needs hts technique reference
│   │       ├── guide.md                  # Brainstorm session instructions
│   │       └── ref-hts-shaping.md        # Winston techniques for shaping
│   ├── 03-outline/
│   │   ├── SKILL.md                      # Talk architecture (label-branched)
│   │   └── outline-guide/                # Promoted: label-branched + hts reference
│   │       ├── guide.md                  # Common outline instructions
│   │       ├── inform-guide.md           # Inform-specific: sections + board/slides
│   │       ├── expose-persuade-guide.md  # Expose/persuade: vision, done-something, contributions
│   │       └── ref-hts-delivery.md       # Winston techniques for delivery planning
│   ├── 04-specify/
│   │   ├── SKILL.md                      # Slide-by-slide blueprint
│   │   └── specify-guide.md             # How to write a spec
│   └── 05-produce/
│       ├── SKILL.md                      # Artifact creation
│       └── produce-guide.md              # Production steps + delegation
└── utilities/
    └── list/
        └── SKILL.md                      # Board status scanner
```

## Personas + Interaction Modes

### Stage-Level Personas

| Stage | Persona | Mode | Behavior | Anti-pattern |
|-------|---------|------|----------|-------------|
| Brain-dump | **Listener** | Facilitate | Draw out raw content. Ask for reference repos, file dumps, links. Offer to search the web via **gemini-web-research** skill. Prompt with questions to keep the dump flowing. Capture everything. Don't organize. If the dump is thin, initiate a guided brainstorm to draw more out -- Shape needs enough raw material to propose from. | Over-structuring too early; editing while dumping |
| Shape | **Shaper** | Facilitate | Work through 3 brainstorm sessions then lock-in. Lead with proposals from brain-dump. | Answering for the user; skipping brainstorms |
| Outline | **Architect** | Facilitate | Draft outline from shape, dispatch to label-specific guide. Re-anchor context each step. | Starting blank instead of proposing from shape |
| Specify | **Editor** | Execute | Draft spec from outline, present for feedback. Build, don't facilitate. | Redesigning; re-opening shape/outline decisions |
| Produce | **Producer** | Execute | Build artifacts, delegate to skills. Report progress. | Over-creating manually instead of delegating |
| List | **Librarian** | Execute | Scan and report. | Editorializing |

### Guide-Level Persona Refinements

These are written into specific guide files, not the stage SKILL.md:

**Outline (type-dependent):**
- `inform-guide.md`: **Instructional Designer** -- thinks in learning objectives, knowledge scaffolding, building understanding step by step
- `expose-persuade-guide.md`: **Speechwriter** -- thinks in narrative arc, persuasive structure, audience journey

**Produce (step-dependent):**
- Image creation steps: **Illustrator** -- visual metaphors, symbols, pictograms, chalkboard sequences (delegates to **nano-banana** skill)
- Deck assembly steps: Producer (no shift -- delegates to **pptx** skill)

## Delegation Targets

| Stage | Delegates to | For what |
|-------|-------------|----------|
| Brain-dump | **gemini-web-research** skill | Web research when user wants external material |
| Shape | -- | Pure conversation |
| Outline | -- | Pure conversation |
| Specify | -- | Skill drafts from deliverables |
| Produce | **pptx** skill | PPTX file creation |
| Produce | **nano-banana** skill | Image generation (symbols, chalkboard sequences) |

## Agent Embedding

**None.** This process is lightweight and collaborative. Unlike mob (20+ source files) or android-inspectpro-review (15+ Kotlin files), presentation items have no external source material to research -- the user's brain is the source. The main context can hold all deliverables (brain-dump + shape + outline) without overflowing. Domain knowledge lives in guides, not agent instructions.

## Cross-References

None. Direct-output process -- all deliverables stay in the ticket folder.

## Reference Example Placement

Two guides promoted to folders:

| Guide | Why Promoted | Reference Files |
|-------|-------------|-----------------|
| `shape-guide/` | Winston's shaping techniques need a curated reference | `ref-hts-shaping.md` -- Star elements, empowerment promise, fencing, situating, audience |
| `outline-guide/` | Label-branched guides + delivery techniques reference | `inform-guide.md`, `expose-persuade-guide.md`, `ref-hts-delivery.md` -- cycling, verbal punctuation, questions, start/stop, slide crimes |

Flat guides (no promotion needed): `specify-guide.md`, `produce-guide.md`
