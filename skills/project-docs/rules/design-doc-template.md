# Design Document Template Rules

设计文档模板规范，按需调用。

## 总体设计文档 (`docs/design/README.md`)

必须包含以下章节：

| 章节 | 说明 | 推荐图表 |
|------|------|----------|
| Overview | 系统定位与核心价值 | — |
| Architecture | 高层架构图 | `graph TD` / `flowchart TD` |
| Modules | 模块清单与链接（表格） | — |
| Technical Decisions | 技术决策与备选方案对比 | — |
| Data Model | 核心数据结构 | `classDiagram` |
| API Design | 接口定义（表格） | — |
| Security Considerations | 安全考量 | — |
| Deployment | 部署架构 | `graph LR` / `flowchart LR` |

## 模块设计文档 (`docs/design/<module>/README.md`)

必须包含以下章节：

| 章节 | 说明 | 推荐图表 |
|------|------|----------|
| Overview | 模块职责与非职责 | — |
| Architecture | 组件图 | `graph TD` |
| Interfaces | 公开 API 与依赖关系 | — |
| Key Sequences | 关键交互流程 | `sequenceDiagram` |
| State Machine | 状态机（如适用） | `stateDiagram-v2` |
| Error Handling | 错误类型与恢复策略 | — |
| Testing Strategy | 测试策略 | — |
| Performance Considerations | 性能考量 | — |
| Future Improvements | 已知限制与改进计划 | — |

## 模板文件

- 总体设计：`templates/design-overview.md`
- 模块设计：`templates/module-design.md`

创建文档时**直接使用模板**，不要在 SKILL.md 中内联模板代码。
