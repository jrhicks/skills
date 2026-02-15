# Insight Dump: Skill & Agent Concerns Adapted for Process Skills

Captured 2026-02-14. To be woven into the meta-kanban guides.

## Source Material

- Skill meta-requirements: `_project/requirements/ears/agent/skills.ears.md` (6 concerns, 21 requirements)
- Agent meta-requirements: `_project/requirements/ears/agent/agents.ears.md` (7 concerns, 20 requirements)

## Core Insight

Meta-kanban produces skills that govern processes. The generic skill/agent meta-requirements apply but need adaptation -- process skills have a fixed template (dispatch, sub-skills, stages, done flow) that handles many concerns automatically. The per-process design questions are different from generic skill design.

---

## Adapted Skill Concerns for Process Skills

### 1. Orchestration

**Template handles:** Pipeline sequencing (stages run in order), dispatch routing.

**Per-process question:** "Which stages involve enough research or processing that they'd benefit from background agents?" -- forking context to protect the main window from bloat.

### 2. Delegation and Composition

**Template handles:** Trello API delegation, sub-skill dispatch, guide loading.

**Per-process questions:**
- "What hardened agents should this process's stages use?" -- codebase-analyzer, codebase-locator, codebase-pattern-finder for research. These solve under-dumping/over-dumping and protect the context window.
- "What hardened skills should stages delegate to instead of reimplementing?" -- gemini-web-research for web research, nano-banana for images, trello skill for card management. Process skills should compose existing capabilities, not rebuild them.
- "What other skills or boards does this process feed into or pull from?" -- cross-board connections for feeder processes.

**Known violation:** Trello operations are currently embedded as raw `trello_api.py` calls in every process skill instead of delegating to the trello skill. Root cause: trello skill is user-invocable only, so Claude can't auto-discover it. (TODO: make trello skill model-invocable.)

### 3. Functionality

**Template handles:** Pipeline structure, stage dispatch.

**Per-process question:** "What domain knowledge do the stage personas need that a generic pipeline wouldn't have?" -- captured through guides and reference examples. Largely already covered by existing design steps.

### 4. Guardrails

**Template handles:** Idempotency (mode detection: start vs resume), mutation tracking (kanban folder moves + Trello state), recoverability (deliverable accumulation -- files persist across sessions).

**Per-process question:** "What happens when Trello and local state diverge?" -- the one guardrail the template doesn't fully solve. Mob has a sync utility for this; not every process does.

### 5. User Interface

**Template handles:** Invokability (user-invoked via slash command), menu (dispatch table), sub-command routing.

**Per-process design -- three layers:**

#### Layer 1: Todos as Navigation (Universal)

Every sub-skill creates todos on stage entry. This is the "way back from rabbit holes" -- visible progress tracking so the user always knows where they are and what's left. Not a UI choice, just infrastructure. Apply to all process skills built by meta-kanban.

#### Layer 2: Interaction Mode (Per Step)

Each step uses the mode that fits its work:

| Mode | When | Pattern |
|------|------|---------|
| **Execute** | Autonomous work with a clear spec | Executive summary of intent, then do it, then report results |
| **Facilitate** | Decisions to be made, understanding to build | Provoke conversation, present drafts for reaction, guide toward clarity |
| **Review** | Multiple items needing individual attention | Itemize, go through one at a time, encourage deep dives |

**Sub-skills must explicitly detail the interaction mode.** Don't depend on persona name implying a mode -- a fresh context won't infer "Builder means execute mode." Write the interaction contract into the sub-skill SKILL.md.

#### Layer 3: Interaction Rules

**Outline before itemizing.** Any time you present items one at a time (review or facilitate), show the full outline first: "Here are the N items we'll cover: [concise list]." The user needs the map before the territory -- without it they're guessing how many, what kind, and whether to skip ahead.

**One-at-a-time is expensive -- use it for high-leverage outputs only.** Final requirements, design decisions, architectural critiques -- things where the user's input on each item could meaningfully change the outcome. For lower-leverage lists ("here are the 12 files I'll create"), a batch summary is fine. This is part of the art of process design, not a mechanical rule.

#### Persona Drives Mode (But Doesn't Replace Explicit Contract)

- Builder --> Execute
- Architect/Facilitator --> Facilitate
- Pragmatic Critic --> Review

Persona assignment implies interaction mode, but the sub-skill must spell it out explicitly.

### 6. Progressive Discovery

**Template handles:** Dispatch table routes to sub-skills, guides load only when needed, reference examples live in folders alongside guides.

**Per-process question:** "For each stage, does the persona need teaching material (guides, ref examples) or just instructions?" Match guide depth to persona needs:
- Autonomous personas need specs/instructions
- Collaborative personas need scaffolds and reference examples

**Turtles all the way down.** Progressive discovery is recursive at every level:
- Main SKILL.md --> concise, links to sub-skills
- Sub-skill SKILL.md --> concise, links to guides
- Guides --> concise, link to reference examples
- Reference examples --> the actual depth

At every level: describe concisely, link deeper. Never inline what can be linked. This keeps context windows small and lets Claude load exactly what it needs for the current step.

**Implementation audit.** After the Builder creates all skill files, audit progressive discovery: Is the main SKILL.md concise enough? Does it describe-and-link or inline? Are guides loading only when needed? This is a verification step in the implement phase, not a design step.

---

## Agent Embedding for Process Skills

Embed agents for any task that could be context-heavy where we only need the outcome, or that can be done in parallel. See agent meta-requirements (`_project/requirements/ears/agent/agents.ears.md`) and Claude context engineering best practices.

Key agent concerns to address when embedding:

| Concern | Design Question |
|---------|----------------|
| Orchestration | Sub-agents? Turn budget? |
| Delegation | Telephone risk across interpretation hops? |
| Context Management | What must be faithfully preserved? What's out of scope? |
| Persona and Model | What role? Which model (haiku for volume, opus for reasoning)? |
| Guardrails | Tool restrictions? File modification boundaries? |

---

## Claude Extension Mastery Step (New in Implement Phase)

**The big addition.** Before the Builder goes autonomous, add a collaborative step where the user and Claude translate the design spec into a skill that follows skill/agent best practices. This is the bridge between "good process design" and "good Claude extension."

### What it does

Walk through the adapted concerns checklist with the user:
1. **Delegation audit** -- identify hardened agents and skills each stage should use instead of reimplementing
2. **Agent embedding plan** -- for any task that could be context-heavy and we only need the outcome, or can be done in parallel
3. **Interaction mode contracts** -- define execute/facilitate/review explicitly for each sub-skill
4. **Todo structure** -- plan the todo-on-entry items for each stage
5. **Progressive discovery plan** -- what level of guide depth each stage needs

### Where it goes in implement

```
1. Find and validate
2. Start implementing (move folders)
3. Read design spec
4. Claude Extension Mastery (NEW -- collaborative, pre-automation)
5. Execute implementation (autonomous Builder)
6. Progressive discovery audit (NEW -- post-build verification)
7. Complete and move to done
```

### Back-propagation

Earlier steps should set up for success by seeding awareness of these concerns:

- **Framing** -- Q1 (orchestration) should prompt thinking about which stages might need background agents. Q3 (what flows through) should consider delegation to existing skills.
- **Design / 04-skill-structure** -- persona assignments should include interaction mode. Agent embedding should be part of the directory tree design. Delegation targets should be identified.
- **Design Review** -- common mistake: "Did the design consider skill/agent concerns?" Cross-reference the adapted concerns checklist.

The goal: by the time you reach Claude Extension Mastery in implement, most of the answers are already in the design files. The mastery step is confirmation and refinement, not discovery from scratch.

---

## Integration Plan (What Files Change)

### Implement phase (04-implement/SKILL.md)
- Add step 4: Claude Extension Mastery (collaborative, pre-automation)
- Add step 6: Progressive Discovery Audit (post-build verification)
- Renumber existing steps accordingly

### Skill template guide (04-implement/skill-template-guide/guide.md)
- Add todo-on-entry pattern as universal infrastructure
- Add interaction mode documentation requirement for each sub-skill
- Add progressive discovery audit checklist

### Skill structure guide (03-design/04-skill-structure-guide/guide.md)
- Add "Interaction Mode" to persona assignments (not just name + behavior)
- Add "Agent Embedding" section
- Add "Delegation Targets" section
- Reference adapted concerns checklist

### Design Review (03-design/SKILL.md)
- Add "skill/agent concerns addressed?" to common mistakes

### Framing guide (02-frame/framing-guide.md)
- Seed orchestration awareness in Q4 (main steps)
- Seed delegation awareness in Q3 (what flows through) or new question

---

## TODOs

- [ ] Make trello skill model-invocable, consolidate raw trello_api.py calls across process skills
- [ ] Add auto-todo creation pattern to skill-template-guide as universal infrastructure
- [ ] Write Claude Extension Mastery step into implement SKILL.md
- [ ] Add progressive discovery audit to implement phase
- [ ] Back-propagate concerns into skill-structure-guide (interaction modes, agent embedding, delegation)
- [ ] Back-propagate awareness into framing guide
- [ ] Add skill concerns check to design review common mistakes
- [ ] Write interaction mode contracts into existing process skills (mob, android-inspectpro-review, meta-kanban itself) -- future work, not part of this integration
