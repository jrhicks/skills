# Skill Template Guide

Write the skill files for the new process. Use `04-skill-structure.md` from the process's design files as the spec.

## Persona

**Builder** -- Execute the spec faithfully. Build exactly what the design files describe. Work autonomously -- the design phase was the time for questions. Do not redesign or second-guess design decisions at this stage.

## Gotcha: Not Every Design Concern Is a Separate File

Several concerns from the design spec get wired into skill files rather than existing as standalone artifacts:
- **Personas** are written into each sub-skill's `## Persona` section (per `04-skill-structure.md` persona assignments)
- **Cross-references** are inline in the main SKILL.md and in output-producing guide files
- **Discussion capture** is a built-in behavior added to every sub-skill (see below)
- **Reference examples** are placed in promoted guide folders (per `04-skill-structure.md` reference example placement)

Don't create separate files for these. They refine skill files.

## Main SKILL.md Template

The main SKILL.md follows a consistent pattern across all kanban skills. Use this structure:

```yaml
---
name: <skill-name>
description: |
  <2-3 line description>
  Triggers: "/<skill-name>", "<verb> <noun>".
user-invocable: true
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---
```

Required sections (in order):
1. **Usage** -- all verbs with argument syntax
2. **Board Configuration** -- Board name, ID, URL, Lists table, Labels table
3. **Trello API** -- delegates to the trello skill (see Skill Delegation below)
4. **Pipeline** -- stage table (number, name, verb, what happens, produces)
5. **Labels** -- label descriptions with reference examples if applicable
6. **Done Flow** -- standard done pattern description
7. **Dispatch** -- verb-to-file table for workflow stages and utilities
8. **Location** -- folder structure tree showing where items live
9. **Element Location** -- how to find an item (glob pattern)
10. **Card Format** -- frontmatter + body template
11. **Deliverable Sequence** -- per-stage list of deliverable files
12. **Cross-references** -- where outputs go (if feeder process). Inline here, not a separate file.
13. **Examples** -- usage examples

Note: The main SKILL.md does NOT include a `## Persona` section. Personas belong in sub-skill SKILL.md files and guide files only.

## Sub-Skill SKILL.md Template

Each sub-skill follows a consistent pattern:

1. **Title** -- `# /<skill-name> <verb> <item-name>`
2. **Description** -- what this stage does
3. **Persona + Interaction Mode** -- `## Persona` section (see format below)
4. **Find and Validate** -- search glob pattern, read card.md, validation rules
5. **Mode Detection** -- Start Mode vs Resume Mode vs Error cases
6. **Start** -- folder move + done:false + Trello move + mark_undone + create todos
7. **Work** -- what to produce, which guides to read, label-branching if any
8. **Complete** -- done:true + Trello mark_done + offer next steps

### Persona + Interaction Mode Section

Every sub-skill SKILL.md must include both a `## Persona` section and an explicit interaction mode. These are placed after the title/description, before the first procedural heading. Use the assignments from `04-skill-structure.md` and the interaction mode contracts from the Claude Extension Mastery step.

```markdown
## Persona

**Name** -- What to do (1-2 sentences). What NOT to do (1 sentence).

**Interaction: Execute/Facilitate/Review.** Describe exactly how this step engages the user (1-2 sentences).
```

The interaction mode is not optional. Don't depend on the persona name implying a mode -- a fresh context won't infer "Builder means execute mode." Spell it out:

| Mode | Contract |
|------|----------|
| **Execute** | Present executive summary of intent, then do the work, then report results. |
| **Facilitate** | Provoke conversation, present drafts for reaction, guide toward clarity. |
| **Review** | Present outline of all items first, then go through high-leverage items one at a time. |

Rules for one-at-a-time modes (Review and some Facilitate):
- Always show the full outline before diving in -- the user needs the map before the territory
- One-at-a-time is expensive -- use only when the user's input on each item could meaningfully change the outcome
- For transparency-only lists, batch it

The main dispatcher SKILL.md does NOT get a persona section (it just routes). Guide files may carry per-step persona refinements that specialize the stage-level persona.

For the final stage (if it has a double-move to Done): add a step that moves to `done/` folder + Trello Done list.

### Stage Completion: Offer Next Steps

Every sub-skill's Complete step must end by offering three options:

1. **Commit** -- `/commit` to save the work
2. **Retro** -- `/retro` to reflect on the session before moving on
3. **Next phase** -- `/<skill-name> <next-verb> <item-name>` to advance

This prevents dead air after completing a stage and keeps momentum.

### Todo-on-Entry (Universal)

Every sub-skill must create todos for visible progress tracking and a way back from rabbit holes.

**Start mode (first invocation):** After the folder move and Trello update, create todos for each step in the stage.

**Resume mode:** Check if todos already exist for this stage. If not (e.g., stage was started in an older session before todos were standard), create them and mark completed steps as done based on what deliverables already exist. If todos exist, pick up where they left off.

The specific todos come from the Claude Extension Mastery step's todo structure plan. Each todo should be concise enough to scan but descriptive enough to resume from.

### Discussion Capture (Built-in Behavior)

Every sub-skill SKILL.md must include this instruction in its Work section:

> If an aha moment or insight arises during work -- something that changes understanding, reveals a pattern, or would help future work on this or other items -- append it to `discussion.md` in the item's folder. Format: `## YYYY-MM-DD -- <insight title>` followed by the insight. This is standing behavior at every stage, not a deliverable.

This ensures discussion capture is woven into the skill's DNA rather than being a separate concern to design.

## Guide Promotion

Check `04-skill-structure.md` for which guides should be promoted to folders. For each promoted guide:

1. Create a folder with the guide's name (e.g., `analyze-guide/` instead of `analyze-guide.md`)
2. Place the guide content in `guide.md` inside the folder
3. Create the `ref-*.md` files specified in `04-skill-structure.md`
4. Add a `## Reference Examples` section to `guide.md` pointing to the ref files
5. Update the sub-skill SKILL.md to read `<guide-name>/guide.md` instead of `<guide-name>.md`

Guides not flagged for promotion stay as flat `.md` files.

## Reference Examples

Study these annotated skill trees from existing processes for concrete implementation patterns:

- **`ref-android-inspectpro-review-skill.md`** -- 4-stage feeder process with label branching, multiple synthesis lenses, double-move apply stage, and agent spectrum (promoted source-analyzer + inline lens extractors and card drafters)
- **`ref-mob-skill.md`** -- 6-stage direct-output process with collection-guides, framework-guides, deep prototype hierarchy, extra sync utility, and agent spectrum (promoted element-researcher + inline EARS drafter and parallel platform scaffolders)

## Embedded Agents

If `04-skill-structure.md` specifies embedded agents, build them using the Task tool. Agents are spawned via `Task()` -- no installation or agent definition file required (though promoted agents use one for complex instructions).

### Task Tool Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `subagent_type` | yes | Agent type: `general-purpose` (all tools), `Explore` (read-only, fast), `Bash` (shell only) |
| `prompt` | yes | Instructions for the agent. **Must include a persona.** |
| `description` | yes | Short summary, 3-5 words (e.g., "Inventory source files") |
| `model` | no | `haiku` (fast/cheap), `sonnet` (balanced), `opus` (deep reasoning). Omit to inherit parent model. |
| `max_turns` | no | Max agentic turns before stopping. Set to prevent runaway agents. |
| `run_in_background` | no | `true` to run concurrently. Use for parallel independent tasks. |

### Model Selection

Match the model to the **task complexity**, not the project importance.

| Model | Cost | Speed | Use When |
|-------|------|-------|----------|
| `haiku` | lowest | fastest | Scanning, inventory, extraction, reformatting. The task is formulaic -- read X, return Y in format Z. No judgment calls. |
| `sonnet` | mid | mid | Analysis, drafting, pattern recognition. The agent needs to understand code and make reasonable inferences. Default when unsure. |
| `opus` | highest | slowest | Architectural reasoning, cross-referencing complex relationships, nuanced judgment. The agent needs to reason about trade-offs, not just extract and transform. |

**Rules of thumb:**
- **"Scan 20 files and return a table"** -- haiku. Formulaic extraction.
- **"Read this codebase and draft EARS requirements"** -- sonnet. Needs code understanding + structured writing.
- **"Analyze how these 3 subsystems interact and identify design tensions"** -- opus. Needs relational reasoning.
- **Parallel agents doing independent work** -- haiku. Volume + independence = cheap and fast.
- **Single agent doing the critical research for a stage** -- sonnet or opus. Quality matters more than speed.
- **Omit `model`** to inherit the parent conversation's model. Good when the agent should match whatever the user is running.

**Constraints:**
- Skills run in the main context and CAN spawn agents freely
- Spawned agents cannot spawn further agents (one level deep)
- Background agents cannot access MCP tools
- Background agents get permissions pre-approved at launch; unapproved tool calls fail silently

### Inline Agents

For focused, simple tasks (scan files, return summary). Write the Task call directly in the SKILL.md or guide file:

```markdown
Spawn a background agent to inventory the source files:

Task(
  subagent_type="general-purpose",
  prompt="**Persona: Inventory Specialist.** Be exhaustive on structure, silent on style.
    Read all files in <path>. For each file, extract: name, purpose, key methods.
    Return a markdown table. Preserve exact class and method names.",
  description="Inventory source files",
  model="haiku",
  max_turns=15,
  run_in_background=true
)
```

**Every agent must have a persona** in its prompt -- even a one-liner. Without it, agents default to generic behavior and over-dump or wander.

### Promoted Agents

For agents with detailed domain knowledge, multi-step procedures, or specific fidelity rules. Create a definition file and reference it:

1. Create `agents/<agent-name>.md` in the skill folder
2. Write the full agent instructions in the file (persona, steps, output format, fidelity rules)
3. Reference from the SKILL.md:

```markdown
Spawn a background agent for deep analysis:

Task(
  subagent_type="general-purpose",
  prompt="Read `agents/analyze-agent.md` in this skill folder and follow those instructions.
    Item to analyze: <item-name>. Item folder: <path>.",
  description="Analyze <item>",
  model="sonnet",
  max_turns=25
)
```

### Parallel Agents

For independent work that can run simultaneously, spawn multiple agents with `run_in_background=true`:

```markdown
Spawn parallel agents for platform scaffolding:

Task(
  subagent_type="general-purpose",
  prompt="**Persona: Android Scaffolder.** Read the interface at <path> and EARS at <path>.
    Scaffold the Android POC structure. Preserve exact interface attribute names.",
  description="Scaffold Android POC",
  model="haiku",
  max_turns=15,
  run_in_background=true
)

Task(
  subagent_type="general-purpose",
  prompt="**Persona: iOS Scaffolder.** Read the interface at <path> and EARS at <path>.
    Scaffold the iOS POC structure. Preserve exact interface attribute names.",
  description="Scaffold iOS POC",
  model="haiku",
  max_turns=15,
  run_in_background=true
)
```

Review results from both agents sequentially after they complete.

### Agent Prompt Best Practices

1. **Always set a persona** -- even one line focuses the agent's behavior
2. **Specify output format** -- "return a markdown table" / "return YAML frontmatter + body"
3. **Name fidelity boundaries** -- "preserve exact class names" / "preserve config JSON keys"
4. **Restrict scope** -- "read only files in <path>" / "do not modify any files"
5. **Set max_turns** -- prevent runaway agents (15 for scans, 25-30 for deep analysis)
6. **Use `Explore` for read-only research** -- faster than `general-purpose` when no writes needed

**Promotion heuristic:** If the agent prompt exceeds ~20 lines or needs reference material, promote to a file. Same heuristic as guide promotion.

## Skill Delegation

When a skill depends on another skill's capabilities, delegate to it **by name** -- never reference its internal file paths, script paths, or invocation syntax. The skill system resolves internals. Leaking them creates coupling that breaks when the referenced skill reorganizes, and defeats the purpose of having a skill abstraction.

**Wrong:**
```markdown
For Trello operations, use `.claude/skills/trello/SKILL.md`.
Script path: `python3 .claude/skills/trello/scripts/trello_api.py <command> [args]`
```

**Right:**
```markdown
For Trello write operations, delegate to the **trello** skill. It handles all card operations (create, move, update, mark done/undone, list, etc.) and EARS sync.
```

This applies to any skill-to-skill dependency, not just Trello. If the process skill needs image generation, it delegates to the **nano-banana** skill. If it needs code review, it delegates to the **standards-review** skill. Always by name.

## Trello IDs

Trello board should already be created (Step 1 of implement). Wire all IDs into:
- Main SKILL.md Board Configuration section
- Each sub-skill's hardcoded list IDs for move_card commands
- Notice sub-skill's label IDs for create_card commands
