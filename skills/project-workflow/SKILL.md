---
name: project-workflow
description: "Manage overall project workflow and orchestrate skill execution. Use for complex features, multi-file changes, or when user explicitly mentions workflow. For simple bugs and minor changes, use quick-fix mode instead."
---

# Project Workflow Management

## Overview

Project workflow orchestrates skill execution across stages, providing structured tracking and progress reporting.

### Workflow Scenarios

| Scenario | Flow |
|----------|------|
| `project_init` | 1. brainstorming → 2. project-structure → 3. project-docs → 4. writing-plans → 5. [execute] → 6. project-docs |
| `feature_dev` | 1. brainstorming → 2. project-docs → 3. writing-plans → 4. [execute] → 5. requesting-code-review → 6. finishing-a-development-branch |
| `bug_fix` | 1. brainstorming → 2. project-docs → 3. systematic-debugging → 4. [execute] → 5. verification-before-completion |
| `docs_update` | 1. brainstorming → 2. project-docs → 3. [execute] |
| `refactor` | 1. analyze existing code → 2. project_init → 3. feature_dev |
| `tech_research` | 1. brainstorming → 2. [execute] → 3. project-docs |

**Workflow principles:**
- **First stage:** `brainstorming` — User participation point
- **Middle stages:** Automated execution
- **Final stage:** `project-docs` — Code-doc alignment check

**`[execute]`** = Choose between `executing-plans` or `subagent-driven-development` (see below)

### Parallel Development

Use `dispatching-parallel-agents` for multiple independent tasks:

| Use Case | Condition |
|----------|-----------|
| Multiple modules | Different subsystems |
| Multiple bugs | Different root causes, no shared state |
| Multiple features | No dependencies |

**Requirements:** No shared state, no sequential dependencies, each task independent.

### Execution Mode Selection

| Mode | Skill | Session | Review | Best For |
|------|-------|---------|--------|----------|
| Parallel | `executing-plans` | New worktree | After all tasks | Major features, long work |
| Same | `subagent-driven-development` | Current | After each task | Independent tasks, quick fixes |

**Decision:**
- Tasks independent + stay current session → `subagent-driven-development`
- Tasks need isolation + context switch → `executing-plans`

## Core Philosophy: From Conversation to Orchestration

Traditional AI programming mindset:
```
I ask → AI answers → I ask again → AI answers again
```

Opencode workflow mindset:
```
I give instruction → AI breaks down tasks → Multiple Agents collaborate → Automatically complete
```

When you master "orchestration" rather than "conversation", you become an AI team manager rather than an AI user.

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
| Code Refactoring | `refactor` | Restructuring existing code |
| Technical Research | `tech_research` | Technology selection, POC |

## Workflow Definitions

### Project Initialization (`project_init`)

| Stage | Skill | Output |
|-------|-------|--------|
| 1 | brainstorming | Project design |
| 2 | project-structure | `src/`, `tests/`, `docs/`, `scripts/` |
| 3 | project-docs | `docs/design/README.md` |
| 4 | writing-plans | `docs/plans/YYYY-MM-DD-init-plan.md` |
| 5 | [execute] | Code implementation |
| 6 | project-docs | Code-doc alignment check |

**[execute]** = `executing-plans` or `subagent-driven-development` (see Execution Mode Selection above)

### Feature Development (`feature_dev`)

| Stage | Skill | Output |
|-------|-------|--------|
| 1 | brainstorming | Feature design |
| 2 | project-docs | `docs/design/<feature>/README.md` |
| 3 | writing-plans | `docs/plans/YYYY-MM-DD-feature-plan.md` |
| 4 | [execute] | Code implementation |
| 5 | requesting-code-review | Code review report |
| 6 | finishing-a-development-branch | Branch merged |

### Bug Fix (`bug_fix`)

| Stage | Skill | Output |
|-------|-------|--------|
| 1 | brainstorming | Problem analysis (design issue vs code issue) |
| 2 | systematic-debugging | Root cause analysis |
| 3 | [execute] | Bug fix code |
| 4 | verification-before-completion | Verification report |

**Issue classification:**
- Design issue: Design doc update required
- Code issue: Verify existing doc still correct

### Documentation Update (`docs_update`)

| Stage | Skill | Output |
|-------|-------|--------|
| 1 | brainstorming | Update scope definition |
| 2 | project-docs | Updated design docs |
| 3 | [execute] | Documentation changes |

### Code Refactoring (`refactor`)

| Stage | Skill | Output |
|-------|-------|--------|
| 1 | brainstorming | Refactoring analysis |
| 2 | [execute] | Refactored code |
| 3 | verification-before-completion | Tests pass verification |
| 4 | requesting-code-review | Code quality review |
| 5 | project-docs | Updated design docs |

### Technical Research (`tech_research`)

| Stage | Skill | Output |
|-------|-------|--------|
| 1 | brainstorming | Option analysis, recommendation |
| 2 | [execute] | Prototype implementation |
| 3 | project-docs | Research report (`docs/research/<topic>.md`) |


## Integration with Other Skills

Workflow stages automatically trigger corresponding skills:

| Stage | Skill | Purpose |
|-------|-------|---------|
| Design phase | `brainstorming` | Design refinement with user participation |
| Structure phase | `project-structure` | Project scaffolding |
| Docs phase | `project-docs` | Design documentation sync |
| Planning phase | `writing-plans` | Implementation planning |
| Execution phase | `executing-plans` / `subagent-driven-development` | Code execution |
| Debug phase | `systematic-debugging` | Root cause analysis |
| Review phase | `requesting-code-review` | Code quality check |
| Completion phase | `finishing-a-development-branch` | Branch merge and cleanup |
| Verification phase | `verification-before-completion` | Fix verification |

**Skill invocation:**
- Use `skill` tool to load skill content
- Follow skill instructions exactly
- Complete skill checklist before advancing

## Best Practices

### Think First, Code Later

Always start with design. Use `brainstorming` skill to:
- Understand requirements
- Explore approaches
- Present design for approval

### Small Steps, Fast Iteration

Break down tasks. Use `writing-plans` skill to:
- Create detailed task list
- Define clear boundaries
- Enable independent testing

### Continuous Review

Never skip review. Use `requesting-code-review` skill before completion:
- Check implementation vs design
- Verify tests pass
- Ensure code quality

### Clear Boundaries

Define constraints clearly:
- What NOT to modify
- API compatibility requirements
- Error handling expectations

### Use AGENTS.md for Project Standards

Create `AGENTS.md` in project root:

```markdown
# 项目规范

## 技术栈
- 前端：React 18 + TypeScript + Vite
- 后端：Node.js + Express + PostgreSQL
- 部署：Docker + AWS

## 编码规范
- 使用 ESLint + Prettier
- 组件使用函数式 + Hooks
- 状态管理使用 Zustand
- API 调用使用 React Query

## 目录结构
- `/src/components` - 可复用组件
- `/src/features` - 功能模块
- `/src/hooks` - 自定义 Hooks
- `/src/utils` - 工具函数

## 命名规范
- 组件：PascalCase
- 函数：camelCase
- 常量：UPPER_SNAKE_CASE
- 文件：kebab-case
```

## Common Pitfalls

| Pitfall | Wrong | Right |
|---------|-------|-------|
| One-shot large tasks | "帮我实现一个完整的电商系统" | Break into phases: design → modules → integration |
| No clear boundaries | "优化这个模块的性能" | Define constraints: no API changes, compatibility, tests |
| Skip code review | 实现 → 直接提交 | 实现 → 审查 → 修复 → 提交 |
| Ignore testing | 功能实现完就算完成 | 实现 → 单元测试 → 集成测试 → 手动测试 |

## Troubleshooting

### Q: When should I skip workflow?

Skip workflow when:
- Change is obvious and localized (single file)
- Fix is a simple parameter/config update
- User explicitly wants quick iteration
- Change has minimal risk

### Q: What if I started workflow but realized it's too simple?

Cancel workflow and use quick-fix for the actual change.

### Q: How do I know which scenario to use?

| Task Type | Scenario |
|-----------|----------|
| Fixing bugs | `bug_fix` |
| Adding features | `feature_dev` |
| Updating docs | `docs_update` |
| New project | `project_init` |
| Refactoring code | `refactor` |
| Technology research | `tech_research` |

## Summary

Good workflow principles:

1. **Think first, code later** - Design → Evidence → Implementation
2. **Small steps, fast iteration** - Break down → Implement → Verify
3. **Continuous review** - Review → Test → Improve
4. **Clear boundaries** - Defined scope → Controlled risk
5. **User participation** - First stage (brainstorming) + Final review
