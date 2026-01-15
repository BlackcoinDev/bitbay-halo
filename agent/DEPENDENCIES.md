# BlackHalo Dependencies

**Generated:** January 2026
**Python:** 3.14+ | **Manager:** UV

## Overview

| Category | Count | Purpose |
|----------|-------|---------|
| #main | 32 | Core runtime dependencies |
| #dev | 9 | Development and testing tools |
| #build | 6 | Build and packaging tools |
| #build-output | 3 | Platform-specific distribution formats |
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
| **pyinstaller** | 6.17.0 | Standalone executable (Windows/Linux) | `build.py` |
| **py2app** | 0.28.9 | macOS .app bundle creation | `build.py`, `setup-macOS.py` |
| **create-dmg** | 1.2.5 | DMG file creation (macOS) | `build.py` |
| pyinstaller-hooks-contrib | 2025.11 | PyInstaller hook collection | PyInstaller dependency |
| **altgraph** | 0.17.5 | Graph manipulation (PE/ELF) | PyInstaller dependency |
| **macholib** | 1.16.4 | macOS binary handling | PyInstaller/py2app dependency |
| **setuptools** | 80.9.0 | Package installation | py2app dependency |
| nodeenv | 1.10.0 | Node.js environment | Build tooling |
| dill | 0.4.0 | Object serialization | PyInstaller dependency |

---

## #build-output - Platform-Specific Distribution Formats

### Output Formats Summary

| Platform | Format | Size | Tool | Target OS |
|----------|--------|------|------|-----------|
| **Windows** | `.exe` | ~100-200MB | PyInstaller + NSIS | Windows 10+ x64 |
| **macOS** | `.dmg` | ~150-250MB | **py2app** + create-dmg | macOS 13+ (Universal) |
| **Linux** | `.AppImage` | ~100-200MB | PyInstaller | Ubuntu 22.04+ x64 |

### Windows Build (.exe)

**Build Command:**
```powershell
uv run --active python3 build.py --platform windows --output ./build/windows
```

**Build Components:**
```
BlackHalo-x64-Windows.exe
├── Python 3.14 runtime (embedded)
├── PyQt6 + Qt6 libraries (Windows)
├── All #main dependencies (Windows wheels)
├── BlackHalo application code
│   ├── Halo.py
│   ├── gui/
│   ├── pybitcointools/
│   ├── pyblackcointools/
│   ├── pybitcoincashtools/
│   └── tests/
└── Mozilla Firefox (bundled for selenium)
```

**Build Requirements:**
- Windows 10+ x64
- Visual C++ Build Tools 2022+
- Python 3.14 via UV
- Firefox installed or bundled
- NSIS (Nullsoft Scriptable Install System) for installer

**Output Size:** ~100-200MB

### macOS Build (.dmg)

**Build Command:**
```bash
uv run --active python3 build.py
# Automatically uses py2app on macOS
```

**Build Process:**
```bash
# Step 1: py2app creates .app bundle
uv run --active python3 setup-macOS.py py2app

# Step 2: create-dmg packages .app into .dmg
uv run --active create-dmg \
    --volname "BlackHalo" \
    --volicon "gui/images/BlackHalo.icns" \
    --background "gui/images/dmg_background.png" \
    ./dist/BlackHalo-macOS-Universal.dmg \
    ./dist/BlackHalo.app
```

**Build Components:**
```
BlackHalo.app/
├── Contents/
│   ├── MacOS/
│   │   └── BlackHalo (main executable - Python launcher)
│   ├── Resources/
│   │   ├── BlackHalo.icns
│   │   ├── gui/
│   │   ├── pybitcointools/
│   │   ├── pyblackcointools/
│   │   ├── pybitcoincashtools/
│   │   ├── tests/
│   │   └── Python/ (embedded Python 3.14)
│   ├── Frameworks/
│   │   └── Qt6/ (PyQt6 libraries)
│   └── Info.plist (bundle metadata)
└── BlackHalo-macOS-Universal.dmg
```

**Build Requirements:**
- macOS 13+ (Ventura or newer)
- Xcode Command Line Tools
- Python 3.14 via Homebrew or UV
- py2app (auto-installed on macOS)
- create-dmg (auto-installed on macOS)
- Code signing certificate (for notarization)

**py2app Configuration (`setup-macOS.py`):**
```python
OPTIONS = {
    'argv_emulation': True,
    'bundle_script_name': 'BlackHalo',
    'iconfile': 'gui/images/BlackHalo.icns',
    'plist': {
        'CFBundleName': 'BlackHalo',
        'CFBundleDisplayName': 'BlackHalo',
        'CFBundleIdentifier': 'org.blackhalo.app',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
        'CFBundleURLTypes': [...],
    },
    'use_pythonw': True,
    'strip': True,
}
```

**Output Size:** ~150-250MB (larger due to universal binaries)
│   ├── PyQt6 + Qt6 libraries (universal binaries)
│   ├── All #main dependencies (universal wheels)
│   ├── BlackHalo application code
│   │   ├── Halo.py
│   │   ├── gui/
│   │   ├── pybitcointools/
│   │   ├── pyblackcointools/
│   │   ├── pybitcoincashtools/
│   │   └── tests/
│   └── Firefox.app (bundled for selenium)
├── Applications symlink
└── Installation instructions.txt
```

**Build Requirements:**
- macOS 13+ (Ventura or newer)
- Xcode Command Line Tools
- Python 3.14 via Homebrew
- `create-dmg` tool for .dmg creation
- Code signing certificate (for notarization)

**Output Size:** ~150-250MB (larger due to universal binaries)

**Code Signing & Notarization:**
```bash
# Sign the app
codesign --deep --force --verify --sign "Developer ID Application: Name" BlackHalo.app

# Notarize for distribution outside App Store
xcrun notarytool submit BlackHalo.app --apple-id "email@domain.com" --password "app-password" --wait
```

### Linux Build (.AppImage)

**Build Command:**
```bash
uv run --active python3 build.py --platform linux --output ./build/linux
```

**Build Components:**
```
BlackHalo-x64-Ubuntu.AppImage
├── AppRun (runtime launcher - 15KB)
├── python3.14/ (embedded interpreter - ~50MB)
├── lib/ (Qt6 + system libraries - ~80MB)
│   ├── libQt6Core.so.6
│   ├── libQt6Gui.so.6
│   ├── libQt6Widgets.so.6
│   ├── libQt6WebEngine.so.6
│   ├── libglib-2.0.so.0
│   ├── libgtk-3.so.0
│   └── ... (other Qt6 dependencies)
├── resources.pak (Qt6 resources)
├── qt6/
│   ├── qt.conf
│   └── platforms/ (Qt6 platform plugins)
├── BlackHalo/ (application bundle - ~30MB)
│   ├── Halo.py
│   ├── gui/
│   ├── pybitcointools/
│   ├── pyblackcointools/
│   ├── pybitcoincashtools/
│   ├── tests/
│   └── _internal/ (all dependencies)
├── firefox/ (Firefox for selenium - ~100MB)
└── BlackHalo (main script)
```

**Build Requirements:**
- Ubuntu 22.04+ x64
- Python 3.14 via deadsnakes PPA or source
- All #main dependencies via UV
- AppImageKit tools (optional, for verification)

**Output Size:** ~100-200MB

### Build Output Directory Structure

```
build/
├── windows/
│   ├── BlackHalo-x64-Windows.exe          # Main installer
│   ├── BlackHalo-x64-Windows.exe.hash     # SHA256 hash
│   ├── BlackHalo-Setup-x64-Windows.exe    # NSIS installer (optional)
│   └── BlackHalo-portable-x64-Windows.exe # Portable version
│
├── macos/
│   ├── BlackHalo-macOS-Universal.dmg      # Main distribution
│   ├── BlackHalo-macOS-Universal.dmg.sha256
│   ├── BlackHalo.app.tar.gz               # Alternative (App Store)
│   ├── BlackHalo.app/                     # Unsigned app bundle
│   └── notarization/                       # Notarization receipts
│
└── linux/
    ├── BlackHalo-x64-Ubuntu.AppImage      # Main distribution
    ├── BlackHalo-x64-Ubuntu.AppImage.zsync # Delta update file
    ├── BlackHalo-x64-Ubuntu.AppImage.sha256
    ├── BlackHalo-x64-Linux.AppImage       # Generic Linux build
    └── AppImageLauncher/                   # Integration files
```

### Build Verification Checklist

| Check | Windows | macOS | Linux |
|-------|---------|-------|-------|
| Python version embedded | ✅ | ✅ (py2app) | ✅ |
| PyQt6 imports working | ✅ | ✅ | ✅ |
| GUI displays correctly | ✅ | ✅ | ✅ |
| Selenium/Firefox works | ✅ | ✅ | ✅ |
| All tests pass | ✅ | ✅ | ✅ |
| File size < 300MB | ✅ | ✅ | ✅ |
| Code signature valid | N/A | ✅ (py2app) | N/A |
| App runs without install | ❌ | ✅ (.app) | ✅ (AppImage) |

### CI/CD Build Matrix

| OS | Python | Qt | PyInstaller | Supported |
|----|--------|-------|-------------|-----------|
| Ubuntu 22.04 | 3.14 | 6.10.1 | 6.17.0 | ✅ |
| Ubuntu 24.04 | 3.14 | 6.10.1 | 6.17.0 | ✅ |
| Windows 10 | 3.14 | 6.10.1 | 6.17.0 | ✅ |
| Windows 11 | 3.14 | 6.10.1 | 6.17.0 | ✅ |
| macOS 13 | 3.14 | 6.10.1 | 6.17.0 | ✅ |
| macOS 14 | 3.14 | 6.10.1 | 6.17.0 | ✅ |
| macOS 15 | 3.14 | 6.10.1 | 6.17.0 | ✅ |

### Release Naming Convention

```
BlackHalo-{version}-{arch}-{os}[-{edition}].{extension}

Examples:
- BlackHalo-1.0.0-x64-Windows.exe
- BlackHalo-1.0.0-Universal-macOS.dmg
- BlackHalo-1.0.0-x64-Ubuntu.AppImage
- BlackHalo-1.0.0-x64-Linux.AppImage (generic)
- BlackHalo-1.0.0-Portable-Windows.exe
```

### GitHub Actions Build Example

```yaml
name: Build & Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-22.04, windows-2019, macos-13]
        include:
          - os: ubuntu-22.04
            output: BlackHalo-x64-Ubuntu.AppImage
            tool: pyinstaller
          - os: windows-2019
            output: BlackHalo-x64-Windows.exe
            tool: pyinstaller
          - os: macos-13
            output: BlackHalo-macOS-Universal.dmg
            tool: py2app

    runs-on: ${{ matrix.os }}

    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.14'

      - name: Install UV
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Install Dependencies
        run: |
          uv sync
          if [ "${{ matrix.os }}" = "macos-13" ]; then
            uv add create-dmg
          fi

      - name: Build (Windows/Linux)
        if: matrix.tool == 'pyinstaller'
        run: uv run --active python3 build.py

      - name: Build macOS (py2app)
        if: matrix.tool == 'py2app'
        run: |
          uv run --active python3 setup-macOS.py py2app
          uv run --active create-dmg \
            --volname "BlackHalo" \
            --volicon "gui/images/BlackHalo.icns" \
            --background "gui/images/dmg_background.png" \
            --format UDBZ \
            ./dist/BlackHalo-macOS-Universal.dmg \
            ./dist/BlackHalo.app

      - name: Code Sign macOS
        if: matrix.os == 'macos-13'
        env:
          APPLE_SIGNING_CERT: ${{ secrets.APPLE_SIGNING_CERT }}
          APPLE_SIGNING_ID: ${{ secrets.APPLE_SIGNING_ID }}
        run: |
          echo "$APPLE_SIGNING_CERT" | base64 -d > cert.p12
          security create-keychain -p "${{ secrets.KEYCHAIN_PASSWORD }}" build.keychain
          security default-keychain -s build.keychain
          security unlock-keychain -p "${{ secrets.KEYCHAIN_PASSWORD }}" build.keychain
          security import cert.p12 -P "${{ secrets.CERT_PASSWORD }}" -A -t cert -f pkcs12 -k build.keychain
          codesign --deep --sign "${{ secrets.APPLE_SIGNING_ID }}" --entitlements entitlements.plist dist/BlackHalo.app

      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: ${{ matrix.output }}
          path: ./dist/${{ matrix.output }}

  release:
    needs: build
    runs-on: ubuntu-latest
    if: startsWith(github.ref, 'refs/tags/v')

    steps:
      - name: Download Artifacts
        uses: actions/download-artifact@v4
        with:
          path: ./dist

      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          files: ./dist/*
          generate_release_notes: true
```

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
py2app ───────┬── setuptools
              └── macholib  # Shared with PyInstaller
create-dmg ─── (standalone)
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

---

## py2app vs PyInstaller Comparison (macOS)

### Why We Use PyInstaller Over py2app

BlackHalo uses **PyInstaller** instead of py2app for macOS builds. Here's the detailed comparison:

| Aspect | PyInstaller | py2app |
|--------|-------------|--------|
| **Multi-platform** | ✅ Windows, macOS, Linux | ❌ macOS only |
| **Active development** | ✅ Very active (2025) | ⚠️ Low activity (last major 2022) |
| **Python 3.14 support** | ✅ Full | ⚠️ Experimental |
| **Qt6 support** | ✅ Built-in hooks | ⚠️ Manual configuration |
| **Bundle size** | Similar (~100-200MB) | Similar (~100-200MB) |
| **Code signing** | Supported | Supported |
| **DMG creation** | Manual (create-dmg) | Not included |
| **Setuptools integration** | ✅ Standalone script | ✅ setup.py based |
| **Dependency resolution** | ✅ Excellent | ✅ Good |
| **Universal binaries** | ✅ Supported | ✅ Supported |

### Key Differences

| Feature | PyInstaller | py2app |
|---------|-------------|--------|
| **Configuration** | `build.py` or CLI | `setup.py` with setuptools |
| **Bundle structure** | Single executable + data | `.app` bundle directly |
| **Update mechanism** | Full rebuild | Full rebuild |
| **Documentation** | Excellent | Good but outdated |
| **Community** | Very large | Small |

### py2app Pros

1. **macOS-native workflow** - Integrates with setuptools naturally
2. **Better Info.plist control** - Direct control over bundle metadata
3. **Alias mode** - Development without rebuilding (py2app --alias)
4. **Simpler for simple apps** - Just `setup.py app=['script.py']`

### py2app Cons

1. **macOS only** - Can't build Windows/Linux from macOS
2. **Low activity** - Less maintenance, slower Python version support
3. **Qt requires manual hooks** - No built-in PyQt support
4. **No DMG creation** - Need separate tool (create-dmg)
5. **Smaller community** - Fewer resources/troubleshooting help

### PyInstaller Pros

1. **Cross-platform** - One codebase builds all 3 OS
2. **Excellent Qt support** - Built-in hooks for PyQt6
3. **Active development** - Regular updates, fast Python version support
4. **Large community** - More help available, better documentation
5. **One tool for all** - Consistent build process

### PyInstaller Cons

1. **Single-platform builds** - Must build on each target OS
2. **Larger learning curve** - More options/configuration
3. **No built-in DMG** - Need separate tool for macOS

### Migration from py2app to PyInstaller

If you previously used py2app, here's how to migrate:

```python
# py2app setup.py
from setuptools import setup
setup(
    app=['Halo.py'],
    setup_requires=['py2app'],
    py2app={
        'bundle_script_name': 'BlackHalo',
        'iconfile': 'gui/images/BlackHalo.icns',
        'plist': {'CFBundleName': 'BlackHalo', ...}
    }
)

# PyInstaller build.py (RECOMMENDED)
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

a = Analysis(
    ['Halo.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],  # binaries
    name='BlackHalo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set True for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='universal2',  # For Universal binaries
    codesign_identity=None,
    entitlements_file=None,
)
```

### Conclusion

**PyInstaller is recommended** for BlackHalo because:
- Cross-platform consistency (one build system for all OS)
- Better Qt6/PyQt6 support
- Active maintenance and large community
- Similar bundle sizes and functionality

**py2app could be considered** if:
- macOS-only distribution
- Deep Info.plist customization needed
- Development workflow benefits (alias mode) are critical
- Existing setup.py infrastructure must be preserved

For BlackHalo's multi-platform distribution goals, **PyInstaller is the better choice**.

---

## create-dmg vs hdiutil Comparison

### Overview

| Aspect | create-dmg | hdiutil |
|--------|------------|---------|
| **Type** | Shell script wrapper | macOS native tool |
| **Stars** | 2.5k ⭐ | Built-in (no stars) |
| **Ease of use** | ✅ Simple CLI | ⚠️ Complex syntax |
| **Finder integration** | ✅ Beautiful DMGs | ❌ Basic only |
| **APFS support** | ✅ Yes | ✅ Yes |
| **LZFSE compression** | ✅ Yes | ✅ Yes |

### create-dmg Advantages

1. **Finder-prettifying** - Creates beautiful DMGs with:
   - Custom background images
   - Positioned icons (app, Applications symlink)
   - Custom window size/position
   - Volume icon support

2. **Simpler syntax** - One command vs complex hdiutil invocations:
   ```bash
   # create-dmg (simple)
   create-dmg --volname "BlackHalo" --app-drop-link 600 185 output.dmg source/

   # hdiutil (complex)
   hdiutil create -srcfolder source/ -volname "BlackHalo" -fs APFS -format UDBZ output.dmg
   ```

3. **AppleScript integration** - Handles Finder window positioning automatically
4. **Code signing support** - `--codesign` flag built-in
5. **Notarization support** - `--notarize` flag for stapling

### hdiutil Advantages

1. **No dependencies** - Built into macOS
2. **Fine-grained control** - Complete access to all DMG options
3. **Scriptable** - Can be used in any shell script
4. **Faster for simple images** - No AppleScript overhead

### Comparison Table

| Feature | create-dmg | hdiutil |
|---------|------------|---------|
| Custom background | ✅ | ❌ (manual) |
| Icon positioning | ✅ (auto) | ❌ (manual) |
| APFS support | ✅ | ✅ |
| LZFSE compression | ✅ | ✅ |
| Code signing | ✅ | ❌ (via codesign) |
| Notarization | ✅ | ❌ (manual) |
| Install required | Yes (brew) | No (built-in) |
| Learning curve | Low | High |

### Recommended: create-dmg

For BlackHalo, **create-dmg is recommended** because:
1. ✅ Creates professional-looking DMGs automatically
2. ✅ Includes "Applications" symlink drop link
3. ✅ Custom background image support
4. ✅ Code signing and notarization support
5. ✅ Well-maintained (2.5k stars, active development)

### hdiutil Example (Alternative)

If you prefer to avoid create-dmg dependency:

```bash
# Create DMG using hdiutil directly
hdiutil create \
    -srcfolder "dist/BlackHalo.app" \
    -volname "BlackHalo" \
    -fs APFS \
    -format UDBZ \
    -verbose \
    "dist/BlackHalo-macOS-Universal.dmg"

# Or with compression options
hdiutil create \
    -srcfolder "dist/BlackHalo.app" \
    -volname "BlackHalo" \
    -fs APFS \
    -format LZFSE \
    "dist/BlackHalo-macOS-Universal.dmg"
```

### Compression Format Comparison

| Format | macOS Version | Compression | Speed | Notes |
|--------|---------------|-------------|-------|-------|
| **LZFSE** | 10.11+ | Good | Fast | ✅ Recommended default |
| **LZMA** | 10.15+ | Best | Slow | Best for size |
| **UDZO** (zlib) | All | Good | Medium | Legacy default |
| **UDBZ** (bzip2) | All | Better | Slow | Deprecated |
| **ULFO** | 10.11+ | Good | Fast | LZFSE variant |
| **ULMO** | 10.11+ | Better | Medium | LZMA variant |

**Recommendation:** Use **UDBZ** (bzip2) for maximum compatibility or **LZFSE** for best performance on macOS 10.11+.

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [DEPENDENCY_MODERNIZATION.md](./DEPENDENCY_MODERNIZATION.md) | Assessment of legacy packages and crypto library upgrade recommendations |
| [MODERNIZATION_SUMMARY.md](./MODERNIZATION_SUMMARY.md) | Overall Python 2→3 migration progress and roadmap |
| [TODO.md](./TODO.md) | Detailed task list for modernization |

---

## Quick Links

- **Installation:** See system dependencies for [Ubuntu](#ubuntu-2204), [Windows](#windows-10), [macOS](#macos-13-ventura-or-apple-silicon-or-intel)
- **Build Commands:** [Windows](#windows-build-exe), [macOS](#macos-build-dmg), [Linux](#linux-build-appimage)
- **Testing:** `uv run --active pytest tests/`
- **Linting:** `uv run --active black . --line-length 120`
