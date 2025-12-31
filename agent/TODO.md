# BlackHalo TODO List - Python 3.14 + PyQt6 Migration

## Current Status Analysis

### ✅ Already Completed
- **Python 3.14.2** - Confirmed working
- **PyQt6 imports** - Present in main files
  - `Halo.py`: `from PyQt6 import QtCore, QtGui, QtWebEngineWidgets, QtWidgets, sip, uic`
  - `gui/mainwindow.py`: `from PyQt6 import QtCore, QtGui, QtWebEngineCore, QtWebEngineWidgets, QtWidgets, uic`
  - `gui/styles/*.py`: PyQt6 imports present
- **UV Environment** - PyQt6 dependencies installed and working
- **Test Suite** - 32/32 tests passing
- **Legacy Build Analysis** - BUILD SCRIPTS ETC folder analyzed for proven patterns

### 🚨 Critical Issues Found
- **Print statements** still exist in multiple files (Python 2 syntax)
- **Import compatibility issues** with missing dependencies
- **Mixed Qt usage patterns** (some PyQt4 patterns still present)
- **BitMessage module** still using Python 2.7 patterns

### 🏗️ Legacy Build Script Insights (2014 → 2025)
**Valuable patterns found in BUILD SCRIPTS ETC:**
- **Modular build architecture** - Excellent foundation for modern scripts
- **Platform abstraction concepts** - Cross-compilation patterns still valid
- **Dependency verification strategies** - Proven approach for build environments
- **Pre-built library fallback** - LevelDB strategy adaptable to Python components
- **Static linking approach** - Single executable distribution model

**Modern adaptations:**
- **Debian 7 (2014)** → **Ubuntu 24.04 (2025)**
- **MXE cross-compiler** → **Modern MinGW-w64/ARM64 toolchains**
- **Makefile builds** → **PyInstaller/CMake modern approach**
- **apt dependencies** → **UV package management**
- **Manual testing** → **Automated CI/CD**

## Phase 1: Python 3.14 Compatibility (Week 1-2)

### High Priority Tasks

#### 1.1 Fix Print Statements
**Status**: 🔴 Critical - Multiple files affected
```python
# Files needing print statement conversion:
- pybitcointools/deterministic.py
- pybitcointools/mnemonic.py  
- highlevelcrypto.py
- pyblackcointools/main.py
- pyblackcointools/bci.py
- test_pyblackcointools.py
- test_pyelliptic.py
```

**Commands to run**:
```bash
# Convert print statements to Python 3 syntax
find . -name "*.py" -exec sed -i 's/^print \([^=].*\)$/print(\1)/g' {} \;
find . -name "*.py" -exec sed -i 's/^print \([^=].*\)$/print(\1)/g' {} \;
```

#### 1.2 Fix Import Compatibility
**Status**: 🔴 Critical - Import errors in key files

**Files needing import fixes**:
```python
# BitMHalo.py
import xmlrpclib  # Should be: import xmlrpc.client as xmlrpc_client
import pyzmail    # Already installed via UV
import stopit     # Already installed via UV

# Halo.py  
import PyQt6.QtCore  # Missing - add to requirements
```

#### 1.3 Update String Handling
**Status**: 🟡 Medium - Unicode/string compatibility
```python
# Replace Python 2 patterns:
unicode(text)              # → str(text) or handle encoding explicitly
text.encode('utf-8')       # → text.encode('utf-8') if isinstance(text, str)
string.letters             # → string.ascii_letters
```

#### 1.4 Fix urllib2 References
**Status**: 🔴 Critical - Python 3 compatibility
```python
# Files needing urllib2 → urllib.request migration:
- pyblackcointools/bci.py
- BitMessage modules
- Halo.py (some references)
```

## Phase 2: PyQt6 Migration Completion (Week 3-4)

### High Priority Tasks

#### 2.1 Complete Qt Import Updates
**Status**: 🟡 In Progress - Main files updated, need verification

**Check and fix remaining PyQt4 patterns**:
```python
# Look for PyQt4 specific patterns:
QtGui.QApplication.UnicodeUTF8  # → Removed in PyQt6, use encoding param
QtCore.SIGNAL, QtCore.SLOT     # → Use new style signals in PyQt6
```

#### 2.2 Update Qt API Calls
**Status**: 🟡 Medium - Some API changes between PyQt4→PyQt6

**Common PyQt6 API changes**:
```python
# QApplication
QtWidgets.QApplication.UnicodeUTF8  # → Remove, use encoding parameter
QtWidgets.QApplication.translate()  # → Same but check encoding

# Signals/Slots
QtCore.SIGNAL("signal()")           # → QtCore.pyqtSignal()
QtCore.SLOT("slot()")               # → Not needed in PyQt6
```

#### 2.3 Update Web Engine Usage
**Status**: 🟡 Medium - Already using PyQt6.QtWebEngine*

**Verify web components**:
```python
# Already using PyQt6 imports:
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
```

#### 2.4 Update UI File Generation
**Status**: 🟡 Low - Future consideration

**Consider regenerating .ui files with PyQt6**:
```bash
# If .ui files need regeneration:
pyuic6 mainwindow.ui -o mainwindow_py6.py
```

## Phase 3: Dependency Management (Week 5-6)

### High Priority Tasks

#### 3.1 Update requirements.txt
**Status**: ✅ Completed - Modern requirements with PyQt6

#### 3.2 Fix Missing Dependencies
**Status**: 🔴 Critical - Some imports failing

**Install missing packages via UV**:
```bash
uv add xmlrpc-client pycryptodome stopit pyzmail39
uv add psutil  # For cross-platform process management
uv add requests  # For HTTP operations
```

#### 3.3 Update BitMessage Integration
**Status**: 🔴 Critical - BitMessage module needs Python 3 updates

**Priority fixes**:
```python
# BitMessage/bitmessagemain.py
import xmlrpc.client as xmlrpc_client  # Python 3 compatibility
import urllib.request as urllib2       # Replace urllib2
print statements → print() functions
```

## Phase 4: Testing and Validation (Week 7-8)

### High Priority Tasks

#### 4.1 Test Core Functionality
**Status**: 🟡 Pending - Need to verify after fixes

**Test checklist**:
```bash
# Core imports
python3 -c "import PyQt6.QtWidgets; print('PyQt6 working')"
python3 -c "import pyblackcointools; print('BlackCoin tools working')"
python3 -c "import Bitmessage.class_api; print('BitMessage working')"

# Main application startup test
python3 Halo.py  # Should start without errors
```

#### 4.2 Fix Remaining Test Failures
**Status**: 🟡 Pending - Dependent on above fixes

#### 4.3 Integration Testing
**Status**: 🟡 Pending - After individual components work

## Phase 5: Cross-Platform Preparation (Week 9-10)

### Medium Priority Tasks

#### 5.1 Platform Abstraction Implementation
**Status**: 🟡 Future - Prepare for cross-platform distribution

**See CROSSCOMPILATION.md for detailed setup**

## Success Criteria

### Phase 1 Success:
- [ ] `python3 Halo.py` starts without import errors
- [ ] All print statements converted to Python 3 syntax
- [ ] Core PyQt6 imports working
- [ ] BitMessage module loads without errors

### Phase 2 Success:
- [ ] GUI starts and displays properly
- [ ] No PyQt4 compatibility warnings
- [ ] Web engine components functional
- [ ] Main window loads without errors

### Phase 3 Success:
- [ ] All dependencies resolved
- [ ] UV environment contains all required packages
- [ ] Test suite passes (32/32 tests)
- [ ] BlackCoin integration functional

### Phase 4 Success:
- [ ] Core smart contract functionality works
- [ ] BlackCoin daemon connection established
- [ ] Multi-signature operations functional
- [ ] No critical runtime errors

## Rollback Plan

If migration fails at any point:

1. **Create backup**: `git stash` current state
2. **Rollback command**: `git stash pop` to restore working state
3. **Isolation testing**: Test individual components separately
4. **Incremental approach**: Fix one module at a time

## Command Reference

```bash
# Development environment
uv sync                    # Sync dependencies
uv run --active python3 Halo.py  # Run with UV environment
uv run --active pytest tests/    # Run tests

# Python 3 fixes
find . -name "*.py" -exec sed -i 's/print \([^=].*\)$/print(\1)/g' {} \;
find . -name "*.py" -exec sed -i 's/import urllib2$/import urllib.request as urllib2/g' {} \;

# PyQt6 verification  
python3 -c "from PyQt6 import QtWidgets; app = QtWidgets.QApplication([]); print('PyQt6 working')"

# Test run
uv run --active python3 testblock.py
```

## Notes

- **Incremental approach**: Fix one component at a time, test frequently
- **UV environment**: Always use `uv run --active` for testing
- **Backup strategy**: Keep working state before major changes
- **Cross-platform prep**: See CROSSCOMPILATION.md for distribution planning