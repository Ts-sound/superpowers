# CircleCI Templates

## Basic CI

```yaml
# .circleci/config.yml

version: 2.1

jobs:
  test:
    docker:
      - image: python:3.12
    steps:
      - checkout
      - run:
          name: Install dependencies
          command: pip install -r requirements.txt
      - run:
          name: Run tests
          command: pytest

workflows:
  main:
    jobs:
      - test
```

## Build and Deploy

```yaml
version: 2.1

jobs:
  build:
    docker:
      - image: python:3.12
    steps:
      - checkout
      - run:
          name: Build
          command: |
            pip install pyinstaller
            pyinstaller -F -n app main.py
      - store_artifacts:
          path: dist/

  deploy:
    docker:
      - image: python:3.12
    steps:
      - checkout
      - run:
          name: Deploy
          command: deploy.sh

workflows:
  build-deploy:
    jobs:
      - build
      - deploy:
          requires:
            - build
          filters:
            branches:
              only: main
```

## Orbs (Reusable Packages)

```yaml
version: 2.1

orbs:
  python: circleci/python@2.0
  docker: circleci/docker@2.0

jobs:
  test:
    executor: python/default
    steps:
      - python/install-packages
      - run: pytest

  docker-build:
    executor: docker/docker
    steps:
      - docker/build:
          image: myapp
      - docker/push:
          image: myapp

workflows:
  main:
    jobs:
      - test
      - docker-build:
          requires:
            - test
```

## Parallelism

```yaml
jobs:
  test:
    parallelism: 4
    docker:
      - image: python:3.12
    steps:
      - checkout
      - run:
          name: Split tests
          command: |
            pytest $(circleci tests glob "tests/*.py" | circleci tests split)
```

## Contexts (Shared Secrets)

```yaml
workflows:
  deploy:
    jobs:
      - deploy:
          context: production-secrets

jobs:
  deploy:
    docker:
      - image: python:3.12
    steps:
      - run:
          name: Deploy
          command: deploy.sh
          environment:
            API_KEY: $API_KEY  # from context
```

## Resource Classes

```yaml
jobs:
  build:
    resource_class: medium
    docker:
      - image: python:3.12
    steps:
      - checkout
      - run: build.sh

# Available: small, medium, medium+, large, xlarge
```

## Key Differences from GitHub Actions

| Feature | CircleCI | GitHub Actions |
|---------|----------|----------------|
| Runner | `docker:` / `machine:` | `runs-on:` |
| Secrets | Contexts | `secrets.X` |
| Reuse | Orbs | Composite actions |
| Parallelism | `parallelism:` | Matrix strategy |
| Artifacts | `store_artifacts:` | `upload-artifact` |
| Resource size | `resource_class:` | Standard runners |

## Common Issues

### Resource Class Not Available

Must match project plan:
```yaml
resource_class: medium  # must be allowed for project
```

### Context Not Found

Verify context exists in organization settings.

### Docker Layer Caching

```yaml
jobs:
  build:
    docker:
      - image: python:3.12
    steps:
      - checkout
      - setup_remote_docker:
          docker_layer_caching: true
```