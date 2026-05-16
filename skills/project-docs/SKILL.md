---
name: project-docs
description: "How to manage project documentation structure. Make sure to use this skill whenever the user mentions project docs, design documents, documentation structure, creating design docs, updating architecture docs, or needs to organize docs/design/ directory. Also trigger when adding new features, completing bug fixes, or initializing projects to check if design docs need updates. Works closely with writing-plans and mermaid-diagram skills."
---

# Project Documentation Management

## Overview

Manage project documentation structure with focus on design documents. This skill creates and maintains the `docs/design/` directory, integrates with mermaid-diagram for visualizations, and coordinates with writing-plans.

## Rules (Load on Demand)

Rules are modular. Load only the ones needed for the current task from `rules/`:

| Rule File | When to Load |
|-----------|--------------|
| `rules/editing.md` | Document editing, proofreading, polishing |
| `rules/directory-structure.md` | Setting up or reorganizing `docs/` |
| `rules/design-doc-template.md` | Creating design or module documents |
| `rules/mermaid-diagram.md` | Adding diagrams to documents |
| `rules/sync-rules.md` | After code changes, checking doc accuracy |
| `rules/best-practices.md` | General guidance, code review of docs |

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

Mermaid diagrams are generated directly — no external skill invocation needed.
See `rules/mermaid-diagram.md` for diagram type selection.

## When to Use This Skill

- User says "create design doc" or "document the architecture"
- User wants to "organize docs" or "setup documentation"
- Adding new features → check design doc updates
- Completing bug fixes → verify design accuracy
- Project initialization → create initial design structure
