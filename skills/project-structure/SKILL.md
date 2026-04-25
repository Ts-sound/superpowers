---
name: project-structure
description: "How to manage project engineering structure. Make sure to use this skill whenever the user mentions project structure, directory layout, scaffolding a new project, organizing code, setting up repository structure, creating standard folders like src/, tests/, docs/, scripts/, or needs help with project initialization, configuration files, or build scripts."
---

# Project Structure Management

## Overview

Help users create and manage standardized project engineering structures. This skill provides templates and workflows for setting up well-organized code repositories with proper directory layouts, configuration files, and automation scripts.

## Standard Directory Structure

```
project-name/
├── src/                        # Source code
├── tests/                      # Test code (mirrors src structure)
├── docs/                       # Documentation
│   ├── design/                # Design documents
│   ├── plans/                 # Implementation plans
│   └── requirements.md        # Requirements
├── scripts/                    # Automation scripts
├── config/                     # Configuration files
├── log/                        # Log files (optional)
├── .github/workflows/          # GitHub Actions CI/CD
├── README.md                   # Primary README (English)
├── README.zh.md                # Chinese README (optional)
├── AGENTS.md                   # Project conventions for AI
├── pyproject.toml              # Modern Python config (or language-specific)
├── requirements.txt            # Dependencies
├── .gitignore
└── LICENSE
```

## Supported Languages

| Language | Config Files | Test Framework | Template Dir |
|----------|--------------|----------------|--------------|
| Python | pyproject.toml, requirements.txt | pytest | `templates/python/` |
| JavaScript/TypeScript | package.json, tsconfig.json | jest | `templates/javascript/` |
| Java | pom.xml | junit | `templates/java/` |
| Go | go.mod | go test | `templates/go/` |

## Workflow

### Project Type Confirmation

Before creating structure, confirm project details:

**Questions to ask:**
1. **Project type**: python/micropython/nodejs/java/go/rust/embedded/...
2. **Build method**: compiled/interpreted/mixed
3. **CI/CD needs**: Use `project-ci-cd` skill to assess

### Generate Structure

1. Create directories based on project type
2. Copy templates from `templates/<language>/`
3. Create automation scripts from `templates/scripts/`
4. Create common files from `templates/common/`

### Template Files

| Template | Purpose | Location |
|----------|---------|----------|
| pyproject.toml | Python project config | `templates/python/pyproject.toml` |
| requirements.txt | Python dependencies | `templates/python/requirements.txt` |
| README.md | Project documentation | `templates/common/README.md` |
| README.zh.md | Chinese README | `templates/common/README.zh.md` |
| AGENTS.md | AI conventions | `templates/common/AGENTS.md` |
| setup.sh | Unix setup script | `templates/scripts/setup.sh` |
| setup-venv.ps1 | Windows venv script | `templates/scripts/setup-venv.ps1` |
| test.sh | Test script | `templates/scripts/test.sh` |
| build.sh | Build script | `templates/scripts/build.sh` |
| ci.yml | GitHub Actions | `templates/github-actions/ci.yml` |

**Use templates directly** - don't inline code in SKILL.md.

### Fake File Marking

For features not needed by the project type, create placeholder files with SKIP comments:

```bash
# scripts/ci.sh
# SKIP: not needed for micropython project - deployment via direct flash
```

**Fake files should be committed to git** to maintain structure completeness.

## Commands

### Create New Project

1. Ask for project name and language
2. Generate directory structure
3. Copy language-specific config templates
4. Copy script templates
5. Copy common templates (README, AGENTS, LICENSE)
6. Set up CI/CD or create SKIP placeholder

### Check Existing Structure

1. Scan current directory
2. Check for required directories (src/, tests/, docs/, scripts/)
3. Verify config files exist
4. Report missing or recommended additions

## Language-Specific Structures

### Python (Layered Architecture)

```
src/
├── models/        # Data models (@dataclass)
├── services/      # Business logic
├── repositories/  # Data access (I/O)
├── ui/            # User interface
└── utils/         # Utilities

tests/
├── models/
├── services/
├── repositories/
└── conftest.py    # Shared fixtures
```

**Files:** See `templates/python/` directory.

### JavaScript/TypeScript

```
src/
├── index.ts
└── index.js

tests/
└── index.test.ts
```

**Files:** See `templates/javascript/` directory.

### Java

```
src/
├── main/java/
└── test/java/
```

**Files:** See `templates/java/` directory.

### Go

```
cmd/<app-name>/main.go
pkg/
internal/
tests/
```

**Files:** See `templates/go/` directory.

## Best Practices

1. **Consistent naming** — lowercase with hyphens for directories
2. **Plural forms** — `tests/`, `docs/`, `scripts/` (not singular)
3. **Separation of concerns** — Keep source, tests, docs separate
4. **Automation first** — Always include setup/test/build scripts
5. **CI/CD ready** — Use `project-ci-cd` skill to determine and configure
6. **Fake files committed** — SKIP placeholders in git
7. **pyproject.toml preferred** — Modern Python config over setup.py
8. **Bilingual README** — README.md + README.zh.md with language switch
9. **AGENTS.md** — Project conventions for AI agents
10. **Mirrored test structure** — tests/ mirrors src/

## When to Use This Skill

- User wants to "create a new project" or "set up a repository"
- User asks about "project structure" or "directory layout"
- User needs to "organize code" or "scaffold a project"
- User mentions standard folders like src/, tests/, docs/
- User needs help with project initialization or configuration