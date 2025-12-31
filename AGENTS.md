# Agent Guidelines for BlackHalo Development

## Build and Test Commands

### Primary Build Scripts
```bash
# Main application build
./bitmhalo.sh                           # Build BitMHalo with PyInstaller

# Linux cryptocurrency daemon build
./BUILD SCRIPTS ETC/linux.sh --build    # Build BlackCoin daemon
./BUILD SCRIPTS ETC/linux.sh --reset    # Reset and rebuild environment

# Alternative build scripts
./BUILD SCRIPTS ETC/osx64.sh            # macOS build
./BUILD SCRIPTS ETC/win32.sh            # Windows build
./LinuxHaloSetup.sh                     # Linux setup and build
```

### Test Commands
```bash
# Run blockchain API tests
python testblock.py                     # Run main test suite

# BitMessage tests
cd Bitmessage && python tests.py        # Run BitMessage unit tests
cd Bitmessage-BitMHalo-v0.6 && python -m pytest src/  # PyBitmessage tests

# Single test execution
python -m unittest testblock.bitcoinapi.stat_hash
python -m pytest Bitmessage/tests.py::test_specific_function
```

### Development Setup
```bash
# Install dependencies (Python 2.7)
pip install -r Bitmessage-BitMHalo-v0.6/requirements.txt

# Manual dependency installation
pip install PyQt4 python-qt4 pyzmail stopit xmlrpclib

# Install build tools
pip install pyinstaller
```

## Code Style Guidelines

### Python Version and Compatibility
- **Python 2.7+** required (this is legacy codebase)
- No Python 3+ features or syntax
- Use `print` statements (not functions)
- Handle `unicode` vs `str` differences explicitly

### Import Conventions
```python
# Standard library imports first
import urllib2
import re
import time
import calendar
import datetime

# Third-party imports
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyzmail

# Local imports last
from custom.Demo1 import *
import pyblackcointools
```

### Naming Conventions

**Python Variables** (from gui/README.md):
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

### Formatting Rules

**Indentation**:
- Use 4 spaces (no tabs)
- Align with opening delimiter for hanging indents

**Line Length**:
- Maximum 120 characters preferred
- Break long lines at logical operators

**Spacing**:
- No spaces around `=` in keyword arguments
- Single space around binary operators
- No space after function names in calls

### Error Handling

**Exception Patterns**:
```python
try:
    # Risky operation
    data = urllib2.urlopen(url).read()
except Exception, e:
    # Log error and continue
    self._debug("Error: " + str(e))
    continue

# Specific exception handling
except urllib2.URLError, e:
    handle_url_error(e)
```

**Error Recovery**:
- Always provide fallback mechanisms
- Log errors with debug levels
- Continue processing when possible
- Use meaningful error messages

### Type Handling

**String Types** (Python 2.7):
```python
# Handle unicode/str differences
if isinstance(text, unicode):
    text = text.encode('utf-8')

# String formatting
print "Block: %d | Interval: %s" % (block, interval)
```

**Cryptographic Types**:
```python
# Binary data handling
if re.match('^[0-9a-fA-F]*$', tx):
    tx = tx.decode('hex')

# Address validation
if addr[0] == 'b':
    return mk_scripthash_script(addr)
```

### GUI Development

**Qt Framework Rules**:
- Use PyQt4 (legacy version)
- Follow UI naming schema strictly
- Implement proper signal/slot connections
- Handle widget cleanup in destructors

**Form Development**:
- Use Qt Designer .ui files
- Generate Python classes with `pyuic4`
- Implement custom validation in form classes
- Use internationalization ready patterns

### Cryptographic Code

**Security Practices**:
- Always validate input parameters
- Use proper key derivation functions
- Implement proper random number generation
- Never log private keys or sensitive data

**Blockchain Integration**:
- Handle network timeouts gracefully
- Implement retry logic for API calls
- Validate transaction formats strictly
- Use proper fee calculation methods

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

### Configuration Management

**Config File Handling**:
- Parse Halo.cfg with delimiter-based structure
- Validate all configuration parameters
- Provide sensible defaults
- Handle missing config files gracefully

**Environment Variables**:
- Support both env vars and config files
- Validate environment-specific settings
- Document all configuration options

### Testing Guidelines

**Unit Test Structure**:
- Place tests in testblock.py or dedicated test files
- Use unittest framework
- Mock external API calls
- Test both success and failure cases

**Integration Testing**:
- Test complete contract workflows
- Validate multi-signature operations
- Test cross-currency functionality
- Verify GUI interactions

### Documentation Standards

**Code Comments**:
- Explain complex algorithms
- Document public API methods
- Include usage examples
- Mark deprecated features

**Function Documentation**:
```python
def process_escrow_contract(self, contract_data):
    """Process escrow contract with double deposit mechanism.
    
    Args:
        contract_data (dict): Contract parameters including deposits and terms
        
    Returns:
        dict: Processing result with status and transaction data
    """
```

### Git Workflow

**Commit Guidelines**:
- Write clear commit messages
- Group related changes
- Test before committing
- Follow existing file organization

**Branch Strategy**:
- Use feature branches for new functionality
- Keep master branch stable
- Document breaking changes
- Tag releases appropriately

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

### Performance Guidelines

**Optimization Priorities**:
- Minimize blockchain API calls
- Cache frequently used data
- Use efficient data structures
- Implement proper garbage collection

**Memory Management**:
- Clean up Qt resources properly
- Avoid memory leaks in long-running operations
- Use context managers for file operations
- Monitor memory usage in test cases

This codebase represents a sophisticated cryptocurrency platform with smart contracts and decentralized exchange functionality. Follow these guidelines to maintain code quality and compatibility with the existing architecture.