---
name: pptx
description: "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill."
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX Skill

## Quick Reference

| Task | Guide |
|------|-------|
| Read/analyze content | `python -m markitdown presentation.pptx` |
| Edit or create from template | Read [editing.md](editing.md) |
| Create from scratch | Read [pptxgenjs.md](pptxgenjs.md) |

---

## Reading Content

```bash
# Text extraction
python -m markitdown presentation.pptx

# Visual overview
python scripts/thumbnail.py presentation.pptx

# Raw XML
python scripts/office/unpack.py presentation.pptx unpacked/
```

---

## Editing Workflow

**Read [editing.md](editing.md) for full details.**

1. Analyze template with `thumbnail.py`
2. Unpack → manipulate slides → edit content → clean → pack

---

## Creating from Scratch

**Read [pptxgenjs.md](pptxgenjs.md) for full details.**

Use when no template or reference presentation is available.

---

## Record360 Style Guide (Default)

Unless the user specifies otherwise, use this style for all presentations.

### Slide Types & Backgrounds

Three slide types with distinct backgrounds:

| Type | Background | Use For |
|------|-----------|---------|
| **Title/Section** | `backgrounds/r360-dark.png` (dark navy with organic waves) | Title slide, section dividers, closing slide |
| **Interlude** | `backgrounds/r360-light.png` (light blue-gray with organic waves) | Transition slides, quote slides, visual breaks |
| **Content** | Solid white `{ color: "FFFFFF" }` | All content slides (the bulk of the deck) |

**Loading backgrounds in code:**
```javascript
const fs = require("fs");
const SKILL_DIR = ".claude/skills/pptx";
const darkBg = "image/png;base64," + fs.readFileSync(`${SKILL_DIR}/backgrounds/r360-dark.png`).toString("base64");
const lightBg = "image/png;base64," + fs.readFileSync(`${SKILL_DIR}/backgrounds/r360-light.png`).toString("base64");

// Title slide
slide.background = { data: darkBg };
// Interlude slide
slide.background = { data: lightBg };
// Content slide
slide.background = { color: "FFFFFF" };
```

### Color Palette

| Role | Hex | Name | Usage |
|------|-----|------|-------|
| Primary | `1E2A5E` | Record360 Navy | Headers on white bg, cards, accents |
| Accent | `E04040` | Record360 Red | Subtitles, highlights, key numbers |
| Text | `1E293B` | Dark Slate | Body text on white backgrounds |
| Muted | `4A5568` | Gray | Secondary text, captions, bullets |
| Light Text | `CADCFC` | Ice Blue | Text on dark backgrounds |
| White | `FFFFFF` | White | Primary text on dark backgrounds |

### Typography

Fonts chosen for Google Slides compatibility (no font substitution issues).

| Element | Font | Size | Color |
|---------|------|------|-------|
| Slide title (dark bg) | Arial Black | 44-54pt bold | `FFFFFF` |
| Slide title (white bg) | Arial Black | 36-44pt bold | `1E2A5E` |
| Subtitle / date | Arial | 20-22pt bold | `E04040` |
| Section header | Arial Black | 20-24pt bold | `1E2A5E` |
| Body text | Arial | 14-16pt | `1E293B` |
| Bullet text | Arial | 14-16pt | `4A5568` |
| Captions | Arial | 10-12pt | `4A5568` |
| Big stat number | Arial Black | 60-72pt bold | `E04040` or `CADCFC` (on dark) |
| Stat label | Arial | 14-16pt | `4A5568` or `FFFFFF` (on dark) |

### Content Slide Design

Content slides use a **clean white background**. Add visual interest through:

- **Navy accent cards** (`1E2A5E` fill) for stat callouts or key points
- **White cards with shadow** on interlude slides for contrast
- **Left-aligned text** for all body content; center only titles
- **Charts and tables** with the Record360 color palette

**Layout options:**
- Two-column (text left, visual right)
- Icon + text rows
- 2x2 or 2x3 grid of cards
- Large stat callout with description

**Data display:**
- Big stat numbers (60-72pt) with small labels below
- Comparison columns (before/after, side-by-side)
- Timeline or process flow

### Spacing

- 0.5" minimum margins from slide edges
- 0.3-0.5" between content blocks
- Leave breathing room -- don't fill every inch

### Avoid

- **Don't repeat the same layout** -- vary columns, cards, and callouts across slides
- **Don't center body text** -- left-align paragraphs and lists; center only titles
- **Don't use accent lines under titles** -- use whitespace instead
- **Don't use low-contrast elements** -- test readability against the background
- **Don't forget text box padding** -- set `margin: 0` when aligning with shapes
- **Don't mix spacing randomly** -- pick 0.3" or 0.5" gaps and use consistently

---

## QA (Required)

**Assume there are problems. Your job is to find them.**

Your first render is almost never correct. Approach QA as a bug hunt, not a confirmation step. If you found zero issues on first inspection, you weren't looking hard enough.

### Content QA

```bash
python -m markitdown output.pptx
```

Check for missing content, typos, wrong order.

**When using templates, check for leftover placeholder text:**

```bash
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|this.*(page|slide).*layout"
```

If grep returns results, fix them before declaring success.

### Visual QA

**⚠️ USE SUBAGENTS** — even for 2-3 slides. You've been staring at the code and will see what you expect, not what's there. Subagents have fresh eyes.

Convert slides to images (see [Converting to Images](#converting-to-images)), then use this prompt:

```
Visually inspect these slides. Assume there are issues — find them.

Look for:
- Overlapping elements (text through shapes, lines through words, stacked elements)
- Text overflow or cut off at edges/box boundaries
- Decorative lines positioned for single-line text but title wrapped to two lines
- Source citations or footers colliding with content above
- Elements too close (< 0.3" gaps) or cards/sections nearly touching
- Uneven gaps (large empty area in one place, cramped in another)
- Insufficient margin from slide edges (< 0.5")
- Columns or similar elements not aligned consistently
- Low-contrast text (e.g., light gray text on cream-colored background)
- Low-contrast icons (e.g., dark icons on dark backgrounds without a contrasting circle)
- Text boxes too narrow causing excessive wrapping
- Leftover placeholder content

For each slide, list issues or areas of concern, even if minor.

Read and analyze these images:
1. /path/to/slide-01.jpg (Expected: [brief description])
2. /path/to/slide-02.jpg (Expected: [brief description])

Report ALL issues found, including minor ones.
```

### Verification Loop

1. Generate slides → Convert to images → Inspect
2. **List issues found** (if none found, look again more critically)
3. Fix issues
4. **Re-verify affected slides** — one fix often creates another problem
5. Repeat until a full pass reveals no new issues

**Do not declare success until you've completed at least one fix-and-verify cycle.**

---

## Converting to Images

Convert presentations to individual slide images for visual inspection:

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

This creates `slide-01.jpg`, `slide-02.jpg`, etc.

To re-render specific slides after fixes:

```bash
pdftoppm -jpeg -r 150 -f N -l N output.pdf slide-fixed
```

---

## Dependencies

- `pip install "markitdown[pptx]"` - text extraction
- `pip install Pillow` - thumbnail grids
- `npm install -g pptxgenjs` - creating from scratch
- LibreOffice (`soffice`) - PDF conversion (auto-configured for sandboxed environments via `scripts/office/soffice.py`)
- Poppler (`pdftoppm`) - PDF to images

### Node.js Runtime

This project uses asdf for Node.js. Always set both PATH and NODE_PATH when running pptxgenjs:

```bash
PATH="/Users/jeffreyhicks/.asdf/installs/nodejs/22.12.0/bin:$PATH" \
NODE_PATH="/Users/jeffreyhicks/.asdf/installs/nodejs/22.12.0/lib/node_modules" \
node generate-slides.js
```

### Preview

Open generated .pptx in Keynote (free, pre-installed on Mac):
```bash
open -a Keynote output.pptx
```

Quick Look preview (no app needed): select file in Finder, press Space.
