---
name: dev-reflection
description: Analyze development workflow after completion to identify problems and generate skill optimization suggestions
---

# Development Reflection

## Purpose

Analyze commit data after development to identify problem patterns and optimize skills.

**Trigger:**
- Automatically after finishing-a-development-branch completes
- Manually when user requests workflow analysis

**Announce:** "Analyzing development workflow for optimization opportunities."

## Process

### Step 1: Collect Commit Data

```bash
# Get commit history for this branch
git log --oneline --since="<start-date>" --until="<end-date>"

# Count commits by type
git log --format="%s" --since="<start-date>" | grep -cE "^feat:|^docs:"
git log --format="%s" --since="<start-date>" | grep -cE "^fix:|^refactor:"

# Get fix commit details
git log --format="%h|%s|%ad" --date=short | grep -E "^fix:|^refactor:"
```

Calculate:
- Total commits
- Fix commits count
- Fix rate = fix / (feat + fix)

### Step 2: Compare Plan vs Execution

Check:
- Planned tasks vs actual commits
- Extra tasks generated?
- Time deviation (if estimations available)

### Step 3: Identify Problem Patterns

**Classify fix commits:**

| Type | Pattern | Example |
|------|---------|---------|
| Terminology | Inconsistent naming | "组长" vs "正式组长" |
| Format | Mixed formats | 20% vs 0.2 |
| Validation | Range mismatch | 0-100 vs 0-1 |
| Logic | Wrong conditions | Missing edge case |
| Architecture | Layer violations | UI accessing models |

**Detect recurring patterns:**
- Same type appearing in multiple commits?
- Similar issue in previous versions?

### Step 4: Generate Suggestions

Output to: `temp/skill-optimization-YYYY-MM-DD.md`

**Template:**

```markdown
# Skill Optimization Suggestions

## Summary

- Planned tasks: N
- Total commits: M
- Fix commits: K
- Fix rate: X%

## Problem Patterns

| Type | Count | Examples |
|------|-------|----------|
| Terminology | 2 | "组长"→"正式组长" |
| Format | 1 | 百分比→小数 |

## Suggestions by Skill

### <skill-name>

**Problem:**
- <specific issue>

**Suggestion:**
- <actionable fix>

## Priority

| Skill | Priority | Impact |
|-------|----------|--------|
| brainstorming | P0 | Prevent terminology issues |
```

### Step 5: Interactive Selection

Present options:

```
Found N optimization suggestions:

1. Apply to skill files (immediate)
2. Save document only
3. View details first
4. Handle later

Choose?
```

**If Option 1:** Apply changes to relevant SKILL.md files

**If Option 2:** Just save the document

**If Option 3:** Show full document, then present options again

**If Option 4:** Document saved, exit

## Key Metrics

| Metric | Formula | Healthy | Warning |
|--------|---------|---------|---------|
| Fix rate | fix/(feat+fix) | < 20% | > 30% |
| Extra tasks | (actual-plan)/plan | < 10% | > 20% |
| Time deviation | (actual-estimated)/estimated | < 30% | > 50% |

**Warning threshold exceeded → Suggest skill optimization**

## Common Patterns

### Terminology Issues → brainstorming skill

```
Fix: Add terminology confirmation step
Location: After design approval
Check: Role names, display text, config fields
```

### Format Inconsistency → brainstorming skill

```
Fix: Add format specification step
Check: Number formats (decimal/percentage), validation ranges
```

### Architecture Violations → subagent-driven skill

```
Fix: Add architecture check in spec reviewer
Check: Layer access rules, dependency injection
```

### Late Bug Discovery → finishing skill

```
Fix: Add consistency check before merge
Check: Terminology, formats, validation ranges
```

## Integration

**Called by:**
- finishing-a-development-branch (Step 5b)

**Can call:**
- None

## Example Output

```
# Skill Optimization Suggestions

Based on v0.4.0 development.

## Summary

- Planned tasks: 13
- Total commits: 13
- Fix commits: 5
- Fix rate: 38% ⚠️ (threshold: 30%)

## Problem Patterns

| Type | Count | Examples |
|------|-------|----------|
| Terminology | 2 | "组长"→"正式组长", Role enum mismatch |
| Format | 2 | 20%→0.2, validation range 0-100→0-1 |
| Logic | 1 | Missing edge case |

## Suggestions

### brainstorming (P0)

**Problem:** Terminology and format discovered late

**Suggestion:**
- Add Step 3b: Confirm terminology and formats
- Check: Role names, number formats, validation ranges
- Include in design doc: terminology table

### finishing-a-development-branch (P1)

**Problem:** Bugs found after tests pass

**Suggestion:**
- Add Step 1c: Consistency check
- Verify: Enum values match UI, formats match validation

### writing-plans (P2)

**Problem:** Tasks too granular, many related fixes

**Suggestion:**
- Group related tasks
- Reduce spec verbosity
```