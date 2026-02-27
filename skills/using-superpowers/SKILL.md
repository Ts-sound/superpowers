---
name: using-superpowers
description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions
---

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## How to Access Skills

**In Claude Code:** Use the `Skill` tool. When you invoke a skill, its content is loaded and presented to you—follow it directly. Never use the Read tool on skill files.

**In other environments:** Check your platform's documentation for how skills are loaded.

# Using Skills

## The Rule

**Invoke relevant or requested skills BEFORE any response or action.** Even a 1% chance a skill might apply means that you should invoke the skill to check. If an invoked skill turns out to be wrong for the situation, you don't need to use it.

```mermaid
graph TD
    A["User message received"] --> D{"Might any skill apply?"};
    B["About to EnterPlanMode?"] --> C{"Already brainstormed?"};
    C -->|no| E["Invoke brainstorming skill"];
    C -->|yes| D;
    E --> D;
    D -->|yes, even 1%| F["Invoke Skill tool"];
    D -->|definitely not| L["Respond <br> (including clarifications)"];
    F --> G["Announce:  <br> 'Using [skill] to [purpose]'"];
    G --> H{"Has checklist?"};
    H -->|yes| I["Create TodoWrite todo per item "];
    H -->|no| J["Follow skill exactly"];
    I --> J;

    classDef endnode fill:#f9f;
    classDef decision fill:#ddf;
    classDef process fill:#e6f2ff;
    
    %% 给节点分配样式
    class A,B,L endnode;
    class C,D,H decision;
    class E,F,G,I,J process;
```

## Red Flags

These thoughts mean STOP—you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | Skill check comes BEFORE clarifying questions. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "I can check git/files quickly" | Files lack conversation context. Check for skills. |
| "Let me gather information first" | Skills tell you HOW to gather information. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I remember this skill" | Skills evolve. Read current version. |
| "This doesn't count as a task" | Action = task. Check for skills. |
| "The skill is overkill" | Simple things become complex. Use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |
| "This feels productive" | Undisciplined action wastes time. Skills prevent this. |
| "I know what that means" | Knowing the concept ≠ using the skill. Invoke it. |

## Skill Priority

When multiple skills could apply, use this order:

1. **Process skills first** (brainstorming, debugging) - these determine HOW to approach the task
2. **Implementation skills second** (frontend-design, mcp-builder) - these guide execution

"Let's build X" → brainstorming first, then implementation skills.
"Fix this bug" → debugging first, then domain-specific skills.

## Skill Types

**Rigid** (TDD, debugging): Follow exactly. Don't adapt away discipline.

**Flexible** (patterns): Adapt principles to context.

The skill itself tells you which.

## User Instructions

Instructions say WHAT, not HOW. "Add X" or "Fix Y" doesn't mean skip workflows.

## Available Skills

### Diagram Creation
- **mermaid-diagram** - Create mermaid diagrams (flowchart, sequence, gantt, class, state, pie, timeline, user journey)
  - Triggers: "draw a flowchart", "create sequence diagram", "mermaid chart"

### Project Management
- **project-structure** - Manage project engineering structure (src/, tests/, docs/, scripts/)
  - Triggers: "create project", "project structure", "scaffold repository", "setup directory"

### Documentation
- **project-docs** - Manage project documentation (docs/design/, module design, sync check)
  - Triggers: "create design doc", "update architecture", "check docs sync"
