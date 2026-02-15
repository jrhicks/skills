#!/usr/bin/env python3
"""
Gemini Web Research Script
Uses Google Gemini API with Google Search grounding for web research.
"""

import argparse
import os
import sys
import json
from google import genai
from google.genai import types


def setup_client():
    """Initialize the Gemini client with API key from environment."""
    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.", file=sys.stderr)
        print("Get your API key from: https://aistudio.google.com/apikey", file=sys.stderr)
        print("Then set it with: export GOOGLE_API_KEY='your-key-here'", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    return client


def research_topic(client, query, max_tokens=8192):
    """
    Research a topic using Gemini with Google Search grounding.

    Args:
        client: Gemini client instance
        query: Research query string
        max_tokens: Maximum tokens in response

    Returns:
        tuple: (response_text, grounding_metadata)
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=query,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                response_modalities=["TEXT"],
                max_output_tokens=max_tokens,
            )
        )

        # Extract text and grounding metadata
        text = response.text if hasattr(response, 'text') else str(response)
        grounding_metadata = None

        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'grounding_metadata'):
                grounding_metadata = candidate.grounding_metadata

        return text, grounding_metadata

    except Exception as e:
        print(f"Error during research: {e}", file=sys.stderr)
        sys.exit(1)


def format_as_markdown(text, grounding_metadata):
    """Format research results as Markdown with citations."""
    output = text + "\n\n"

    if grounding_metadata:
        # Add sources section
        if hasattr(grounding_metadata, 'grounding_chunks') and grounding_metadata.grounding_chunks:
            output += "## Sources\n\n"
            seen_urls = set()
            for chunk in grounding_metadata.grounding_chunks:
                if hasattr(chunk, 'web') and chunk.web:
                    url = chunk.web.uri if hasattr(chunk.web, 'uri') else None
                    title = chunk.web.title if hasattr(chunk.web, 'title') else url

                    if url and url not in seen_urls:
                        output += f"- [{title}]({url})\n"
                        seen_urls.add(url)

        # Add search queries used
        if hasattr(grounding_metadata, 'search_entry_point') and grounding_metadata.search_entry_point:
            if hasattr(grounding_metadata.search_entry_point, 'rendered_content'):
                output += f"\n---\n{grounding_metadata.search_entry_point.rendered_content}\n"

    return output


def format_as_json(text, grounding_metadata):
    """Format research results as JSON."""
    result = {
        "text": text,
        "sources": []
    }

    if grounding_metadata:
        if hasattr(grounding_metadata, 'grounding_chunks') and grounding_metadata.grounding_chunks:
            seen_urls = set()
            for chunk in grounding_metadata.grounding_chunks:
                if hasattr(chunk, 'web') and chunk.web:
                    url = chunk.web.uri if hasattr(chunk.web, 'uri') else None
                    title = chunk.web.title if hasattr(chunk.web, 'title') else url

                    if url and url not in seen_urls:
                        result["sources"].append({
                            "title": title,
                            "url": url
                        })
                        seen_urls.add(url)

    return json.dumps(result, indent=2)


def format_as_text(text, grounding_metadata):
    """Format research results as plain text."""
    output = text + "\n\n"

    if grounding_metadata:
        if hasattr(grounding_metadata, 'grounding_chunks') and grounding_metadata.grounding_chunks:
            output += "SOURCES:\n\n"
            seen_urls = set()
            for chunk in grounding_metadata.grounding_chunks:
                if hasattr(chunk, 'web') and chunk.web:
                    url = chunk.web.uri if hasattr(chunk.web, 'uri') else None
                    title = chunk.web.title if hasattr(chunk.web, 'title') else url

                    if url and url not in seen_urls:
                        output += f"- {title}\n  {url}\n\n"
                        seen_urls.add(url)

    return output


def main():
    parser = argparse.ArgumentParser(
        description='Research topics using Google Gemini with search grounding'
    )
    parser.add_argument('query', help='Research query')
    parser.add_argument('-o', '--output', help='Output file path (default: stdout)')
    parser.add_argument('-f', '--format', choices=['markdown', 'json', 'text'],
                       default='markdown', help='Output format (default: markdown)')
    parser.add_argument('--max-tokens', type=int, default=8192,
                       help='Maximum tokens in response (default: 8192)')

    args = parser.parse_args()

    # Setup client
    client = setup_client()

    # Perform research
    text, grounding_metadata = research_topic(client, args.query, args.max_tokens)

    # Format output
    if args.format == 'markdown':
        output = format_as_markdown(text, grounding_metadata)
    elif args.format == 'json':
        output = format_as_json(text, grounding_metadata)
    else:  # text
        output = format_as_text(text, grounding_metadata)

    # Write output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Research saved to: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == '__main__':
    main()
