# BlackHalo Development Guide

**Updated:** January 2026
**Python:** 3.14+ | **GUI:** PyQt6 | **Manager:** UV

## Quick Reference

| Task | Location |
|------|----------|
| Main app | `./Halo.py` (1570 lines) |
| Build | `./build.py` |
| Tests | `./tests/` |
| GUI | `./gui/` ||

## Conventions

- **Line length:** 180 chars (black, flake8, pylint)
- **Indentation:** 4 spaces
- **Naming:** `snake_case` (vars/functions), `PascalCase` (classes), `type_name` (GUI)
- **Imports:** isort with black profile
- **Testing:** pytest, `test_*.py` pattern

## Anti-Patterns (Forbidden)

- `# type: ignore`, `# noqa:`, `# pylint: disable:` — Fix root cause
- Python 2 syntax: `print "x"`, `except E, e:`, `unicode(x)`
- `urllib2` — use `urllib.request`
- Empty `except:` blocks

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
