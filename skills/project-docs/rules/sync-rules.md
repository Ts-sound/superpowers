# Document Sync Rules

文档同步规则，按需调用。

## 触发条件

以下操作完成后，必须检查并更新相关设计文档：

| 操作 | 检查内容 |
|------|----------|
| 新增功能 | 对应模块设计文档是否覆盖 |
| 缺陷修复 | 设计文档描述的准确性 |
| 模块重构 | 架构图、接口定义、依赖关系 |
| 技术栈变更 | Technical Decisions 与 Deployment 章节 |

## 同步检查流程

```
1. 识别变更的模块/文件
2. 查找对应的设计文档
3. 报告需要更新的内容
4. 确认后自动更新
```

## 工作流集成

```
brainstorming → project-docs (docs/design/) → writing-plans (docs/plans/) → implementation
```

- `project-docs`：负责 **是什么**（设计、架构）
- `writing-plans`：负责 **怎么做**（实施任务）
