# BlackHalo Dependencies

**Generated:** January 2026
**Python:** 3.14+ | **Manager:** UV

## Overview

| Category | Count | Purpose |
|----------|-------|---------|
| #main | 32 | Core runtime dependencies |
| #dev | 9 | Development and testing tools |
| #build | 6 | Build and packaging tools |
| **Total** | **85 packages** | Installed via UV |

---

## #main - Core Runtime Dependencies

### GUI Framework

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **pyqt6** | 6.10.1 | Main GUI framework | `Halo.py`, `gui/mainwindow.py`, `gui/styles/*.py` |
| pyqt6-qt6 | 6.10.1 | Qt6 runtime bindings | PyQt6 dependency |
| pyqt6-sip | 13.10.3 | SIP bindings for PyQt6 | PyQt6 dependency |
| pyqt6-webengine | 6.10.0 | Web engine for embedded browser | `Halo.py`, `gui/mainwindow.py` |
| pyqt6-webengine-qt6 | 6.10.1 | Qt6 web engine bindings | PyQt6 dependency |
| **pillow** | 12.0.0 | Image processing for steganography | `Halo.py:254-255` (Image, ImageQt), `stepic.py:33` |

### Cryptography

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **pycryptodome** | 3.23.0 | AES encryption, hashing | `Halo.py:214,218-219` (Crypto.Cipher.AES, Crypto.Hash.SHA256) |
| **cryptography** | 46.0.3 | OpenSSL bindings, key operations | `Bitmessage/pyopenssl-master/OpenSSL/_util.py` |
| **cffi** | 2.0.0 | C foreign function interface | `Bitmessage/pyopenssl-master/memdbg.py` |
| pycparser | 2.23 | C code parser for cffi | `Bitmessage/pyopenssl-master/memdbg.py` |
| **base58** | 2.1.1 | Bitcoin address encoding | `Halo.py:221`, `src/crypto/__init__.py` |

### Blockchain/RPC

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **python-bitcoinrpc** | 1.0 | Bitcoin Core RPC client | `Halo.py:215-217` (AuthServiceProxy) |
| **pytokens** | 0.3.0 | Token handling | Used in Bitmessage module |
| **six** | 1.17.0 | Python 2/3 compatibility shim | `Bitmessage/pyopenssl-master/*` (Python 2 legacy code) |

### Networking

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **requests** | 2.32.5 | HTTP client | `gtranslate.py:14,170,192` (GET/POST requests) |
| **urllib3** | 2.6.2 | HTTP library (requests dependency) | `Halo.py` via requests |
| **certifi** | 2025.11.12 | SSL certificates | `requests` dependency |
| charset-normalizer | 3.4.4 | Character encoding | `requests` dependency |
| idna | 3.11 | Internationalized domain names | `requests` dependency |
| **pysocks** | 1.7.1 | SOCKS proxy support | `Halo.py:250,491-500` (socks.socksocket, setdefaultproxy) |
| **websocket-client** | 1.9.0 | WebSocket connections | Used in Bitmessage module |
| **wsproto** | 1.3.2 | WebSocket protocol | `trio` dependency |
| **h11** | 0.16.0 | HTTP/1.1 protocol | `trio` dependency |
| **trio** | 0.32.0 | Async I/O framework | Used in Bitmessage module (168 imports) |
| trio-websocket | 0.12.2 | WebSocket for trio | `trio` dependency |
| sniffio | 1.3.1 | Async library detection | `trio` dependency |
| outcome | 1.3.0.post0 | Async result handling | `trio` dependency |

### Browser/Automation

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **selenium** | 4.39.0 | Firefox automation | `Halo.py:256-257,304` (webdriver.Firefox, Options) |
| mechanize | 0.4.10 | Stateful web browsing | `Halo.py:244,294,19883` (mechanize.Browser) |
| **html5lib** | 0.999999999 | HTML5 parser | Used in mechanize (22 imports) |
| webencodings | 0.5.1 | Web encoding utilities | `html5lib` dependency |

### Email/Messaging

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **pyzmail39** | 0.0.2 | Email composition/sending | `BitMHalo.py:38,354` (compose_mail) |
| **yandex-translate** | 0.3.5 | Translation API | `Halo.py:258,305` (YandexTranslate) |
| msgpack | 1.1.2 | Binary serialization | Used in Bitmessage module |

### Data/Serialization

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **ujson** | 5.11.0 | Fast JSON parsing | `Halo.py:253,302,2198` (loads/dumps) |
| **python-bsonjs** | 0.7.0 | BSON serialization | `Halo.py:262,308` (import bsonjs) |
| sortedcontainers | 2.4.0 | Sorted collections | Used in Bitmessage module |

### Images/QRCodes

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **qrcode** | 8.2 | QR code generation | `build.py:38` (included in build) |
| **pydenticon** | 0.3.1 | Identicon generation | `Bitmessage/bitmessageqt/__init__.py` |
| **stepic** | 0.5.0 | Steganography (hidden data in images) | `Halo.py:265` |

### IPC/Interop

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **rpyc** | 6.0.2 | Remote Python procedure calls | `Halo.py:215`, `BitMHalo.py:6` (IPC between server/BitMessage) |

### Translation

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **gtranslate** | - | Google Translate wrapper | `Halo.py:263,309` (gtranslate2) |

### Utilities

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **click** | 8.3.1 | CLI interface | Used in build scripts |
| **packaging** | 25.0 | Package version handling | Used in build system |
| **plumbum** | 1.10.0 | Shell command toolkit | Used in build scripts |
| attrs | 25.4.0 | Attribute utilities | Used in test suite |
| **stopit** | 1.1.2 | Timeout/thread interruption | `build.py:46`, `BitMHalo.py:39` |

---

## #dev - Development & Testing

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **pytest** | 9.0.2 | Test framework | `tests/conftest.py`, all `test_*.py` files |
| pytest-cov | 7.0.0 | Coverage reporting | Test configuration |
| **coverage** | 7.13.1 | Code coverage measurement | CI/CD pipeline |
| **black** | 25.12.0 | Code formatter | `pyproject.toml` config |
| **flake8** | 7.3.0 | Linting | CI/CD checks |
| isort | 7.0.0 | Import sorter | `pyproject.toml` config |
| **mypy** | 1.19.1 | Type checking | Type annotations |
| **pyright** | 1.1.407 | LSP type checking | IDE integration |
| **pylint** | 4.0.4 | Advanced linting | Code quality |
| astroid | 4.0.2 | AST parsing (pylint dependency) | |
| pyflakes | 3.4.0 | Lightweight linting | |
| pycodestyle | 2.14.0 | PEP8 style checker | |
| mccabe | 0.7.0 | Cyclomatic complexity | |
| iniconfig | 2.3.0 | INI file parsing | pytest dependency |

---

## #build - Build & Packaging

| Package | Version | Usage | Location |
|---------|---------|-------|----------|
| **pyinstaller** | 6.17.0 | Standalone executable creation | `build.py` |
| pyinstaller-hooks-contrib | 2025.11 | PyInstaller hook collection | PyInstaller dependency |
| **altgraph** | 0.17.5 | Graph manipulation (PE/ELF) | PyInstaller dependency |
| **macholib** | 1.16.4 | macOS binary handling | PyInstaller dependency |
| **setuptools** | 80.9.0 | Package installation | Legacy build support |
| nodeenv | 1.10.0 | Node.js environment | Build tooling |
| dill | 0.4.0 | Object serialization | PyInstaller dependency |

---

## Dependency Graph

```
# GUI Framework
pyqt6 ──┬── pyqt6-qt6
        ├── pyqt6-sip
        └── pyqt6-webengine ── pyqt6-webengine-qt6
pillow ── (standalone, no deps)

# Cryptography
pycryptodome ── (standalone)
cryptography ──┬── cffi ── pycparser
               └── (OpenSSL bindings)
base58 ── (standalone)

# Networking
requests ──┬── urllib3 ──┬── certifi
           │             ├── charset-normalizer
           │             └── idna
           └── (HTTP client)
pysocks ── (SOCKS proxy)
websocket-client ── (WebSocket)
trio ──┬── trio-websocket ── wsproto
       ├── h11
       ├── sniffio
       └── outcome

# Browser Automation
selenium ── (standalone)
mechanize ──┬── html5lib ──┬─ webencodings
            │             └── (six for py2/3 compat)
            └── (form handling)

# Email/Messaging
pyzmail39 ── (standalone)
yandex-translate ── (standalone)
msgpack ── (standalone)

# Data Serialization
ujson ── (standalone)
python-bsonjs ── (standalone)

# Testing
pytest ──┬── pytest-cov ── coverage
         └── iniconfig

# Build
pyinstaller ──┬── altgraph
              ├── macholib
              ├── pyinstaller-hooks-contrib
              └── dill
setuptools ── (standalone)
```

---

## Run Commands

```bash
# Development
uv run --active python3 Halo.py           # Run application
uv run --active pytest tests/             # Run tests
uv run --active black . --line-length 120 # Format code
uv run --active flake8 .                  # Lint code
uv run --active pytest --cov             # Tests with coverage

# Build
uv run --active python3 build.py          # Build executable
uv pip install -e .                       # Install in dev mode
```

---

## Notes

1. **PyQt6 is the main GUI framework** - All GUI components use PyQt6
2. **selenium/mechanize for web scraping** - Used for market data and automation
3. **trio for async I/O** - Bitmessage uses trio for async operations
4. **pycryptodome for crypto** - Used for AES encryption and hashing
5. **six for Python 2 compatibility** - Only used in legacy Bitmessage code
6. **Build system uses PyInstaller** - Creates standalone executables

---

## Cross-Platform Support

**Target Platforms:** Windows 10+, Ubuntu 22.04+, macOS 13+

### OS-Specific Packages

| Package | Windows | Ubuntu | macOS | Notes |
|---------|---------|--------|-------|-------|
| **types-pywin32** | ✅ | ❌ | ❌ | Windows-only type stubs |
| **librt** | ❌ | ✅ | ✅ | POSIX shared memory (Linux/macOS) |
| **geckodriver** | ✅ | ✅ | ✅ | Required for selenium (Firefox) |

### Platform-Specific Behaviors

| Package | Windows | Ubuntu | macOS |
|---------|---------|--------|-------|
| **selenium** | Works with Firefox | Works with Firefox | Works with Firefox |
| **mechanize** | Works | Full functionality | May need CA cert workaround |
| **Qt6** | Direct3D rendering | X11 libraries needed | Metal rendering |

### System Dependencies by OS

#### Ubuntu 22.04+

```bash
sudo apt update
sudo apt install -y \
    python3.14 \
    python3.14-venv \
    python3.14-dev \
    build-essential \
    libssl-dev \
    libsqlite3-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgtk-3-0 \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    firefox-geckodriver

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows 10+

```powershell
# Install Python 3.14+ from Microsoft Store or python.org
# Enable "Add Python to PATH" during installation

# Install Visual C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Install "Desktop development with C++" workload

# Install Firefox for selenium
# Download from: https://www.mozilla.org/firefox/

# Download geckodriver
# https://github.com/mozilla/geckodriver/releases
# Add to PATH or place in same directory as Firefox
```

#### macOS 13+ (Ventura/Apple Silicon or Intel)

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.14
brew install python@3.14

# Install dependencies
brew install \
    sqlite \
    openssl \
    mesa \
    adwaita-icon-theme \
    hicolor-icon-theme

# Firefox and geckodriver
brew install --cask firefox
brew install geckodriver

# Set OpenSSL flags for Homebrew Python
export LDFLAGS="-L$(brew --prefix openssl)/lib"
export CPPFLAGS="-I$(brew --prefix openssl)/include"

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Platform Detection in Code

```python
# build.py
platform_name = platform.system().lower()  # 'windows', 'darwin', or 'linux'

# pyelliptic/openssl.py
if "darwin" in sys.platform:  # macOS
    # Use macOS-specific OpenSSL path
elif "win32" in sys.platform or "win64" in sys.platform:  # Windows
    # Use Windows-specific OpenSSL path
else:  # Linux
    # Use system OpenSSL
```

### PyInstaller Cross-Compilation

PyInstaller creates platform-specific executables. Build on each target:

| Build On | Produces |
|----------|----------|
| Ubuntu | `.AppImage` for Linux |
| Windows | `.exe` for Windows |
| macOS | `.dmg` for macOS |

**Note:** Cannot cross-compile (e.g., build Windows exe on Linux) without additional setup.
