#!/bin/bash
# Auto-format script - fixes code style issues
# Usage: ./tests/scripts/format.sh [path]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/../.."
VENV="$PROJECT_ROOT/venv/bin"
TARGET="${1:-.}"

cd "$PROJECT_ROOT"

echo "=== Sorting imports (isort) ==="
"$VENV/isort" "$TARGET"

echo ""
echo "=== Formatting code (black) ==="
"$VENV/black" "$TARGET"

echo ""
echo "=== Running final lint check (flake8) ==="
"$VENV/flake8" "$TARGET" || true

echo ""
echo "Done! Code formatted."
