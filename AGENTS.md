# BlackHalo Development Guide

**Updated:** January 2026
**Python:** 3.14+ | **GUI:** PyQt6 | **Manager:** UV

## Quick Reference

| Task | Location |
|------|----------|
| Main app | `./Halo.py` (~47k lines) |
| Build | `./build.py` (~400 lines) |
| Tests | `./tests/` (12 files) |
| GUI | `./gui/` (~100 files) |

## Conventions

- **Line length:** 180 chars (black, flake8, pylint)
- **Indentation:** 4 spaces
- **Naming:** Mixed `snake_case` (vars) and `camelCase` (functions/legacy), `PascalCase` (classes)
- **Imports:** isort with black profile
- **Testing:** pytest, `test_*.py` pattern
- **Defensive Programming:** MANDATORY. Validate all inputs, handle all edge cases explicitly.

## Strict Standards (Zero Tolerance)

- **NO IGNORES:** `# type: ignore`, `# noqa`, `# pylint: disable` are STRICTLY FORBIDDEN. Fix the root cause.
- **NO EXCLUDES:** Do not use `exclude` patterns in `pyproject.toml` or other configs. All code must pass.
- **NO BACKWARDS COMPATIBILITY:** Do not compromise code quality for legacy support.
- **NO COMPATIBILITY FILES:** Do not use shims like `six.py` or `future`.
- **NO DEPRECATED APIS:** e.g. use `urllib.request` or `requests` instead of `urllib2`.

## Run Commands

```bash
uv run --active python3 Halo.py           # App
uv run --active pytest tests/             # Tests
uv run --active black . --line-length 180 # Format
uv run --active pyinstaller Halo.py       # Build
```

## Architecture Notes

- **Dual build system:** Modern (UV/PyInstaller) + Legacy (2014 C++ daemons)
- **Cross-compilation:** Windows/macOS/Linux/ARM64 via PyInstaller
- **Crypto priority:** BlackCoin → BitBay → Bitcoin (legacy)
- **Monolith:** `Halo.py` is a massive legacy monolithic file containing core logic, networking, and legacy UI code.
