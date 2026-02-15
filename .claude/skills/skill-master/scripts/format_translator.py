#!/usr/bin/env python3
"""
Format Translator for skill-master.
Converts non-SKILL.md skill formats (MCP server JSON, etc.) into Claude Code SKILL.md format.
"""

import argparse
import json
import sys
from pathlib import Path


def detect_format(data):
    """Auto-detect the source format from parsed JSON data."""
    if isinstance(data, dict):
        # MCP server: has "tools" array with inputSchema
        if "tools" in data and isinstance(data["tools"], list):
            for tool in data["tools"]:
                if isinstance(tool, dict) and "inputSchema" in tool:
                    return "mcp"
            # tools array but no inputSchema -- still likely MCP
            if data["tools"]:
                return "mcp"
        # Cursor rules format (future)
        if "rules" in data:
            return "cursor"
    return None


def translate_mcp(data):
    """Translate MCP server JSON to SKILL.md content."""
    name = data.get("name", "unknown-server")
    description = data.get("description", "MCP server translated by skill-master.")
    tools = data.get("tools", [])

    lines = []

    # YAML frontmatter
    lines.append("---")
    lines.append(f"name: {name}")
    lines.append("description: |")
    lines.append(f"  {description}")
    lines.append("  Translated from MCP server definition by skill-master.")
    lines.append("---")
    lines.append("")
    lines.append(f"# {name}")
    lines.append("")
    lines.append(description)
    lines.append("")

    if not tools:
        lines.append("*No tools defined in source.*")
        return "\n".join(lines) + "\n"

    lines.append("## Tools")
    lines.append("")

    for tool in tools:
        tool_name = tool.get("name", "unnamed")
        tool_desc = tool.get("description", "No description provided.")
        input_schema = tool.get("inputSchema", {})

        lines.append(f"### {tool_name}")
        lines.append("")
        lines.append(tool_desc)
        lines.append("")

        properties = input_schema.get("properties", {})
        required = input_schema.get("required", [])

        if properties:
            lines.append("**Parameters:**")
            lines.append("")
            lines.append("| Parameter | Type | Required | Description |")
            lines.append("|-----------|------|----------|-------------|")

            for param_name, param_def in properties.items():
                param_type = param_def.get("type", "any")
                param_desc = param_def.get("description", "")
                is_required = "Yes" if param_name in required else "No"
                lines.append(f"| {param_name} | {param_type} | {is_required} | {param_desc} |")

            lines.append("")

    return "\n".join(lines) + "\n"


def translate_cursor(data):
    """Placeholder for Cursor rules translation (future)."""
    print("Error: Cursor rules translation is not yet implemented.", file=sys.stderr)
    print("This format will be supported in a future version.", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Translate non-SKILL.md skill formats into Claude Code SKILL.md format."
    )
    parser.add_argument("input", help="Path to source file (MCP server JSON, etc.)")
    parser.add_argument("-o", "--output", help="Output path (default: stdout)")
    parser.add_argument(
        "--format",
        choices=["auto", "mcp", "cursor"],
        default="auto",
        help="Source format (default: auto-detect)",
    )

    args = parser.parse_args()

    # Read input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            raw = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse JSON
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Error: Input is not valid JSON: {e}", file=sys.stderr)
        print("Supported formats: MCP server JSON", file=sys.stderr)
        sys.exit(1)

    # Detect or use specified format
    fmt = args.format
    if fmt == "auto":
        fmt = detect_format(data)
        if fmt is None:
            print("Error: Could not auto-detect format.", file=sys.stderr)
            print("The input JSON does not match any known format.", file=sys.stderr)
            print("Supported formats:", file=sys.stderr)
            print("  - MCP server (JSON with 'tools' array containing 'inputSchema')", file=sys.stderr)
            print("Use --format to specify explicitly.", file=sys.stderr)
            sys.exit(1)

    # Translate
    if fmt == "mcp":
        output = translate_mcp(data)
    elif fmt == "cursor":
        translate_cursor(data)
        return  # translate_cursor exits
    else:
        print(f"Error: Unknown format: {fmt}", file=sys.stderr)
        sys.exit(1)

    # Write output
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"SKILL.md written to: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
