---
name: gemini-web-research
description: |
  Research topics on the web using Google Gemini API with Google Search grounding.
  Use when the user requests: web research, topic investigation, fact-finding, current information,
  or wants to learn about a specific subject with cited sources.
  Triggers: "research this topic", "look up information about", "find out about",
  "what's the latest on", "investigate", "search the web for".
---

# Gemini Web Research - AI-Powered Web Research

Research topics using Google's Gemini model with Google Search grounding to get current, cited information from the web.

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

### Basic Research

```bash
python scripts/web_research.py "your research query"
```

### Save to File

```bash
python scripts/web_research.py "your research query" -o output.md
```

### Output Formats

```bash
# Markdown format (default)
python scripts/web_research.py "quantum computing advances" -f markdown

# JSON format (for programmatic use)
python scripts/web_research.py "quantum computing advances" -f json

# Plain text format
python scripts/web_research.py "quantum computing advances" -f text
```

### Advanced Options

```bash
python scripts/web_research.py "research query" \
  -o results.md \
  -f markdown \
  --max-tokens 8192
```

## Output Location

By default, research results are printed to stdout. Use `-o` flag to save to a file.
Consider saving research to `research-outputs/` directory in project root.

## When to Use

Use this skill when the user needs:
- **Current information**: Latest news, trends, or developments
- **Fact-checking**: Verify claims or get accurate data
- **Topic exploration**: Learn about unfamiliar subjects
- **Cited sources**: Information backed by web sources
- **Comprehensive overviews**: Multi-faceted topics requiring multiple sources

## Skill Workflow

1. **Understand the query**: Clarify what aspect of the topic interests the user
2. **Run research**: Execute the script with the query
3. **Review results**: Check that the response is comprehensive and relevant
4. **Present findings**: Share the key insights with the user
5. **Provide sources**: Include citations so the user can verify information

## Research Quality Tips

**Be specific**: Instead of "AI", use "latest developments in large language models 2026"

**Multiple queries**: For complex topics, break into separate focused queries:
- "history of electric vehicles"
- "current electric vehicle market share 2026"
- "future predictions for electric vehicles"

**Follow-up questions**: Based on initial results, ask clarifying questions to dive deeper

## Examples

Research current events:
```bash
python scripts/web_research.py "latest developments in renewable energy technology 2026" -o research-outputs/renewable-energy.md
```

Fact-check a claim:
```bash
python scripts/web_research.py "statistics on global carbon emissions 2025" -f markdown
```

Explore a technical topic:
```bash
python scripts/web_research.py "how do quantum computers achieve quantum advantage" -o research-outputs/quantum-computing.md
```

Compare perspectives:
```bash
python scripts/web_research.py "different economic perspectives on universal basic income" -f text
```

## Features

- **Grounded responses**: All information is grounded in real web search results
- **Source citations**: Get links to source material for verification
- **Current information**: Access to recent web content (not limited by training cutoff)
- **Comprehensive summaries**: Structured, organized information with key findings
- **Multiple formats**: Output as markdown, JSON, or plain text

## Limitations

- Requires active internet connection
- API key required (uses Gemini API quota)
- Search results quality depends on query specificity
- May not access paywalled or restricted content
- Information accuracy depends on web source quality

## Best Practices

1. **Verify critical information**: Cross-reference important facts
2. **Check source dates**: Ensure information is current
3. **Read original sources**: Click through to source links for full context
4. **Refine queries**: Iterate on query wording for better results
5. **Save important research**: Use `-o` flag to keep research for future reference
