# CI/CD Troubleshooting Guide

## Diagnosis Flow

### Phase 1: Read Error Messages

1. **Check workflow run logs** - Actions → Failed run → Logs
2. **Read stack traces completely** - file paths, line numbers
3. **Note error codes** - 403, 404, 500, timeout

### Phase 2: Identify Failure Layer

Multi-component systems: CI → Build → Deploy → Target

**Add diagnostic logging:**
```yaml
- name: Debug secrets
  run: |
    echo "Token available: ${GITHUB_TOKEN:+YES}${GITHUB_TOKEN:-NO}"
    echo "Secret X: ${SECRET_X:+SET}${SECRET_X:-UNSET}"
```

### Phase 3: Check Recent Changes

```bash
git diff HEAD~5 -- .github/workflows/
git log --oneline -5 -- .github/workflows/
```

## Common Issues

### 403 Forbidden

**Symptoms:**
- "Resource not accessible by integration"
- "Permission denied"

**Causes & Fixes:**

| Cause | Fix |
|-------|-----|
| Missing permissions block | Add `permissions: contents: write` |
| Wrong permission level | Check operation needs |
| Branch protection | Add bypass for workflows |
| Environment approval | Approve or remove restriction |
| Fork PR | Cannot use secrets (design) |

**Verification:**
```yaml
# Add at top of workflow
permissions:
  contents: write  # for releases
```

### Secrets Not Available

**Symptoms:**
- Empty environment variables
- "Secret X not found"

**Diagnosis:**
1. Check secret exists: Settings → Secrets
2. Verify syntax: `${{ secrets.MY_SECRET }}` (not `$MY_SECRET`)
3. Check workflow can access: not fork PR
4. Environment secrets need approval

**Verification:**
```yaml
- name: Check secrets
  run: echo "Secret present: ${SECRET:+YES}${SECRET:-NO}"
  env:
    SECRET: ${{ secrets.MY_SECRET }}
```

### Build Fails

**Symptoms:**
- Compilation errors
- Dependency resolution fails

**Diagnosis:**
1. Check build tool version
2. Verify dependencies in lock file
3. Check environment differences (OS, Python)
4. Add verbose output

**Example:**
```yaml
- name: Install with verbose
  run: pip install -v -r requirements.txt
```

### Timeout Issues

**Symptoms:**
- "The operation was canceled"
- Job exceeds time limit

**Causes:**
- Long-running build
- Network timeouts
- Resource contention

**Fixes:**
```yaml
jobs:
  build:
    timeout-minutes: 30  # increase if needed
```

### Action Not Found

**Symptoms:**
- "Action 'X' not found"
- "Unable to resolve action"

**Fixes:**
1. Pin to specific version: `actions/checkout@v4`
2. Check action exists and is public
3. Verify workflow syntax

### Cache Issues

**Symptoms:**
- Cache not restoring
- "Cache not found for key"

**Fix:**
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

## Platform-Specific Issues

### GitHub Actions

**Runner Issues:**
| Runner | Common Issues |
|--------|---------------|
| ubuntu-latest | Standard, most compatible |
| windows-latest | Path separators, PowerShell |
| macos-latest | macOS-specific paths |

**Windows Path Fix:**
```yaml
- name: Windows path
  shell: bash  # force bash
  run: echo "${GITHUB_WORKSPACE}/src"
```

### GitLab CI

**Docker Issues:**
```yaml
variables:
  DOCKER_TLS_CERTDIR: ""
  DOCKER_HOST: "tcp://docker:2375"
```

**Cache Not Working:**
```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
```

### CircleCI

**Resource Class Error:**
```yaml
resource_class: medium  # must match project plan
```

**Parallelism:**
```yaml
parallelism: 4
```

### Jenkins

**Credential Not Found:**
```groovy
withCredentials([string(
  credentialsId: 'my-secret',
  variable: 'MY_VAR'
)]) {
  sh 'echo Using credential'
}
```

## Workflow Hangs/Deadlocks

**Symptoms:**
- Job runs forever
- No output after certain step

**Diagnosis:**
1. Add logging at each step
2. Identify where it stops
3. Check for blocking I/O

**Example:**
```yaml
- name: Step 1
  run: echo "[START] Step 1"
- name: Step 2
  run: echo "[START] Step 2"
- name: Step 3 (maybe hangs)
  run: |
    echo "[START] Step 3"
    # ... actual command
    echo "[END] Step 3"
```

## Quick Fixes Reference

| Error | Quick Fix |
|-------|-----------|
| 403 on release | Add `permissions: contents: write` |
| 403 on pages | Add `permissions: pages: write` |
| 403 on package | Add `packages: write` |
| Secrets empty | Check `${{ secrets.X }}` syntax |
| Build timeout | Increase `timeout-minutes` |
| Action not found | Pin version: `@v4` |
| Path issues (Windows) | Use `shell: bash` |

## Verification Commands

**Check workflow syntax:**
```bash
# Local validation (if actionlint installed)
actionlint .github/workflows/workflow.yml
```

**View workflow runs:**
```bash
gh run list --workflow=ci.yml
gh run view <run-id> --log
```

**Download artifacts:**
```bash
gh run download <run-id>
```