# Agent Guidelines for BlackHalo Development

## Current Modernization Status (2025)

### ✅ Foundation Already Established (40% Complete)
- **Python 3.14.2** - Fully functional, modern language features
- **PyQt6 imports** - Present in all major files (Halo.py, gui/mainwindow.py, etc.)
- **UV Package Management** - Modern dependency resolution system
- **Test Suite** - 32/32 tests passing, solid foundation
- **GUI Startup** - Main application starts successfully

### 🔧 Modernization Roadmap (60% Remaining)
- **Python 2→3 compatibility** - Print statements, imports, string handling
- **Legacy build pattern modernization** - 2014 scripts → 2025 approach
- **Cross-compilation setup** - Multi-platform distribution
- **Dependency resolution** - Missing packages via UV

---

## CODE QUALITY STANDARD

**CRITICAL: 100% Quality Code Requirement**

This project maintains the highest code quality standards. The following rules apply without exception:

### 1.1 No Ignore Directives Allowed

```python
# ❌ FORBIDDEN - Never use these:
# type: ignore
# noqa: ...
# pylint: disable=...
# pyright: ignoreNextLine
```

### 1.2 Rule: Fix the Root Cause

When a linter, type checker, or compiler reports an issue:

1. **First choice:** Fix the actual problem in the code
2. **Second choice:** Refactor to avoid the issue
3. **Third choice:** Document why the code is correct as-is

### 1.3 Exception Process

If there is **NO OTHER WAY** to resolve an issue:

1. **Present the exception** clearly with:
   - The exact error/warning
   - Why the current code is correct
   - Why there is no alternative solution

2. **User must approve** the exception

3. **Document the exception** in `agent/PHASES.md` with:
   ```
   ## EXCEPTION: [Brief Title]
   
   **Issue:** [Exact error/warning]
   
   **Why code is correct:** [Explanation]
   
   **No alternative because:** [Reason]
   
   **Approved by:** [User/Date]
   
   **Last review:** [Date]
   ```

### 1.4 Quality Gates

| Tool | Purpose | Pass Criteria |
|------|---------|---------------|
| pytest | Runtime tests | 32/32 passing |
| pyright | Type checking | Zero errors |
| flake8 | Style | No violations |
| black | Formatting | No changes needed |

### 1.5 Why This Matters

- **Technical debt** accumulates when ignores are used
- **Future developers** can't trust the code
- **Refactoring** becomes impossible
- **Security** can be compromised

### 1.6 Current Status

**Tests:** ✅ 32/32 passing  
**Pyright:** ⚠️ ~7000 warnings (mostly false positives from legacy code)  
**Action:** Legacy warnings are acceptable during Phase 1. New code must be clean.

---

## Build and Test Commands (UV-Based)

### Primary Build Scripts
```bash
# Modern UV-based cross-platform build (recommended)
python3 build.py                    # Run modernized UV build script

# Legacy build scripts (analyzed for patterns, being modernized)
./BUILD SCRIPTS ETC/linux.sh --build    # Proven 2014 patterns for modern adaptation
./BUILD SCRIPTS ETC/linux.sh --reset    # Reset and rebuild environment
./BUILD SCRIPTS ETC/win32.sh        # Windows cross-compilation patterns
./BUILD SCRIPTS ETC/osx64.sh        # macOS build patterns
./LinuxHaloSetup.sh                 # Legacy Linux setup (being modernized)

# Individual script execution (after fixes)
uv run --active python3 Halo.py     # Direct application startup
uv run --active pyinstaller Halo.py # Create executable
```

### UV Environment Management
```bash
# Install UV if not available
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize or sync UV project
uv sync                             # Sync dependencies from pyproject.toml

# Add dependencies
uv add PyQt6 PyQt6-WebEngine pyzmail39 stopit pycryptodome

# Run commands in UV environment
uv run --active python3 script.py   # Run Python script with dependencies
uv run --active pytest tests/       # Run tests with dependencies
uv run --active black . --line-length=120  # Format code
uv run --active pyinstaller script.py  # Build executable
```

### Test Commands
```bash
# Run blockchain API tests
uv run --active python3 testblock.py                # Run main test suite

# Modern pytest with coverage using UV
uv run --active pytest tests/ --cov=Bitmessage --cov=highlevelcrypto --cov-report=term-missing

# Single test execution patterns
uv run --active pytest tests/test_addresses.py::test_specific_function
uv run --active python3 -m unittest testblock.bitcoinapi.stat_hash
uv run --active pytest tests/test_crypto.py -v
uv run --active pytest tests/test_protocol.py

# BitMessage tests
cd Bitmessage && uv run --active python3 tests.py        # Run BitMessage unit tests
cd Bitmessage-BitMHalo-v0.6 && uv run --active pytest src/  # PyBitmessage tests

# Run specific test file
uv run --active pytest tests/test_protocol.py
```

### Lint and Format Commands
```bash
# Code formatting and sorting using UV
uv run --active black . --line-length=120
uv run --active isort . --profile=black --line-length=120

# Linting using UV
uv run --active flake8 . --max-line-length=120
uv run --active pylint --rc-file=.pylintrc Bitmessage/ highlevelcrypto.py

# Run all quality checks
uv run --active python3 tests/scripts/lint.py
```

### Development Setup
```bash
# Check Python version (requires 3.8+, Python 3.14+ preferred)
python3 --version

# UV-based setup (recommended)
uv sync                           # Install all dependencies from pyproject.toml
uv add pyinstaller               # Add build tools

# Manual dependency installation (if needed)
uv add PyQt6 PyQt6-WebEngine pyzmail39 stopit pycryptodome requests pillow qrcode

# Alternative: Install system-wide (Linux)
sudo apt install python3-pyqt6 python3-pyqt6.qtwebengine

# Install legacy dependencies if needed (for compatibility)
uv add -r Bitmessage-BitMHalo-v0.6/requirements.txt  # If file exists
```

## Python Version and Compatibility

### Current Status: Mixed Python 2.7 and 3.14+ Code
- **Python 3.14+** - Primary target, foundation established
- **Legacy Python 2.7** - Still present in some modules, being migrated
- **Mixed imports** - Some Python 2/3 compatibility issues remain
- **Print statements** - Multiple files need conversion from Python 2 syntax

### Import Conventions (Modern Python 3.14+)
```python
# Standard library imports first
import urllib.request as urllib2  # Python 3 compatibility
import re
import time
import calendar
import datetime

# Third-party imports (managed by UV)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import pyzmail

# Local imports last
from custom.Demo1 import *
import pyblackcointools

# Python 2/3 compatibility patterns
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
```

## Code Formatting and Modernization

### Python 3.14+ Standards
- **Line Length**: Maximum 120 characters (configured in .flake8, pyproject.toml)
- **Indentation**: 4 spaces (no tabs)
- **Print Functions**: Use `print()` not `print` statements
- **String Formatting**: Use f-strings for Python 3.6+, `.format()` for compatibility
- **Import Sorting**: Use `isort` with black profile
- **Excluded Paths**: Bitmessage-BitMHalo-v0.6, BUILD SCRIPTS ETC, bridge, data, agent, BitMData, images

### Critical Python 2→3 Conversions Needed
```python
# Print statements → Print functions
print "message"              # OLD
print("message")             # NEW

# String handling
unicode(text)                # OLD
str(text)                    # NEW

# urllib imports
import urllib2               # OLD
import urllib.request as urllib2  # NEW

# Exception syntax
except Exception, e:         # OLD
except Exception as e:       # NEW
```

### Legacy Build Script Patterns (2014 → 2025)
**Valuable patterns from BUILD SCRIPTS ETC:**
- **Modular architecture** - Separate check/reset/build functions
- **Platform abstraction** - OS version verification, tool checking
- **Dependency management** - Systematic package installation
- **Cross-compilation** - Single source, multiple targets

**Modern adaptations:**
- **Debian 7 (2014)** → **Ubuntu 24.04 (2025)**
- **MXE cross-compiler** → **Modern MinGW-w64/ARM64 toolchains**
- **Makefile builds** → **PyInstaller/CMake modern approach**
- **apt dependencies** → **UV package management**
- **Manual testing** → **Automated CI/CD**

## Cross-Platform Distribution Strategy

### Target Platforms (From Ubuntu 24.04 AMD64)
```bash
✅ Windows x64 (Intel/AMD) - MinGW-w64 cross-compilation
✅ macOS Universal (Intel + ARM64) - Xcode toolchain
✅ Linux x64 (Intel/AMD) - Native builds
✅ Linux ARM64 (Raspberry Pi, Apple Silicon) - GCC cross-compiler
✅ Windows ARM64 (Surface, etc.) - MinGW-w64 (limited)
```

### Modern Cross-Compilation Commands
```bash
# Windows x64 build
uv run --active pyinstaller --onefile --windowed --name=BlackHalo-windows-x64 Halo.py

# Linux ARM64 build  
aarch64-linux-gnu-uv run --active pyinstaller --onefile --windowed --name=BlackHalo-linux-arm64 Halo.py

# Native Linux build
uv run --active pyinstaller --onefile --windowed --name=BlackHalo-linux-x64 Halo.py
```

## Cryptocurrency Integration

### Supported Cryptocurrencies (Priority-Based)
1. **BlackCoin (BLK)** - PRIMARY FOCUS
   - Official modern cryptocurrency (Bitcoin Core v26.2.0 + PoS v3.1)
   - Website: https://blackcoinmore.org
   - Daemon: `blackmored`
   - RPC Port: 15715

2. **BitBay (BAY)** - SECONDARY SUPPORT
   - Dynamic pegged currency system
   - Advanced market features
   - Daemon: `bitbayd`
   - RPC Port: 19915

3. **Bitcoin (BTC)** - LEGACY SUPPORT
   - Not real Bitcoin (uses BlackCoin daemon)
   - Consider removal or real Bitcoin Core integration

### BlackCoin Integration Testing
```bash
# Test BlackCoin daemon connection
uv run --active python3 -c "
import pyblackcointools
print('BlackCoin integration working')
"

# Test RPC communication
uv run --active python3 -c "
from bitcoinrpc.authproxy import AuthServiceProxy
print('RPC integration working')
"
```

## Naming Conventions

### Python Variables
- `variableName` - Class/object members/properties
- `var_name` - Temporary scope variables
- `i,j,k` - Short names for small scope loops

### GUI Variables (Qt Framework)
- `type_variableName` format for UI controls
- Examples: `le_firstName`, `l_statusLabel`, `btn_submitButton`
- Type prefixes: `l` (QLabel), `le` (QLineEdit), `btn` (QPushButton)

### Functions and Classes
- `function_name` for functions (snake_case)
- `ClassName` for classes (PascalCase)
- `CONSTANT_NAME` for constants
- `global_variable` for module-level variables

## Error Handling and Testing

### Modern Exception Patterns
```python
try:
    # Risky operation
    data = urllib2.urlopen(url).read()
except Exception as e:
    # Log error and continue
    self._debug("Error: " + str(e))
    continue

# Specific exception handling
except urllib2.URLError as e:
    handle_url_error(e)
```

### Type Handling (Python 3.14+)
```python
# String types (Python 3+)
text = text.encode('utf-8') if isinstance(text, str) else text

# String formatting
print(f"Block: {block} | Interval: {interval}")

# Cryptographic types
if re.match('^[0-9a-fA-F]*$', tx):
    tx = bytes.fromhex(tx)
```

## Modernization Phases

### Phase 1: Core Compatibility (Weeks 1-2)
- [ ] Fix print statements (Python 2→3)
- [ ] Resolve import compatibility issues
- [ ] Fix urllib2 → urllib.request references
- [ ] Complete dependency resolution via UV

### Phase 2: Build System Modernization (Weeks 3-4)
- [ ] Apply legacy build patterns to modern approach
- [ ] Create modular build scripts (based on 2014 patterns)
- [ ] Implement platform abstraction layer
- [ ] Setup cross-compilation toolchains

### Phase 3: Cross-Platform Integration (Weeks 5-6)
- [ ] PyInstaller cross-compilation setup
- [ ] Qt6 runtime bundling
- [ ] BlackCoin daemon integration
- [ ] Platform-specific optimizations

### Phase 4: Automation & Testing (Weeks 7-8)
- [ ] GitHub Actions workflow setup
- [ ] Multi-platform testing matrix
- [ ] Automated release pipeline
- [ ] Performance optimization

### Phase 5: Distribution (Weeks 9-10)
- [ ] Code signing setup
- [ ] Platform-specific installers
- [ ] Distribution channel preparation
- [ ] Final testing and validation

## Critical Development Notes

### What Works Now (Safe to Use)
- ✅ Python 3.14.2 environment
- ✅ PyQt6 imports and GUI startup
- ✅ UV package management
- ✅ Test suite (32/32 passing)
- ✅ Basic cryptocurrency integration

### What Needs Fixing (Use with Caution)
- 🔧 Print statements in multiple files
- 🔧 Import compatibility issues
- 🔧 Legacy BitMessage module
- 🔧 Cross-compilation setup

### Legacy Build Script Resources
The `BUILD SCRIPTS ETC/` folder contains **valuable 2014 patterns** that provide an excellent foundation for modern cross-platform builds. These proven patterns should guide the modernization approach.

## Security Considerations

### Key Management
- Never commit private keys
- Use secure random number generation
- Implement proper key rotation
- Validate all cryptographic inputs

### Application Security
- Sanitize user inputs
- Implement proper access controls
- Use secure communication protocols
- Log security-relevant events

## Documentation Resources

### Key Documents
- `agent/TODO.md` - Detailed modernization roadmap
- `agent/ARCHITECTURE.md` - Current codebase analysis
- `agent/CRYPTOCURRENCIES.md` - Multi-currency support details
- `agent/BLACKHALO.md` - Startup/shutdown procedure analysis
- `agent/BUILD_SCRIPTS_ANALYSIS.md` - Legacy build pattern modernization
- `agent/CROSSCOMPILATION.md` - Cross-platform distribution strategy
- `agent/MODERNIZATION_SUMMARY.md` - Executive summary and roadmap

This codebase represents a sophisticated cryptocurrency platform with smart contracts and decentralized exchange functionality. The UV-based workflow and legacy build pattern analysis provide a solid foundation for successful modernization to Python 3.14 + PyQt6 with cross-platform distribution capability.