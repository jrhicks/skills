# Reference: android-inspectpro-review Skill Structure

4-stage **feeder process** -- outputs leave the board as MOB cards and skill guide updates.

```
.claude/skills/android-inspectpro-review/
├── SKILL.md                                    # Main dispatcher
│                                               #   Frontmatter, usage, board config, pipeline,
│                                               #   labels, done flow, dispatch, location, card
│                                               #   format, deliverables, cross-references, examples.
│                                               #   NO persona section (dispatcher only routes).
│
├── agents/
│   └── source-analyzer.md                      # PROMOTED agent: deep Android source analysis
│                                               #   Persona: Android Archaeologist.
│                                               #   Reads Kotlin/Java source files for a topic,
│                                               #   traces data flows, maps class hierarchies,
│                                               #   identifies patterns. Returns structured
│                                               #   inventory (class table + key findings).
│                                               #   Fidelity: preserve exact class/method names,
│                                               #   package paths, and XML layout references.
│                                               #   Model: sonnet. Turns: 25.
│                                               #   Promoted because domain-specific multi-step
│                                               #   procedure with Android pattern recognition.
│
├── utilities/
│   └── list/
│       └── SKILL.md                            # Board status scanner
│                                               #   Globs all stage folders, counts items, shows
│                                               #   done/undone status per item.
│
└── workflow/
    ├── 01-notice/
    │   └── SKILL.md                            # Instant recognition
    │                                           #   Persona: Registrar (autonomous).
    │                                           #   Creates folder + card.md with label.
    │                                           #   Infers label from context; asks only when
    │                                           #   genuinely ambiguous. No guides needed.
    │
    ├── 02-analyze/
    │   ├── SKILL.md                            # Label-branched analysis
    │   │                                       #   Persona: Investigator (autonomous).
    │   │                                       #   Mode detection: start vs resume.
    │   │                                       #   Reads card label, dispatches to the matching
    │   │                                       #   guide file. Produces inventory + deep dives.
    │   │                                       #
    │   │                                       #   AGENT: Spawns agents/source-analyzer.md
    │   │                                       #   (promoted) to scan source files and produce
    │   │                                       #   the structured inventory. Main context gets
    │   │                                       #   the inventory result without reading 15+ files.
    │   │
    │   ├── pattern-guide.md                    # Guide for "pattern" label topics
    │   │                                       #   How to analyze cross-cutting architectural
    │   │                                       #   patterns (DI, threading, lifecycle).
    │   └── functionality-guide.md              # Guide for "functionality" label topics
    │                                           #   How to analyze feature-specific code paths
    │                                           #   (UI, data flow, validation).
    │
    ├── 03-synthesize/
    │   ├── SKILL.md                            # Multiple guided discussions
    │   │                                       #   Persona: Synthesizer (collaborative).
    │   │                                       #   Runs 4 discussion lenses in sequence.
    │   │                                       #   Each lens has its own guide file.
    │   │                                       #   Produces one deliverable per lens.
    │   │                                       #
    │   │                                       #   AGENTS: Before each lens discussion, spawns
    │   │                                       #   an INLINE haiku agent to pre-read the
    │   │                                       #   inventory + analysis and extract key points
    │   │                                       #   relevant to that lens. Persona: "<Lens>
    │   │                                       #   Extractor -- pull only what's relevant to
    │   │                                       #   <lens>, ignore everything else." Keeps the
    │   │                                       #   collaborative discussion focused without
    │   │                                       #   loading all raw analysis into context.
    │   │
    │   ├── modernize-guide.md                  # Lens: modernization opportunities
    │   ├── sdui-guide.md                       # Lens: SDUI applicability
    │   ├── react-guides-guide.md               # Lens: React/RN implementation notes
    │   └── android-guides-guide.md             # Lens: Android-specific takeaways
    │
    └── 04-apply/
        ├── SKILL.md                            # Double-move stage (apply then done)
        │                                       #   Persona: Librarian (autonomous).
        │                                       #   Distills artifacts, applies to other processes.
        │                                       #   After applying: moves item to done/ folder
        │                                       #   (second move within same stage handler).
        │                                       #
        │                                       #   AGENTS: Spawns parallel INLINE haiku agents
        │                                       #   to draft MOB card content and skill guide
        │                                       #   updates simultaneously. Persona per agent:
        │                                       #   "Card Drafter -- draft a MOB trello.md from
        │                                       #   these findings. Preserve requirement IDs."
        │                                       #   Main context reviews drafts, not raw findings.
        │
        ├── notice-guide.md                     # Guide for creating MOB cards from findings
        └── skill-updates-guide.md              # Guide for updating skill guide files
```

## Key Patterns

**Label branching (02-analyze):** The SKILL.md reads the card's label and dispatches to a different guide file. This avoids a monolithic guide that tries to cover all topic types.

**Multiple lenses (03-synthesize):** Four separate guide files, each applying a different analytical lens to the same analyzed material. The SKILL.md orchestrates the sequence and tracks which lenses are complete.

**Double-move (04-apply):** The final active stage both produces deliverables AND moves items to done. The SKILL.md handles both the apply work and the terminal move in one handler, avoiding a separate "done" stage sub-skill.

**Feeder cross-references:** The main SKILL.md has a cross-references section documenting where outputs go (MOB kanban cards, skill guide updates in other skills).

**Promoted agent (agents/source-analyzer.md):** The analyze stage reads 15+ Android source files per topic -- too much for the main context. A promoted agent definition handles the deep research and returns a structured inventory. Promoted because the Android-specific pattern recognition needs detailed multi-step instructions (>20 lines).

**Inline agents (03-synthesize, 04-apply):** Lightweight agents that pre-extract or draft. Short personas (one-liner), focused prompts, haiku model for volume. No definition file needed -- the Task call is self-contained in the SKILL.md.

**Agent spectrum in one process:** This process uses both patterns: promoted for the complex domain-specific analysis, inline for the focused extract-and-draft tasks. The promotion heuristic is the same as for guides.
