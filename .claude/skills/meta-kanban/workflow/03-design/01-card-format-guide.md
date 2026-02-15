# Card Format Guide

Design what humans see on Trello and what machines track locally. The creative decisions here are about labels (types) and Trello-visible content (what's worth showing at a glance). The mechanical stuff (frontmatter fields, done flag) follows a standard template.

This is the first design step -- you need to understand what types of things flow through the process before designing stages for them. Types inform everything downstream: label-branched deliverables, type-specific guides, stage granularity.

## Persona

**Information Designer** -- Help the user brainstorm what types of things flow through their process and what's worth showing on a Trello card. Present options and have fun with it -- label colors matter for visual scanning. Do not over-engineer the metadata or add fields without a clear consumer.

## Creative Decisions

### Labels (Types)

What are the different types of things that flow through this pipeline? Labels create instant visual categories on the Trello board.

For each label:
- **Name** -- short, descriptive (e.g., `pattern`, `functionality`, `implementation`, `platform`)
- **Color** -- pick from Trello's palette. Choose colors that contrast well when scanning the board. No two labels should share a color.
- **Description** -- one sentence explaining when this label applies

Trello color palette: `blue`, `green`, `yellow`, `orange`, `red`, `purple`, `sky`, `lime`, `pink`, `black`

*Examples from existing boards:*

android-inspectpro-review (2 labels):
| Label | Color | When to Use |
|-------|-------|-------------|
| pattern | blue | Cross-cutting architectural idioms (DI, threading, lifecycle) |
| functionality | green | User-facing capabilities (checklist, photo, sync) |

sdui-and-mob (2+ labels):
| Label | Color | When to Use |
|-------|-------|-------------|
| implementation | green | Standard SDUI element implementation |
| platform | blue | Platform-level capability or infrastructure |

### Trello Card Content

This is the curation decision: what do humans need to see at a glance on the Trello card? Not everything in the local files belongs on the card. Pick the signal, not the noise.

Good candidates for Trello-visible content:
- **User stories** -- who wants this and why
- **Acceptance criteria** -- how we know it's done
- **Requirements summary** -- curated highlights, not the full EARS list
- **References** -- links to files on GitHub so people can dig deeper

*Examples:*

android-inspectpro-review (simple): Just a brief description of the topic.

sdui-and-mob (structured):
```
**Notice:** In InspectPro, configurators have Textboxes for free-text input.

**Stories:**
- As an owner of InspectPro configurations, I want Textbox in SDUI...

**Acceptance Criteria:**
- Looks and behaves like original InspectPro Classic Android Textbox
- Configuration migration requires minimal change

**Requirements**
1. Material outlined text input with floating hint
2. Multiline mode when lines > 1
[...summary, not all 27]

**References:** [Textbox.android.ears.md](https://github.com/...)
```

### Card File Name

What is the local metadata file called?

- `card.md` -- simpler boards where Trello is just a tracking mirror
- `trello.md` -- boards that actively sync structured content with Trello cards

## Standard Template (Mechanical)

These fields are standard across all boards. Don't redesign them -- just fill in the board-specific values.

```yaml
---
card_id: <from Trello>
card_url: <from Trello>
<name_field>: <human-readable name>    # pick: title, topic, process, element
<label_field>: <label>                 # pick: label, domain, type
done: false
---

<body content matching the Trello card content design above>
```

Optional standard fields:
- `list: <current stage>` -- if the board syncs list position
- `synced_at: <date>` -- if the board uses timed sync

## Deliverable

Produce `01-card-format.md` in the process folder. Include:
1. Label table (name, color, description for each)
2. Trello card body template (what sections appear on the card)
3. Local card file template (frontmatter + body)
4. Card file name choice (`card.md` or `trello.md`)
