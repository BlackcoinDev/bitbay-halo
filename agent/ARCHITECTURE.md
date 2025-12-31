# BlackHalo Architecture Analysis

## Iteration 1: System Architecture and File Organization

### Core Application Structure

The BlackHalo codebase is organized as a monolithic Python application with **49,664 lines** in the primary `Halo.py` file, making it one of the most substantial cryptocurrency applications ever written in Python.

```
BlackHalo Architecture (87,966 lines total in root Python files)
├── Halo.py (49,664 lines)              # Primary application engine
├── ANewBitHalo.py (8,197 lines)        # Alternative GUI implementation  
├── BitMHalo.py (1,404 lines)           # BitMessage integration bridge
├── ATemplates.py (5,926 lines)         # Template management system
├── Bitmessage/                          # BitMessage protocol implementation
│   ├── bitmessageqt/ (4,169 lines)     # PyQt4 GUI components
│   ├── pyelliptic/                     # Cryptographic primitives
│   ├── class_*.py (10+ files)          # Core threading classes
│   └── [30+ other modules]
├── pyblackcointools/                   # BlackCoin cryptocurrency integration
├── pybitcointools/                     # Bitcoin utilities
├── pybitcoincashtools/                 # Bitcoin Cash support
└── gui/                               # Qt-based user interface
    ├── styles/                        # QSS style sheets
    ├── forms/                         # Qt Designer UI files
    ├── images/                        # GUI assets
    └── fonts/                         # Custom typography
```

### Entry Points and Launch Sequence

**Primary Launch Path:**
1. `Halo.py` - Main application entry (49,664 lines)
2. Initializes Qt application and main window
3. Loads configuration from `Halo.cfg`
4. Starts multiple specialized threads
5. Connects to cryptocurrency daemon (blackmored)

**Alternative Launch Path:**
1. `ANewBitHalo.py` - Alternative GUI implementation (8,197 lines)
2. Uses different UI framework approach
3. May provide different feature set

**BitMessage Bridge:**
1. `BitMHalo.py` - Communication bridge (1,404 lines)
2. XML-RPC server on port 8878
3. Integrates email/BitMessage protocols
4. Provides encrypted communication layer

### Configuration Architecture

**Main Configuration System:**
- `Halo.cfg` - Primary configuration file
- Delimiter-based parsing with `=`
- Multiple coin-specific configs:
  - `Halo - BlackHalo Config.cfg`
  - `Halo - BitBay Config.cfg` 
  - `Halo - BitHalo Config.cfg`

**Key Configuration Sections:**
```python
# Private key management
PrivKeyFilename1, PrivKeyFilename2
PrivKeyFiledir1, PrivKeyFiledir2
keysconnected

# Communication settings
BitMessage, EnableBM, EnableEmail

# Market and trading
Market, Spam, Wizard
accounttype, language, Debug
```

### Dependency Architecture

**Core Dependencies (External):**
- PyQt4/PyQt6 (GUI framework)
- pyelliptic (cryptographic library)
- bitcoinrpc.authproxy (RPC communication)
- pyzmail (email integration)
- stopit (threading control)

**Internal Dependencies:**
- pyblackcointools (custom BlackCoin implementation)
- pybitcointools (Bitcoin utilities)
- pybitcoincashtools (Bitcoin Cash support)
- BitMessage modules (encrypted messaging)

## Iteration 2: Threading and Concurrency Architecture

### Multi-Threaded Design Pattern

BlackHalo implements a **sophisticated multi-threaded architecture** with 8+ specialized threads running simultaneously to handle different aspects of the cryptocurrency platform.

### Thread Architecture Overview

**Thread Hierarchy (8 Primary Threads):**

```python
# 1. RPC Thread (lines 9164-9723)
class RPCThread(QtCore.QThread):
    """XML-RPC API server for external communication"""
    - Port 8878 for external API access
    - Handles configuration changes
    - Manages application state queries
    
# 2. BitMessage Thread (lines 9724-10102)  
class BitMessageThread(QtCore.QThread):
    """Encrypted communication and email bridge"""
    - SMTP/IMAP protocol handling
    - BitMessage integration
    - Message delivery and processing
    
# 3. BlackCoin Thread (lines 10103-12296)
class BlackCoinThread(QtCore.QThread):
    """Cryptocurrency daemon communication"""
    - RPC calls to blackmored daemon
    - Balance monitoring and updates
    - Transaction broadcasting
    - Staking operations
    
# 4. Download Thread (lines 12297-13200)
class DownloadThread(QtCore.QThread):
    """Blockchain synchronization and data download"""
    - Electrum server synchronization
    - Blockchain data downloading
    - Peer-to-peer network coordination
    
# 5. Python Thread (lines 8334-8357)
class PythonThread(QtCore.QThread):
    """Smart contract execution environment"""
    - Python contract logic execution
    - Sandboxed code execution
    - Dynamic contract loading
    
# 6. Bridge Thread (lines 8358-8917)
class BridgeThread(QtCore.QThread):
    """Safe file operations and data bridge"""
    - Safe file saving operations
    - Data synchronization between threads
    - Backup and recovery operations
    
# 7. File Thread (lines 8918-9163)
class FileThread(QtCore.QThread):
    """File system operations and storage"""
    - Configuration file management
    - Log file operations
    - Data persistence layer
    
# 8. Peg Thread (lines 2722-2800)
class PegThread(QtCore.QThread):
    """Dynamic currency pegging system"""
    - BitBay pegged currency management
    - Exchange rate tracking
    - Bridge operations
```

### Thread Communication Patterns

**Qt Signal/Slot System:**
```python
# Thread communication via Qt signals
QtCore.QObject.connect(thread, QtCore.SIGNAL("finished()"), self.update_ui)
QtCore.QObject.connect(thread, QtCore.SIGNAL("dataReady"), self.process_data)
```

**Shared State Management:**
```python
# Global shared state (Halo.py:133-134)
global CoinSelect
CoinSelect = {}  # Cryptocurrency configuration

# Thread-safe shared variables
shared.knownNodes = {}  # Network node management
shared.config = {}      # Configuration state
shared.myapp = None     # Application instance
```

**RPC Communication:**
```python
# BlackCoin daemon communication pattern
BLKurl = 'http://'+CoinSelect['rpcuser']+':'+CoinSelect['rpcpassword']+'@localhost:'+CoinSelect['rpcport']
BLK = AuthServiceProxy(BLKurl)

# Standard Bitcoin RPC calls
BLK.getblockcount()
BLK.getconnectioncount()
BLK.getbestblockhash()
```

### Concurrency Challenges

**Thread Synchronization:**
- Multiple threads accessing shared configuration
- Cryptocurrency state synchronization across threads
- File I/O coordination between threads
- GUI updates from background thread execution

**Deadlock Prevention:**
- Qt's event loop coordination
- Thread-safe shared state management
- Timeout mechanisms for long-running operations

## Iteration 3: GUI and User Interface Architecture

### Dual GUI Framework Approach

BlackHalo implements **two different GUI frameworks** running in parallel, creating a complex interface architecture.

### Primary GUI: PyQt4/PyQt6 Hybrid (Halo.py)

**Main Window Implementation:**
```python
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(809, 620)
        MainWindow.setStyleSheet(_fromUtf8('font: 11px "Arial Unicode MS";'))
```

**Mixed Framework Challenges:**
- Generated PyQt4 UI code (lines 3-6: "Created by PyQt4 UI code generator 4.10.4")
- Modern PyQt6 imports (lines 19-23: `from PyQt6 import QtCore, QtGui, QtWebEngineWidgets...`)
- Compatibility layer for PyQt4 → PyQt6 migration

### Alternative GUI: ANewBitHalo.py (8,197 lines)

**Complete Alternative Implementation:**
- Separate main window class
- Different layout and widget management
- Independent of Halo.py GUI code
- May provide enhanced or different functionality

### GUI Resource Management

**Style System Architecture:**
```
gui/
├── styles/
│   ├── base_rc.py (19,632 lines)     # Base style definitions
│   ├── bay_rc.py (8,730 lines)       # BitBay theme
│   └── [theme-specific files]
├── forms/                             # Qt Designer UI files
├── images/                           # GUI assets and icons
└── fonts/                            # Custom typography
```

**Dynamic Style Loading:**
```python
# Style sheet management (Halo.py:63)
MainWindow.setStyleSheet(_fromUtf8('font: 11px "Arial Unicode MS";'))

# Multi-theme support
if window.language != "DEFAULT" and window.language != "en":
    # Load language-specific styles
    if window.language not in window.translations:
        window.translations[window.language] = {}
```

### Internationalization Architecture

**Multi-Language Support System:**
```python
def _translate(context, text, disambig=None):
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    if window.language != "DEFAULT" and window.language != "en":
        if window.language not in window.translations:
            window.translations[window.language] = {}
        if text not in window.translations[window.language]:
            if text == "":
                return ""
            window.translist.append(text)
        else:
            translateThis = ast.literal_eval(window.translations[window.language][text])
            return str(translateThis)
    return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
```

**Translation Management:**
- Real-time language switching
- Dynamic text collection (`window.translist.append(text)`)
- Support for multiple languages simultaneously
- Integration with external translation services

### Widget Architecture and Naming Conventions

**GUI Variable Naming (per gui/README.md):**
```python
# Class/object members/properties
variableName = "value"

# Temporary scope variables  
var_name = "temporary"

# UI control naming: type_variableName
le_firstName      # QLineEdit for first name
l_statusLabel     # QLabel for status display
btn_submitButton  # QPushButton for submit action

# Type prefixes:
# l = QLabel, le = QLineEdit, btn = QPushButton
```

### Form Generation and Dynamic UI

**Dynamic Form Creation:**
- Contract-specific form generation
- Market order interface (`gui/marketorderdlg.py`)
- Help system integration (`gui/helpbox.py`)
- Real-time data display widgets

**Qt Designer Integration:**
- UI files in `gui/forms/` directory
- Generated Python classes from .ui files
- Manual UI code generation (PyQt4 generator comments)

### Web Integration Architecture

**Embedded Web Components:**
```python
from PyQt6 import QtWebEngineWidgets, QtWebEngineCore
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
```

**Web-based Features:**
- Blockchain explorer integration
- Market data display
- External service integration
- Real-time web content updates

## Iteration 4: Cryptocurrency and Blockchain Integration Architecture

### Multi-Cryptocurrency Support System

BlackHalo implements a **sophisticated multi-cryptocurrency architecture** supporting Bitcoin, BlackCoin, and BitBay through a unified interface system.

### Cryptocurrency Selection Architecture

**Dynamic Coin Selection System:**
```python
# Global coin configuration (Halo.py:133-134)
global CoinSelect
CoinSelect = {}

# Coin definitions (from agent documentation)
CoinSelect = {
    'BTC': {'name': 'Bitcoin', 'version': 'BitHalo'},
    'BAY': {'name': 'BitBay', 'version': 'Halo'}, 
    'BLK': {'name': 'BlackCoin', 'version': 'BlackHalo'}
}
```

**Configuration-Driven Architecture:**
- Single codebase supports multiple cryptocurrencies
- Runtime coin selection via configuration
- Shared smart contract engine across all coins
- Unified GUI with coin-specific adaptations

### BlackCoin Integration (Primary Focus)

**BlackCoin Daemon Communication:**
```python
# RPC Configuration (Halo.py:517-522)
NewCoin['daemon']="blackmored"           # Official BlackCoin node (Bitcoin Core v26.2.0)
NewCoin['rpcuser']="blackcoinrpc"
NewCoin['rpcpassword']="32w54er56t7y89j8h34w5e6t7y89ik34sAs4"
NewCoin['rpcport']="15715"               # Blackcoin More port
```

**RPC Communication Pattern:**
```python
# BlackCoinThread implementation (lines 10103-12296)
BLKurl = 'http://'+CoinSelect['rpcuser']+':'+CoinSelect['rpcpassword']+'@localhost:'+CoinSelect['rpcport']
BLK = AuthServiceProxy(BLKurl)

# Standard Bitcoin Core RPC calls
BLK.getblockcount()
BLK.getconnectioncount() 
BLK.getbestblockhash()
```

### pyblackcointools Architecture (Custom Library)

**Internal BlackCoin Implementation:**
```
pyblackcointools/
├── main.py          # Core cryptographic functions
├── transaction.py   # Transaction handling  
├── deterministic.py # Key derivation
├── bci.py          # Blockchain interaction
└── composite.py    # Multi-signature operations
```

**Custom vs External Dependencies:**
- **Critical Finding**: All BlackCoin functionality is **custom-integrated**
- No external BlackCoin-specific Python packages required
- Internal implementation provides full BlackCoin support
- Direct integration with BlackCoin daemon

**Python 2.7 → 3.14 Migration Requirements:**
```python
# bci.py line 2: Required changes
import urllib2                    # OLD
import urllib.request as urllib2   # NEW

# main.py: Print statement conversion  
print message                    # OLD
print(message)                   # NEW
```

### Smart Contract Execution Engine

**Python Contract Architecture:**
```python
# PythonThread (lines 8334-8337)
class PythonThread(QtCore.QThread):
    """Thread for any special Python contracts or API calls"""
    - Sandboxed Python code execution
    - Dynamic contract loading
    - Smart contract logic processing
    - External API integration
```

**Contract Types Supported:**
1. **Simple Escrow Contracts** - Basic two-party escrow
2. **Employment Contracts** - Work-for-hire arrangements  
3. **Barter Contracts** - Asset exchange agreements
4. **Custom Python Contracts** - User-defined logic
5. **Joint Accounts** - Multi-signature shared wallets

**Contract Examples (custom/ directory):**
- `Demo1.py` - Contract form customization
- `Demo2.py` - Escrow panel customization
- `Demo3.py` - Advanced contract logic

### Multi-Signature Architecture

**Composite Operations System:**
```python
# pyblackcointools/composite.py
# Multi-signature address creation
# Joint account management  
# Threshold signature schemes
# Multi-signature transaction coordination
```

**Two-Key Account System:**
- Primary and secondary private keys
- Separate password requirements per key
- Enhanced security through dual authorization
- Support for cold staking operations

### BitBay Dynamic Currency System

**Pegged Currency Architecture:**
```python
# BitBay-specific RPC methods (NOT Blackcoin-specific)
BLK.getpeginfo()          # BitBay pegged currency system
BLK.getfractions(txid)    # BitBay liquid/reserve tracking
BLK.bridges()             # BitBay cross-chain bridges
BLK.merklesin()           # BitBay merkle operations
BLK.merklesout()          # BitBay merkle operations
BLK.listfrozen()          # BitBay frozen funds management
```

**Dynamic Currency Features:**
- Inflation/deflation controls through voting
- Algorithmic interest rate management
- Bond-like instruments and advanced contracts
- Self-banking capabilities

### Blockchain Synchronization Architecture

**DownloadThread Implementation:**
```python
class DownloadThread(QtCore.QThread):
    """For BitHalo electrum server and general downloading"""
    - Electrum server synchronization
    - Blockchain data downloading  
    - Network synchronization
    - Peer management
```

**Electrum Integration:**
```python
import electrumaccessor as ea  # Electrum synchronization
```

**Blockchain Data Management:**
- Real-time blockchain synchronization
- Transaction verification and validation
- Network peer coordination
- Block height tracking and updates

### Security Architecture

**Cryptographic Foundation:**
```python
# Crypto imports and usage
import Crypto  # General crypto functions
from Crypto.Cipher import AES  # AES Encryption
from Crypto.Hash import SHA256  # Hash functions
import pyelliptic  # ECC implementation using OpenSSL
```

**Security Features:**
- ECC key agreement (ECDH)
- Digital signatures (ECDSA)
- Hybrid encryption (ECIES)
- AES-256 symmetric encryption
- CSPRNG and HMAC-SHA512
- Multi-signature security model
- Two-factor authentication support

This architecture represents one of the most sophisticated cryptocurrency platforms ever implemented, combining smart contracts, multi-currency support, and advanced security features in a single Python application.