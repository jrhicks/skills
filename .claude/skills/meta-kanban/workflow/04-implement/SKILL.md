# /meta-kanban implement <process-name>

Build the process: skill files, Trello board, and kanban folders. Uses the 4 design files as spec. Includes a collaborative pre-build step to ensure the skill follows Claude extension best practices.

## Process

### 1. Find and Validate Process

Search all stage folders for the process:
```
~/.kanban/meta-kanban/*/process-name/
```

Read `card.md` inside it.

- If process not found, suggest using `notice` first.
- If process is already in `05_done/`, report it is fully done. Ask if they want to revisit.
- If process is in `04_implementing/` with `done: true`, this means implementing was marked done but not moved yet. Proceed to step 8 (Final Move).

## Mode Detection

**Start Mode** (move from previous stage):
- Process is in `03_designing/` with `done: true`
- Action: Move to `04_implementing/`, mark undone, begin work

**Resume Mode** (continue current stage):
- Process is already in `04_implementing/` with `done` absent or false
- Action: Skip move, pick up where left off

**Error cases:**
- Process in `03_designing/` without `done: true`: "Process design is not complete yet. Finish all 4 design files first."
- Process in `01_noticed/` or `02_framing/`: "Process has not reached implementing stage yet."

### 2. Start Implementing

**Skip this step if resuming (process already in `04_implementing/`).**

Three actions:

1. Move process folder from current stage to `04_implementing/`:
   ```bash
   mv ~/.kanban/meta-kanban/03_designing/process-name/ \
      ~/.kanban/meta-kanban/04_implementing/process-name/
   ```

2. Set `done: false` in card.md

3. Trello: move card + mark undone:
   ```bash
   python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 6990dbb9d52291a2bb89ec62
   python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
   ```

### 3. Create Todos

On first entry, create todos for each implementation step:
1. Resolve output paths from scope
2. Read design spec
3. Claude Extension Mastery
4. Create Trello board
5. Write skill files (with hardcoded board path)
6. Create kanban folders (at resolved output path)
7. Progressive discovery audit

On resume, check if todos exist. If not, create them and mark completed steps as done based on what's already been built.

### 4. Resolve Output Paths

Read `scope` from `card.md`. All output paths in steps 6-7 depend on this:

| Scope | Skill output | Kanban output |
|-------|-------------|---------------|
| `global` | `~/.claude/skills/<skill-name>/` | `~/.kanban/<board-name>/` |
| `project` | `.claude/skills/<skill-name>/` | `.kanban/<board-name>/` |

The created skill's own SKILL.md must document its board location using the resolved path (not a variable). This ensures the skill knows where its board is without re-resolving scope.

### 5. Read Design Spec

Read all 4 design files from the process folder:
- `01-card-format.md`
- `02-board-structure.md`
- `03-deliverables.md`
- `04-skill-structure.md`

These are the spec. Implementation must match.

### 6. Claude Extension Mastery

**Persona: Facilitator.** This is a collaborative pre-build step. The design spec describes a good *process* -- this step ensures it will also be a good *Claude extension*. Walk through each item with the user, presenting a draft recommendation for them to react to.

**Interaction: Facilitate.** Present an outline of the 5 items below, then work through each one. These are high-leverage decisions -- take them one at a time.

Read `_project/requirements/ears/agent/skills.ears.md` and `_project/requirements/ears/agent/agents.ears.md` for the full concern checklists. Then work through:

#### 5a. Delegation Audit

For each stage, identify hardened agents and skills it should use instead of reimplementing:
- **Research tasks** -- codebase-analyzer, codebase-locator, codebase-pattern-finder
- **Web research** -- gemini-web-research skill
- **Image generation** -- nano-banana skill
- **Trello operations** -- trello skill (when model-invocable)
- **Other existing skills** -- check what's available before building new capabilities

Process skills should compose existing capabilities, not rebuild them.

#### 5b. Agent Embedding Plan

For any task that could be context-heavy where we only need the outcome, or that can be done in parallel -- plan an embedded agent. Agents are spawned via the Task tool -- no installation required.

**Every agent gets a persona**, even lightweight inline ones. Without a persona, agents default to generic behavior and either over-dump or wander. A one-liner is enough: "You are a code inventory specialist. Be exhaustive on structure, silent on style opinions."

**Inline vs. promoted:** If the agent prompt is short (5-15 lines), inline it in the SKILL.md or guide. If it needs detailed domain knowledge, multi-step procedures, or reference material (~20+ lines), promote to a definition file (e.g., `agents/analyze-agent.md`) and have the Task call read it.

For each embedded agent, address:
- What persona (name + behavioral instruction)?
- Inline or promoted to a definition file?
- What model? Match to task complexity, not project importance:
  - **haiku** for formulaic work (scan, extract, reformat)
  - **sonnet** for analytical work (understand code, draft specs). Default when unsure.
  - **opus** for reasoning work (cross-reference relationships, design tensions)
- What must be faithfully preserved from source material (telephone risk)?
- What tool restrictions and file modification boundaries?
- What is the turn budget?

See agent meta-requirements (`_project/requirements/ears/agent/agents.ears.md`) for the full concern checklist.

#### 5c. Interaction Mode Contracts

For each sub-skill, define the interaction mode explicitly. Don't depend on persona name implying a mode -- a fresh context won't infer it. Write the contract into the sub-skill spec:

| Mode | When | Pattern |
|------|------|---------|
| **Execute** | Autonomous work with a clear spec | Executive summary of intent, then do it, then report results |
| **Facilitate** | Decisions to be made, understanding to build | Provoke conversation, present drafts for reaction, guide toward clarity |
| **Review** | High-leverage items needing individual attention | Present outline first, then go through one at a time |

Rules:
- Any one-at-a-time mode must show the full outline before diving in
- One-at-a-time is expensive -- use it only when the user's input on each item could meaningfully change the outcome. For transparency-only lists, batch it.

#### 5d. Todo Structure

Plan the todo-on-entry items for each stage. When a user first invokes a stage, the sub-skill auto-creates todos for each step. This gives visible progress tracking and a way back from rabbit holes.

List the todos each sub-skill will create on entry.

#### 5e. Progressive Discovery Plan

For each stage, decide guide depth:
- **Autonomous personas** need specs and instructions
- **Collaborative personas** need scaffolds and reference examples

Apply the turtles-all-the-way-down principle: at every level, describe concisely and link deeper. Never inline what can be linked.

### 7. Execute Implementation

**Persona: Builder.** Execute the spec faithfully. Work autonomously -- the mastery step was the time for questions. Do not redesign or second-guess decisions at this stage.

Three guided sub-steps. Each has a guide file in this folder. Work through them in order.

#### Step 1: Create Trello Board

Read `trello-setup-guide.md` in this folder. Using `02-board-structure.md` as the spec, create:
- Trello board with the designed name
- Lists matching the stages
- Labels matching the types

Record all IDs. These are needed for the next step.

#### Step 2: Write Skill Files

Read `skill-template-guide/guide.md` in this folder. Using `04-skill-structure.md` as the spec + the decisions from step 5 (Claude Extension Mastery), create:
- Main SKILL.md (dispatcher) -- wire in Trello IDs from Step 1
- Sub-skill SKILL.md files (one per stage) -- wire in list IDs, interaction mode contracts, todo-on-entry items
- Guide files -- create as folders with ref files where `04-skill-structure.md` specifies promotion
- Utility SKILL.md files
- Agent definitions (if step 5b identified embedded agents)

#### Step 3: Create Kanban Folders

Read `kanban-setup-guide/guide.md` in this folder. Using `02-board-structure.md` as the spec and the resolved output paths from step 4, create:
- `<kanban-output>/<board-name>/` root folder (global: `~/.kanban/`, project: `.kanban/`)
- Stage folders with `.gitkeep` files
- `discussion.md` at the board root (if cross-topic discussion was designed)

### 8. Progressive Discovery Audit

**Persona: Pragmatic Critic.** After all files are built, audit progressive discovery in practice:
- Is the main SKILL.md concise enough? Does it describe-and-link or does it inline?
- Do sub-skills load guides only when needed?
- Are reference examples in linked folders, not inlined?
- Does every level follow: describe concisely, link deeper?

Fix any violations before marking done.

### 9. Complete and Move to Done

When all implementation is complete and the audit passes, four actions:

1. Move process folder to `05_done/`:
   ```bash
   mv ~/.kanban/meta-kanban/04_implementing/process-name/ \
      ~/.kanban/meta-kanban/05_done/process-name/
   ```

2. Set `done: true` in card.md

3. Trello: move card to Done list + mark done:
   ```bash
   python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 6990dbb82caeaef658278bc5
   python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
   ```

Report what was implemented and where, then offer next steps:
1. `/commit` to save the work
2. `/retro` to reflect on the session
3. The process is complete -- no next phase
