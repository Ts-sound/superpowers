# CI/CD Permissions Guide

## GitHub Actions Permissions

### Permission Levels

| Permission | Scope | Use Cases |
|------------|-------|-----------|
| `contents: read` | Repository read | Default, checkout, read files |
| `contents: write` | Repository write | Releases, commits, push |
| `packages: write` | GitHub Packages | npm, Docker, PyPI publishing |
| `pages: write` | GitHub Pages | Static site deployment |
| `pull-requests: write` | PR operations | Create/update PRs, labels |
| `id-token: write` | OIDC token | AWS/GCP/Azure authentication |
| `issues: write` | Issues | Create/update issues |
| `deployments: write` | Deployments | Deployment records |

### Default Behavior

**Without explicit `permissions` block:**
- `GITHUB_TOKEN` is **read-only** for contents
- Many operations will fail with 403

### Common Configurations

**Release Workflow:**
```yaml
permissions:
  contents: write
```

**Package Publish:**
```yaml
permissions:
  contents: read
  packages: write
```

**Pages Deployment:**
```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

**PR Workflow:**
```yaml
permissions:
  contents: read
  pull-requests: write
```

### Fine-Grained Permissions

```yaml
permissions:
  contents: write   # specific permission
  issues: read      # another specific
```

**All permissions:**
```yaml
permissions: write-all
```

**Read-only:**
```yaml
permissions: read-all
```

## GitLab CI Permissions

### Token Types

| Token | Scope | Use Cases |
|-------|-------|-----------|
| `CI_JOB_TOKEN` | Project-scoped | Push to same project |
| Project Access Token | Custom scopes | External operations |
| Deploy Token | Read/Write | Container registry |

### Configuration

```yaml
variables:
  GITLAB_TOKEN: $CI_JOB_TOKEN

deploy:
  script:
    - git push https://oauth2:${GITLAB_TOKEN}@gitlab.com/project.git
```

### Protected Branches

- Only maintainers can push to protected branches
- CI jobs need appropriate access level

## CircleCI Permissions

### Contexts

Store secrets in Contexts for sharing across projects.

```yaml
workflows:
  deploy:
    context: production-secrets
    jobs:
      - deploy
```

### Environment Variables

Project-level vs Context-level:
- Project: Single project access
- Context: Shared across projects

## Jenkins Permissions

### Authorization Strategy

| Strategy | Description |
|----------|-------------|
| Matrix-based | Fine-grained per-user |
| Project-based | Per-project permissions |
| Folder-based | Folder-level control |

### Credential Types

| Type | Use Cases |
|------|-----------|
| Username/Password | Git, API access |
| SSH Key | Git, deployment |
| Secret Text | API keys, tokens |
| Secret File | Certificates, configs |

### Pipeline Credentials

```groovy
withCredentials([usernamePassword(
  credentialsId: 'github-token',
  usernameVariable: 'GIT_USER',
  passwordVariable: 'GIT_TOKEN'
)]) {
  sh 'git push https://${GIT_USER}:${GIT_TOKEN}@github.com/repo.git'
}
```

## Security Best Practices

### Never Do

1. **Hardcode secrets** in workflow files
2. **Log secrets** in output (GitHub masks them)
3. **Use secrets in fork PRs** - they're unavailable
4. **Over-permission** - grant minimum needed

### Always Do

1. **Add `permissions` block** explicitly
2. **Use secret references** `${{ secrets.X }}`
3. **Restrict trigger branches** - not all branches
4. **Review third-party actions** - pin versions

### Secret Management

GitHub Secrets:
- Settings → Secrets and variables → Actions
- Repository secrets: current repo only
- Environment secrets: require approval
- Organization secrets: shared across repos

## Permission Troubleshooting Flowchart

```
Error 403?
│
├─ Is permissions block present?
│   └─ NO → Add appropriate permissions
│
├─ Does permission match operation?
│   └─ NO → Add missing permission
│
├─ Is branch protected?
│   └─ YES → Check if workflow can bypass
│
├─ Is from fork PR?
│   └─ YES → Secrets unavailable by design
│
├─ Environment protection enabled?
│   └─ YES → Needs approval
│
└─ Check token expiration/action restrictions
```