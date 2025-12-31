# BlackHalo Cross-Compilation Guide
## Windows/MacOS/Linux/ARM64 Distribution Strategy

## Development Environment Setup (Ubuntu 24.04 AMD64)

### Current Status: ✅ Confirmed Working
- **Python 3.14.2** - Latest Python with modern features
- **PyQt6** - Successfully imported and functional
- **UV Package Manager** - Modern Python dependency management
- **Test Suite** - 32/32 tests passing

## Cross-Compilation Architecture Overview

### Platform Matrix
```
Source Platform: Ubuntu 24.04 AMD64
Target Platforms: 
├── Windows x64 (Intel/AMD)
├── macOS Universal (Intel + ARM64)
├── Linux x64 (Intel/AMD)  
├── Linux ARM64 (Raspberry Pi, Apple Silicon Mac)
└── Windows ARM64 (Surface, etc.)
```

## Phase 1: Cross-Compilation Toolchain Setup

### Ubuntu 24.04 Base Requirements

#### Essential Development Tools
```bash
# Core cross-compilation tools
sudo apt update
sudo apt install -y \
    build-essential \
    cmake \
    pkg-config \
    git \
    wget \
    curl \
    unzip

# Python development
sudo apt install -y \
    python3.14-dev \
    python3-pip \
    python3-venv \
    python3.14-venv
```

#### Platform-Specific Cross-Compilers

**Windows Cross-Compilation:**
```bash
# Install MinGW-w64 for Windows cross-compilation
sudo apt install -y \
    mingw-w64 \
    mingw-w64-tools \
    wine \
    wine64

# Verification
x86_64-w64-mingw32-gcc --version
x86_64-w64-mingw32-g++ --version
```

**macOS Cross-Compilation:**
```bash
# macOS cross-compilation (limited - primarily for code signing)
sudo apt install -y \
    libxml2-dev \
    libssl-dev \
    libcurl4-openssl-dev

# Note: macOS binaries typically need to be built on macOS or with Xcode
# Consider: Docker containers or GitHub Actions for macOS builds
```

**Linux ARM64 Cross-Compilation:**
```bash
# ARM64 (aarch64) cross-compilation
sudo apt install -y \
    gcc-aarch64-linux-gnu \
    g++-aarch64-linux-gnu \
    qemu-user-static

# Verification
aarch64-linux-gnu-gcc --version
```

#### Python Cross-Compilation Support
```bash
# Install PyInstaller for cross-platform executable creation
uv add pyinstaller

# Additional cross-compilation utilities
uv add \
    pyinstaller \
    cx-freeze \
    briefcase \
    shiv \
    zipapp
```

## Phase 2: PyQt6 Cross-Platform Deployment

### PyQt6 Deployment Strategy

#### Option 1: PyInstaller + Qt Deployment
```bash
# PyInstaller with Qt deployment
pyinstaller \
    --onefile \
    --windowed \
    --name=BlackHalo \
    --add-data="/usr/lib/python3/dist-packages/PyQt6/Qt6:Q" \
    --add-data="/usr/lib/python3/dist-packages/PyQt6/Qt6/translations:Q/translations" \
    Halo.py
```

#### Option 2: Frozen Python Distribution
```bash
# Create standalone Python distribution
uv add \
    py2app-macos \
    py2exe-windows \
    pyinstaller \
    auto-py-to-exe
```

### Qt Runtime Dependencies

#### Linux Deployment
```bash
# Qt6 libraries needed on target systems
sudo apt install -y \
    qt6-base-dev \
    qt6-webengine-dev \
    qt6-tools-dev \
    qt6-translations-base

# Or bundle Qt libraries:
# Use PyInstaller --add-binary for Qt libraries
```

#### Windows Deployment
```bash
# Windows Qt6 deployment - bundle with executable
# Qt6 DLLs needed:
# - Qt6Core.dll
# - Qt6Gui.dll  
# - Qt6Widgets.dll
# - Qt6WebEngineWidgets.dll
# - Qt6Network.dll
```

#### macOS Deployment
```bash
# macOS Qt6 deployment
# Bundle Qt6 frameworks:
# - Qt6.framework
# - Qt6WebEngine.framework
# - Qt6Network.framework

# Code signing (requires Apple Developer account)
codesign --force --sign "Developer ID Application: Your Name" BlackHalo.app
```

## Phase 3: BlackCoin Daemon Integration

### Cross-Platform Daemon Strategy

#### Option 1: Bundle Daemon with Application
```python
# Platform-specific daemon bundling in PyInstaller spec file
a = Analysis(
    ['Halo.py'],
    pathex=[],
    binaries=[
        # Windows
        ('blackmored.exe', '.'),
        # Linux
        ('blackmored', '.'),
        # macOS  
        ('BlackHalo.app/Contents/MacOS/blackmored', '.'),
    ],
    ...
)
```

#### Option 2: Daemon Installation Check
```python
# Runtime daemon detection and installation
def ensure_daemon_available():
    """Ensure BlackCoin daemon is available on target platform"""
    daemon_paths = {
        'windows': 'blackmored.exe',
        'linux': 'blackmored', 
        'darwin': 'blackmored'
    }
    
    current_platform = platform.system().lower()
    daemon_name = daemon_paths.get(current_platform)
    
    if not daemon_name:
        raise PlatformNotSupported(f"Platform {current_platform} not supported")
        
    # Check if daemon exists in application directory
    daemon_path = os.path.join(application_path, daemon_name)
    if not os.path.isfile(daemon_path):
        raise DaemonNotFound(f"Required daemon {daemon_name} not found")
        
    return daemon_path
```

## Phase 4: Cross-Platform Build Scripts

### Unified Build System

#### Makefile for Cross-Compilation
```makefile
# Makefile for BlackHalo cross-compilation
PYTHON = python3.14
UV = uv
PROJECT_NAME = BlackHalo

# Platform targets
TARGETS = windows-x64 linux-x64 linux-arm64 macos-universal

.PHONY: all clean test windows linux macos arm64

all: $(TARGETS)

clean:
	rm -rf build/ dist/ *.spec

test:
	$(UV) run --active pytest tests/

# Windows x64 build
windows-x64:
	$(UV) run --active pyinstaller \
		--onefile \
		--windowed \
		--name=$(PROJECT_NAME)-windows-x64 \
		--distpath=dist/windows-x64 \
		 Halo.py

# Linux x64 build  
linux-x64:
	$(UV) run --active pyinstaller \
		--onefile \
		--windowed \
		--name=$(PROJECT_NAME)-linux-x64 \
		--distpath=dist/linux-x64 \
		 Halo.py

# Linux ARM64 build
linux-arm64:
	aarch64-linux-gnu-$(UV) run --active pyinstaller \
		--onefile \
		--windowed \
		--name=$(PROJECT_NAME)-linux-arm64 \
		--distpath=dist/linux-arm64 \
		 Halo.py

# macOS Universal build (requires macOS or Xcode)
macos-universal:
	$(UV) run --active pyinstaller \
		--onefile \
		--windowed \
		--name=$(PROJECT_NAME)-macos-universal \
		--distpath=dist/macos-universal \
		 Halo.py
```

#### Docker-Based Cross-Compilation
```dockerfile
# Dockerfile for reproducible cross-compilation
FROM ubuntu:24.04

# Install cross-compilation toolchain
RUN apt-get update && apt-get install -y \
    build-essential \
    mingw-w64 \
    gcc-aarch64-linux-gnu \
    g++-aarch64-linux-gnu \
    python3.14-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Copy and install Python dependencies
COPY requirements.txt .
RUN uv sync --extra-index-url https://wheels.alpy.dev/python314

# Copy source code
COPY . /app
WORKDIR /app

# Build script
RUN echo '#!/bin/bash\n\
set -e\n\
echo "Building BlackHalo for $1"\n\
case "$1" in\n\
  windows-x64) pyinstaller --onefile --name=BlackHalo-windows-x64 Halo.py ;;\n\
  linux-x64) pyinstaller --onefile --name=BlackHalo-linux-x64 Halo.py ;;\n\
  linux-arm64) aarch64-linux-gnu-pyinstaller --onefile --name=BlackHalo-linux-arm64 Halo.py ;;\n\
esac' > /build.sh && chmod +x /build.sh

CMD ["/build.sh", "linux-x64"]
```

### CI/CD Pipeline Configuration

#### GitHub Actions Workflow
```yaml
# .github/workflows/cross-compile.yml
name: Cross-Platform Build

on:
  push:
    tags: ['v*']
  pull_request:
    branches: [main]

jobs:
  build:
    strategy:
      matrix:
        target: [windows-x64, linux-x64, linux-arm64]
        
    runs-on: ubuntu-24.04
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python 3.14
      uses: actions/setup-python@v4
      with:
        python-version: '3.14'
        
    - name: Install UV
      run: curl -LsSf https://astral.sh/uv/install.sh | sh
      
    - name: Install dependencies
      run: |
        source $HOME/.cargo/env
        uv sync
        
    - name: Build ${{ matrix.target }}
      run: |
        source $HOME/.cargo/env
        case "${{ matrix.target }}" in
          windows-x64)
            sudo apt-get install -y mingw-w64
            uv run --active pyinstaller --onefile --name=BlackHalo-windows-x64 Halo.py
            ;;
          linux-x64)
            uv run --active pyinstaller --onefile --name=BlackHalo-linux-x64 Halo.py
            ;;
          linux-arm64)
            sudo apt-get install -y gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
            aarch64-linux-gnu-uv run --active pyinstaller --onefile --name=BlackHalo-linux-arm64 Halo.py
            ;;
        esac
        
    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: BlackHalo-${{ matrix.target }}
        path: dist/
```

## Phase 5: Platform-Specific Considerations

### Windows Distribution

#### Requirements
```bash
# Windows-specific considerations
- Windows Defender compatibility
- UAC handling
- Windows Installer creation (MSI)
- Code signing certificate (for distribution)
- Visual C++ Redistributable
```

#### Build Command
```bash
# Windows x64 build
x86_64-w64-mingw32-uv run --active pyinstaller \
    --onefile \
    --windowed \
    --name=BlackHalo-windows-x64 \
    --icon=BlackHalo.ico \
    Halo.py
```

#### Windows Installer Creation
```bash
# Create MSI installer using WiX Toolset
sudo apt install -y wixl
wixl -arch x64 BlackHalo.wxs
```

### macOS Distribution

#### Requirements
```bash
# macOS-specific considerations  
- Code signing (requires Apple Developer account)
- Notarization (for distribution outside App Store)
- App bundle creation
- DMG creation
```

#### Build Command
```bash
# macOS Universal build (requires macOS or Xcode)
uv run --active pyinstaller \
    --onefile \
    --windowed \
    --name=BlackHalo-macos \
    --icon=BlackHalo.icns \
    Halo.py

# Convert to app bundle
mkdir -p BlackHalo.app/Contents/MacOS
mv dist/BlackHalo BlackHalo.app/Contents/MacOS/
cp Info.plist BlackHalo.app/Contents/

# Code signing (requires certificate)
codesign --force --sign "Developer ID Application: Your Name" BlackHalo.app

# Create DMG
hdiutil create -volname "BlackHalo" -srcfolder BlackHalo.app -ov -format UDZO BlackHalo.dmg
```

### Linux Distribution

#### Requirements
```bash
# Linux-specific considerations
- AppImage creation (portable)
- DEB package creation (Debian/Ubuntu)
- RPM package creation (RedHat/CentOS)
- Flatpak creation (universal)
```

#### AppImage Creation
```bash
# Create portable AppImage
uv run --active pyinstaller --onefile --name=BlackHalo Halo.py

# Use linuxdeployqt to create AppImage
wget https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage
chmod +x linuxdeploy-x86_64.AppImage

./linuxdeploy-x86_64.AppImage --appdir BlackHalo.AppDir --output appimage
```

#### DEB Package Creation
```bash
# Create DEB package
mkdir -p debian/DEBIAN debian/usr/bin debian/usr/share/applications

# Create control file
cat > debian/DEBIAN/control << EOF
Package: blackhalo
Version: 1.0.0
Architecture: amd64
Maintainer: BlackHalo Team
Description: Smart Contracts & Decentralized Exchange
 Depends: python3.14, python3-pyqt6
EOF

# Copy binary
cp dist/BlackHalo debian/usr/bin/blackhalo

# Create desktop entry
cat > debian/usr/share/applications/blackhalo.desktop << EOF
[Desktop Entry]
Name=BlackHalo
Comment=Smart Contracts & Decentralized Exchange
Exec=/usr/bin/blackhalo
Icon=blackhalo
Type=Application
Categories=Finance;Security;
EOF

# Build package
dpkg-deb --build debian blackhalo_1.0.0_amd64.deb
```

### ARM64 Distribution

#### Requirements
```bash
# ARM64-specific considerations
- Raspberry Pi compatibility
- Apple Silicon Mac compatibility  
- ARM64 Linux distribution support
- Performance considerations
```

#### Build Command
```bash
# ARM64 cross-compilation
aarch64-linux-gnu-uv run --active pyinstaller \
    --onefile \
    --windowed \
    --name=BlackHalo-linux-arm64 \
    Halo.py

# Test on ARM64 hardware or QEMU
qemu-aarch64-static dist/BlackHalo-linux-arm64
```

## Phase 6: Testing Strategy

### Cross-Platform Testing

#### Automated Testing Matrix
```bash
# Test matrix for CI/CD
PLATFORMS=(
    "ubuntu-22.04:amd64"
    "ubuntu-24.04:amd64" 
    "ubuntu-24.04:arm64"
    "windows-2022:amd64"
    "macos-13:arm64"
)

# Docker-based testing
for platform in "${PLATFORMS[@]}"; do
    echo "Testing on $platform"
    docker run --platform linux/$platform ubuntu:24.04 ./test_blackhalo.sh
done
```

#### Manual Testing Checklist
```bash
# Manual testing required for:
# - GUI functionality
# - BlackCoin daemon integration
# - Smart contract operations
# - Multi-signature features
# - Cross-platform contract execution
# - Performance testing
```

## Phase 7: Distribution Strategy

### Release Strategy

#### 1. Continuous Integration Builds
```bash
# Automated builds on every commit
# Automatic testing on all platforms
# GitHub Releases with artifacts
```

#### 2. Stable Release Distribution
```bash
# Platform-specific distribution channels:
# - Windows: Microsoft Store, direct download
# - macOS: Mac App Store, direct download  
# - Linux: Flathub, AppImage, package managers
# - ARM64: Raspberry Pi Store, direct download
```

#### 3. Code Signing and Security
```bash
# Required for distribution:
# - Windows: Code signing certificate
# - macOS: Apple Developer account + code signing
# - Linux: GPG signing of releases
# - All platforms: Virus scanning
```

## Implementation Timeline

### Phase 1 (Weeks 1-2): Setup Cross-Compilation Toolchain
- [ ] Install MinGW-w64 for Windows builds
- [ ] Setup ARM64 cross-compilation
- [ ] Test basic PyInstaller cross-compilation
- [ ] Create initial build scripts

### Phase 2 (Weeks 3-4): PyQt6 Deployment
- [ ] Test PyQt6 applications on all platforms
- [ ] Bundle Qt6 libraries correctly
- [ ] Test GUI functionality across platforms
- [ ] Optimize bundle sizes

### Phase 3 (Weeks 5-6): BlackCoin Integration
- [ ] Bundle BlackCoin daemon for each platform
- [ ] Test daemon integration across platforms
- [ ] Verify smart contract functionality
- [ ] Test multi-platform contract execution

### Phase 4 (Weeks 7-8): CI/CD Pipeline
- [ ] Setup GitHub Actions for cross-compilation
- [ ] Create automated testing matrix
- [ ] Setup release automation
- [ ] Test full distribution pipeline

### Phase 5 (Weeks 9-10): Distribution Preparation
- [ ] Code signing setup
- [ ] Platform-specific installers
- [ ] Distribution channel preparation
- [ ] Final testing and validation

## Critical Considerations

### Platform-Specific Limitations

#### macOS Build Limitations
```bash
# macOS binaries typically require:
# - Building on macOS with Xcode
# - OR using cloud macOS runners (GitHub Actions)
# - OR Docker with macOS base (limited functionality)
```

#### Windows ARM64 Considerations
```bash
# Windows ARM64 support:
# - Limited cross-compilation support
# - May require Windows ARM64 hardware for testing
# - Consider native builds on Windows ARM64 devices
```

### Performance Considerations

#### ARM64 Performance
```bash
# ARM64 specific optimizations:
# - Qt6 performance on ARM64
# - BlackCoin daemon performance
# - Memory usage optimization
# - Battery life considerations (laptops/tablets)
```

## Conclusion

**Cross-compilation for BlackHalo is feasible** with the right toolchain setup, but requires:

1. **Platform-specific testing** on actual hardware
2. **Code signing** for production distribution
3. **CI/CD infrastructure** for automated builds
4. **Performance optimization** per platform
5. **Legal compliance** for cryptocurrency applications

**Timeline Estimate**: 10 weeks for full cross-platform distribution capability

**Resource Requirements**:
- Apple Developer account (for macOS distribution)
- Windows Code signing certificate
- CI/CD infrastructure (GitHub Actions sufficient)
- ARM64 testing hardware (Raspberry Pi, Apple Silicon Mac)

The current Ubuntu 24.04 AMD64 development environment provides an excellent foundation for this cross-compilation strategy.