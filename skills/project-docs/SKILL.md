---
name: project-docs
description: "How to manage project documentation structure. Make sure to use this skill whenever the user mentions project docs, design documents, documentation structure, creating design docs, updating architecture docs, or needs to organize docs/design/ directory. Also trigger when adding new features, completing bug fixes, or initializing projects to check if design docs need updates. Works closely with writing-plans and mermaid-diagram skills."
---

# Project Documentation Management

## Overview

Manage project documentation structure with focus on design documents. This skill creates and maintains the `docs/design/` directory, integrates with mermaid-diagram for visualizations, and coordinates with writing-plans.

## Directory Structure

```
docs/
├── design/                     # Design documents
│   ├── README.md               # Overall system design
│   └── <module>/README.md      # Module designs
├── plans/                      # Implementation plans (writing-plans)
│   └── YYYY-MM-DD-<topic>.md
├── requirements.md             # Requirements
└── terminology.md              # Terminology definitions

Root-level docs:
├── README.md                   # Primary (English)
├── README.zh.md                # Chinese (optional)
└── AGENTS.md                   # AI conventions
```

## Template Files

| Template | Purpose | Location |
|----------|---------|----------|
| design-overview.md | System design | `templates/design-overview.md` |
| module-design.md | Module design | `templates/module-design.md` |
| README.md | Project README | See project-structure/templates/ |
| AGENTS.md | AI conventions | See project-structure/templates/ |

**Use templates directly** - don't inline code in SKILL.md.

## Workflow

### Creating Design Documents

1. **Understand scope** — Ask about project/module being documented
2. **Check existing docs** — Look for existing design documents
3. **Copy template** — Use `templates/design-overview.md` or `templates/module-design.md`
4. **Add diagrams** — Use mermaid for visualizations
5. **Review and validate** — Ensure completeness

### Document Sync Check

Triggered after: Adding new features, Completing bug fixes, Module refactoring

**Check process:**
1. Identify what changed (new files, modified modules)
2. Find affected design documents
3. Report what needs updates
4. Offer to update automatically

## Integration with Other Skills

### With writing-plans

```
brainstorming → project-docs (docs/design/) → writing-plans (docs/plans/) → implementation
```

- `project-docs`: the **what** (design, architecture)
- `writing-plans`: the **how** (implementation tasks)

### With mermaid-diagram

**Use mermaid for:**

| Design Section | Diagram Type |
|----------------|--------------|
| Architecture overview | `flowchart TD` |
| Module structure | `flowchart LR` |
| Class structure | `classDiagram` |
| Sequence/Interaction | `sequenceDiagram` |
| State Machine | `stateDiagram-v2` |

**Generate directly** - no external skill invocation needed.

## Commands

### Create Overall Design

1. Copy `templates/design-overview.md`
2. Customize for project
3. Add mermaid diagrams (architecture, data model)

### Create Module Design

1. Copy `templates/module-design.md`
2. Customize for module
3. Add appropriate diagrams (component, sequence, state)

### Check Doc Sync

1. Identify changed modules
2. Check corresponding design docs
3. Report needed updates

## Best Practices

1. **Design separate from plans** — `docs/design/` vs `docs/plans/`
2. **Use mermaid for visuals** — Diagram worth 1000 words
3. **Module short names** — `auth/` not `authentication/`
4. **Update on changes** — Reflect current state
5. **Link related docs** — Cross-reference modules
6. **Bilingual README** — Primary + localized with switch links
7. **AGENTS.md for AI** — Conventions for AI agents

## Anti-Patterns

- Implementation details in design docs (that's for plans)
- Design docs without diagrams when visuals help
- Letting design docs drift from implementation
- Long names for module directories

## When to Use This Skill

- User says "create design doc" or "document the architecture"
- User wants to "organize docs" or "setup documentation"
- Adding new features → check design doc updates
- Completing bug fixes → verify design accuracy
- Project initialization → create initial design structure