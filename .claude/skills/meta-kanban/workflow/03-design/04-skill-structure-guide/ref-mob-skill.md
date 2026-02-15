# Reference: mob (SDUI and MOB) Skill Structure

6-stage **direct-output process** -- deliverables (EARS specs, interfaces, implementations) are the end-products.

```
.claude/skills/mob/
├── SKILL.md                                    # Main dispatcher
│                                               #   Same structure as all kanban skills: frontmatter,
│                                               #   usage, board config, pipeline (6 stages), labels,
│                                               #   done flow, dispatch, location, card format,
│                                               #   deliverables, examples. NO persona section.
│
├── agents/
│   └── element-researcher.md                   # PROMOTED agent: cross-platform element research
│                                               #   Persona: Platform Researcher.
│                                               #   Reads source files across Android/iOS codebases
│                                               #   for a specific UI element. Maps: how it renders,
│                                               #   what config drives it, what state it manages,
│                                               #   how it validates. Returns structured comparison
│                                               #   table (Android vs iOS vs SDUI target).
│                                               #   Fidelity: preserve exact config JSON keys,
│                                               #   class names, layout XML references, and
│                                               #   Gson deserializer mappings.
│                                               #   Model: sonnet. Turns: 30.
│                                               #   Promoted because cross-platform research
│                                               #   requires detailed platform-specific instructions
│                                               #   and fidelity rules for config key preservation.
│
├── utilities/
│   ├── list/
│   │   └── SKILL.md                            # Board status scanner (standard)
│   └── sync/
│       └── SKILL.md                            # Trello sync utility (extra)
│                                               #   Syncs local card state with Trello.
│                                               #   Example of a non-standard utility.
│
└── workflow/
    ├── 01-notice/
    │   ├── SKILL.md                            # Element recognition
    │   │                                       #   Persona: Registrar (autonomous).
    │   │                                       #   Creates PascalCase folder + trello.md.
    │   └── collection-guides/                  # Per-collection notice guides
    │       ├── inspectpro-classic-android-implementation.md
    │       └── inspectpro-classic-ios-implementation.md
    │                                           #   Each collection guide describes how to
    │                                           #   recognize elements from that source.
    │                                           #   Dispatched by label/collection.
    │
    ├── 02-frame/
    │   ├── SKILL.md                            # Behavior research
    │   │                                       #   Persona: Investigator (collaborative).
    │   │                                       #   Produces framing.md deliverable.
    │   │                                       #
    │   │                                       #   AGENT: Spawns agents/element-researcher.md
    │   │                                       #   (promoted) to scan Android + iOS source for
    │   │                                       #   the element. Returns platform comparison
    │   │                                       #   table. Main context uses the result to
    │   │                                       #   facilitate framing discussion with user
    │   │                                       #   without loading 20+ source files.
    │   │
    │   ├── collection-guides/                  # Per-collection framing guides
    │   │   ├── inspectpro-classic-android-implementation.md
    │   │   └── inspectpro-classic-ios-implementation.md
    │   └── framework-guides/                   # Per-framework framing guides
    │       ├── build-capabilities.md           #   How to frame build-capability elements
    │       └── primitive-capabilities.md       #   How to frame primitive-capability elements
    │                                           #   Two guide subdirectory types:
    │                                           #   collection-guides = source-specific
    │                                           #   framework-guides = element-type-specific
    │
    ├── 03-specify/
    │   ├── SKILL.md                            # EARS writing
    │   │                                       #   Persona: Specifier (collaborative).
    │   │                                       #   Produces EARS requirements file.
    │   │                                       #
    │   │                                       #   AGENT: Spawns INLINE haiku agent to read
    │   │                                       #   framing.md + relevant meta-requirements
    │   │                                       #   and draft initial EARS requirements.
    │   │                                       #   Persona: "EARS Drafter -- produce
    │   │                                       #   requirements following the meta-requirement
    │   │                                       #   concern structure. Preserve exact config
    │   │                                       #   JSON keys from framing." Main context
    │   │                                       #   reviews and refines collaboratively with
    │   │                                       #   user rather than writing from scratch.
    │   │
    │   ├── collection-guides/                  # Same pattern as 02-frame
    │   │   ├── inspectpro-classic-android-implementation.md
    │   │   └── inspectpro-classic-ios-implementation.md
    │   ├── framework-guides/
    │   │   ├── build-capabilities.md
    │   │   └── primitive-capabilities.md
    │   └── primitive-meta-requirements/        # EARS meta-requirements per primitive
    │       ├── component_implementation.ears.md
    │       ├── screen_implementation.ears.md
    │       ├── operation_implementation.ears.md
    │       └── provider_implementation.ears.md
    │                                           #   Meta-requirements define the standard
    │                                           #   concern sections that every element of
    │                                           #   that primitive type must address.
    │
    ├── 04-prototype/
    │   ├── SKILL.md                            # Build interface + component
    │   │                                       #   Persona: Builder (autonomous).
    │   │                                       #   Deep guide hierarchy for implementation.
    │   │                                       #
    │   │                                       #   AGENTS: Spawns parallel INLINE agents
    │   │                                       #   for platform scaffolding. After building
    │   │                                       #   the React interface + component, spawns
    │   │                                       #   up to 2 agents in parallel:
    │   │                                       #   - "Android POC Scaffolder -- read the
    │   │                                       #     interface and EARS, scaffold the Android
    │   │                                       #     POC structure." (haiku, 15 turns)
    │   │                                       #   - "iOS POC Scaffolder -- read the interface
    │   │                                       #     and EARS, scaffold the iOS POC structure."
    │   │                                       #     (haiku, 15 turns)
    │   │                                       #   Parallelism -- platforms are independent.
    │   │                                       #   Main context reviews scaffolds sequentially.
    │   │
    │   ├── implementation/                     # Step-by-step implementation guides
    │   │   ├── 01-create-interface/            #   Per-primitive interface creation
    │   │   │   ├── component.md
    │   │   │   ├── screen.md
    │   │   │   ├── operation.md
    │   │   │   ├── worksheet.md
    │   │   │   └── provider.md
    │   │   ├── 02-react-implementation/        #   Per-primitive React implementation
    │   │   │   ├── component.md
    │   │   │   ├── screen.md
    │   │   │   ├── operation.md
    │   │   │   ├── worksheet.md
    │   │   │   └── provider.md
    │   │   ├── 03-studio-confirmation/         #   Studio rendering verification
    │   │   │   └── guide.md
    │   │   ├── 04-android-poc/                 #   Per-primitive Android proof-of-concept
    │   │   │   ├── component.md
    │   │   │   ├── screen.md
    │   │   │   ├── operation.md
    │   │   │   ├── worksheet.md
    │   │   │   └── provider.md
    │   │   ├── 05-ios-poc/                     #   Per-primitive iOS proof-of-concept
    │   │   │   ├── component.md
    │   │   │   ├── screen.md
    │   │   │   ├── operation.md
    │   │   │   ├── worksheet.md
    │   │   │   └── provider.md
    │   │   └── audits/                         #   Per-primitive audit checklists
    │   │       ├── component.md
    │   │       ├── screen.md
    │   │       ├── operation.md
    │   │       ├── worksheet.md
    │   │       └── provider.md
    │   ├── build-capability/                   # Guides for build-capability elements
    │   │   ├── 00-overview.md
    │   │   ├── 01-react-and-studio.md
    │   │   ├── 02-android-poc.md
    │   │   └── 03-ios-poc.md
    │   └── primitive-capability/               # Guides for primitive-capability elements
    │       ├── 00-overview.md
    │       ├── 01-interface-type.md
    │       ├── 02-studio-implementation.md
    │       ├── 03-react-runtime.md
    │       ├── 04-android-runtime-poc.md
    │       └── 05-ios-runtime-poc.md
    │
    ├── 05-nativify/
    │   └── SKILL.md                            # Native platform implementations
    │                                           #   Persona: Builder (autonomous).
    │                                           #   Placeholder for future stages.
    │
    └── 06-distill/
        └── SKILL.md                            # Final review
                                                #   Persona: Reviewer (collaborative).
                                                #   Placeholder for future stages.
```

## Key Patterns

**Collection-guides + framework-guides (01-03):** Two kinds of guide subdirectories coexist. Collection-guides are source-specific (how to extract from Android vs iOS). Framework-guides are element-type-specific (build-capability vs primitive-capability). The SKILL.md dispatches to the right guide based on the card's label/collection.

**Deep prototype hierarchy (04-prototype):** The prototype stage has the deepest nesting because it orchestrates a multi-step build process across platforms. Each step has per-primitive variants (component, screen, operation, worksheet, provider). Three parallel guide tracks: `implementation/` (standard elements), `build-capability/` (framework features), `primitive-capability/` (new primitive types).

**Primitive meta-requirements (03-specify):** EARS files that define the standard concern sections every element of a primitive type must address. These are reference material for the specify stage, not deliverables.

**Extra utility (sync):** Beyond the standard `list/` utility, mob has a `sync/` utility for Trello synchronization. Utilities are added as needed per process.

**Placeholder stages (05-06):** Later pipeline stages have minimal SKILL.md files. Structure is established early; guides are added as the process matures.

**Promoted agent (agents/element-researcher.md):** The frame stage reads 20+ source files across two platforms per element -- too much for the main context. A promoted agent definition handles the cross-platform research and returns a structured comparison table. Promoted because platform-specific fidelity rules (config JSON keys, Gson deserializer mappings) need detailed instructions. The main context uses the result to facilitate framing discussion.

**Inline agents (03-specify, 04-prototype):** Two different agent use cases. Specify uses an inline haiku agent to *draft* from existing material (framing + meta-requirements), so the collaborative session refines rather than writes from scratch. Prototype uses parallel inline agents for *independent platform work* (Android POC and iOS POC can scaffold simultaneously). Different motivations -- drafting vs. parallelism -- same lightweight inline pattern.

**Agent spectrum in one process:** Promoted for the complex cross-platform research (detailed fidelity rules, 30 turns), inline for focused draft-and-scaffold tasks (short personas, haiku model). Matches the promotion heuristic: >20 lines of instructions = promote to file.
