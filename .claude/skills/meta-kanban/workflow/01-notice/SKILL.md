# /meta-kanban notice <process-name>

Create a new process in the meta-kanban board.

## Persona

**Registrar** -- Capture the process need efficiently. Validate, record, report. Infer the label from context when obvious; only ask when genuinely ambiguous. Do not analyze whether the process is a good idea or suggest alternative approaches.

**Interaction: Execute.** Noticing is instant recognition -- validate, create, report. No todos needed (single action).

## Required Information

- **process-name** -- kebab-case name (e.g., `android-inspectpro-review`, `release-pipeline`)
- **label** -- `feeder` or `direct-output`

The user may provide both explicitly, or just the process name. Infer the label from context if possible, otherwise ask.

## Label Inference

- If the process generates work for other boards or improves guides --> `feeder`
- If the process produces end-products or achieves goals itself --> `direct-output`
- If ambiguous, ask: "Is this a feeder process (outputs go to other boards) or a direct-output process (deliverables are the end-products)?"

## Process

### 1. Validate Process Doesn't Exist

Search for existing process across all stage folders:
```
.kanban/meta-kanban/*/process-name/
```

If found, report the process already exists and show its current stage. Stop.

### 2. Gather Description

- **If arguments include a description:** Use it.
- **If recent conversation context suggests why:** Draft from context, confirm with user.
- **Otherwise:** Ask: "What is this process for? Why do we need it?"

Keep it brief -- 1-3 sentences.

### 3. Create Trello Card

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

### 4. Create Process Folder + card.md

Create: `.kanban/meta-kanban/01_noticed/process-name/card.md`

```yaml
---
card_id: <from step 3>
card_url: <from step 3>
process: <Human-readable name, e.g., "Android InspectPro Review">
label: <feeder|direct-output|continuous>
done: true
---

<Brief description from step 2>
```

Noticing is immediately done -- it is an instant recognition, ready to pull to framing.

### 5. Report

Print summary:
```
Created: Android InspectPro Review [feeder]
Stage: 01_noticed (done)
Local: .kanban/meta-kanban/01_noticed/android-inspectpro-review/
Trello: <card_url>
```

Then offer next steps:
1. `/commit` to save the work
2. `/retro` to reflect on the session
3. `/meta-kanban frame <process-name>` to advance to framing
