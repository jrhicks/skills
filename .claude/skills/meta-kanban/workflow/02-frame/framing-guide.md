# Framing Guide

Answer these fundamental questions to understand the process's nature before designing its board structure. The answers drive every design decision in the next stage.

## Questions

### 1. Purpose

What is this process for? What problem does it solve or what goal does it achieve?

### 2. Process Type

Is this a **feeder** or **direct-output** process?

- **feeder** -- outputs feed other boards or improve guides for other processes. The board itself does not produce end-products.
- **direct-output** -- deliverables are the end-products. Each item progressing through the board produces concrete artifacts.

*Reference examples:*
- **feeder:** android-inspectpro-review (`.claude/skills/android-inspectpro-review/`). Analyzes legacy Android codebase. Outputs leave the board as MOB cards and skill guide updates.
- **direct-output:** sdui-and-mob (`.claude/skills/mob/`). Each SDUI element progresses from Noticed through Distilling, producing EARS requirements, prototype code, native implementations.

### 3. What Flows Through

What are the different types of things that flow through this pipeline? These become labels. Understanding types is foundational -- it must happen before designing stages, because types determine label-branched behavior, type-specific deliverables, and stage granularity.

*Examples from existing processes:*
- android-inspectpro-review: `pattern` (architectural idioms) vs `functionality` (user-facing capabilities)
- sdui-and-mob: `implementation` vs `platform` (domain labels) + taxonomy labels

### 4. Main Steps

Now that you know what types of things flow through, what are the main steps (stages/columns)? What transformation happens at each step?

While discussing stages, note which ones might involve heavy research, large codebases, or processing many items. These are candidates for background agents during implementation -- capture the instinct now, even if the details come later in design. Also note the *kind* of work: formulaic scanning (cheap/fast agents) vs. deep reasoning about relationships (expensive/thorough agents). This distinction drives model selection downstream.

Eliciting good stages is an art. Use this mental model as a scaffold -- not a prescription -- while guiding the user:

1. **Easy inbox.** Make it frictionless for things to enter the process. A notice stage should be lightweight -- just capture what was observed. Don't front-load work here (work is friction) and don't pre-prescribe a solution (locking in too early creates friction in later steps).

2. **Understand before solving.** The next stage is typically about comprehension. Sometimes that means researching what currently exists. Sometimes it means framing -- what do we ultimately want to achieve, who is this for? The form varies but the intent is the same: build understanding before committing to a direction.

3. **Break down, then bring together.** Analysis (decomposing into understandable parts) often precedes synthesis (converging the parts into a solution). Not every process needs both as separate stages -- simpler processes may combine them -- but the mental distinction matters.

4. **Do the work.** Implementation, building, executing. The stage where artifacts get produced.

5. **Refine.** Quality assurance, review, iteration. Catching what the doing stage missed.

6. **Ship.** Delivery, deployment, release notes, documentation. Moving the output to where it needs to go.

7. **Done.** Terminal state.

Not every process needs all of these. Some collapse multiple concerns into one stage. Some skip stages entirely. The facilitator's job is to listen for which of these concerns are present in the user's process and help them find the right granularity -- enough stages to create clear handoff points, few enough to avoid bureaucratic overhead.

**Dependency analysis (when domain techniques are known).** If the process is grounded in a known methodology or set of techniques (e.g., Winston's speaking techniques, a design framework, an engineering discipline), stages can be derived analytically rather than intuitively:

1. Explore all source material for the domain
2. List each technique with its inputs (what must be known first) and outputs (what becomes known after)
3. Build a dependency graph
4. Find natural tiers -- groups of techniques whose dependencies are all satisfied by earlier tiers
5. Tiers become candidate stages

This produces stages grounded in "what's known when" rather than arbitrary groupings. Use this approach when the user references existing guides, frameworks, or methodologies.

### 5. Deliverables

What should each step produce? Work through this stage by stage using todos to track progress.

**Context anchoring (critical).** At the start of each stage's deliverable discussion, display a running deliverable table:

```
| Stage      | Deliverables                             |
|------------|------------------------------------------|
| Brain-dump | 01-overview.md, 02-dump/                 |
| Shape      | shape-brainstorms/{03,04,05}, 06-shape   |
| Outline    | << discussing now >>                     |
| Specify    | (pending)                                |
| Produce    | (pending)                                |
```

Update and re-display this table every time a stage is locked. The user will lose track of which stage they're in -- the table re-anchors without requiring them to hold state.

**Lead with proposals, not questions.** The facilitator has context from the full discussion so far. Use it. For each stage:
1. **Propose** -- offer a draft deliverable list with size estimates, logical groupings, and naming. Give the user something concrete to react to.
2. **Refine** -- incorporate feedback, adjust groupings, rename.
3. **Lock in** -- confirm and advance to the next stage.

Create a todo for each stage's deliverables before diving in. This prevents rabbit holes -- if a discussion goes deep on one stage's deliverables, the todo list shows where you left off and what remains.

**Gotcha: Not every step needs its own deliverable.** Some steps refine an existing deliverable rather than creating a new file. If a step's output is "update the spec from step 2 with more detail," that's refinement, not a new artifact. Only create a new deliverable when the concern genuinely needs its own file.

*Consider:*
- Do some stages have multiple sub-deliverables?
- Do different label types produce different deliverables at the same stage?

### 6. Where Outputs Go

Where do outputs from this process end up?

- Other kanban boards?
- Skill guide updates?
- Code repositories?
- Documentation?
- External systems (Trello, GitHub, etc.)?

Also consider: are there existing skills or agents that already do some of what this process needs? Process skills should compose existing capabilities (codebase-analyzer, gemini-web-research, nano-banana, etc.) rather than rebuilding them. Note any reuse opportunities -- they'll inform delegation decisions during design.

### 7. Done Flow

Does the standard per-stage done pattern work, or does this process need something different?

Standard pattern: arrive in stage (undone) --> work --> mark done (ready to pull) --> move to next stage (undone).

## Deliverable

Produce `framing.md` in the process folder. Structure it with the same 7 sections, each containing the answers discovered during discussion. Keep answers concrete and specific -- they will drive the designing stage.
