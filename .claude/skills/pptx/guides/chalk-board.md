# Chalkboard Sequences

Progressive reveal slides that simulate drawing on a board. Used in Zoom/virtual presentations where you can't walk to a physical board.

> For why boards matter (empathetic mirroring, pacing, engagement), see the **presentation** skill's how-to-speak reference.

---

## Concept

Winston's board technique works because the audience watches you build an idea piece by piece. In a slide-only world, simulate this with **2 back-to-back slides** that progressively reveal a drawing. The audience sees it "appear" as you advance.

**Key rules:**
- **2 slides per drawing** (not 3 -- more feels like animation, not drawing)
- **Green chalkboard** background, chalk-style illustrations, minimal text
- **Complete mode switch** -- don't mix chalkboard slides with polished slides. It should feel like you closed the slide deck and walked to a board
- Chalkboard slides are **separate from content slides** -- they punctuate the talk

---

## Workflow with Nano Banana

### Step 1: Generate the complete drawing

Start with the final state -- everything visible. This is your last slide in the sequence.

```bash
python scripts/generate_image.py generate \
  "Green chalkboard background with chalk-style drawing of [FULL CONCEPT]. \
   White and pale yellow chalk on dark green board. Hand-drawn feel, \
   minimal text, educational sketch style. No photorealism." \
  generated-images/chalk-[name]-full.png --aspect 16:9
```

### Step 2: Generate the partial drawing

Generate the first stage separately -- just the foundation element. Don't use `transform` to erase from the full image (Gemini tends to over-erase small elements).

```bash
python scripts/generate_image.py generate \
  "Green chalkboard background with chalk-style drawing of [PARTIAL CONCEPT ONLY]. \
   White and pale yellow chalk on dark green board. Hand-drawn feel, \
   minimal text, educational sketch style. No photorealism. \
   Same style and positioning as if this were the start of a larger drawing." \
  generated-images/chalk-[name]-1.png --aspect 16:9
```

### Step 3: Use as full-bleed slide backgrounds

In PptxGenJS, add each image as a full-bleed background:

```javascript
slide.addImage({
  path: 'generated-images/chalk-[name]-1.png',
  x: 0, y: 0, w: '100%', h: '100%'
});
```

---

## When to Use Transform vs Generate

| Approach | When | Why |
|----------|------|-----|
| **Generate each stage separately** | Elements are small or text-based | Gemini over-erases when removing small details from a complex image |
| **Transform to remove pieces** | Large, distinct regions | Works when the "remove this" instruction targets a clearly bounded area |

**Default to generating each stage separately.** It produces more consistent results.

---

## Example: Formula Sequence (K + P + t)

Winston's communication formula: Knowledge + Practice + talent (talent smallest).

**Slide 1** -- just "K" on the board:
```bash
python scripts/generate_image.py generate \
  "Green chalkboard with a single large letter K written in white chalk. \
   Hand-drawn chalk style. Centered. Nothing else on the board." \
  generated-images/hts/chalk-formula-1.png --aspect 16:9
```

**Slide 2** -- full formula "K + P + t" (t visibly smaller):
```bash
python scripts/generate_image.py generate \
  "Green chalkboard with chalk equation: K + P + t where K and P are large \
   and t is noticeably smaller. White chalk, hand-drawn. Educational style." \
  generated-images/hts/chalk-formula-full.png --aspect 16:9
```

---

## Example: Arch Sequence (Near Miss)

Winston's PhD work on arch learning -- the concept of a "near miss."

**Slide 1** -- just the arch:
```bash
python scripts/generate_image.py generate \
  "Green chalkboard with chalk drawing of a simple arch: two vertical blocks \
   supporting a horizontal block on top. White chalk, hand-drawn, centered." \
  generated-images/hts/chalk-arch-1.png --aspect 16:9
```

**Slide 2** -- arch + near miss with annotation:
```bash
python scripts/generate_image.py generate \
  "Green chalkboard with two chalk drawings side by side. Left: a proper arch \
   (two pillars with block on top). Right: a near miss (pillars touching, \
   block resting on them but not spanning a gap). Arrow or label showing \
   'near miss'. White and yellow chalk, hand-drawn." \
  generated-images/hts/chalk-arch-full.png --aspect 16:9
```

---

## Placement in a Deck

Chalkboard sequences work best as **punctuation between polished sections**:

```
[Title Slide]           -- polished, dark
[Chalkboard: K]         -- mode switch: "let me draw something"
[Chalkboard: K+P+t]    -- reveal the full idea
[Content slides...]     -- back to polished
...
[Chalkboard: arch]      -- another mode switch
[Chalkboard: near miss] -- reveal the insight
[Content slides...]     -- back to polished
[Contributions]         -- polished, final
```

The mode switch is the point. The audience should feel the shift.
