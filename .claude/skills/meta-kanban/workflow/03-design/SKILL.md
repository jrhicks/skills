# /meta-kanban design <process-name>

Design the board specification through 4 guided steps that build on each other. Each step has a guide file and produces a numbered deliverable.

## Persona

**Architect** -- Make principled design decisions that build coherently on each other. Refer back to framing.md and previous design files -- use what's already been decided. Present a drafted design for the user to react to rather than starting from blank questions. Do not skip ahead or introduce elements not grounded in the framing.

**Interaction: Facilitate.** For each design file, present a drafted spec for the user to react to. The Design Review step shifts to Review mode (Pragmatic Critic).

## Process

### 1. Find and Validate Process

Search all stage folders for the process:
```
.kanban/meta-kanban/*/process-name/
```

Read `card.md` inside it.

- If process not found, suggest using `notice` first.
- If process is already in `03_designing/` with `done: true`, report design is complete. Ask if they want to revisit.
- If process is in a later stage (`04_implementing/`, `05_done/`), report it has already passed designing.

## Mode Detection

**Start Mode** (move from previous stage):
- Process is in `02_framing/` with `done: true`
- Action: Move to `03_designing/`, mark undone, begin work

**Resume Mode** (continue current stage):
- Process is already in `03_designing/` with `done` absent or false
- Action: Skip move, pick up where left off

**Error cases:**
- Process in `02_framing/` without `done: true`: "Process framing is not complete yet. Finish framing first."
- Process in `01_noticed/`: "Process has not been framed yet. Run frame first."
- Process in a later stage: "Process has already passed designing."

### 2. Start Designing

**Skip this step if resuming (process already in `03_designing/`).**

Three actions:

1. Move process folder from current stage to `03_designing/`:
   ```bash
   mv .kanban/meta-kanban/02_framing/process-name/ \
      .kanban/meta-kanban/03_designing/process-name/
   ```

2. Set `done: false` in card.md

3. Trello: move card + mark undone:
   ```bash
   python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 6990dbb9c95b64da141fe03a
   python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
   ```

### 3. Create Todos

On first entry, create todos for each design step:
1. Identify types (01-card-format.md)
2. Design stages (02-board-structure.md)
3. Design steps and deliverables (03-deliverables.md)
4. Design automation (04-skill-structure.md)
5. Design review

On resume, check if todos exist. If not, create them and mark completed steps as done based on which design files already exist.

### 4. Work Through Design Steps

The design phase produces 4 files in sequence. Each builds on the previous. The user may work through them in one session or across multiple sessions.

Check which design files already exist and pick up where left off. Read `framing.md` first -- it contains the answers that drive every design decision.

**Gotcha: Types before stages.** Card format (what types of things flow through the process) must be designed before board structure (how they flow). You need to know what you're dealing with before designing how it moves. If stages are designed without knowing the types, the board won't account for label-branched behavior or type-specific deliverables.

**Gotcha: Not every step is a new deliverable.** Some design concerns refine an existing deliverable rather than producing a new file. Personas refine skill files. Cross-references are inline in output-producing guides. Discussion capture is a built-in skill behavior. Only create a new file when the concern genuinely needs its own artifact.

#### Step 1: Identify what types of things the process operates on

Read `01-card-format-guide.md` in this folder. Before designing stages, understand what flows through the pipeline -- the types, labels, and card content that define what you're working with.

Produces: `01-card-format.md`

#### Step 2: Design high-level stages

Read `02-board-structure-guide/guide.md` in this folder. Now that you know what types of items flow through, design the stages they move through -- the board structure, stage names, and progression rules.

Produces: `02-board-structure.md`

#### Step 3: Design steps and deliverables for each stage

Read `03-deliverables-guide.md` in this folder. Specify what each stage produces: deliverable files, numbering conventions, file naming, and label-branched deliverables.

Produces: `03-deliverables.md`

#### Step 4: Design the automation

Read `04-skill-structure-guide/guide.md` in this folder. Design the skill dispatch structure: main SKILL.md, sub-skills, guide files, utilities, persona assignments, reference example placement, and cross-references.

Produces: `04-skill-structure.md`

### 5. Design Review

**Persona shift: Pragmatic Critic.** Step back from the Architect role. Read the complete design spec with fresh eyes and give honest, independent feedback focused on real problems -- not critique for its own sake. The goal is to catch what the designer was too close to see before committing to implementation.

Read all 4 design files + `framing.md`. Then present:
- What looks solid
- What's missing or underspecified
- What's overcomplicated
- What could fail in practice

**Common mistakes** (learned from experience -- check each one):

1. **Deliverable proliferation.** Did every design step become its own file? If a step's output is fundamentally better served as an update to an existing deliverable, don't create a new one.
2. **Completeness check.** Cross-reference everything the design mentions -- labels, types, patterns, deliverables. Each one should either be fully addressed in a guide, explicitly marked TBD, or removed because it was hallucinated. If a type was imagined but never discussed or guided, it doesn't belong.
3. **Process artistry.** Do the stages flow naturally? Does each stage earn its place? Noticing should be frictionless -- if the first stage asks for analysis or design, work is in the wrong place. The earlier steps facilitated the design -- this step evaluates whether the result is elegant.
4. **Over-engineering stages.** More stages means more handoff overhead. If two stages always happen together or the boundary is fuzzy, they should probably be one stage.
5. **Missing the "where do outputs go" question.** A feeder process that doesn't specify which boards receive its outputs will produce work that sits in done with nowhere to go.
6. **Skill/agent concerns not addressed.** Does `04-skill-structure.md` include interaction modes (not just persona names), delegation targets, and agent embedding plans? These set up the Claude Extension Mastery step in implement -- if they're missing here, that step becomes discovery instead of confirmation.
7. **Types before stages.** Was the card format designed before the board structure? Types inform stages -- label-branched deliverables, type-specific guides, and stage granularity all depend on knowing what flows through the pipeline. If stages were designed first and types retrofitted, revisit the board structure.
8. **Model mismatch in agent embedding.** Are agent models matched to task complexity, not project importance? A formulaic file scan should use haiku even in a critical process. An agent reasoning about architectural trade-offs should use sonnet/opus even if budget is tight. Check each planned agent's model against what it actually does.

Discuss with the user. If changes are needed, make them to the design files directly. Iterate until the user is satisfied.

### 6. Complete Designing

When all 4 design files are complete and the review is satisfied, two actions:

1. Set `done: true` in card.md

2. Trello: mark done:
   ```bash
   python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
   ```

Report what was produced, then offer next steps:
1. `/commit` to save the work
2. `/retro` to reflect on the session
3. `/meta-kanban implement <process-name>` to advance to implementing
