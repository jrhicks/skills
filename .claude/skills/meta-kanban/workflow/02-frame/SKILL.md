# /meta-kanban frame <process-name>

Frame a process by answering fundamental questions about its purpose, flow, and types.

## Persona

**Facilitator** -- Guide a conversation to surface what this process truly needs. Listen for underlying intent, reflect back what you hear, then record. When the user's answers are clear, capture them and move on -- don't re-ask for confirmation on things they've already said. Do not impose structure prematurely or answer the user's questions for them.

**Interaction: Facilitate.** Present the 7 framing questions as an outline, then work through each one. Some questions will spark rich discussion, others will be quick. Read the room.

**Lead, don't wait.** You have context the user doesn't hold in working memory. Use it. Lead with proposals and drafts for the user to react to -- not open questions that leave the user doing the intellectual work alone. Show size estimates, logical groupings, dependency-driven sequencing. When discussing deliverables stage by stage, re-anchor context every time you advance (show what's locked so far, which stage you're on, what belongs here).

## Process

### 1. Find and Validate Process

Search all stage folders for the process:
```
~/.kanban/meta-kanban/*/process-name/
```

Read `card.md` inside it.

- If process not found, suggest using `notice` first.
- If process is already in `02_framing/` with `done: true`, report framing is complete. Ask if they want to revisit.
- If process is in a later stage (`03_designing/`, `04_implementing/`, `05_done/`), report it has already passed framing.

## Mode Detection

**Start Mode** (move from previous stage):
- Process is in `01_noticed/` with `done: true`
- Action: Move to `02_framing/`, mark undone, begin work

**Resume Mode** (continue current stage):
- Process is already in `02_framing/` with `done` absent or false
- Action: Skip move, pick up where left off

**Error cases:**
- Process in `01_noticed/` without `done: true`: "Process is still being noticed. Mark it done first."
- Process in a later stage: "Process has already passed framing."

### 2. Start Framing

**Skip this step if resuming (process already in `02_framing/`).**

Three actions:

1. Move process folder from current stage to `02_framing/`:
   ```bash
   mv ~/.kanban/meta-kanban/01_noticed/process-name/ \
      ~/.kanban/meta-kanban/02_framing/process-name/
   ```

2. Set `done: false` in card.md

3. Trello: move card + mark undone:
   ```bash
   python3 .claude/skills/trello/scripts/trello_api.py move_card <card_id> 6990dbb967427e703c09558b
   python3 .claude/skills/trello/scripts/trello_api.py mark_undone <card_id>
   ```

### 3. Create Todos

On first entry, create todos for each framing question:
1. Purpose
2. Process Type
3. What Flows Through
4. Main Steps
5. Deliverables
6. Where Outputs Go
7. Done Flow
8. Write framing.md

On resume, check if todos exist. If not, create them and mark completed questions as done based on what's already in `framing.md`.

### 4. Work Through Framing

Read `framing-guide.md` in this folder. Use it to guide a discussion with the user about the process's fundamental nature. Produce `framing.md` in the process folder answering all the guide's questions.

If `framing.md` already exists (resume mode), check what questions remain unanswered and continue.

**Explore domain material proactively.** When the card.md description mentions existing skills, guides, or reference material, explore them with an Explore agent before starting the discussion -- don't wait for the user to point you at them. When the user references code or artifacts during discussion, explore immediately. Don't guess from partial knowledge -- explore the source. The user is pointing you at answers, not asking you to speculate.

### 5. Complete Framing

When `framing.md` is complete, two actions:

1. Set `done: true` in card.md

2. Trello: mark done:
   ```bash
   python3 .claude/skills/trello/scripts/trello_api.py mark_done <card_id>
   ```

Report what was produced, then offer next steps:
1. `/commit` to save the work
2. `/retro` to reflect on the session
3. `/meta-kanban design <process-name>` to advance to designing
