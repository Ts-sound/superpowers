---
name: project-workflow
description: "How to manage overall project workflow and orchestrate skill execution. Make sure to use this skill whenever the user mentions workflow management, project progress, advancing to next stage, or needs to coordinate multiple skills. Also trigger when initializing new projects, starting new features, fixing bugs, or updating documentation. Works closely with brainstorming, project-structure, project-docs, writing-plans, project-task, executing-plans, and other skills."
---

# Project Workflow Management

## Overview

Manage overall project workflow and orchestrate skill execution across different stages. This skill provides structured workflow tracking, automatic stage advancement, and progress reporting for various project scenarios.

## Supported Scenarios

| Scenario | ID | Use Case |
|----------|-----|----------|
| Project Initialization | `project_init` | New project, repository setup |
| Feature Development | `feature_dev` | Adding new features, modules |
| Bug Fix | `bug_fix` | Fixing bugs, issue resolution |
| Documentation Update | `docs_update` | Design changes, doc sync |

## Workflow Definitions

### Project Initialization (`project_init`)

```
1. project-structure → 2. brainstorming → 3. project-docs → 4. writing-plans → 5. project-task
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Structure | project-structure | `src/`, `tests/`, `docs/`, `scripts/` |
| 2. Design | brainstorming | Design document |
| 3. Docs | project-docs | `docs/design/README.md` |
| 4. Plan | writing-plans | `docs/plan/YYYY-MM-DD-init-plan.md` |
| 5. Task | project-task | `docs/task/init.yaml` |

### Feature Development (`feature_dev`)

```
1. brainstorming → 2. project-docs → 3. writing-plans → 4. project-task → 5. executing-plans → 6. requesting-code-review → 7. finishing-a-development-branch
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Design | brainstorming | Feature design |
| 2. Docs | project-docs | `docs/design/<feature>/README.md` |
| 3. Plan | writing-plans | `docs/plan/YYYY-MM-DD-feature-plan.md` |
| 4. Task | project-task | `docs/task/<feature>.yaml` |
| 5. Execute | executing-plans | Code implementation |
| 6. Review | requesting-code-review | Code review report |
| 7. Complete | finishing-a-development-branch | Branch merged |

### Bug Fix (`bug_fix`)

```
1. systematic-debugging → 2. project-task → 3. executing-plans → 4. verification-before-completion
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Debug | systematic-debugging | Root cause analysis |
| 2. Task | project-task | `docs/task/bugfix-<id>.yaml` |
| 3. Execute | executing-plans | Bug fix code |
| 4. Verify | verification-before-completion | Verification report |

### Documentation Update (`docs_update`)

```
1. project-docs → 2. project-task
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Docs | project-docs | Updated design docs |
| 2. Task | project-task | `docs/task/docs-sync.yaml` |

## Directory Structure

```
docs/
└── workflow/
    ├── <name>.yaml          # Individual workflow state files
    └── README.md            # Workflow guide (optional)
```

## Workflow State Format

```yaml
scenario: "feature_dev"
project_name: "auth-feature"
created: "2024-01-01T00:00:00Z"
updated: "2024-01-01T00:00:00Z"

current_stage: 2                  # Current stage index (1-based)
status: "in_progress"             # active | completed | archived

stages:
  - id: 1
    name: "brainstorming"
    skill: "brainstorming"
    status: "completed"
    started_at: "2024-01-01T10:00:00Z"
    completed_at: "2024-01-01T11:00:00Z"
    output: "docs/plans/2024-01-01-auth-design.md"
    
  - id: 2
    name: "project-docs"
    skill: "project-docs"
    status: "completed"
    started_at: "2024-01-01T11:00:00Z"
    completed_at: "2024-01-01T12:00:00Z"
    output: "docs/design/auth/README.md"
    
  - id: 3
    name: "writing-plans"
    skill: "writing-plans"
    status: "in_progress"
    started_at: "2024-01-01T12:00:00Z"
    completed_at: null
    output: null
```

## Python Script: workflow_manager.py

### Location
`skills/project-workflow/scripts/workflow_manager.py`

### Commands

| Command | Description |
|---------|-------------|
| `init <scenario> <name>` | Initialize new workflow |
| `status [name]` | Show current/specified workflow status |
| `next` | Advance to next stage (auto-trigger skill) |
| `goto <stage-id>` | Jump to specified stage |
| `report` | Generate progress report for all workflows |
| `list` | List all active workflows |
| `archive <name>` | Archive completed workflow |

### Usage Examples

```bash
# Initialize new workflow
python workflow_manager.py init feature_dev auth-feature

# Show status
python workflow_manager.py status auth-feature

# Advance to next stage (auto-triggers next skill)
python workflow_manager.py next auth-feature

# Generate report
python workflow_manager.py report

# List active workflows
python workflow_manager.py list

# Archive completed workflow
python workflow_manager.py archive auth-feature
```

## Integration with Other Skills

### Skill Orchestration

**Workflow automatically triggers:**

| Stage | Triggered Skill | Action |
|-------|-----------------|--------|
| brainstorming | `brainstorming` | Design refinement |
| project-structure | `project-structure` | Project scaffolding |
| project-docs | `project-docs` | Design documentation |
| writing-plans | `writing-plans` | Implementation planning |
| project-task | `project-task` | Task creation |
| executing-plans | `executing-plans` | Code execution |
| systematic-debugging | `systematic-debugging` | Bug investigation |
| verification-before-completion | `verification-before-completion` | Fix verification |
| requesting-code-review | `requesting-code-review` | Code review |
| finishing-a-development-branch | `finishing-a-development-branch` | Branch completion |

### With project-task

**Relationship:**
- `project-workflow` manages **macro stages** (design → plan → task → execute)
- `project-task` manages **micro tasks** within each stage
- State files are separate:
  - Workflow: `docs/workflow/<name>.yaml`
  - Tasks: `docs/task/<name>.yaml`
- Scripts are separate:
  - Workflow: `workflow_manager.py`
  - Tasks: `task_manager.py`

## Commands Reference

### Initialize Workflow

```bash
python workflow_manager.py init <scenario> <name>
```

**Scenarios:** `project_init`, `feature_dev`, `bug_fix`, `docs_update`

### Advance Stage

```bash
python workflow_manager.py next <name>
```

Actions:
1. Mark current stage as `completed`
2. Mark next stage as `in_progress`
3. Auto-trigger the corresponding skill
4. Update state file

### Generate Report

```bash
python workflow_manager.py report
```

Output includes:
- All active workflows
- Completion percentages
- Current stage for each
- Overall progress summary

## Best Practices

1. **One workflow per feature** — Create separate workflow for each feature/bug
2. **Follow the sequence** — Stages are linear; complete each before advancing
3. **Auto-trigger enabled** — Let workflow_manager trigger skills automatically
4. **Archive when done** — Keep active workflows clean by archiving completed ones
5. **Check status frequently** — Use `status` command to track progress

## When to Use This Skill

- User says "start a new project" or "initialize workflow"
- User wants to "advance to next stage" or "what's next"
- Starting new feature development
- Fixing bugs with structured approach
- Checking overall project progress
- Coordinating multiple skill executions
