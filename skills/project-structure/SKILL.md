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
├── tests/                      # Test code
├── docs/                       # Documentation
├── scripts/                    # Automation scripts
│   ├── setup.sh               # Environment setup
│   ├── test.sh                # Automated testing
│   └── build.sh               # Build automation
├── config/                     # Configuration files
├── data/                       # Data files (optional)
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD
├── README.md
├── .gitignore
└── LICENSE
```

## Supported Languages

| Language | Config Files | Test Framework |
|----------|--------------|----------------|
| Python | requirements.txt, setup.py, pyproject.toml | pytest |
| JavaScript/TypeScript | package.json, tsconfig.json | jest |
| Java | pom.xml | junit |
| Go | go.mod | go test |

## Workflow

### Project Type Confirmation

Before creating structure, confirm project details:

**Questions to ask:**
1. **Project type**: python/micropython/nodejs/java/go/rust/embedded/...
2. **Build method**: compiled/interpreted/mixed
3. **CI/CD needs**: Does this project need CI/CD configuration?

### Generate Structure

1. Create directories based on project type
2. Generate configuration files
3. Create automation scripts

### Fake File Marking

For features not needed by the project type, create placeholder files with SKIP comments:

**Example 1 - CI/CD script for MicroPython:**
```bash
# scripts/ci.sh
# SKIP: not needed for micropython project - deployment via direct flash
#!/bin/bash
echo "CI/CD not required"
```

**Example 2 - GitHub Actions for embedded:**
```yaml
# .github/workflows/ci.yml
# SKIP: not needed for micropython project - no automated testing pipeline
```

**Fake files should be committed to git** to maintain structure completeness.

### Configure Scripts

Set up setup.sh, test.sh, build.sh based on project type.

### Add CI/CD

Configure GitHub Actions if needed, otherwise create skipped placeholder.

## Script Templates

### setup.sh

Purpose: Environment setup and dependency installation

**For Python:**
```bash
#!/bin/bash
# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize configuration
echo "Setup complete!"
```

### test.sh

Purpose: Run automated tests

**For Python with pytest:**
```bash
#!/bin/bash
# Activate virtual environment
source venv/bin/activate

# Run pytest with coverage
pytest tests/ --cov=src --cov-report=html

# Show coverage summary
coverage report
```

### build.sh

Purpose: Build and package the project

**For Python:**
```bash
#!/bin/bash
# Activate virtual environment
source venv/bin/activate

# Build package
python setup.py sdist bdist_wheel

echo "Build complete! Check dist/ for packages."
```

## Language-Specific Templates

### Python

**Directory structure:**
```
project/
├── src/
│   └── <package_name>/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── setup.py
├── pyproject.toml
└── pytest.ini
```

**requirements.txt:**
```
pytest>=7.0.0
pytest-cov>=4.0.0
```

**pyproject.toml:**
```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
requires-python = ">=3.10"
```

**pytest.ini:**
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
```

### JavaScript/TypeScript

**Directory structure:**
```
project/
├── src/
│   ├── index.ts
│   └── index.js
├── tests/
│   └── index.test.ts
├── package.json
└── tsconfig.json
```

**package.json:**
```json
{
  "name": "project-name",
  "version": "1.0.0",
  "scripts": {
    "test": "jest",
    "build": "tsc"
  }
}
```

### Java

**Directory structure:**
```
project/
├── src/
│   ├── main/
│   │   └── java/
│   └── test/
│       └── java/
└── pom.xml
```

### Go

**Directory structure:**
```
project/
├── cmd/
│   └── <app-name>/
│       └── main.go
├── pkg/
├── internal/
├── tests/
└── go.mod
```

## GitHub Actions CI/CD

**ci.yml:**
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v
```

**For projects that don't need CI/CD** (e.g., MicroPython embedded projects), create a placeholder with SKIP comment:

```yaml
# .github/workflows/ci.yml
# SKIP: not needed for micropython project - deployment via direct flash
```

## Commands

### Create New Project

To create a new project structure:

1. Ask for project name and language
2. Generate directory structure
3. Create language-specific config files
4. Add script templates
5. Set up CI/CD configuration

### Check Existing Structure

To validate a project structure:

1. Scan current directory
2. Check for required directories (src/, tests/, docs/, scripts/)
3. Verify config files exist
4. Report missing or recommended additions

## Best Practices

1. **Consistent naming** — Use lowercase with hyphens for directories
2. **Plural forms** — Use `tests/`, `docs/`, `scripts/` (not singular)
3. **Separation of concerns** — Keep source, tests, and docs separate
4. **Automation first** — Always include setup/test/build scripts
5. **CI/CD ready** — Include GitHub Actions by default, or mark with SKIP comment if not needed
6. **Fake files committed** — Placeholder files with SKIP comments should be committed to git

## When to Use This Skill

- User wants to "create a new project" or "set up a repository"
- User asks about "project structure" or "directory layout"
- User needs to "organize code" or "scaffold a project"
- User mentions standard folders like src/, tests/, docs/
- User needs help with project initialization or configuration
