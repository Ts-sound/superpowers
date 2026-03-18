---
name: project-workflow
description: "Manage overall project workflow and orchestrate skill execution. Use for complex features, multi-file changes, or when user explicitly mentions workflow. For simple bugs and minor changes, use quick-fix mode instead."
---

# Project Workflow Management

## Overview

Manage overall project workflow and orchestrate skill execution across different stages. This skill provides structured workflow tracking, automatic stage advancement, and progress reporting for various project scenarios.

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

## Agent Roles

The workflow orchestrates the following AI agents:

| Agent | Role | When to Use |
|-------|------|-------------|
| `@architect` | System design, architecture, technical decisions | Design phase, technical planning |
| `@explorer` | Code search, evidence collection | Understanding codebase, finding related code |
| `@librarian` | Best practices, external research | Learning patterns, API documentation |
| `@plan` | Task breakdown, Todo creation | Planning phase |
| `@build` | Code implementation | Implementation phase |
| `@reviewer` | Code review, quality check | After implementation |
| `@tester` | Test writing, verification | Testing phase |
| `@documenter` | Documentation writing | Documentation phase |
| `@frontend-dev` | Frontend implementation | UI/Component development |

## Workflow Definitions

### Five-Step Foundation Workflow (适用于所有任务)

```
1.方案设计 → 2.收集证据 → 3.明确边界 → 4.逐步实现 → 5.代码审查
```

| Step | Agent | Output |
|------|-------|--------|
| 1. 方案设计 | @architect | Architecture, DB schema, API design |
| 2. 收集证据 | @explorer, @librarian | Existing code, best practices |
| 3. 明确边界 | @plan | Todo list, constraints |
| 4. 逐步实现 | @build | Implementation |
| 5. 代码审查 | @reviewer | Review report |

### Project Initialization (`project_init`)

```
1. project-structure → 2. brainstorming → 3. project-docs → 4. writing-plans → 5. executing-plans
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Structure | project-structure | `src/`, `tests/`, `docs/`, `scripts/` |
| 2. Design | brainstorming | Design document |
| 3. Docs | project-docs | `docs/design/README.md` |
| 4. Plan | writing-plans | `docs/plan/YYYY-MM-DD-init-plan.md` |
| 5. Execute | executing-plans | Code implementation |

### Feature Development (`feature_dev`)

```
1. brainstorming → 2. project-docs → 3. writing-plans → 4. executing-plans → 5. requesting-code-review → 6. finishing-a-development-branch
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Design | brainstorming | Feature design |
| 2. Docs | project-docs | `docs/design/<feature>/README.md` |
| 3. Plan | writing-plans | `docs/plan/YYYY-MM-DD-feature-plan.md` |
| 4. Execute | executing-plans | Code implementation |
| 5. Review | requesting-code-review | Code review report |
| 6. Complete | finishing-a-development-branch | Branch merged |

**任务管理**: 使用 TodoWrite 工具管理任务执行进度，不需要创建独立任务文件。

**设计文档更新**: 
- 在 `executing-plans` 阶段完成后，检查实现是否与设计文档一致
- 如有偏差，调用 `project-docs` 更新设计文档
- 更新 `README.md` 反映新功能

**完成检查清单**:
- [ ] 代码实现与设计文档一致
- [ ] 设计文档已更新反映实际实现
- [ ] README.md 已更新（如有新功能/配置）
- [ ] 所有测试通过

### Bug Fix (`bug_fix`)

```
1. systematic-debugging → 2. executing-plans → 3. verification-before-completion
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Debug | systematic-debugging | Root cause analysis |
| 2. Execute | executing-plans | Bug fix code |
| 3. Verify | verification-before-completion | Verification report |

**任务管理**: 使用 TodoWrite 工具管理修复步骤。

### Documentation Update (`docs_update`)

```
1. project-docs → 2. executing-plans
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Docs | project-docs | Updated design docs |
| 2. Execute | executing-plans | Documentation changes |

**任务管理**: 使用 TodoWrite 工具管理文档更新任务。

### Code Refactoring (`refactor`)

```
1. brainstorming → 2. executing-plans → 3. verification-before-completion → 4. requesting-code-review → 5. project-docs
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Analysis | brainstorming | Refactoring plan, risk assessment |
| 2. Execute | executing-plans | Refactored code |
| 3. Verify | verification-before-completion | Tests pass, performance comparison |
| 4. Review | requesting-code-review | Code quality review |
| 5. Docs | project-docs | Updated design docs |

**任务管理**: 使用 TodoWrite 工具管理重构任务，每个模块或功能点一个任务。

**设计文档更新**: 
- 重构完成后必须调用 `project-docs` 更新设计文档
- 确保文档反映新的代码结构和模块划分
- 更新相关架构图和流程图

**完成检查清单**:
- [ ] 重构后所有测试通过
- [ ] 性能没有回退（或有提升）
- [ ] 设计文档已更新反映新结构
- [ ] 模块文档已更新

### Technical Research (`tech_research`)

```
1. brainstorming → 2. executing-plans → 3. project-docs
```

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Research | brainstorming | Option analysis, recommendation |
| 2. Execute | executing-plans | Prototype implementation |
| 3. Docs | project-docs | Research report |

**任务管理**: 使用 TodoWrite 工具管理研究任务。

**研究文档输出**:
- 必须创建调查报告 `docs/research/<topic>.md`
- 包含：技术方案对比、优缺点分析、推荐方案、实施建议
- 如有 POC 代码，说明代码位置和测试结果

**文档结构建议**:
```markdown
# <主题> 调研报告

## 背景
## 候选方案
## 对比分析
## 推荐方案
## 实施计划
## 参考资料
```

## Directory Structure

```
project-root/
├── AGENTS.md                  # Project conventions (recommended)
├── docs/
│   ├── workflow/
│   │   ├── <name>.yaml        # Individual workflow state files
│   │   └── README.md          # Workflow guide (optional)
│   ├── design/                # Design documents
│   └── plan/                  # Implementation plans
└── skills/project-workflow/
    ├── scripts/
    │   └── workflow_manager.py
    ├── templates/
    │   ├── workflow-state.yaml
    │   └── AGENTS.md          # AGENTS.md template
    └── evals/
        └── evals.json
```

**注意**: 任务管理使用 TodoWrite 工具，不需要创建 `docs/task/` 目录。

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
| executing-plans | `executing-plans` | Code execution |
| systematic-debugging | `systematic-debugging` | Bug investigation |
| verification-before-completion | `verification-before-completion` | Fix verification |
| requesting-code-review | `requesting-code-review` | Code review |
| finishing-a-development-branch | `finishing-a-development-branch` | Branch completion |

**任务管理**: 使用 TodoWrite 工具管理任务执行进度。

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
| Stage 1: brainstorming | Design discussion | Architecture, modules, interface design |
| Stage 2: project-docs | Document review | Design document accuracy |

**Typical feedback example**: "modules 与 src 分层不对应" → Return to brainstorming to revise.

All other stages (project-structure, writing-plans, executing-plans) are **automatically executed**.

**任务管理**: 使用 TodoWrite 工具跟踪任务进度，无需用户确认。

## Best Practices

### 1. Think First, Code Later (先思考再动手)

Always start with design:
```
@architect 设计一个用户认证系统，要求：
1. 支持邮箱和手机号登录
2. 支持 OAuth（Google、GitHub）
3. 包含 JWT 令牌管理
4. 考虑安全性和可扩展性
```

### 2. Small Steps, Fast Iteration (小步快跑)

Break down tasks and verify each step:
```
@plan 制定详细的实施计划，每步都可独立测试

@build 按计划实现，每完成一步：
1. 运行测试
2. 让 @reviewer 审查
3. 确认无误后继续下一步
```

### 3. Continuous Review (持续审查)

Never skip code review:
```
@reviewer 审查代码，重点检查：
1. 安全性：SQL 注入、XSS、CSRF
2. 性能：数据库查询优化、缓存策略
3. 错误处理：边界条件、异常情况
4. 代码质量：可读性、可维护性
```

### 4. Clear Boundaries (明确边界)

Define task constraints clearly:
```
@plan 制定实施计划，注意：
1. 不要修改现有的用户表结构
2. 保持与现有 API 的兼容性
3. 添加完整的错误处理
4. 每个步骤都要可以独立测试
```

### 5. Use AGENTS.md for Project Standards

Create `AGENTS.md` in project root to remember project conventions:

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

### 6. Todo-Driven Development

```
@plan 为这个功能创建详细的 Todo 列表

@build 逐项完成，每完成一项：
1. 标记为完成
2. 运行测试
3. 提交代码
4. 继续下一项
```

### 7. Parallel Development

```
同时进行：
1. @build 实现后端 API
2. @frontend-dev 实现前端组件
3. @documenter 编写 API 文档

完成后集成测试
```

### 8. Incremental Commits

```
@build 实现功能，每完成一个小步骤就提交：

git commit -m "feat: add user model"
git commit -m "feat: add user controller"
git commit -m "feat: add user routes"
git commit -m "test: add user tests"
```

## Common Pitfalls

### Pitfall 1: One-Shot Large Tasks

❌ Wrong:
```
帮我实现一个完整的电商系统
```

✅ Right:
```
第一步：设计电商系统的架构
第二步：实现用户模块
第三步：实现商品模块
...
```

### Pitfall 2: No Clear Boundaries

❌ Wrong:
```
优化这个模块的性能
```

✅ Right:
```
优化这个模块的性能，要求：
1. 不要修改 API 接口
2. 保持向后兼容
3. 添加性能测试
4. 目标：响应时间 < 100ms
```

### Pitfall 3: Skip Code Review

❌ Wrong:
```
实现功能 → 直接提交
```

✅ Right:
```
实现功能 → 代码审查 → 修复问题 → 提交
```

### Pitfall 4: Ignore Testing

❌ Wrong:
```
功能实现完就算完成
```

✅ Right:
```
功能实现 → 单元测试 → 集成测试 → 手动测试
```

## Scenario-Based Workflows

### Scenario 1: New Feature Development

```text
# Phase 1: Requirements Analysis
我要开发一个博客评论功能，支持：
- 用户评论和回复
- 点赞和举报
- Markdown 格式
- 实时通知

@architect 分析需求并设计方案

# Phase 2: Research
@explorer 搜索项目中：
- 现有的评论相关代码
- 通知系统的实现
- Markdown 渲染器的使用

@librarian 查找：
- 评论系统的最佳实践
- 防止垃圾评论的方法
- 实时通知的实现方案

# Phase 3: Design Confirmation
基于调研结果，@architect 更新设计方案

# Phase 4: Task Breakdown
@plan 制定详细的实施计划，包括：
1. 数据库表设计
2. API 接口实现
3. 前端组件开发
4. 实时通知集成
5. 测试用例编写

# Phase 5: Implementation
@build 按计划实现，每完成一步：
1. 运行测试
2. 让 @reviewer 审查
3. 确认无误后继续下一步

# Phase 6: Integration Testing
@tester 编写集成测试，覆盖：
- 正常流程
- 边界条件
- 异常情况

# Phase 7: Documentation
@documenter 编写：
- API 文档
- 使用说明
- 部署指南
```

### Scenario 2: Bug Fix

```text
# Problem Description
用户登录时偶尔会失败，错误信息：
"Token validation failed"

复现步骤：
1. 用户登录
2. 等待 5 分钟
3. 刷新页面
4. 出现错误

# Step 1: Problem Localization
@explorer 搜索所有与 Token 验证相关的代码

@architect 分析可能的原因：
- Token 过期时间设置
- 时区问题
- 缓存问题
- 并发问题

# Step 2: Reproduce
@build 编写测试用例复现问题

# Step 3: Root Cause Analysis
基于测试结果，@architect 确定根本原因

# Step 4: Fix Implementation
@build 实施修复方案

# Step 5: Regression Testing
@tester 运行所有相关测试，确保：
- Bug 已修复
- 没有引入新问题
- 边界条件都正常

# Step 6: Code Review
@reviewer 审查修复代码，确认：
- 修复方案合理
- 没有遗漏的场景
- 代码质量符合标准
```

### Scenario 3: Code Refactoring

```text
# Refactoring Goal
auth 模块代码混乱，需要重构

要求：
1. 拆分成更小的模块
2. 提高可测试性
3. 保持 API 兼容性

# Step 1: Current State Analysis
@explorer 分析 auth 模块：
- 代码结构
- 依赖关系
- 调用方式

@architect 评估：
- 存在的问题
- 重构风险
- 重构方案

# Step 2: Planning
@plan 制定重构计划：
1. 添加测试覆盖（确保重构前有测试）
2. 提取公共逻辑
3. 拆分大函数
4. 优化数据结构
5. 更新文档

每一步都要：
- 保持测试通过
- 保持功能不变
- 可以独立提交

# Step 3: Incremental Refactoring
@build 按计划重构，每完成一步：
1. 运行所有测试
2. 手动验证核心功能
3. 提交代码

# Step 4: Performance Testing
@tester 对比重构前后的性能

# Step 5: Code Review
@reviewer 审查重构后的代码：
- 代码质量是否提升
- 是否引入新问题
- 是否达到重构目标
```

### Scenario 4: Technology Selection

```text
# Requirement
项目需要选择一个状态管理库

候选方案：
- Redux
- MobX
- Zustand
- Jotai

# Step 1: Requirements Analysis
@architect 分析项目需求：
- 状态复杂度
- 团队技术栈
- 性能要求
- 学习成本

# Step 2: Research
@librarian 调研每个方案：
- 核心特性
- 优缺点
- 适用场景
- 社区活跃度
- 学习资源

# Step 3: Comparison
@architect 对比分析，给出推荐

# Step 4: POC
@build 用推荐的方案实现一个小原型

# Step 5: Team Decision
基于原型和分析报告，团队讨论决策
```

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
- Refactoring code → `refactor`
- Technology research → `tech_research`

### Q: How do I use agents effectively?

**A:** 
- Start with `@architect` for design
- Use `@explorer` to find existing code
- Use `@plan` for task breakdown
- Use `@build` for implementation
- Always use `@reviewer` before completion

## Summary

A good workflow should:

1. **Think first, code later** - Design → Evidence → Implementation
2. **Small steps, fast iteration** - Break down → Implement → Verify
3. **Continuous review** - Code review → Test → Improve
4. **Clear boundaries** - Defined scope → Controlled risk
5. **Team collaboration** - Unified config → Unified standards → Unified process
