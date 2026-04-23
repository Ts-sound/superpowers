# Project Conventions for AI Agents

This document defines coding standards and conventions for AI agents working on this project.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| Framework | [Specify framework, e.g., Tkinter] |
| Testing | pytest + pytest-cov |
| Build | pyinstaller |

## Architecture

```
src/
├── models/        # Data models (@dataclass)
├── services/      # Business logic
├── repositories/  # Data access (I/O)
├── ui/            # User interface
└── utils/         # Utilities
```

**Rules:**
- No cross-layer calls
- Models contain no business logic
- UI calls services only

## Coding Standards

### Models
- Use `@dataclass` for data classes
- Complete type annotations required
- No business logic in models

### Services
- Business logic implementation
- Dependency injection
- Log important operations

### Style
- Imports: stdlib → third-party → local
- Classes: PascalCase
- Functions/variables: snake_case
- Constants: UPPER_SNAKE_CASE
- Files: snake_case.py

## Naming Conventions

### Files
- Modules: `snake_case.py`
- Tests: `test_<module>.py`
- Models: singular noun (e.g., `person.py`)

### Classes
- Models: singular noun, PascalCase (e.g., `Person`)
- Services: `<Feature>Calculator`
- Repositories: `<Feature>Repo`

### Functions
- Public: `snake_case`
- Private: `_snake_case`
- Event handlers: `on_<event>`

## Git Commit Format

```
<type>: <description>
```

| Type | Usage |
|------|-------|
| feat | New feature |
| fix | Bug fix |
| refactor | Code refactoring |
| docs | Documentation |
| test | Tests |
| chore | Build/tools |
| style | Formatting |

## Test Requirements

- New features require unit tests
- Coverage >= 80%
- Test structure mirrors src structure
- Use pytest.fixture for shared data

## Prohibited Actions

1. UI directly accessing repositories
2. Business logic in models
3. Skipping tests before commit
4. Hardcoded config values
5. Missing type annotations

## Best Practices

1. Clear layered architecture
2. Dependency injection
3. Testable code
4. Necessary logging
5. Clean readable code