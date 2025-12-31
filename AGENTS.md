# Agent Guidelines for BlackHalo Development

## Build and Test Commands (UV-Based)

### Primary Build Scripts
```bash
# Modern UV-based cross-platform build
python3 build.py                    # Run modernized UV build script

# Legacy build scripts (may need modernization)
./bitmhalo.sh                       # Build BitMHalo with PyInstaller
./BUILD SCRIPTS ETC/linux.sh --build    # Build BlackCoin daemon
./BUILD SCRIPTS ETC/linux.sh --reset    # Reset and rebuild environment
./BUILD SCRIPTS ETC/osx64.sh        # macOS build
./BUILD SCRIPTS ETC/win32.sh        # Windows build
./LinuxHaloSetup.sh                 # Linux setup and build
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

# Install legacy dependencies if needed
uv add -r Bitmessage-BitMHalo-v0.6/requirements.txt  # If file exists
```

## Code Style Guidelines

### Python Version and Compatibility
- **Python 3.8+** required for core functionality (Python 3.14+ preferred)
- **Legacy Python 2.7** code exists but being migrated
- Use `print()` functions (not statements) for Python 3+
- Handle `unicode` vs `str` differences explicitly
- Use compatibility imports: `try: import urllib.request as urllib2`

### Import Conventions
```python
# Standard library imports first
import urllib2
import re
import time
import calendar
import datetime

# Third-party imports (managed by UV)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import pyzmail

# Local imports last
from custom.Demo1 import *
import pyblackcointools
```

### Code Formatting
- **Line Length**: Maximum 120 characters (configured in .flake8, pyproject.toml)
- **Indentation**: 4 spaces (no tabs)
- **Formatter**: Use `black` with line-length=120 for new code
- **Import Sorting**: Use `isort` with black profile
- **Excluded Paths**: Bitmessage-BitMHalo-v0.6, BUILD SCRIPTS ETC, bridge, data, agent, BitMData, images

### Linting Configuration
- **flake8**: Max line length 120, extensive legacy ignores for compatibility
- **pylint**: Only Error (E) and Fatal (F) messages enabled, ignores legacy patterns
- **Custom Scripts**: Use `uv run --active python3 tests/scripts/lint.py` for comprehensive checks

### Naming Conventions

**Python Variables**:
- `variableName` - Class/object members/properties
- `var_name` - Temporary scope variables
- `i,j,k` - Short names for small scope loops

**GUI Variables**:
- `type_variableName` format for UI controls
- Examples: `le_firstName`, `l_statusLabel`, `btn_submitButton`
- Type prefixes: `l` (QLabel), `le` (QLineEdit), `btn` (QPushButton)

**Functions and Classes**:
- `function_name` for functions (snake_case)
- `ClassName` for classes (PascalCase)
- `CONSTANT_NAME` for constants
- `global_variable` for module-level variables

### Error Handling

**Exception Patterns**:
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

**Error Recovery**:
- Always provide fallback mechanisms
- Log errors with debug levels
- Continue processing when possible
- Use meaningful error messages

### Type Handling

**String Types** (Python 3+):
```python
# Handle string types
text = text.encode('utf-8') if isinstance(text, str) else text

# String formatting
print(f"Block: {block} | Interval: {interval}")
```

**Cryptographic Types**:
```python
# Binary data handling
if re.match('^[0-9a-fA-F]*$', tx):
    tx = bytes.fromhex(tx)

# Address validation
if addr[0] == 'b':
    return mk_scripthash_script(addr)
```

### GUI Development

**Qt Framework Rules**:
- Use PyQt6 for new development (migrating from PyQt4)
- Follow UI naming schema strictly
- Implement proper signal/slot connections
- Handle widget cleanup in destructors

**Form Development**:
- Use Qt Designer .ui files
- Generate Python classes with `pyuic6` (PyQt6)
- Implement custom validation in form classes
- Use internationalization ready patterns

### Threading Guidelines

**Multi-threading Patterns**:
```python
# Qt thread communication
QtCore.QObject.connect(thread, QtCore.SIGNAL("finished()"), self.update_ui)

# Proper thread cleanup
def stop_thread(self):
    self.thread.terminate()
    self.thread.wait()
```

**RPC Communication**:
- Use separate threads for daemon communication
- Implement timeout handling for RPC calls
- Handle connection failures gracefully
- Cache blockchain data when appropriate

### Security Considerations

**Key Management**:
- Never commit private keys
- Use secure random number generation
- Implement proper key rotation
- Validate all cryptographic inputs

**Application Security**:
- Sanitize user inputs
- Implement proper access controls
- Use secure communication protocols
- Log security-relevant events

## Modernization Status

### Current Challenges
- **Mixed Python Versions**: Legacy Python 2.7 and modern Python 3.14+ code
- **Incomplete PyQt Migration**: Partial PyQt4 to PyQt6 transition
- **Dependency Issues**: Legacy and modern dependencies don't integrate well
- **Platform-Specific Code**: Windows-centric patterns need abstraction

### UV-Based Development Workflow
1. **Initialize**: `uv sync` to install all dependencies
2. **Test**: `uv run --active pytest tests/` to verify functionality
3. **Build**: `uv run --active python3 build.py` for cross-platform builds
4. **Format**: `uv run --active black . --line-length=120` for code formatting

### Recommended Approach
1. **Phase 1**: Use UV for consistent dependency management ✅
2. **Phase 2**: Complete PyQt4 to PyQt6 migration
3. **Phase 3**: Consolidate dependencies and create unified build system
4. **Phase 4**: Test cross-platform functionality

This codebase represents a sophisticated cryptocurrency platform with smart contracts and decentralized exchange functionality. The UV-based workflow provides reliable cross-platform dependency management for modernization efforts.