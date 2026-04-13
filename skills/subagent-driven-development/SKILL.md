---
name: subagent-driven-development
description: Use when executing implementation plans with independent tasks in the current session
---

# Subagent-Driven Development

Execute plan by dispatching fresh subagent per task, with two-stage review after each: spec compliance review first, then code quality review.

**Core principle:** Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration

## When to Use

```mermaid
graph TD
    A{{"Have implementation plan?"}} -->|yes| B{{"Tasks mostly independent?"}};
    A -->|no| F["Manual execution or brainstorm first"];
    B -->|yes| C{{"Stay in this session?"}};
    B -->|no - tightly coupled| F;
    C -->|yes| D["subagent-driven-development"];
    C -->|no - parallel session| E["executing-plans"];

    classDef endnode fill:#f9f;
    classDef decision fill:#ddf;
    classDef process fill:#e6f2ff;

    class A,B,C decision;
    class D,E,F process;
```

**vs. Executing Plans (parallel session):**
- Same session (no context switch)
- Fresh subagent per task (no context pollution)
- Two-stage review after each task: spec compliance first, then code quality
- Faster iteration (no human-in-loop between tasks)

## The Process

```mermaid
graph TD
    Start["Read plan, extract all tasks with full text, note context, inject terminology, create TodoWrite"];
    MoreTasks{{"More tasks remain?"}};
    FinalReview["Dispatch final code reviewer subagent for entire implementation"];
    Superpower["Use superpowers:finishing-a-development-branch"]:::greenNode;

    subgraph PerTask ["Per Task"]
        direction TB
        DispatchImpl["Dispatch implementer subagent (./implementer-prompt.md)"];
        ImplAsk{{"Implementer subagent asks questions?"}};
        AnswerQ["Answer questions, provide context"];
        ImplDo["Implementer subagent implements, tests, commits, self-reviews"];
        DispatchSpec["Dispatch spec reviewer subagent (./spec-reviewer-prompt.md)"];
        SpecCheck{{"Spec reviewer subagent confirms code matches spec?"}};
        FixSpec["Implementer subagent fixes spec gaps"];
        DispatchCode["Dispatch code quality reviewer subagent (./code-quality-reviewer-prompt.md)"];
        CodeCheck{{"Code quality reviewer subagent approves?"}};
        FixQuality["Implementer subagent fixes quality issues"];
        MarkComplete["Mark task complete in TodoWrite"];
    end

    Start --> DispatchImpl;
    DispatchImpl --> ImplAsk;
    ImplAsk -->|no| ImplDo;
    ImplAsk -->|yes| AnswerQ;
    AnswerQ --> DispatchImpl;
    ImplDo --> DispatchSpec;
    DispatchSpec --> SpecCheck;
    SpecCheck -->|yes| DispatchCode;
    SpecCheck -->|no| FixSpec;
    FixSpec -->|re-review| DispatchSpec;
    DispatchCode --> CodeCheck;
    CodeCheck -->|yes| MarkComplete;
    CodeCheck -->|no| FixQuality;
    FixQuality -->|re-review| DispatchCode;
    MarkComplete --> MoreTasks;
    MoreTasks -->|yes| DispatchImpl;
    MoreTasks -->|no| FinalReview;
    FinalReview --> Superpower;

    classDef endnode fill:#f9f; 
    classDef decision fill:#ddf;  
    classDef process fill:#e6f2ff;   
    classDef warningNode fill:red;
    classDef greenNode fill:lightgreen;

    class ImplAsk,SpecCheck,CodeCheck,MoreTasks decision;
    class Start,DispatchImpl,AnswerQ,ImplDo,DispatchSpec,FixSpec,DispatchCode,FixQuality,MarkComplete,FinalReview process;
    class Superpower endnode;
```

**Before dispatching first implementer:**
Inject terminology and format conventions from design doc:
- Enum values and UI labels
- Number formats (decimal/percentage)
- Validation ranges
- Naming conventions

## Prompt Templates

- `./implementer-prompt.md` - Dispatch implementer subagent
- `./spec-reviewer-prompt.md` - Dispatch spec compliance reviewer subagent
- `./code-quality-reviewer-prompt.md` - Dispatch code quality reviewer subagent

## Example Workflow

```
You: I'm using Subagent-Driven Development to execute this plan.

[Read plan file once: docs/plans/feature-plan.md]
[Extract all 5 tasks with full text and context]
[Create TodoWrite with all tasks]

Task 1: Hook installation script

[Get Task 1 text and context (already extracted)]
[Dispatch implementation subagent with full task text + context]

Implementer: "Before I begin - should the hook be installed at user or system level?"

You: "User level (~/.config/superpowers/hooks/)"

Implementer: "Got it. Implementing now..."
[Later] Implementer:
  - Implemented install-hook command
  - Added tests, 5/5 passing
  - Self-review: Found I missed --force flag, added it
  - Committed

[Dispatch spec compliance reviewer]
Spec reviewer: ✅ Spec compliant - all requirements met, nothing extra

[Get git SHAs, dispatch code quality reviewer]
Code reviewer: Strengths: Good test coverage, clean. Issues: None. Approved.

[Mark Task 1 complete]

Task 2: Recovery modes

[Get Task 2 text and context (already extracted)]
[Dispatch implementation subagent with full task text + context]

Implementer: [No questions, proceeds]
Implementer:
  - Added verify/repair modes
  - 8/8 tests passing
  - Self-review: All good
  - Committed

[Dispatch spec compliance reviewer]
Spec reviewer: ❌ Issues:
  - Missing: Progress reporting (spec says "report every 100 items")
  - Extra: Added --json flag (not requested)

[Implementer fixes issues]
Implementer: Removed --json flag, added progress reporting

[Spec reviewer reviews again]
Spec reviewer: ✅ Spec compliant now

[Dispatch code quality reviewer]
Code reviewer: Strengths: Solid. Issues (Important): Magic number (100)

[Implementer fixes]
Implementer: Extracted PROGRESS_INTERVAL constant

[Code reviewer reviews again]
Code reviewer: ✅ Approved

[Mark Task 2 complete]

...

[After all tasks]
[Dispatch final code-reviewer]
Final reviewer: All requirements met, ready to merge

Done!
```

## Advantages

**vs. Manual execution:**
- Subagents follow TDD naturally
- Fresh context per task (no confusion)
- Parallel-safe (subagents don't interfere)
- Subagent can ask questions (before AND during work)

**vs. Executing Plans:**
- Same session (no handoff)
- Continuous progress (no waiting)
- Review checkpoints automatic

**Efficiency gains:**
- No file reading overhead (controller provides full text)
- Controller curates exactly what context is needed
- Subagent gets complete information upfront
- Questions surfaced before work begins (not after)

**Quality gates:**
- Self-review catches issues before handoff
- Two-stage review: spec compliance, then code quality
- Review loops ensure fixes actually work
- Spec compliance prevents over/under-building
- Code quality ensures implementation is well-built

**Cost:**
- More subagent invocations (implementer + 2 reviewers per task)
- Controller does more prep work (extracting all tasks upfront)
- Review loops add iterations
- But catches issues early (cheaper than debugging later)

## Red Flags

**Never:**
- Start implementation on main/master branch without explicit user consent
- Skip reviews (spec compliance OR code quality)
- Proceed with unfixed issues
- Dispatch multiple implementation subagents in parallel (conflicts)
- Make subagent read plan file (provide full text instead)
- Skip scene-setting context (subagent needs to understand where task fits)
- Ignore subagent questions (answer before letting them proceed)
- Accept "close enough" on spec compliance (spec reviewer found issues = not done)
- Skip review loops (reviewer found issues = implementer fixes = review again)
- Let implementer self-review replace actual review (both are needed)
- **Start code quality review before spec compliance is ✅** (wrong order)
- Move to next task while either review has open issues

**If subagent asks questions:**
- Answer clearly and completely
- Provide additional context if needed
- Don't rush them into implementation

**If reviewer finds issues:**
- Implementer (same subagent) fixes them
- Reviewer reviews again
- Repeat until approved
- Don't skip the re-review

**If subagent fails task:**
- Dispatch fix subagent with specific instructions
- Don't try to fix manually (context pollution)

## Integration

**Required workflow skills:**
- **superpowers:using-git-worktrees** - REQUIRED: Set up isolated workspace before starting
- **superpowers:writing-plans** - Creates the plan this skill executes
- **superpowers:requesting-code-review** - Code review template for reviewer subagents
- **superpowers:finishing-a-development-branch** - Complete development after all tasks

**Subagents should use:**
- **superpowers:test-driven-development** - Subagents follow TDD for each task

**Alternative workflow:**
- **superpowers:executing-plans** - Use for parallel session instead of same-session execution
