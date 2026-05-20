#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLUGIN_DIR="${REPO_ROOT}/.claude-plugin"

# Read marketplace name and plugin version from config files
MARKETPLACE_NAME=$(node -e "console.log(require('${PLUGIN_DIR}/marketplace.json').name)")
PLUGIN_NAME=$(node -e "console.log(require('${PLUGIN_DIR}/plugin.json').name)")
VERSION=$(node -e "console.log(require('${PLUGIN_DIR}/plugin.json').version)")

if [ -z "$VERSION" ]; then
    echo "ERROR: failed to read version from ${PLUGIN_DIR}/plugin.json" >&2
    exit 1
fi

CACHE_PATH="${HOME}/.claude/plugins/cache/${MARKETPLACE_NAME}/${PLUGIN_NAME}/${VERSION}"

# Early exit if already correctly linked
if [ "$(readlink -f "$CACHE_PATH" 2>/dev/null)" = "$REPO_ROOT" ]; then
    echo "Already linked: ${CACHE_PATH} -> ${REPO_ROOT}"
    exit 0
fi

# Step 1: Register marketplace if not already registered
if claude plugin marketplace list 2>/dev/null | grep -q "$MARKETPLACE_NAME"; then
    echo "[skip] marketplace '${MARKETPLACE_NAME}' already exists"
else
    echo "[1/3] Adding marketplace '${MARKETPLACE_NAME}'..."
    claude plugin marketplace add "$REPO_ROOT"
fi

# Step 2: Install plugin if not already installed
if claude plugin list 2>/dev/null | grep -q "$PLUGIN_NAME"; then
    echo "[skip] plugin '${PLUGIN_NAME}' already installed"
else
    echo "[2/3] Installing plugin..."
    claude plugin install "${PLUGIN_NAME}@${MARKETPLACE_NAME}"
fi

# Step 3: Replace cache with symlink
if [ -e "$CACHE_PATH" ] || [ -L "$CACHE_PATH" ]; then
    echo "[3/3] Replacing cache with symlink..."
    rm -rf "$CACHE_PATH"
else
    echo "[3/3] Creating symlink..."
fi

mkdir -p "$(dirname "$CACHE_PATH")"
ln -s "$REPO_ROOT" "$CACHE_PATH"

# Clean up stale version cache directories
CACHE_BASE="$(dirname "$CACHE_PATH")"
for dir in "$CACHE_BASE"/*/; do
    dir_name="$(basename "$dir")"
    if [ "$dir_name" != "$VERSION" ] && [ -d "$dir" ] && ! [ -L "$dir" ]; then
        echo "Cleaning up stale version cache: $dir"
        rm -rf "$dir"
    fi
done

echo ""
echo "Done. ${REPO_ROOT} -> ${CACHE_PATH}"
echo "Run 'claude plugin details ${PLUGIN_NAME}' to verify."
