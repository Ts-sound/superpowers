# Jenkins Templates

## Basic Pipeline

```groovy
// Jenkinsfile

pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest'
            }
        }
        
        stage('Build') {
            steps {
                sh 'pip install pyinstaller'
                sh 'pyinstaller -F -n app main.py'
            }
            post {
                success {
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'deploy.sh'
            }
        }
    }
}
```

## Declarative Pipeline with Docker

```groovy
pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-v $HOME/.cache/pip:/root/.cache/pip'
        }
    }
    
    stages {
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest'
            }
        }
    }
}
```

## Multi-Platform Build

```groovy
pipeline {
    agent none
    
    stages {
        stage('Build') {
            parallel {
                stage('Linux') {
                    agent { label 'linux' }
                    steps {
                        sh 'build.sh'
                    }
                }
                stage('Windows') {
                    agent { label 'windows' }
                    steps {
                        bat 'build.bat'
                    }
                }
            }
        }
    }
}
```

## Credentials Usage

```groovy
pipeline {
    agent any
    
    environment {
        API_KEY = credentials('api-key-credential')
    }
    
    stages {
        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-token',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_TOKEN'
                )]) {
                    sh 'git push https://${GIT_USER}:${GIT_TOKEN}@github.com/repo.git'
                }
            }
        }
    }
}
```

## Manual Approval

```groovy
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'build.sh'
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            input {
                message "Deploy to production?"
                ok "Deploy"
                submitter "admin"
            }
            steps {
                sh 'deploy.sh'
            }
        }
    }
}
```

## Environment Variables

```groovy
pipeline {
    agent any
    
    environment {
        APP_NAME = 'myapp'
        VERSION = "${env.BUILD_NUMBER}"
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'echo Building ${APP_NAME} version ${VERSION}'
            }
        }
    }
}
```

## Post Actions

```groovy
pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            mail to: 'team@example.com',
                 subject: "Build Success: ${env.JOB_NAME}",
                 body: "Build ${env.BUILD_NUMBER} succeeded"
        }
        failure {
            mail to: 'team@example.com',
                 subject: "Build Failed: ${env.JOB_NAME}",
                 body: "Build ${env.BUILD_NUMBER} failed"
        }
    }
}
```

## Key Differences from GitHub Actions

| Feature | Jenkins | GitHub Actions |
|---------|---------|----------------|
| Runner | Agent labels | `runs-on:` |
| Secrets | Credentials | `secrets.X` |
| Parallel | `parallel {}` | Matrix strategy |
| Artifacts | `archiveArtifacts` | `upload-artifact` |
| Trigger | Webhook/polling | `on:` |
| Approval | `input {}` | Environment protection |

## Common Issues

### Credential Not Found

Check credential ID in Jenkins → Credentials.

### Agent Not Available

```groovy
agent { label 'linux' }  // must have agent with this label
```

### Docker Permission

Run Jenkins agent with Docker access:
```groovy
agent {
    docker {
        image 'python:3.12'
    }
}
```

### Workspace Cleanup

```groovy
post {
    always {
        cleanWs()
    }
}
```