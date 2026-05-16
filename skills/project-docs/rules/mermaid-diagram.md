# Mermaid Diagram Rules

Mermaid 图表使用规范，按需调用。

## 图表类型选择

| 场景 | 图表类型 |
|------|----------|
| 架构概览 | `graph TD` 或 `flowchart TD` |
| 模块结构 | `graph LR` 或 `flowchart LR` |
| 数据流图 | `flowchart TB` |
| 类结构 | `classDiagram` |
| 时序/交互 | `sequenceDiagram` |
| 状态机 | `stateDiagram-v2` |
| 甘特图 | `gantt` |
| 饼图 | `pie` |
| 用户旅程 | `journey` |

## 数据流图要求

模块间数据流图必须标注：
- **消息类型**（如 `sensor_msgs::Imu`）
- **数据含义**（如 `IMU data`）

参考 `../rules/dataflow.md` 示例。

## 样式规范

- 使用 `classDef` 为不同节点类型定义样式
- 使用 `subgraph` 对相关节点进行分组
- 保持图表简洁，避免过度装饰

## 直接生成

Mermaid 图表**直接生成**，无需调用外部 skill。
