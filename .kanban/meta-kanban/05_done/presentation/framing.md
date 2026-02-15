## 1. Purpose

Create PPTX presentations following Patrick Winston's how-to-speak presentation style, using the pptx skill. Winston's techniques (empowerment promise, cycling, fencing, verbal punctuation, Winston's Star, slide crime avoidance) are powerful but need a systematic process to apply reliably.

## 2. Process Type

**direct-output** -- each presentation progressing through the board produces a finished deck as the end-product.

## 3. What Flows Through

Three presentation types based on Winston's taxonomy:

- **inform** -- teaching, lecturing. Board-primary. Goal is knowledge transfer.
- **expose** -- job talks, conference talks. Slides-primary. Goal is showcasing ideas/accomplishments.
- **persuade** -- oral exams, pitches. Slides-primary. Goal is establishing context and proving capability.

The type determines label-branched behavior in Outline (expose/persuade get vision/done-something/contributions; inform does not) and media decisions (inform defaults to board, expose/persuade default to slides).

## 4. Main Steps

Stages derived from a dependency analysis of Winston's techniques:

1. **Brain-dump** -- raw content dump
2. **Shape** -- define audience + core extraction (salient idea, empowerment promise) + Star elements (symbol, slogan, surprise, salient idea, story) + fencing + situating
3. **Outline** -- talk architecture (vision, done something, inspiration hooks, section outline) + media plan (board vs slides per section, cycling plan, contributions list, how to start/stop)
4. **Specify** -- the complete blueprint: every slide defined with content, verbal punctuation placed, questions placed, slide crime audit, speaker notes written, delivery cues -- everything except physical artifacts
5. **Produce** -- artifact creation: symbol images (Nano Banana), wordsmithed catch phrases, chalkboard sequence pairs, assemble PPTX with speaker notes, upload to Google Slides
6. **Done**

Key insight: the **section outline** is the gateway bottleneck between intellectual design (Shape) and production work (Specify/Produce). Everything above it is discovering what to say; everything below it is deciding how to say it and building it.

## 5. Deliverables

### Brain-dump
- `01-brain-dump.md` -- overview of what was dumped
- `02-brain-dump/` -- folder for random attachments (images, links, notes, whatever)

### Shape
Three brainstorm sessions grouped by sequence and similarity, then a lock-in:
- `shape-brainstorms/03-grounding.md` -- audience, situating, fencing (set first, influences everything)
- `shape-brainstorms/04-core.md` -- salient idea, story, surprise (depends on grounding)
- `shape-brainstorms/05-packaging.md` -- symbol, slogan, empowerment promise (sugar, may crystallize later)
- `06-shape.md` -- locked-in shape merging all brainstorms

### Outline (type-branched)

**inform:**
- `outline-brainstorms/07-sections.md` -- section outline + board vs slides
- `outline-brainstorms/08-delivery.md` -- cycling, hooks, start/stop
- `09-outline.md` -- locked-in outline

**expose / persuade:**
- `outline-brainstorms/07-vision.md` -- vision statement
- `outline-brainstorms/08-done-something.md` -- steps enumerated
- `outline-brainstorms/09-contributions.md` -- what you accomplished
- `outline-brainstorms/10-sections.md` -- section outline + board vs slides
- `outline-brainstorms/11-delivery.md` -- cycling, hooks, start/stop
- `12-outline.md` -- locked-in outline

Sub-skills know which deliverables to create per type -- no runtime inference needed.

### Specify
- `##-spec.md` -- full slide-by-slide blueprint with content, type, speaker notes, delivery cues, verbal punctuation markers, question placements. Produced from prior deliverables, refined through user feedback. Execute mode, not facilitate.

### Produce
```
produce/
  assets/
    chalkboard-sequences/
      sequence-name/
        frame-1.png
        frame-2.png
  speaker-notes.md
  presentation.pptx    # .gitignore
  presentation.pdf     # .gitignore
```

Upload to Google Slides as final step.

## 6. Where Outputs Go

- **Google Slides** -- uploaded as final step of Produce
- **Local** -- all deliverables stay in the ticket folder; `.pptx` and `.pdf` gitignored (binary files)
- **Assets tracked in git** -- images are source content

No outputs feed other processes. This is a self-contained direct-output workflow.

## 7. Done Flow

Auto-done. When a stage's deliverables are complete, the sub-skill marks done and advances to the next stage in one motion. No manual "ready to pull" gate.
