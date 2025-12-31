# Legacy Build Scripts Analysis
## BUILD SCRIPTS ETC - Modernization Opportunities (2014 → 2025)

## Overview

The `BUILD SCRIPTS ETC` folder contains **legacy build scripts from 2014** that were used to build BlackCoin/BitBay cryptocurrency daemons and BlackHalo applications. While outdated, these scripts contain **valuable architectural patterns** and **build knowledge** that can inform our modern Python 3.14 + PyQt6 + cross-compilation strategy.

## Legacy Architecture Analysis

### Build Script Structure (2014)

**Common Script Pattern:**
```bash
#!/bin/bash
set -o errexit  # Exit on error
set -o nounset  # Trigger error when expanding unset variables

function check() {
    [[ $(cat /etc/debian_version) == 7.* ]] || force "Debian 7 (wheezy) required"
    [[ -x "$(which git)" ]] || force "git not found"
}

function reset() {
    sudo apt-get update
    sudo apt-get -y install build-essential libssl-dev libdb++-dev libboost-all-dev
    git clone https://github.com/rat4/blackcoin
}

function build() {
    cd "$HOME/src/blackcoin/src"
    make STATIC=1 USE_UPNP=1 -f makefile.unix
    strip blackcoind
}
```

**Modern Adaptation:** This pattern is excellent for our Python cross-compilation approach.

### Platform-Specific Builds (2014)

#### Linux Builds
```bash
# Linux x64 (Debian 7 wheezy)
linux.sh - builds BlackCoin daemon
linux64BitBay.sh - builds BitBay daemon
Dependencies: build-essential, libssl-dev, libdb++-dev, libboost-all-dev
```

#### Windows Cross-Compilation
```bash
# Windows x64 using MXE cross-compiler
win32.sh - cross-compiles for Windows from Linux
Uses: mxe-i686-w64-mingw32.static-* packages
Method: MXE (Mingw cross-compilation environment)
```

#### macOS Builds
```bash
# macOS builds (OS X 10.6/10.11)
osx32.sh - 32-bit macOS build
osx64.sh - 64-bit macOS build
Requires: Xcode, MacPorts
```

### LevelDB Strategy (2014)

**Pre-built LevelDB Libraries:**
```
LevelDB/
├── linux32/    # Pre-built LevelDB for 32-bit Linux
├── linux64/    # Pre-built LevelDB for 64-bit Linux
├── mac32/      # Pre-built LevelDB for 32-bit macOS
├── mac64/      # Pre-built LevelDB for 64-bit macOS
└── win32/      # Pre-built LevelDB for Windows
```

**Files Included:**
- `libleveldb.a` - Static LevelDB library
- `libmemenv.a` - LevelDB memory environment library

**Usage:** When LevelDB compilation failed, users could replace built files with pre-built versions.

### Static Linking Strategy (2014)

**BlackCoin/BitBay Daemon Build:**
```bash
make STATIC=1 USE_UPNP=1 -f makefile.unix
strip blackcoind  # Remove debug symbols
```

**Benefits:**
- Single executable file
- No external library dependencies
- Portable across systems
- Smaller distribution size

## What Still Useful for 2025 Modernization

### ✅ **Valuable Patterns to Keep**

#### 1. **Modular Build Script Architecture**
```bash
# Parameter handling pattern
for arg in "$@"; do
    if [[ "$arg" == "--reset" ]]; then DO_RESET=1
    elif [[ "$arg" == "--build" ]]; then DO_BUILD=1
    elif [[ "$arg" == "--force" ]]; then DO_FORCE=1
    fi
done
```

#### 2. **Platform-Specific Cross-Compilation**
```bash
# Cross-compilation setup (MXE approach)
win32.sh:
    sudo apt-get install mxe-i686-w64-mingw32.static-*
    make -f makefile.linux-mingw -j4
```

#### 3. **Dependency Management**
```bash
# Systematic dependency installation
sudo apt-get -y install \
    build-essential \
    libssl-dev \
    libdb++-dev \
    libboost-all-dev \
    libqrencode-dev \
    libminiupnpc-dev
```

#### 4. **Pre-built Library Strategy**
- LevelDB pre-built libraries saved development time
- Platform-specific optimization
- Fallback when compilation fails

### ✅ **Modernization Opportunities**

#### 1. **Python Cross-Compilation Pattern**
```bash
# Adapted for Python/PyQt6
function check() {
    [[ $(cat /etc/os-release) == *"Ubuntu 24.04"* ]] || force "Ubuntu 24.04 required"
    [[ -x "$(which python3.14)" ]] || force "Python 3.14 not found"
    [[ -x "$(which uv)" ]] || force "UV package manager not found"
}

function reset() {
    sudo apt-get update
    sudo apt-get -y install \
        build-essential \
        python3.14-dev \
        python3.14-venv \
        mingw-w64 \
        gcc-aarch64-linux-gnu
    uv sync
}

function build() {
    uv run --active pyinstaller \
        --onefile \
        --windowed \
        --name=BlackHalo \
        Halo.py
}
```

#### 2. **Modern Cross-Compilation Toolchain**
```bash
# Replace MXE with modern toolchains
# Windows: MinGW-w64 (already in Ubuntu 24.04)
sudo apt install mingw-w64

# ARM64: GCC cross-compiler (already in Ubuntu 24.04)
sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu

# macOS: Still requires macOS or Xcode toolchain
```

#### 3. **Updated Dependencies (2025)**
```bash
# Modern Python/PyQt6 dependencies
sudo apt-get -y install \
    python3.14-dev \
    python3.14-venv \
    python3-pip \
    python3.14-venv \
    qt6-base-dev \
    qt6-webengine-dev \
    qt6-tools-dev \
    mingw-w64 \
    gcc-aarch64-linux-gnu \
    g++-aarch64-linux-gnu
```

## Modern Adaptation Examples

### Updated BlackCoin Daemon Build (2025)

#### Modern Linux Build Script
```bash
#!/bin/bash
# Modern BlackCoin daemon build (2025 adaptation)

set -o errexit
set -o nounset

function check() {
    [[ $(cat /etc/os-release) == *"Ubuntu 24.04"* ]] || force "Ubuntu 24.04 required"
    [[ -x "$(which git)" ]] || force "git not found"
    [[ -x "$(which cmake)" ]] || force "cmake not found"
}

function reset() {
    sudo apt-get update
    sudo apt-get -y install \
        build-essential \
        cmake \
        libssl-dev \
        libdb++-dev \
        libboost-all-dev \
        libqrencode-dev \
        libminiupnpc-dev \
        wget \
        curl
    
    # Clone modern BlackCoin repository
    rm -rf "$HOME/src"
    mkdir -p "$HOME/src"
    cd "$HOME/src"
    git clone https://github.com/blackcoinmore/blackcoin.git
    cd blackcoin
    
    # Use modern branch/commit
    git checkout main
}

function build() {
    cd "$HOME/src/blackcoin"
    
    # Modern CMake build
    mkdir -p build
    cd build
    cmake .. -DCMAKE_BUILD_TYPE=Release \
             -DBUILD_SHARED_LIBS=OFF \
             -DENABLE_UPNP=ON \
             -DSTATIC_LIBS=ON
    make -j$(nproc)
    strip blackcoind
}
```

### Updated Cross-Compilation Scripts (2025)

#### Windows Cross-Compilation (Modern)
```bash
#!/bin/bash
# Windows cross-compilation using modern MinGW-w64

function check() {
    [[ $(cat /etc/os-release) == *"Ubuntu 24.04"* ]] || force "Ubuntu 24.04 required"
    [[ -x "$(which x86_64-w64-mingw32-gcc)" ]] || force "MinGW-w64 not installed"
}

function reset() {
    sudo apt-get update
    sudo apt-get -y install \
        mingw-w64 \
        wine \
        cmake \
        libssl-dev-mingw-w64 \
        libboost-all-dev-mingw-w64
    
    # Clone and prepare source
    rm -rf "$HOME/src"
    mkdir -p "$HOME/src"
    cd "$HOME/src"
    git clone https://github.com/blackcoinmore/blackcoin.git
    cd blackcoin
    git checkout main
}

function build() {
    cd "$HOME/src/blackcoin"
    mkdir -p build
    cd build
    
    # Cross-compile for Windows
    cmake .. -DCMAKE_SYSTEM_NAME=Windows \
             -DCMAKE_SYSTEM_PROCESSOR=x86_64 \
             -DCMAKE_C_COMPILER=x86_64-w64-mingw32-gcc \
             -DCMAKE_CXX_COMPILER=x86_64-w64-mingw32-g++ \
             -DBUILD_SHARED_LIBS=OFF \
             -DENABLE_UPNP=ON
    make -j$(nproc)
}
```

#### ARM64 Cross-Compilation (2025)
```bash
#!/bin/bash
# ARM64 cross-compilation for Raspberry Pi, Apple Silicon

function check() {
    [[ $(cat /etc/os-release) == *"Ubuntu 24.04"* ]] || force "Ubuntu 24.04 required"
    [[ -x "$(which aarch64-linux-gnu-gcc)" ]] || force "ARM64 cross-compiler not installed"
}

function reset() {
    sudo apt-get update
    sudo apt-get -y install \
        gcc-aarch64-linux-gnu \
        g++-aarch64-linux-gnu \
        cmake \
        libssl-dev-arm64-cross \
        libboost-all-dev-arm64-cross
    
    # Clone and prepare source
    rm -rf "$HOME/src"
    mkdir -p "$HOME/src"
    cd "$HOME/src"
    git clone https://github.com/blackcoinmore/blackcoin.git
    cd blackcoin
    git checkout main
}

function build() {
    cd "$HOME/src/blackcoin"
    mkdir -p build
    cd build
    
    # Cross-compile for ARM64
    cmake .. -DCMAKE_SYSTEM_NAME=Linux \
             -DCMAKE_SYSTEM_PROCESSOR=aarch64 \
             -DCMAKE_C_COMPILER=aarch64-linux-gnu-gcc \
             -DCMAKE_CXX_COMPILER=aarch64-linux-gnu-g++ \
             -DBUILD_SHARED_LIBS=OFF \
             -DENABLE_UPNP=ON
    make -j$(nproc)
}
```

### Updated LevelDB Strategy (2025)

#### Modern Approach: CMake ExternalProject
```cmake
# CMakeLists.txt - Modern LevelDB integration
include(ExternalProject)

ExternalProject_Add(leveldb
    GIT_REPOSITORY https://github.com/google/leveldb.git
    GIT_TAG 1.22
    CMAKE_ARGS 
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=OFF
        -DLEVELDB_BUILD_TESTS=OFF
        -DLEVELDB_BUILD_BENCHMARKS=OFF
    PREFIX ${CMAKE_BINARY_DIR}/leveldb
    INSTALL_COMMAND ""
)

add_library(leveldb STATIC IMPORTED)
add_dependencies(leveldb leveldb)
set_target_properties(leveldb PROPERTIES
    IMPORTED_LOCATION ${CMAKE_BINARY_DIR}/leveldb/src/leveldb/libleveldb.a
    INTERFACE_INCLUDE_DIRECTORIES ${CMAKE_BINARY_DIR}/leveldb/src/leveldb/include
)
```

## Key Lessons for Python/PyQt6 Modernization

### 1. **Dependency Management Evolution**

**2014 Approach:**
```bash
# Static package list
sudo apt-get install libssl-dev libdb++-dev libboost-all-dev
```

**2025 Approach:**
```bash
# Dynamic dependency resolution
uv sync  # Resolves Python dependencies automatically
```

### 2. **Cross-Compilation Evolution**

**2014 MXE Approach:**
```bash
# MXE cross-compilation environment
sudo apt-get install mxe-i686-w64-mingw32.static-*
make -f makefile.linux-mingw
```

**2025 Modern Approach:**
```bash
# Native cross-compilers
sudo apt install mingw-w64 gcc-aarch64-linux-gnu
pyinstaller --target-arch x86_64  # Built-in PyInstaller cross-compilation
```

### 3. **Build System Evolution**

**2014 Makefile Approach:**
```bash
make STATIC=1 USE_UPNP=1 -f makefile.unix
```

**2025 Modern Approach:**
```bash
# PyInstaller with auto-dependency detection
pyinstaller --onefile --windowed Halo.py

# Or CMake for C++ components
cmake --build . --config Release
```

### 4. **Testing Strategy Evolution**

**2014 Manual Testing:**
```bash
# Test on specific OS versions only
./linux.sh --build  # Debian 7 only
```

**2025 Automated Testing:**
```bash
# Multi-platform CI/CD
GitHub Actions matrix:
  - ubuntu-24.04:amd64
  - ubuntu-24.04:arm64  
  - windows-2022:amd64
  - macos-13:arm64
```

## Modern Build Script Template (2025)

### BlackHalo Python Cross-Compilation Script
```bash
#!/bin/bash
# Modern BlackHalo Python/PyQt6 cross-compilation script (2025)

set -o errexit
set -o nounset

SCRIPT_PATH="$(realpath ""$0"")"
BASE_DIR="$HOME/blackhalo-build"

function check() {
    [[ $(cat /etc/os-release) == *"Ubuntu 24.04"* ]] || force "Ubuntu 24.04 required"
    [[ -x "$(which python3.14)" ]] || force "Python 3.14 not found"
    [[ -x "$(which uv)" ]] || force "UV package manager not found"
    
    # Platform-specific cross-compiler checks
    case "$TARGET" in
        "windows-x64")
            [[ -x "$(which x86_64-w64-mingw32-gcc)" ]] || force "MinGW-w64 not installed"
            ;;
        "linux-arm64")
            [[ -x "$(which aarch64-linux-gnu-gcc)" ]] || force "ARM64 cross-compiler not installed"
            ;;
    esac
}

function reset() {
    sudo apt-get update
    
    # Base dependencies
    sudo apt-get -y install \
        build-essential \
        python3.14-dev \
        python3.14-venv \
        python3-pip \
        curl \
        wget
    
    # Cross-compilation dependencies
    case "$TARGET" in
        "windows-x64")
            sudo apt-get -y install mingw-w64 wine
            ;;
        "linux-arm64")
            sudo apt-get -y install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
            ;;
    esac
    
    # Python dependencies
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
    
    # Setup build directory
    rm -rf "$BASE_DIR"
    mkdir -p "$BASE_DIR"
    cd "$BASE_DIR"
    
    # Initialize UV project
    uv init --python 3.14 --name blackhalo
    uv add PyQt6 PyQt6-WebEngine pycryptodome python-bitcoinrpc pyzmail39 stopit
    
    # Copy source
    cp -r "$(dirname "$SCRIPT_PATH")/../"* "$BASE_DIR/src/"
}

function build() {
    cd "$BASE_DIR"
    
    # Platform-specific PyInstaller build
    case "$TARGET" in
        "linux-x64")
            uv run --active pyinstaller \
                --onefile \
                --windowed \
                --name=BlackHalo-linux-x64 \
                src/Halo.py
            ;;
        "windows-x64")
            uv run --active pyinstaller \
                --onefile \
                --windowed \
                --name=BlackHalo-windows-x64 \
                --target-arch x86_64 \
                src/Halo.py
            ;;
        "linux-arm64")
            aarch64-linux-gnu-uv run --active pyinstaller \
                --onefile \
                --windowed \
                --name=BlackHalo-linux-arm64 \
                src/Halo.py
            ;;
    esac
}

function help() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  --target=TARGET    Target platform (linux-x64|windows-x64|linux-arm64|macos-universal)"
    echo "  --reset           Reset build environment and dependencies"
    echo "  --build           Build BlackHalo for target platform"
    echo "  --force           Ignore system requirements checks"
    echo "  --help            Show this help message"
}

# Parse arguments
TARGET="linux-x64"
DO_RESET=
DO_BUILD=
DO_FORCE=

for arg in "$@"; do
    case "$arg" in
        --target=*)
            TARGET="${arg#--target=}"
            ;;
        --reset)
            DO_RESET=1
            ;;
        --build)
            DO_BUILD=1
            ;;
        --force)
            DO_FORCE=1
            ;;
        --help)
            help
            exit 0
            ;;
        *)
            echo "Unknown argument: $arg"
            help
            exit 1
            ;;
    esac
done

if [[ -z "$DO_RESET" && -z "$DO_BUILD" ]]; then
    help
    exit 1
fi

check

if [[ -n "$DO_RESET" ]]; then
    reset
fi

if [[ -n "$DO_BUILD" ]]; then
    build
fi

echo "Build completed successfully for $TARGET!"
```

## Implementation Recommendations

### Phase 1: Extract Proven Patterns (Week 1)
1. **Adopt modular build script architecture**
2. **Implement platform-specific dependency management**
3. **Create fallback strategies** (like LevelDB pre-built approach)
4. **Use modern equivalents** of proven 2014 patterns

### Phase 2: Modern Toolchain Integration (Week 2-3)
1. **Replace MXE with modern MinGW-w64**
2. **Integrate UV package management**
3. **Adopt PyInstaller for Python cross-compilation**
4. **Implement modern testing strategies**

### Phase 3: Advanced Features (Week 4)
1. **CI/CD integration** using GitHub Actions
2. **Automated cross-platform testing**
3. **Modern signing and distribution**
4. **Performance optimization**

## Conclusion

The 2014 BUILD SCRIPTS ETC folder contains **valuable architectural patterns** that are still relevant for modern Python/PyQt6 cross-compilation:

**✅ Keep:**
- Modular script architecture
- Platform abstraction concepts
- Dependency verification strategies
- Static linking approaches
- Fallback mechanisms

**🔄 Modernize:**
- OS versions (Debian 7 → Ubuntu 24.04)
- Cross-compilation toolchains (MXE → modern MinGW/ARM64)
- Build systems (Makefile → PyInstaller/CMake)
- Package management (apt → UV)
- Testing strategies (manual → automated)

**🎯 Result:** A modern, maintainable cross-platform build system that leverages proven 2014 patterns with 2025 technology stack.

The legacy scripts provide an excellent foundation for our BlackHalo Python 3.14 + PyQt6 + cross-compilation strategy!