#!/bin/bash

set -e

echo "=== Setting up project environment ==="

# Detect project type and set up accordingly
if [ -f "requirements.txt" ]; then
    echo "Python project detected"
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3.10 -m venv venv
    fi
    
    # Activate virtual environment
    echo "Activating virtual environment..."
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    
    echo "Python setup complete!"
    
elif [ -f "package.json" ]; then
    echo "Node.js project detected"
    
    # Install dependencies
    echo "Installing dependencies..."
    npm install
    
    echo "Node.js setup complete!"
    
elif [ -f "pom.xml" ]; then
    echo "Java project detected"
    
    # Build with Maven
    echo "Building with Maven..."
    mvn clean install
    
    echo "Java setup complete!"
    
elif [ -f "go.mod" ]; then
    echo "Go project detected"
    
    # Download dependencies
    echo "Downloading Go dependencies..."
    go mod download
    
    echo "Go setup complete!"
    
else
    echo "No known project type detected."
    echo "Please create requirements.txt, package.json, pom.xml, or go.mod"
    exit 1
fi

echo "=== Setup complete! ==="
