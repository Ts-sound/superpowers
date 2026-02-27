#!/bin/bash

set -e

echo "=== Running tests ==="

# Detect project type and run tests accordingly
if [ -f "requirements.txt" ]; then
    echo "Python project detected"
    
    # Activate virtual environment
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    
    # Run pytest with coverage
    echo "Running pytest..."
    pytest tests/ -v --cov=src --cov-report=term-missing
    
    # Generate HTML coverage report
    echo "Generating coverage report..."
    coverage html
    
    echo "Coverage report available at htmlcov/index.html"
    
elif [ -f "package.json" ]; then
    echo "Node.js project detected"
    
    # Run npm test
    echo "Running npm test..."
    npm test
    
elif [ -f "pom.xml" ]; then
    echo "Java project detected"
    
    # Run Maven tests
    echo "Running Maven tests..."
    mvn test
    
elif [ -f "go.mod" ]; then
    echo "Go project detected"
    
    # Run Go tests
    echo "Running Go tests..."
    go test -v ./...
    
else
    echo "No known project type detected."
    exit 1
fi

echo "=== Tests complete! ==="
