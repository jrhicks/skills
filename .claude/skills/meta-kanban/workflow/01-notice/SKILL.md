# /meta-kanban notice <process-name>

Create a new process in the meta-kanban board.

## Persona

**Registrar** -- Capture the process need efficiently. Validate, record, report. Infer the label from context when obvious; only ask when genuinely ambiguous. Do not analyze whether the process is a good idea or suggest alternative approaches.

**Interaction: Execute.** Noticing is instant recognition -- validate, create, report. No todos needed (single action).

## Required Information

- **process-name** -- kebab-case name (e.g., `android-inspectpro-review`, `release-pipeline`)
- **label** -- `feeder` or `direct-output`
- **scope** -- `global` or `project`

The user may provide all explicitly, or just the process name. Infer the label from context if possible, otherwise ask. Always ask scope explicitly (see step 1.5).

## Label Inference

- If the process generates work for other boards or improves guides --> `feeder`
- If the process produces end-products or achieves goals itself --> `direct-output`
- If ambiguous, ask: "Is this a feeder process (outputs go to other boards) or a direct-output process (deliverables are the end-products)?"

## Process

### 1. Validate Process Doesn't Exist

Search for existing process across all stage folders:
```
~/.kanban/meta-kanban/*/process-name/
```

If found, report the process already exists and show its current stage. Stop.

### 2. Ask Scope

Use AskUserQuestion to ask where the output skill and kanban board should live:

**Question:** "Where should this process's output live?"

| Option | Description |
|--------|-------------|
| **Global** (`~/.claude/skills/` + `~/.kanban/`) | Available in every project. Not version-controlled with any repo -- back up separately. Good for: personal workflows, presentations, learning processes. |
| **Project** (`.claude/skills/` + `.kanban/`) | Lives in the current repo. Version-controlled, travels with clones/branches, but only available in this project. Good for: project-specific pipelines, codebase review, team processes. |

Record the answer as `scope: global` or `scope: project` in card.md (step 4).

### 3. Gather Description

- **If arguments include a description:** Use it.
- **If recent conversation context suggests why:** Draft from context, confirm with user.
- **Otherwise:** Ask: "What is this process for? Why do we need it?"

Keep it brief -- 1-3 sentences.

### 4. Create Trello Card

Create a card in the Noticing list with the appropriate label:

```bash
# feeder
python3 .claude/skills/trello/scripts/trello_api.py create_card 6990dbbaff67775efd5cf00e --name "ProcessName" --desc "description" --labels "6990dbbae8112060ab42c14e"

# direct-output
python3 .claude/skills/trello/scripts/trello_api.py create_card 6990dbbaff67775efd5cf00e --name "ProcessName" --desc "description" --labels "6990dbbaff63cfef09c33f8f"

```

Mark as done immediately (noticing is instant recognition):

```bash
python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
```

### 5. Create Process Folder + card.md

Create: `~/.kanban/meta-kanban/01_noticed/process-name/card.md`

```yaml
---
card_id: <from step 4>
card_url: <from step 4>
process: <Human-readable name, e.g., "Android InspectPro Review">
label: <feeder|direct-output|continuous>
scope: <global|project>
done: true
---

<Brief description from step 2>
```

Noticing is immediately done -- it is an instant recognition, ready to pull to framing.

### 6. Report

Print summary:
```
Created: Android InspectPro Review [feeder] [project]
Stage: 01_noticed (done)
Local: ~/.kanban/meta-kanban/01_noticed/android-inspectpro-review/
Output scope: project (.claude/skills/ + .kanban/)
Trello: <card_url>
```

Then offer next steps:
1. `/commit` to save the work
2. `/retro` to reflect on the session
3. `/meta-kanban frame <process-name>` to advance to framing
