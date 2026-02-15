# Trello Card Format Convention

Standard format for Trello cards synced from project management tickets.

## Structure

```
**Notice:** <internal context -- why we care, authentic voice, describe the pain>

**Stories:**

- As a <role>, I want <goal> so that <benefit>.
- As a <role>, I want <goal> so that <benefit>.

**Acceptance Criteria:**

- <testable condition, <200 chars>
- <testable condition, <200 chars>
...

---

**Requirements**

1. <requirement summary, <100 chars>
2. <requirement summary, <100 chars>
...

---

**References:** [filename](https://github.com/Record360/record-paas/blob/main/path/to/file.ears.md)
```

## Rules

- **Notice** -- internal context, authentic voice. Describe the actual pain -- don't sanitize it. This is for us.
- **Stories** -- one per stakeholder perspective. Standard format: "As a [role], I want [goal] so that [benefit]." Multiple stories capture different angles (mobile dev, backend dev, VP, etc.).
- **Acceptance Criteria** -- bullet list of testable conditions. Each under 200 chars. These define "done."
- **Requirements** -- ordered list, each under 100 chars. Summarize the EARS intent. In `trello.md` include full EARS IDs (e.g., `SRV-STOR-001:`) for cross-referencing; `sync_ears.py` strips them when pushing to Trello.
- **References** -- GitHub permalink to the EARS source file(s). Multiple files get multiple links.
- **Separator** -- use `---` before Requirements and before References.

## Multiple EARS Files

When a ticket spans multiple EARS files, list all in References:

```
**References:**
- [upload-storage.ears.md](https://github.com/Record360/record-paas/blob/main/_project/requirements/ears/server/upload-storage.ears.md)
- [UploadProvider.ears.md](https://github.com/Record360/record-paas/blob/main/.claude/skills/mob/meta-requirements/provider_implementation.ears.md)
```

Requirements from different files are merged into a single numbered list. Group by file if helpful, but keep the list flat.

## trello.md (Local Cache)

Each ticket folder in `_project/management/` can have a `trello.md` that caches the card content locally. This is the preferred source for syncing -- edit `trello.md`, then push with `sync_ears.py`.

**Frontmatter:**
```yaml
---
card_id: 698d260f3659b4006b47461d
card_url: https://trello.com/c/ACRdV8cj
list: Noticing
synced_at: 2026-02-11
---
```

**Body:** Same format as the Trello card (Notice/Story/Acceptance Criteria/Requirements/References).

**EARS IDs:** `trello.md` keeps full IDs (e.g., `SRV-STOR-001:`) so you can `grep -r SRV-STOR-005` to find which tickets reference a requirement. `sync_ears.py` strips them for the Trello card display.

**Workflow:**
1. Create card on Trello, note the card_id
2. Create `trello.md` in the ticket folder with frontmatter + curated content
3. Push with `python3 .claude/skills/trello/scripts/sync_ears.py <path>/trello.md`
4. Script updates `synced_at` on push
5. Edit `trello.md` locally, re-push when ready
