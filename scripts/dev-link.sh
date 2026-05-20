#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLUGIN_NAME="superpowers"
MARKETPLACE_NAME="superpowers-dev"

# Read version from plugin.json
VERSION=$(node -e "console.log(require('${REPO_ROOT}/.claude-plugin/plugin.json').version)")

# Step 1: Add marketplace if not already registered
if claude plugin marketplace list 2>/dev/null | grep -q "$MARKETPLACE_NAME"; then
    echo "[skip] marketplace '$MARKETPLACE_NAME' already exists"
else
    echo "[1/3] Adding marketplace '$MARKETPLACE_NAME'..."
    claude plugin marketplace add "$REPO_ROOT"
fi

# Step 2: Install (or reinstall) plugin
echo "[2/3] Installing plugin..."
claude plugin install "${PLUGIN_NAME}@${MARKETPLACE_NAME}" 2>/dev/null || {
    claude plugin uninstall "$PLUGIN_NAME" 2>/dev/null
    claude plugin install "${PLUGIN_NAME}@${MARKETPLACE_NAME}"
}

# Step 3: Replace cache with symlink
CACHE_DIR="${HOME}/.claude/plugins/cache/${MARKETPLACE_NAME}/${PLUGIN_NAME}/${VERSION}"

# Remove it whether it's a real directory or a broken symlink
if [ -e "$CACHE_DIR" ] || [ -L "$CACHE_DIR" ]; then
    echo "[3/3] Replacing cache with symlink..."
    rm -rf "$CACHE_DIR"
else
    echo "[3/3] Creating symlink..."
fi

ln -s "$REPO_ROOT" "$CACHE_DIR"

echo ""
echo "Done. ${REPO_ROOT} -> ${CACHE_DIR}"
echo "Run 'claude plugin details ${PLUGIN_NAME}' to verify."
