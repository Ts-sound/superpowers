# GitLab CI Templates

## Basic CI

```yaml
# .gitlab-ci.yml

stages:
  - test
  - build
  - deploy

test:
  stage: test
  image: python:3.12
  script:
    - pip install -r requirements.txt
    - pytest
  coverage: '/TOTAL.*\s+(\d+%)/'

build:
  stage: build
  image: python:3.12
  script:
    - pip install pyinstaller
    - pyinstaller -F -n app main.py
  artifacts:
    paths:
      - dist/

deploy:
  stage: deploy
  script:
    - ./deploy.sh
  only:
    - main
```

## Docker Build

```yaml
docker-build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  variables:
    DOCKER_TLS_CERTDIR: ""
    DOCKER_HOST: "tcp://docker:2375"
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_TAG .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_TAG
  only:
    - tags
```

## Pages Deployment

```yaml
pages:
  stage: deploy
  script:
    - npm install
    - npm run build
    - mv dist public
  artifacts:
    paths:
      - public
  only:
    - main
```

## Multi-Project Pipeline

```yaml
trigger-downstream:
  stage: deploy
  trigger:
    project: downstream/project
    branch: main
    strategy: depend
```

## Cache Configuration

```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .cache/pip/

test:
  script:
    - npm install
    - npm test
  cache:
    key: ${CI_JOB_NAME}
    paths:
      - node_modules/
```

## Environment Variables

```yaml
variables:
  PYTHON_VERSION: "3.12"
  APP_NAME: "myapp"

deploy:
  stage: deploy
  environment:
    name: production
    url: https://app.example.com
  script:
    - deploy.sh
  only:
    - main
```

## Manual Approval

```yaml
deploy:
  stage: deploy
  when: manual
  allow_failure: false
  script:
    - deploy.sh
  only:
    - main
```

## Key Differences from GitHub Actions

| Feature | GitLab CI | GitHub Actions |
|---------|-----------|----------------|
| Runner selection | `image:` tag | `runs-on:` |
| Artifacts | `artifacts:` | `upload-artifact` action |
| Secrets | CI variables | `secrets.X` |
| Permissions | Token scopes | `permissions:` block |
| Trigger | `only:` / `except:` | `on:` |
| Services | `services:` | Container actions |

## Common Issues

### Docker-in-Docker

Must set:
```yaml
variables:
  DOCKER_TLS_CERTDIR: ""
  DOCKER_HOST: "tcp://docker:2375"
services:
  - docker:dind
```

### Protected Branches

Cannot push to protected branches from CI without:
1. Project access token with write scope
2. Maintainer permission on runner

### Cache Not Persisting

Use consistent key:
```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
```