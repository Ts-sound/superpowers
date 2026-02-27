#!/bin/bash

set -e

echo "=== Building project ==="

# Detect project type and build accordingly
if [ -f "requirements.txt" ]; then
    echo "Python project detected"
    
    # Activate virtual environment
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    
    # Build package
    echo "Building Python package..."
    if [ -f "setup.py" ]; then
        python setup.py sdist bdist_wheel
        echo "Build complete! Check dist/ for packages."
    elif [ -f "pyproject.toml" ]; then
        python -m build
        echo "Build complete! Check dist/ for packages."
    else
        echo "No setup.py or pyproject.toml found."
        exit 1
    fi
    
elif [ -f "package.json" ]; then
    echo "Node.js project detected"
    
    # Build with npm
    echo "Running npm build..."
    npm run build
    
    echo "Build complete! Check dist/ or build/ for output."
    
elif [ -f "pom.xml" ]; then
    echo "Java project detected"
    
    # Build with Maven
    echo "Building with Maven..."
    mvn clean package
    
    echo "Build complete! Check target/ for artifacts."
    
elif [ -f "go.mod" ]; then
    echo "Go project detected"
    
    # Build Go binary
    echo "Building Go binary..."
    go build -o bin/app ./cmd/...
    
    echo "Build complete! Check bin/ for binary."
    
else
    echo "No known project type detected."
    exit 1
fi

echo "=== Build complete! ==="
