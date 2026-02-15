# Setup: skill-audit Skill

## What It Is

Read-only static security auditor for Claude Code skills. Performs 5-phase analysis with 6 detection rules (SKL-001 through SKL-006) and produces a risk score (0-10). Runs in a forked sub-agent context using only Read, Grep, Glob, and WebFetch -- it cannot modify files or execute scripts.

## Where to Get It

**Source**: github.com/anysiteio/agent-skills

The skill-audit skill lives in the `skills/skill-audit/` directory of that repository.

## Installation Steps

### 1. Clone the repo to a temp location

```bash
git clone --depth 1 https://github.com/anysiteio/agent-skills.git /tmp/agent-skills
```

### 2. Copy skill-audit to your skills directory

For personal installation (recommended):
```bash
cp -r /tmp/agent-skills/skills/skill-audit ~/.claude/skills/skill-audit
```

For project installation:
```bash
cp -r /tmp/agent-skills/skills/skill-audit .claude/skills/skill-audit
```

### 3. Clean up temp files

```bash
rm -rf /tmp/agent-skills
```

### 4. Verify installation

```bash
ls ~/.claude/skills/skill-audit/SKILL.md 2>/dev/null || ls .claude/skills/skill-audit/SKILL.md
```

You should see the SKILL.md file. The skill is now discoverable by Claude Code.

## What It Provides

### 5-Phase Analysis
1. **Discovery**: Inventories all files, detects plugin structure
2. **Frontmatter Analysis**: Checks allowed-tools, hooks, permissions
3. **Body Content Analysis**: Scans for dangerous tool refs, prompt injection, sensitive paths
4. **Supporting Files Analysis**: Examines scripts for network egress, credential access
5. **Hooks Analysis**: Detects hook definitions, classifies as benign or dangerous

### 6 Detection Rules
- **SKL-001**: Hooks (benign vs dangerous)
- **SKL-002**: Prompt injection markers
- **SKL-003**: Dangerous tool references
- **SKL-004**: Missing safeguards
- **SKL-005**: Dangerous scripts
- **SKL-006**: Permission escalation

### Risk Scoring
- **0**: Clean, no findings
- **1-3**: Low risk, minor concerns
- **4-6**: Medium risk, review recommended
- **7-8**: Critical risk, likely malicious patterns
- **9-10**: Almost certainly malicious

## Troubleshooting

**SKILL.md not found**: Make sure you copied the entire `skill-audit/` directory, not just individual files.

**Permission denied**: Check file permissions with `ls -la ~/.claude/skills/skill-audit/`.

**Skill not recognized**: Claude Code discovers skills by scanning `~/.claude/skills/` and `.claude/skills/`. Restart your Claude Code session after installation.
