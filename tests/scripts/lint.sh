#!/bin/bash
# Lint check script - reports issues without modifying files
# Usage: ./tests/scripts/lint.sh [path]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/../.."
VENV="$PROJECT_ROOT/venv/bin"
TARGET="${1:-.}"

cd "$PROJECT_ROOT"

echo "=== Checking import order (isort) ==="
"$VENV/isort" --check-only --diff "$TARGET" || true

echo ""
echo "=== Checking formatting (black) ==="
"$VENV/black" --check --diff "$TARGET" || true

echo ""
echo "=== Checking style (flake8) ==="
"$VENV/flake8" "$TARGET" || true

echo ""
echo "To auto-fix, run: ./tests/scripts/format.sh"
