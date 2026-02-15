# Gemini Web Research Skill

AI-powered web research using Google's Gemini with Google Search grounding.

## Quick Start

1. **Get API Key**: Visit https://aistudio.google.com/apikey

2. **Set Environment Variable**:
   ```bash
   export GOOGLE_API_KEY="your-key-here"
   ```

3. **Install Dependencies**:
   ```bash
   pip install google-genai
   ```

4. **Run Research**:
   ```bash
   python scripts/web_research.py "latest AI developments 2026"
   ```

## Usage Examples

```bash
# Basic research (prints to stdout)
python scripts/web_research.py "quantum computing applications"

# Save to file
python scripts/web_research.py "climate change solutions" -o research-outputs/climate.md

# JSON output for scripts
python scripts/web_research.py "web3 technology" -f json > results.json

# Plain text
python scripts/web_research.py "space exploration news" -f text
```

## When to Invoke

Use this skill when you see user requests like:
- "Research X"
- "What's the latest on Y?"
- "Find information about Z"
- "Look up facts about..."
- "Investigate..."

## Features

- Real-time web search results
- Source citations included
- Multiple output formats
- Comprehensive summaries
- Organized, structured output

## Output Formats

- **Markdown** (default): Formatted with headings, source links
- **JSON**: Structured data for programmatic use
- **Text**: Plain text with sources

## Tips

- Be specific in queries for better results
- Break complex topics into multiple queries
- Save important research with `-o` flag
- Check source links for verification
- Use current year in query for latest info (e.g., "AI trends 2026")
