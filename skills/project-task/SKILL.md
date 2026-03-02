---
name: project-task
description: "How to manage task lists and execute them automatically. Make sure to use this skill whenever the user mentions task management, task lists, executing tasks, tracking progress, or needs to organize docs/task/ directory. Also trigger when converting plans from docs/plan/ to executable tasks, or when checking task progress. Works closely with writing-plans, project-docs, and project-structure skills."
---

# Task List Management

## Overview

Manage task lists stored in `docs/task/[name].yaml` and execute tasks automatically with dependency management. This skill provides structured task tracking, automatic execution, and progress reporting.

## Directory Structure

```
docs/
└── task/
    ├── [name].yaml          # Task list files
    └── README.md            # Task management guide (optional)
```

## Task YAML Format

```yaml
name: "Project Name"
description: "Project description"
created: "2024-01-01"
updated: "2024-01-02"

tasks:
  - id: 1
    name: "Task name"
    description: "Detailed task description"
    status: "pending"        # pending | in_progress | completed | blocked
    priority: "high"         # low | medium | high
    created: "2024-01-01"
    started: null            # Auto-recorded start time
    completed: null          # Auto-recorded completion time
    dependencies: []         # List of dependent task IDs
    notes: []                # Execution notes
```

## Task Status Flow

```
pending → in_progress → completed
    ↓         ↓
 blocked ← (dependency check)
```

## Workflow

### Creating Task Lists

1. **Understand scope** — Ask about project/feature being tracked
2. **Check existing plans** — Look for `docs/plan/` files to convert
3. **Create structure** — Set up `docs/task/` if needed
4. **Generate tasks** — Create task list from plan or user input
5. **Validate** — Ensure tasks are hour-level granularity

### Executing Tasks

1. **Load task file** — Read `docs/task/[name].yaml`
2. **Check dependencies** — Verify prerequisite tasks are complete
3. **Execute in order** — Run tasks sequentially via Python script
4. **Update status** — Mark `pending` → `in_progress` → `completed`
5. **Record timestamps** — Auto-log started/completed times
6. **Report progress** — Generate completion summary

### Converting Plans to Tasks

1. **Read plan file** — Load `docs/plan/YYYY-MM-DD-topic-plan.md`
2. **Extract tasks** — Parse implementation steps from plan
3. **Create task file** — Generate `docs/task/[topic].yaml`
4. **Set dependencies** — Link related tasks
5. **Validate** — Confirm task granularity (hour-level)

## Integration with Other Skills

### With writing-plans

**Flow:**
```
writing-plans → creates docs/plan/YYYY-MM-DD-topic-plan.md
    ↓
project-task → converts plan → docs/task/topic.yaml
    ↓
task_manager.py → executes tasks automatically
```

**Conversion process:**
- Extract implementation steps from plan
- Convert each step to hour-level task
- Preserve task dependencies from plan structure
- Maintain traceability (plan → task mapping)

### With project-docs

- Both use `docs/` directory structure
- Task files live in `docs/task/`
- Design docs live in `docs/design/`
- Plan docs live in `docs/plan/`

### With project-structure

- Uses standard `docs/` directory
- Follows project structure conventions

## Python Script: task_manager.py

### Location
`skills/project-task/scripts/task_manager.py`

### Commands

| Command | Description |
|---------|-------------|
| `create <name>` | Create new task list |
| `add <file> <task>` | Add task to list |
| `run <file>` | Execute tasks automatically |
| `status <file>` | Show task status |
| `report` | Generate progress report |
| `convert <plan-file>` | Convert plan to tasks |

### Usage Examples

```bash
# Create new task list
python task_manager.py create auth

# Add task
python task_manager.py add docs/task/auth.yaml "Implement login API"

# Execute tasks
python task_manager.py run docs/task/auth.yaml

# Check status
python task_manager.py status docs/task/auth.yaml

# Generate report
python task_manager.py report

# Convert plan to tasks
python task_manager.py convert docs/plan/2024-01-01-auth-plan.md
```

## Task Granularity

Tasks should be **hour-level** units:

**Good (hour-level):**
- "Implement user login API endpoint" (~2 hours)
- "Write unit tests for auth module" (~1 hour)
- "Update database schema for user table" (~1 hour)

**Too large:**
- "Implement authentication system" (multiple days)
- "Build entire API" (multiple days)

**Too small:**
- "Create file" (minutes)
- "Add import statement" (minutes)

## Best Practices

1. **Hour-level tasks** — Each task should take 1-4 hours
2. **Clear dependencies** — Specify task prerequisites explicitly
3. **Descriptive names** — Task name should indicate what "done" looks like
4. **Auto-timestamps** — Let script record start/complete times
5. **Regular updates** — Run tasks frequently to maintain momentum

## When to Use This Skill

- User says "create task list" or "manage tasks"
- User wants to "track progress" or "execute tasks"
- Converting plans from `docs/plan/` to executable tasks
- Running automated task execution
- Checking task completion status
- Generating progress reports
