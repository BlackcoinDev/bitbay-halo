#!/usr/bin/env python3
"""Auto-format script - fixes code style issues."""
import os
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
VENV_BIN = PROJECT_ROOT / ".venv" / "bin"
TARGET = sys.argv[1] if len(sys.argv) > 1 else "."


def run(tool: str, *args: str) -> None:
    cmd = [str(VENV_BIN / tool), *args]
    print(f"=== Running: {' '.join(cmd)} ===")
    env = os.environ.copy()
    env["PYTHONWARNINGS"] = "ignore"
    subprocess.run(cmd, cwd=PROJECT_ROOT, env=env)
    print()


if __name__ == "__main__":
    run("isort", TARGET)
    run("black", TARGET)
    run("flake8", TARGET)
    print("Done! Code formatted.")
