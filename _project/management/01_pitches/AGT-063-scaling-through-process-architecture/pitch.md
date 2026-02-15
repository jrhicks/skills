---
Num: 063
Title: Scaling Through Process Architecture
TLDR: Presentation on how to cut through AI agent hype with process-aligned skill design
Status: New
Updated At: 2026-02-14T20:15:00Z
---

# Scaling Through Process Architecture

**Format: Presentation / talk.** Not a feature to build -- a presentation to give.

## The Promise (What You'll Walk Away With)

1. **Empowerment** -- Understand what top leadership expects: more people empowered by AI, not more AI replacing people
2. **Principled** -- Learn how to use AI in a principled way (CMM, Goldratt -- define before you automate)
3. **Innovative** -- Use the same tools and techniques as the most innovative practitioners of AI
4. **Caring** -- Understand how applying these skills will have a positive impact on people's lives

## The Idea

This is NOT about scaling AI in the traditional sense (more agents, bigger context, faster inference). This is about scaling the *effective use* of AI in an organization to achieve product development.

The problem: it is incredibly easy to make an infinite mess of agents, skills, commands, and extensions. The hype and confusion around the new technology creates a sea of half-built tooling that nobody can navigate or maintain. Every team ends up with a graveyard of "AI experiments" that looked clever in a demo but don't compose into real work.

The thesis: things start to crystallize and become easy to grok and move forward when you align your Claude Code extensions (skills) with processes. Specifically:

- **1 skill = 1 process** -- a skill IS a business process, not a bag of tricks
- **1 sub-skill = 1 task** in that process (progressive disclosure -- you don't see all tasks at once, just the one you're on)
- **Multiple guides per sub-skill** depending on the type of thing moving through that process (pattern vs functionality, component vs provider, etc.)
- **Processes feed other processes** -- one process can both kick off new work items in another process AND improve the guides/sub-skills of another process

## The PhD Toxicologist Analogy

Claude 4.6 is like a PhD toxicologist -- deep expertise, can analyze complex problems, produces high-quality output. But how do you scale PhD-level expertise to 60,000 personnel on a Deepwater Horizon-scale operation? You don't clone 60,000 PhDs. You build process:

- **Processes** that break the work into systematic steps
- **Roles** that define who does what at each step
- **Handoffs** that move work products between processes
- **Guides** that encode expertise so the process can be followed consistently

The PhD's knowledge gets systematized INTO the process -- into the guides, the decision criteria, the quality gates. The process is how you scale the expert.

## The Concrete Example

The android-inspectpro-review skill, designed in a single conversation:

- **The process**: Noticing -> Researching -> Synthesizing -> Tracing
- **The sub-skills**: Researching branches by topic type (pattern topics get discussion + pattern-analysis, functionality topics get inventory + per-class research)
- **The guides**: Different deliverable templates for pattern vs functionality topics
- **Process-to-process flow**:
  - Tracing stage produces pitches -> management pipeline (another process)
  - Tracing stage produces MOB cards -> sdui-and-mob kanban (another process)
  - Discussion deliverables (modernize-discussion.md, sdui-discussion.md) -> improve guides in MOB's prototype sub-skills (feeding another process's guides)

```
android-inspectpro-review (process)
  Tracing stage outputs:
    |
    |--> management pipeline (process)
    |      pitch -> groom -> plan -> implement -> review -> complete
    |
    |--> sdui-and-mob kanban (process)
    |      notice -> frame -> specify -> prototype -> nativify -> distill
    |
    `--> MOB prototype guides (sub-process)
           react-implementation, android-poc, ios-poc
```

## The Three Levels of Systematization

1. **Systematizing the kick-off of new things** -- the review process discovers what needs to be built and generates pitches and MOB cards. You don't decide what to build next -- the process surfaces it.

2. **Systematizing the creation of guides** -- as topics are researched, the discussion deliverables produce insights that improve the guides other processes use. The system improves itself.

3. **Making a process for making processes** -- the meta-level. The android-inspectpro-review skill design session itself followed a repeatable pattern: identify what the cards are, define the stages, map deliverables per stage, connect outputs to other boards. That pattern itself could become a skill.

## Why It Matters

The answer to "how do you use AI effectively at scale?" is not "more agents." It's the same answer it has always been for expert work: process architecture. The AI is the PhD. The skill system is the process manual. The guides are the encoded expertise. The inter-process flows are the organizational nervous system.

BPM diagrams should make this concrete and visual -- showing how the abstract maps to industrial process management patterns that have worked for decades.

## BPM Diagram Ideas

- **The mess vs the system**: Before/after showing scattered agents/skills vs process-aligned skills
- **Single process anatomy**: Skill = process, sub-skills = tasks, guides = type-specific instructions
- **Process network**: 3-4 processes as swim lanes with arrows showing outputs becoming inputs
- **Guide branching**: How one sub-skill fans out into different guide paths based on the type of thing
- **The PhD scaling diagram**: 1 PhD -> process architecture -> 60,000 personnel

## The Three Types of Skills

### 1. Process Skills (kanban-based)

The core thesis. A skill IS a process. Sub-skills are tasks. Guides vary by type of thing. Examples: android-inspectpro-review, mob, management pipeline.

The person designing these skills is acting as a **process analyst** -- not a programmer, not a prompt engineer. They're asking: what are the stages? What are the deliverables? What types of things flow through? Where do outputs go?

### 2. Utility Skills (non-process, still valuable)

Not everything is a process. Some skills are interfaces to external systems that process skills depend on. For example, the Trello skill gives us a visual board of WIP. It doesn't own a process -- it serves them:

- Each work item becomes a card
- The type of card becomes a label
- Key deliverable summaries populate the body
- References link back to in-folder deliverables

Utility skills are the connective tissue. Process skills generate the work; utility skills make it visible, sync it, move it between systems.

### 3. The Meta-Skill: A Process for Creating Processes and Skills

The final level. A skill whose process is: design a new process, build the skill for it, connect it to the network of existing processes.

This meta-skill would:
- Help identify what the cards are (what flows through?)
- Define the stages (what progression do cards follow?)
- Map deliverables per stage (what gets produced?)
- Connect outputs to other boards (where do deliverables land?)
- Help feed work items into the new process from existing processes
- Help complete the guides by drawing on what other processes have learned

The android-inspectpro-review design session IS the prototype of this meta-skill. We designed a process in conversation by asking exactly these questions. Systematize that conversation and you have a process for making processes.

## The AI Empowerment Wildly Important Goal

The crowning framework. Four steps to go from zero to systematized AI-assisted product development:

1. **Claude Code Setup** -- Get the tool running. Baseline configuration. This is table stakes, not the hard part.

2. **Process Discovery, Analysis, Creation** -- The actual work. Identify your processes (what does your team do repeatedly?). Analyze them (what are the stages, what types of things flow through, what are the deliverables?). Create them as kanban boards with clear progression.

3. **Skill, Sub-Skill & Guide Creation** -- Encode the processes into Claude Code skills. 1 skill per process, 1 sub-skill per task, guides per type of thing. This is where the PhD's expertise gets systematized into something repeatable.

4. **Tracking** -- Make it visible. Utility skills (Trello, dashboards) that show WIP across all processes. Cards, labels, summaries, references back to deliverables. The organizational nervous system that lets you see the whole network of processes working together.

Most organizations get stuck at step 1 and call it "AI adoption." The real value is in steps 2-4.

Many processes already exist -- sales in Salesforce, support in Zendesk, customer success in Process Street, management OPPs in EOS. Step 2 isn't starting from scratch. It's recognizing what you already have and identifying the gaps -- especially in product development and engineering where processes are often ad-hoc despite being the core value engine.

## Worked Example: Point Solution Research

Another process to show the meta-skill in action. First question: "What are the units of work?" Are they products? Functionality categories? Assume products for now.

Steps (rough):
- Research (discover what's out there)
- ... middle steps TBD (evaluate? compare? shortlist?)
- Outcomes: Do these drive notices to the SDUI & MOB board? Do we end up creating a board for "App Building"?

This example shows how the meta-process helps with the AI Empowerment WIG -- you start with "I need to research point solutions" and the meta-skill walks you through: what are the cards, what are the stages, where do outputs go. Even if the middle steps are fuzzy, the framework gives you a structure to discover them.

## Process Maturity and the Economics of Automation

There's a known concept -- possibly "Capability Maturity Model" or "Process Maturity Scale" -- that when companies grow capabilities, they usually reach for automation first. But automation SHOULD be downstream of process definition. You automate a process, not a void.

### The Formula

There should be formulas that can look at:
- Your revenue (say $13M)
- Your current process maturity level
- And calculate what profit would be once you mature

But these formulas need updating to reflect the breadth of automation now possible at EVERY step of a process, not just the repetitive manual steps. AI changes the automation surface area dramatically.

### The Worst Case: Automation Without Throughput

This is the cautionary tale captured by the WIG framework:

**Automation without throughput actually erodes profit.** It creates Work In Progress and increases costs without driving revenue. You get:
- More agents running
- More half-finished work piling up
- More infrastructure costs
- Zero additional revenue
- The "infinite mess of agents" problem at the organizational level

**Automation WITH process management** is sane, organized, profitable -- and ultimately empowering. The process ensures throughput. Cards move through stages to completion. Outputs feed other processes. Work finishes.

The difference between the two is exactly what this presentation argues for: process first, automation second. The AI Empowerment WIG puts process discovery (step 2) before skill creation (step 3) for exactly this reason.

### Research Threads

**Capability Maturity Model (CMM/CMMI)** -- The SEI's 5-level maturity model (Initial, Managed, Defined, Quantitatively Managed, Optimizing) may be the framework being referenced. The key insight: most organizations try to jump from Level 1 (ad-hoc) to automation without passing through Level 3 (defined processes). CMM argues you can't effectively automate what you haven't defined. The AI Empowerment WIG mirrors this: step 2 (process definition) must precede step 3 (skill/automation creation).

**Goldratt's Theory of Constraints** -- The WIP/throughput argument maps directly to Goldratt. In "The Goal," the lesson is that local optimization (automating individual steps) without system-level throughput management actually makes things worse. WIP accumulates at bottlenecks, cycle time increases, costs go up, revenue stays flat. Goldratt's Five Focusing Steps (identify constraint, exploit, subordinate, elevate, repeat) could frame the process maturity journey. The constraint in AI adoption isn't the AI's capability -- it's the absence of defined processes for the AI to operate within.

Both frameworks support the same conclusion: the bottleneck isn't AI capability, it's process maturity. Automate a defined process and you get throughput. Automate chaos and you get expensive chaos.

## EPIC Thread

Company motto: **Empowerment, Principled, Innovative, Caring**

Weave the first three naturally into the language of the presentation -- not as forced branding but as words that genuinely describe what's happening:

- **Empowerment** -- this is literally the WIG name ("AI Empowerment"). Process architecture empowers developers to do expert-level work systematically. The PhD's knowledge empowers 60,000 personnel through process.
- **Principled** -- CMM and Goldratt ARE principled frameworks. Define before you automate. Throughput before local optimization. These aren't just best practices -- they're principles. Principled finances sustain the operation.
- **Innovative** -- the meta-skill (a process for making processes), the process-to-process network, encoding expertise into guides -- these are genuine innovations in how teams work with AI.

- **Caring** -- two dimensions. Internally: employees gain the skills to be equipped in the new AI economy. This isn't about replacing people -- it's about growing them into process analysts, skill designers, guide authors. Externally: the safety point solutions we build save lives. The throughput we're optimizing for ultimately protects people.

## Related Pitches

- **AGT-064: Meta-Kanban** (`_project/management/01_pitches/AGT-064-meta-kanban/pitch.md`) -- The concrete implementation of the "Meta-Skill" described in this presentation. A kanban board + skill for designing new kanban-based workflows. Uses android-inspectpro-review (feeder process) and sdui-and-mob (direct-output process) as reference examples of completed processes.

## Open Questions

- What format? (Slides, written essay, interactive demo?)
- Should we include a live demo of running a topic through the pipeline?
- How technical should the BPM diagrams be? (Formal BPMN 2.0 vs simplified flows?)
- Is there a real Deepwater Horizon process document we could reference?
- Audience: developers? engineering managers? both?

## Next Steps

- [ ] Build the android-inspectpro-review skill (provides the concrete example)
- [ ] Research BPM/BPMN notation for the diagrams
- [ ] Draft the PhD toxicologist analogy with specific Deepwater Horizon numbers
- [ ] Create the process-to-process flow diagram
- [ ] Decide on presentation format
