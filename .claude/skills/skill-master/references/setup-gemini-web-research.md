# Setup: gemini-web-research Skill

## What It Is

Web research skill powered by Google's Gemini API with Google Search grounding. Provides current, cited information from the web. skill-master delegates all discovery and reputation research to this skill.

## Where to Get It

- **Already in this project**: `.claude/skills/gemini-web-research/`
- **Source repo**: github.com/anthropics/skills (or your project's copy)

## Installation Steps

### 1. Copy the skill directory

For personal installation (available across all projects):
```bash
cp -r .claude/skills/gemini-web-research ~/.claude/skills/gemini-web-research
```

Or keep it in your project's `.claude/skills/` (already there if cloned from this repo).

### 2. Install Python dependency

```bash
pip install google-genai
```

### 3. Set API key

See `setup-api-keys.md` for GOOGLE_API_KEY setup.

### 4. Verify installation

```bash
# Check skill exists
ls ~/.claude/skills/gemini-web-research/SKILL.md 2>/dev/null || ls .claude/skills/gemini-web-research/SKILL.md

# Test the script (requires GOOGLE_API_KEY)
python3 .claude/skills/gemini-web-research/scripts/web_research.py "test query"
```

## What It Provides

- Gemini-powered web search with Google Search grounding
- Source citations with URLs
- Multiple output formats (markdown, json, text)
- CLI interface via `scripts/web_research.py`
