#!/usr/bin/env python3
"""Lint check script - reports issues without modifying files."""
import os
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
VENV_BIN = PROJECT_ROOT / ".venv" / "bin"
TARGET = sys.argv[1] if len(sys.argv) > 1 else "."


def run(tool: str, *args: str) -> int:
    cmd = [str(VENV_BIN / tool), *args]
    print(f"=== Running: {' '.join(cmd)} ===")
    env = os.environ.copy()
    env["PYTHONWARNINGS"] = "ignore"
    result = subprocess.run(cmd, cwd=PROJECT_ROOT, env=env)
    print()
    return result.returncode


if __name__ == "__main__":
    run("isort", "--check-only", "--diff", TARGET)
    run("black", "--check", "--diff", TARGET)
    run("flake8", TARGET)
    run("pyright", TARGET)
    run("pylint", TARGET)
    print("To auto-fix, run: python tests/scripts/format.py")
