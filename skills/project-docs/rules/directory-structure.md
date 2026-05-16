# Directory Structure Rules

项目文档目录结构规范，按需调用。

## 目录结构

```
docs/
├── design/                     # 设计文档
│   ├── README.md               # 系统总体设计
│   └── <module>/README.md      # 模块设计
├── plans/                      # 实施计划（writing-plans）
│   └── YYYY-MM-DD-<topic>.md
├── requirements.md             # 需求文档
└── terminology.md              # 术语定义

根目录文档：
├── README.md                   # 主文档（英文）
├── README.zh.md                # 中文文档（可选）
└── AGENTS.md                   # AI 协作规范
```

## 设计 vs 计划

- `docs/design/` — **是什么**（架构、设计决策）
- `docs/plans/` — **怎么做**（实施步骤、任务分解）

两者必须分离，不可混写。

## 模块命名

- 使用短名：`auth/` 而非 `authentication/`
- 使用小写+短横线：`api-gateway/` 而非 `APIGateway/`
