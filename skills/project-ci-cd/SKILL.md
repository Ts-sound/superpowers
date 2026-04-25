---
name: project-ci-cd
description: "CI/CD workflow management. Use when setting up CI/CD, troubleshooting workflow failures, reviewing workflow files, or determining if project needs CI/CD. Triggers on: CI/CD, GitHub Actions, workflow, pipeline, permissions, secrets, 403 error, deployment automation, release, build, test automation."
---

# Project CI/CD Management

## Overview

Help set up, troubleshoot, and review CI/CD workflows. Default platform is GitHub Actions.

## When to Use This Skill

- Setting up new CI/CD workflow
- Troubleshooting workflow failures (403, secrets, permissions)
- Reviewing workflow file changes
- Determining if project needs CI/CD

## Determine CI/CD Need

### Quick Assessment

| Project Type | CI/CD Recommendation |
|--------------|---------------------|
| Library/Package | CI + Auto-publish |
| Application | CI + Build + Deploy |
| Documentation | Build + Pages deployment |
| Tool/Script | Optional CI, no release needed |
| Embedded/IoT | Build + Flash (no CI typically) |

### Questions to Ask

1. **Build needed?** Compiled code requires build step
2. **Tests exist?** Automated testing needs CI
3. **Publish target?** npm, PyPI, Docker, GitHub Releases
4. **Deployment?** Server, Pages, cloud platform

## Platform Selection

| Platform | Best For |
|----------|----------|
| GitHub Actions | GitHub projects (default) |
| GitLab CI | GitLab self-hosted, Docker-native |
| CircleCI | Commercial projects, parallel builds |
| Jenkins | Enterprise, high customization |

**Default: GitHub Actions** - most projects use GitHub.

## Permissions Checklist

**CRITICAL:** Many 403 errors come from missing permissions.

```yaml
permissions:
  contents: write      # Releases, commits, push to repo
  packages: write      # Registry publish (npm, Docker, PyPI)
  pages: write         # GitHub Pages deployment
  pull-requests: write # PR operations
  id-token: write      # OIDC for AWS/GCP/Azure
```

**See `references/permissions-guide.md` for full details.**

## Troubleshooting Quick Reference

### Common 403 Causes

1. **Missing `permissions` block** - default token is read-only
2. **Branch protection rules** - blocking push/merge
3. **Environment restrictions** - requiring approval
4. **Fork PR restrictions** - maintain permission model

### Secrets Not Available

1. Check `env:` section uses `${{ secrets.X }}`
2. Verify secret exists in Settings → Secrets
3. Fork PRs cannot access secrets (security)

**See `references/troubleshooting.md` for full diagnosis flow.**

## Templates

### GitHub Actions (Default)

See `references/github-actions.md` for:

- Basic CI workflow
- Release workflow (with real example)
- Multi-platform build
- Pages deployment

### Other Platforms

See respective reference files:
- `references/gitlab-ci.md`
- `references/circleci.md`
- `references/jenkins.md`

## Workflow Review Checklist

When reviewing workflow files:

1. **Permissions block** - present and appropriate
2. **Secrets usage** - `${{ secrets.X }}` not hardcoded
3. **Branch triggers** - appropriate branches/tags
4. **Dependencies** - actions/checkout@v4, setup-python@v5
5. **Output files** - correct paths for artifacts
6. **Error handling** - continue-on-error where needed

## Integration with Other Skills

| Skill | When to Reference This |
|-------|------------------------|
| brainstorming | "Does project need CI/CD?" |
| project-structure | "CI/CD setup step" |
| requesting-code-review | "Review workflow file" |
| systematic-debugging | "CI/CD failure diagnosis" |
| writing-plans | "Platform considerations" |

## Quick Start

**1. Basic CI:**
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: pytest
```

**2. Release:**
See real example in `references/github-actions.md` - Windows EXE build + GitHub Release.

**3. Add permissions if needed:**
```yaml
permissions:
  contents: write  # for releases
```