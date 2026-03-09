---
name: project-workflow
description: "Manage overall project workflow and orchestrate skill execution. Use for complex features, multi-file changes, or when user explicitly mentions workflow. For simple bugs and minor changes, use quick-fix mode instead."
---

# Project Workflow Management

## Overview

Manage overall project workflow and orchestrate skill execution across different stages. This skill provides structured workflow tracking, automatic stage advancement, and progress reporting for various project scenarios.

## When to Use This Skill

### ✅ Use Workflow For:
- **Complex features** requiring design, planning, and review
- **Multi-file refactoring** affecting architecture
- **Major bug fixes** requiring root cause analysis
- **User explicitly requests** workflow management

### ❌ Skip Workflow For (use quick-fix):
- **Simple typos** or documentation fixes
- **Single-line changes** (config updates, import fixes)
- **Minor refactors** (rename, move files)
- **Quick bug fixes** (obvious root cause, single file)

## Complexity Assessment

| Complexity | Indicators | Recommended Approach |
|------------|------------|---------------------|
| **Low** | "typo", "rename", "simple", "minor" | Quick-fix (skip workflow) |
| **Medium** | Standard feature/bug fixes | User choice |
| **High** | "architecture", "refactor", "migrate", "async" | Full workflow |

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
| `next <name>` | Advance to next stage (auto-trigger skill) |
| `goto <name> <stage-id>` | Jump to specified stage |
| `report` | Generate progress report for all workflows |
| `list` | List all active workflows |
| `archive <name>` | Archive completed workflow |
| `auto '<message>'` | **NEW**: Auto-detect scenario from message |
| `quick-fix '<description>'` | **NEW**: Skip workflow for simple changes |

### Usage Examples

```bash
# Auto-detect scenario (NEW)
python workflow_manager.py auto 'fix the wifi timeout bug'
# Output: Suggests workflow or quick-fix based on complexity

# Quick fix for simple changes (NEW)
python workflow_manager.py quick-fix 'update config timeout value'

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

### Automatic Skill Triggering

When advancing to the next stage with `next` command, the workflow manager:

1. Commits current stage output to git
2. Triggers the next skill automatically
3. Updates workflow state file

```
Stage Complete → Git Commit → Trigger Next Skill → Update State
```

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

## User Participation Points

Only the following stages require user confirmation:

| Stage | Participation | Confirmation Content |
|-------|---------------|---------------------|
| Stage 2: brainstorming | Design discussion | Architecture, modules, interface design |
| Stage 3: project-docs | Document review | Design document accuracy |

**Typical feedback example**: "modules 与 src 分层不对应" → Return to brainstorming to revise.

All other stages (project-structure, writing-plans, project-task) are **automatically executed**.

## Best Practices

1. **Assess complexity first** - Use `auto` command to get recommendation
2. **Quick-fix for simple changes** - Don't over-engineer minor fixes
3. **Full workflow for complex features** - Design → Plan → Execute → Review
4. **Archive when done** - Keep active workflows clean
5. **Check status frequently** - Use `status` or `report` commands

## Troubleshooting

### Q: When should I skip the workflow?

**A:** Skip workflow when:
- Change is obvious and localized (single file)
- Fix is a simple parameter/config update
- User explicitly wants quick iteration
- Change has minimal risk

### Q: What if I started workflow but realized it's too simple?

**A:** Use `archive <name>` to cancel, then use `quick-fix` for the actual change.

### Q: How do I know which scenario to use?

**A:** Use `auto '<message>'` to auto-detect, or:
- Fixing bugs → `bug_fix`
- Adding features → `feature_dev`
- Updating docs → `docs_update`
- New project → `project_init`
