---
name: nano-banana
description: |
  Generate image assets during development using Google's Gemini image model (Nano Banana).
  Use when the user requests: icon generation, placeholder images, logos, UI elements,
  marketing graphics, or image transformations (e.g., "make an illustrated version of this photo").
  Triggers: "generate an icon", "create a placeholder", "make a logo", "illustrate this image",
  "create an asset for", "generate image of", "make me a [visual element]".
---

# Nano Banana - Dev-Time Image Generation

Generate images and transform existing images using Google's Gemini model during development.

## Setup (One-Time)

1. Get API key: https://aistudio.google.com/apikey
2. Set environment variable:
   ```bash
   export GOOGLE_API_KEY="your-key-here"
   ```
3. Install SDK:
   ```bash
   pip install google-genai
   ```

## Usage

### Generate from Text Prompt

```bash
python scripts/generate_image.py generate "prompt" output.png [--aspect 1:1] [--count 1]
```

Aspect ratios: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`

### Transform Existing Image

```bash
python scripts/generate_image.py transform input.png "transformation prompt" output.png
```

## Output Location

Save all generated images to `generated-images/` in project root. Create directory if needed.

## Context-Aware Generation

Before generating, read relevant project files to match existing style:

1. Check for color schemes in CSS/Tailwind config
2. Look at existing assets for style consistency
3. Include style details in the prompt (e.g., "minimalist, using hex #3B82F6")

## Prompt Guidelines

**Icons/UI**: Include size, style, and background
- "64x64 minimalist settings gear icon, flat design, transparent background"

**Placeholders**: Specify dimensions and content type
- "Product placeholder image, 800x600, ecommerce style, neutral gray"

**Transformations**: Be specific about the target style
- "Convert to flat vector illustration style with bold outlines"

**Text in images**: Nano Banana handles text well - specify exact text
- "Blue button with white text saying 'Submit Order'"

## Examples

Generate app icon:
```bash
python scripts/generate_image.py generate \
  "App icon for a recipe app, fork and knife, warm orange gradient, rounded corners, iOS style" \
  generated-images/app-icon.png --aspect 1:1
```

Transform product photo to illustration:
```bash
python scripts/generate_image.py transform \
  photos/banana.jpg \
  "Convert to cute cartoon illustration style with thick outlines" \
  generated-images/banana-illustrated.png
```
