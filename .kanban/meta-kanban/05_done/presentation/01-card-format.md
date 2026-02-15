# Card Format

## Labels

| Label | Color | When to Use |
|-------|-------|-------------|
| inform | blue | Teaching, lecturing. Board-primary. Knowledge transfer. |
| expose | green | Job talks, conference talks. Slides-primary. Showcasing ideas/accomplishments. |
| persuade | orange | Oral exams, pitches. Slides-primary. Establishing context and proving capability. |

Every card gets exactly 1 label.

## Trello Card Content

```
**Topic:** What the presentation is about (1 sentence)

**Audience:** Who this is for

**Type note:** Why this type (inform/expose/persuade) was chosen
```

## Local Card File

**File name:** `card.md`

```yaml
---
card_id: <from Trello>
card_url: <from Trello>
title: <Human-readable name, e.g., "All-Hands Q1 Update">
label: <inform|expose|persuade>
done: false
---

**Topic:** What the presentation is about

**Audience:** Who this is for

**Type note:** Why this type was chosen
```

No sync utility -- Trello is a tracking mirror only.
