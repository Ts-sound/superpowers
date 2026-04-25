# GitHub Actions Templates

## Basic CI Workflow

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
          python-version: '3.12'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run tests
        run: pytest
```

## Release Workflow (Real Example)

**Source:** llamacpp-panel project

```yaml
name: Build and Release

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write

jobs:
  build:
    runs-on: windows-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pyinstaller
          pip install -r requirements.txt

      - name: Build EXE
        run: |
          pyinstaller -F -w -n llamacpp-panel --icon=llamacpp-panel.ico --add-data "llamacpp-panel.ico;." main.py

      - name: Get version from tag
        id: get_version
        run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT
        shell: bash

      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          name: llamacpp-panel ${{ steps.get_version.outputs.VERSION }}
          files: dist/llamacpp-panel.exe
          generate_release_notes: true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Key points:**
1. `permissions: contents: write` - required for releases
2. Tag trigger `v*` - triggers on version tags
3. Version extraction from tag
4. `softprops/action-gh-release` - release creation
5. `secrets.GITHUB_TOKEN` - automatic token

## Multi-Platform Build

```yaml
name: Build

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write

jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Build
        run: |
          pip install pyinstaller
          pip install -r requirements.txt
          pyinstaller -F -n app main.py
      
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: app-${{ matrix.os }}
          path: dist/*

  release:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Download all artifacts
        uses: actions/download-artifact@v4
      
      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          files: app-*/*
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Pages Deployment

```yaml
name: Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build site
        run: |
          npm install
          npm run build
      
      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## Package Publishing

### npm

```yaml
name: Publish npm

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: read
  packages: write

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          registry-url: 'https://npm.pkg.github.com'
      
      - run: npm ci
      - run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### PyPI

```yaml
name: Publish PyPI

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: read

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Build package
        run: |
          pip install build
          python -m build
      
      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          password: ${{ secrets.PYPI_API_TOKEN }}
```

### Docker

```yaml
name: Publish Docker

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: read
  packages: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Login to GitHub Packages
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:latest
```

## Common Patterns

### Matrix Testing

```yaml
strategy:
  matrix:
    python-version: ['3.10', '3.11', '3.12']
    os: [ubuntu-latest, windows-latest]
```

### Conditional Steps

```yaml
- name: Deploy (only main)
  if: github.ref == 'refs/heads/main'
  run: deploy.sh
```

### Cache Dependencies

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

### Use Secrets

```yaml
- name: Deploy
  env:
    API_KEY: ${{ secrets.API_KEY }}
  run: deploy.sh
```

### Output Between Jobs

```yaml
jobs:
  build:
    outputs:
      version: ${{ steps.version.outputs.VERSION }}
    steps:
      - id: version
        run: echo "VERSION=1.0" >> $GITHUB_OUTPUT
  
  deploy:
    needs: build
    steps:
      - run: echo "Version is ${{ needs.build.outputs.version }}"
```

## Version Pinning

Always pin action versions:

| Action | Recommended Version |
|--------|---------------------|
| checkout | `@v4` |
| setup-python | `@v5` |
| setup-node | `@v4` |
| upload-artifact | `@v4` |
| download-artifact | `@v4` |
| cache | `@v4` |
| gh-release | `@v2` |

**Do NOT use:**
- `@main` - unstable
- `@master` - unstable
- No version - may change