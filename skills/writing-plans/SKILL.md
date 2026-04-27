---
name: writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching code
---

# Writing Plans

## Overview

Write comprehensive implementation plans assuming the engineer has zero context for our codebase and questionable taste. Document everything they need to know: which files to touch for each task, code, testing, docs they might need to check, how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.

Assume they are a skilled developer, but know almost nothing about our toolset or problem domain. Assume they don't know good test design very well.

**Announce at start:** "I'm using the writing-plans skill to create the implementation plan."

**Context:** This should be run in a dedicated worktree (created by brainstorming skill).

**Save plans to:** `docs/plans/YYYY-MM-DD-<feature-name>.md`

## Bite-Sized Task Granularity

**Each task covers one logical unit (10-30 minutes):**
- Describe what to build, not how to build it
- Include acceptance criteria and file list
- Subagent implements from design doc, not plan

**Good task:**
```
Task 1: Add Role enum for new identity types

Files: src/models/role.py, tests/models/test_role.py

Acceptance:
- New roles added to enum
- Backward compatible with existing roles
- Tests pass

Implementation: Follow design doc section 3.1
```

**Avoid:**
- Complete code examples in plan
- Overly detailed steps (2-5 minutes is too granular)
- Spec overly restrictive ("only modify these files")

## Plan Document Header

**Every plan MUST start with this header:**

```markdown
# [Feature Name] Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Task Structure

**Simplified format - focus on what, not how:**

````markdown
### Task N: [Feature/Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py`
- Test: `tests/exact/path/to/test.py`

**Acceptance Criteria:**
- [ ] Feature works as described in design doc
- [ ] Tests pass (TDD approach)
- [ ] Follows architecture constraints

**Reference:** Design doc section X.Y

**Implementation Notes:**
- Key constraint or gotcha (1-2 lines max)
- Reference existing patterns to follow
````

**Platform-Specific Considerations (for cross-platform features):**

````markdown
### Platform Considerations

**Windows:**
- Requirement: [e.g., Hide console window]
- Parameters: [e.g., STARTUPINFO + CREATE_NO_WINDOW]
- Test: [e.g., Run exe with -w flag, check for console]

**Linux:**
- Requirement: [e.g., No special handling]
- Test: [e.g., Run in terminal, no unexpected behavior]

**Cross-platform code location:** [e.g., src/utils/cross_platform.py]
````

**Task Groups for Related Work:**

````markdown
### Task Group 1: [Layer Name]

**Tasks:** 1-4
**Goal:** Complete layer X with all dependencies
**Acceptance:** Layer tests pass, backward compatible
**Merge Recommendation:** Combine into single subagent (same file(s))
**Parallel Safe:** No (modifies shared file)

**Task 1:** ...
**Task 2:** ...
**Task 3:** ...
**Task 4:** ...
````

## Task Dependency Analysis (REQUIRED)

**Before listing tasks, analyze dependencies:**

| Pattern | Merge? | Parallel? | Reason |
|---------|--------|-----------|--------|
| Same file, sequential | ✅ Yes | ❌ No | Avoid context switch overhead |
| Same module, different files | ✅ Yes | ❌ No | Related changes, single commit |
| Different modules, no shared state | ❌ No | ✅ Yes | Independent, can run concurrently |
| Different modules, shared interface | ❌ No | ❌ No | Interface must stabilize first |

**Add to plan:**

```markdown
## Execution Strategy

**Merge Groups:**
- Task 1-3 → Single subagent (same file: `src/parser.py`)
- Task 4-6 → Single subagent (same file: `src/engine.py`)

**Parallel Groups:**
- Group 1 (Tasks 1-3) + Group 2 (Tasks 4-6) → Can run concurrently

**Sequential Dependencies:**
- Task 7 depends on Tasks 1-3 (uses parser)
- Task 9 depends on Task 7 (integration)
```

## Remember
- Exact file paths always
- **Keep tasks concise** - describe goal, not implementation
- Reference design doc for implementation details
- Reference relevant skills with @ syntax
- DRY, YAGNI, TDD, frequent commits
- **Core changes in specified files** - related changes allowed in related files
- **Group related tasks** for batch execution

## Execution Handoff

After saving the plan, offer execution choice based on task dependencies:

**If tasks have merge/parallel opportunities:**

**"Plan complete and saved to `docs/plans/<filename>.md`. Execution analysis:**

**Merge opportunities:** Tasks 1-3 (same file), Tasks 4-6 (same file)
**Parallel opportunities:** Group 1 + Group 2 (independent)

**Execution options:**

**1. Subagent-Driven (this session)** - Sequential per merged group, spec + quality review
**2. Parallel Agents (this session)** - Independent groups run concurrently via dispatching-parallel-agents
**3. Parallel Session (separate)** - Open new session with executing-plans, batch execution

**Which approach?"**

**If tasks are all tightly coupled:**

**"Plan complete. All tasks tightly coupled. Two options:**

**1. Subagent-Driven (this session)** - Sequential execution with reviews
**2. Parallel Session (separate)** - New session with executing-plans

**Which approach?"**

**If Subagent-Driven chosen:**
- **REQUIRED SUB-SKILL:** Use superpowers:subagent-driven-development
- Stay in this session
- Fresh subagent per task + code review

**If Parallel Session chosen:**
- Guide them to open new session in worktree
- **REQUIRED SUB-SKILL:** New session uses superpowers:executing-plans

## Post-Execution Checklist

After execution completes, verify:

### For Feature Development
- [ ] Code matches design document
- [ ] Design document updated if implementation differs
- [ ] README.md updated with new features/config
- [ ] All tests pass
- [ ] Code review completed

### For Refactoring
- [ ] All tests pass after refactoring
- [ ] Performance benchmarks (if applicable)
- [ ] Design document updated with new structure
- [ ] Module documentation updated

### For Technical Research
- [ ] Research report created (`docs/research/<topic>.md`)
- [ ] POC code tested and documented
- [ ] Recommendation clearly stated
- [ ] Implementation plan if recommendation accepted
