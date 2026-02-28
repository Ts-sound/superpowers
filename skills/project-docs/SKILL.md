---
name: project-docs
description: "How to manage project documentation structure. Make sure to use this skill whenever the user mentions project docs, design documents, documentation structure, creating design docs, updating architecture docs, or needs to organize docs/design/ directory. Also trigger when adding new features, completing bug fixes, or initializing projects to check if design docs need updates. Works closely with writing-plans and mermaid-diagram skills."
---

# Project Documentation Management

## Overview

Manage project documentation structure with focus on design documents. This skill creates and maintains the `docs/design/` directory, integrates with mermaid-diagram for visualizations, and coordinates with writing-plans for complete documentation workflow.

## Directory Structure

```
docs/
├── plan/                       # Managed by writing-plans
│   └── YYYY-MM-DD-<topic>-plan.md
└── design/                     # Managed by project-docs
    ├── README.md               # Overall system design
    └── <module>/               # Module subdirectories (short names)
        └── README.md           # Module detailed design
```

## Workflow

### Creating Design Documents

1. **Understand scope** — Ask about project/module being documented
2. **Check existing docs** — Look for existing design documents
3. **Create structure** — Set up `docs/design/` if needed
4. **Generate templates** — Create appropriate design doc templates
5. **Add diagrams** — Invoke mermaid-diagram for visualizations
6. **Review and validate** — Ensure completeness

### Document Sync Check

Triggered after:
- Adding new features
- Completing bug fixes
- Module refactoring

**Check process:**
1. Identify what changed (new files, modified modules)
2. Find affected design documents
3. Report what needs updates
4. Offer to update automatically

## Integration with Other Skills

### With writing-plans

**Flow:**
```
brainstorming → design approved
    ↓
project-docs → create/update docs/design/
    ↓
writing-plans → create docs/plan/ implementation plan
    ↓
implementation
```

**Coordination:**
- `project-docs` creates the **what** (design, architecture)
- `writing-plans` creates the **how** (implementation tasks)
- Design docs live in `docs/design/`
- Plan docs live in `docs/plan/`

### With mermaid-diagram

**Always invoke mermaid-diagram** before writing diagram code.

**When to invoke:**

| Design Section | Diagram Type | Purpose |
|----------------|--------------|---------|
| Architecture overview | `flowchart` (graph TD/LR) | System components and relationships |
| Key Sequences | `sequenceDiagram` | Module interactions, API flows |
| State Machine | `stateDiagram-v2` | State transitions, lifecycle |
| Data Model | `classDiagram` | Class structures, relationships |
| Timeline | `timeline` or `gantt` | Project milestones, release schedule |
| User Flows | `journey` | User experience, service design |
| Proportions | `pie` | Distribution, breakdown |

## Design Document Templates

### Overall Design (`docs/design/README.md`)

```markdown
# System Design

## Overview
Brief description of the system and its purpose.

## Architecture
High-level architecture diagram and description.

## Modules
| Module | Description | Link |
|--------|-------------|------|
| auth | Authentication & authorization | [auth/](auth/README.md) |
| api | REST API layer | [api/](api/README.md) |

## Technical Decisions
- Key architectural decisions
- Technology choices and rationale

## Data Model
Core data structures and relationships.
```

### Module Design (`docs/design/<module>/README.md`)

```markdown
# <Module Name> Design

## Overview
Purpose and responsibilities of this module.

## Architecture
Component diagram and description.

## Interfaces
### Public API
Functions/classes exposed by this module.

### Dependencies
Other modules this module depends on.

## Key Sequences
Key functional interaction flows. Use sequence diagrams to illustrate:
- Main use cases
- Error handling flows
- Cross-module interactions

## State Machine
(if applicable) State transitions and conditions.
```

## Commands

### Create Overall Design

```bash
# Create docs/design/README.md with system overview
# Include architecture flowchart via mermaid-diagram
```

### Create Module Design

```bash
# Create docs/design/<module>/README.md
# 
# 1. Invoke mermaid-diagram skill for each diagram type needed
# 2. Include diagrams based on module characteristics:
#    - All modules: Component diagram (flowchart)
#    - Interactive modules: Sequence diagrams (Key Sequences section)
#    - Stateful modules: State diagram (State Machine section)
#    - Data-heavy modules: Class diagram (Data Model section)
```

### Check Doc Sync

```bash
# After feature/bug completion:
# 1. Identify changed modules
# 2. Check corresponding design docs
# 3. Report needed updates
```

## When to Use This Skill

- User says "create design doc" or "document the architecture"
- User wants to "organize docs" or "setup documentation"
- Adding new features → check design doc updates
- Completing bug fixes → verify design accuracy
- User mentions `docs/design/` or design documentation
- Project initialization → create initial design structure

## Best Practices

1. **Keep design separate from plans** — `docs/design/` vs `docs/design/`
2. **Use mermaid for visuals** — A diagram is worth 1000 words
3. **Module short names** — `auth/` not `authentication/`
4. **Update on changes** — Design docs should reflect current state
5. **Link related docs** — Cross-reference between modules

## Anti-Patterns

- Writing implementation details in design docs (that's for plans)
- Creating design docs without diagrams when visuals help
- Letting design docs drift from actual implementation
- Using long names for module directories
