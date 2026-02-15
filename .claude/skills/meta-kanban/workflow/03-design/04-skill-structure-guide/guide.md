# Skill Structure Guide

Design the skill dispatch structure: how the skill is organized into files, what each file does, and how they relate. This is the final design step -- it absorbs several concerns that refine the skill rather than producing separate deliverables.

Read all previous design files (01-03) and `framing.md` first -- they determine what sub-skills, guides, and personas are needed.

## Persona

**Software Architect** -- Design file structure for dispatch, maintenance, and discoverability. Follow established conventions from reference processes. Present a directory tree draft and ask for reactions. Do not invent novel organizational patterns when existing conventions work.

## Questions to Answer

### Main SKILL.md

The main SKILL.md is the dispatcher. It needs:
- Frontmatter (name, description, triggers, allowed-tools)
- Usage section with all verbs
- Board Configuration (Trello IDs)
- Pipeline table
- Label descriptions with reference examples
- Done Flow description
- Dispatch table (verb --> sub-skill file)
- Process/Element Location (folder structure)
- Card format template
- Deliverable sequence
- Cross-references section (if outputs leave the board -- see below)
- Examples

### Sub-Skill Files

One SKILL.md per workflow stage. Each needs:
- Mode detection (start vs resume)
- Stage transition mechanics (folder move + Trello move + done flag)
- Work instructions (what to produce, which guides to read)
- Completion mechanics (mark done + Trello mark_done)

*Pattern from android-inspectpro-review:*
```
workflow/01-notice/SKILL.md    -- instant recognition
workflow/02-analyze/SKILL.md   -- branched by label
workflow/03-synthesize/SKILL.md -- multiple guided discussions
workflow/04-apply/SKILL.md     -- double-move (apply then done)
```

### Guide Files

Where do guide files live? In the same folder as the sub-skill SKILL.md they support.

List each guide file:
- Filename
- Which sub-skill uses it
- What it guides (what lens or perspective it applies)

Guides that need real-world reference examples should be flagged for promotion to folders (see Reference Example Placement below).

### Utilities

What utility sub-skills are needed?

Standard:
- `utilities/list/SKILL.md` -- scan stage folders, show board status

Additional? (sync, archive, report, etc.)

### Persona + Interaction Mode Assignments

Assign a persona and interaction mode to each sub-skill. These are written directly into each file's `## Persona` section during implementation -- they are not a separate deliverable.

Think about the failure mode for each step:
- **Capture stages** fail when Claude over-analyzes instead of recording --> Registrar + Execute
- **Exploration stages** fail when Claude answers for the user instead of facilitating --> Facilitator + Facilitate
- **Design stages** fail when Claude starts from blank instead of drafting from context --> Architect + Facilitate
- **Execution stages** fail when Claude redesigns instead of building --> Builder + Execute
- **Review stages** fail when Claude rubber-stamps instead of critiquing --> Pragmatic Critic + Review
- **Reporting stages** fail when Claude editorializes instead of presenting facts --> Librarian + Execute

The interaction mode must be explicit -- not implied by persona name. Include for each file:
- Persona name and behavioral instruction
- Interaction mode (Execute, Facilitate, or Review) with a sentence describing how the step engages the user
- What NOT to do

**Early collaborative stages should consider what external material the persona should proactively pull in.** A facilitator that only asks questions misses the opportunity to bring in source material (reference repos, file dumps, web research via skills like gemini-web-research). If the stage's input is "the user's brain," the persona should actively help externalize it.

### Delegation Targets

For each stage, identify hardened agents and skills it should use instead of reimplementing. Process skills should compose existing capabilities, not rebuild them.

Common delegation targets:
- **Research tasks** -- codebase-analyzer, codebase-locator, codebase-pattern-finder agents
- **Web research** -- gemini-web-research skill
- **Image generation** -- nano-banana skill
- **Trello operations** -- trello skill
- **Other process skills** -- cross-board connections for feeder processes

For each stage, note: "delegates to X for Y" or "no delegation needed."

### Agent Embedding

For any stage that could be context-heavy where we only need the outcome, or that can run in parallel -- plan an embedded agent. This protects the main context window and solves under-dumping/over-dumping.

**Every agent gets a persona.** Even a lightweight inline agent needs a persona to focus its behavior. Without one, agents default to generic mode and either over-dump or wander. A one-liner is enough: "You are a code inventory specialist. Be exhaustive on structure, silent on style opinions."

**Inline vs. promoted (same heuristic as guide promotion):**

- **Inline** -- The Task prompt is self-contained in the SKILL.md or guide file. Good for focused, simple tasks: "scan these files, return a summary table." The prompt is 5-15 lines including persona.
- **Promoted** -- The agent has detailed domain knowledge, multi-step procedures, or specific fidelity rules that would bloat the SKILL.md. Create an agent definition file (e.g., `agents/analyze-agent.md`) and reference it from the Task call: "Read `agents/analyze-agent.md` and follow those instructions." Progressive discovery -- the SKILL.md describes what the agent does concisely, the file carries the depth.

**Promotion heuristic:** If the agent prompt exceeds ~20 lines or needs reference material, promote to a file. If it's a focused scan-and-summarize, inline it.

**Model selection -- match the model to task complexity, not project importance:**
- **haiku** -- formulaic work: scan files, extract fields, reformat data. No judgment calls.
- **sonnet** -- analytical work: understand code, draft requirements, recognize patterns. Default when unsure.
- **opus** -- reasoning work: cross-reference complex relationships, identify design tensions, make nuanced trade-offs.
- **Parallel agents doing independent work** lean haiku (volume + independence = cheap and fast).
- **Single agent doing critical research** leans sonnet/opus (quality over speed).

For each embedded agent, specify:
- **Persona** -- name and behavioral instruction (required even for inline agents)
- What task it handles and why forking is needed
- Inline or promoted (and file path if promoted)
- Which model and why (match to task complexity per the guidance above)
- What must be faithfully preserved from source material (telephone risk)
- Tool restrictions and file modification boundaries
- Turn budget

See agent meta-requirements (`_project/requirements/ears/agent/agents.ears.md`) for the full concern checklist. Not every process needs embedded agents -- only flag stages where context protection or parallelism matters.

### Cross-References

If outputs from this process leave the board (feeder processes especially), specify where they go. Cross-references are inline -- they belong in:
- The main SKILL.md's cross-references section (board-level overview)
- The specific guide file that produces the output (actionable instructions for the stage)

Don't create a separate cross-references file. The guide that produces an output should know where it goes.

### Reference Example Placement

For each guide that describes structure (folder trees, file organization, stage layouts), decide whether it needs annotated reference trees from existing processes.

Convention:
- **Needs examples** --> promote to folder: `guide-name/guide.md` + `ref-*.md` files
- **Inline snippets suffice** --> keep as flat `guide-name.md`

Specify which guides get promoted and what reference files they'll contain.

### Discussion Capture (Built-in Behavior)

Every card folder includes a `discussion.md` file for capturing aha moments during the card's lifecycle. This is not designed per-process -- it's a built-in behavior of all skills built by meta-kanban.

Every sub-skill SKILL.md should instruct the persona to append insights to `discussion.md` when they arise during work at any stage. This is not a separate deliverable -- it's standing knowledge that accumulates naturally.

### Directory Tree

Draw the complete skill directory tree.

*Example:*
```
.claude/skills/process-name/
├── SKILL.md
├── workflow/
│   ├── 01-notice/
│   │   └── SKILL.md
│   ├── 02-stage/
│   │   ├── SKILL.md
│   │   └── guide.md
│   └── ...
└── utilities/
    └── list/
        └── SKILL.md
```

## Reference Examples

Study these annotated skill trees from existing processes to understand real-world structure decisions:

- **`ref-android-inspectpro-review-skill.md`** -- 4-stage feeder process with label branching, multiple synthesis lenses, double-move apply stage, and agent spectrum (promoted source-analyzer + inline lens extractors and card drafters)
- **`ref-mob-skill.md`** -- 6-stage direct-output process with collection-guides, framework-guides, deep prototype hierarchy, extra sync utility, and agent spectrum (promoted element-researcher + inline EARS drafter and parallel platform scaffolders)

## Deliverable

Produce `04-skill-structure.md` in the process folder. Include:
1. Complete directory tree with description of each file
2. Persona + interaction mode assignment for each sub-skill (name, behavior, mode, anti-pattern)
3. Delegation targets for each stage (which agents/skills it uses)
4. Agent embedding plan (if any stages need forked context)
5. Cross-reference map (where outputs go, which guides carry the instructions)
6. Reference example placement (which guides get promoted to folders, what ref files)
7. Notes on any non-standard patterns
