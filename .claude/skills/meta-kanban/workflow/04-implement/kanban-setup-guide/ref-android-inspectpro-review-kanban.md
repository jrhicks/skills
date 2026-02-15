# Reference: android-inspectpro-review Kanban Structure

4-stage **feeder process** with simple flat structure. Topics are kebab-case folders that move between stages.

```
.kanban/android-inspectpro-review/
├── discussion.md                       # Cross-topic discussion log
│                                       #   Aha moments spanning multiple topics.
│                                       #   Append-only -- never rewrite old entries.
│
├── 01_noticed/                         # Stage 1: Recognize topic
│   └── .gitkeep                        #   Empty stage folders tracked via .gitkeep.
│                                       #   When a topic is noticed, a folder is created
│                                       #   here with card.md inside it.
│
├── 02_analyzing/                       # Stage 2: Study source code
│   └── .gitkeep                        #   Topics move here when analysis begins.
│                                       #   Deliverables accumulate inside the topic folder.
│
├── 03_synthesizing/                    # Stage 3: Extract value through discussions
│   └── .gitkeep                        #   4 discussion lenses produce 4 deliverables.
│
├── 04_applying/                        # Stage 4: Apply findings to other processes
│   └── .gitkeep                        #   Outputs leave the board (MOB cards, guide updates).
│
└── 05_done/                            # Terminal: Fully reviewed
    └── .gitkeep                        #   Completed topics land here.
```

## Key Patterns

**Simple flat structure:** Each stage folder contains item folders directly -- no nested subdirectories within stages. This works well for processes with relatively few items (tens, not hundreds).

**discussion.md at root:** Cross-topic discussion lives at the board root, not inside any stage folder. It persists across the entire board lifecycle.

**.gitkeep convention:** Empty stage folders include `.gitkeep` so git tracks them. When items move between stages, the source folder returns to having just `.gitkeep`.

**Stage naming:** Gerund form for active stages (`analyzing`, `synthesizing`, `applying`), past participle for observation stages (`noticed`), descriptive for terminal (`done`). Number prefix (`01_`, `02_`, ...) ensures filesystem ordering matches pipeline order.

**Item folder naming:** kebab-case (e.g., `dependency-injection`, `checklist-rendering`). Each item folder contains `card.md` plus stage-specific deliverable files.

**5 folders for 4 active stages:** The done folder (`05_done/`) is the 5th folder -- terminal stage that receives completed items.
