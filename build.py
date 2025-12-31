#!/usr/bin/env python3
"""
Cross-platform build script for BlackHalo
Modernized for Python 3.14+ and PyQt6 using UV
"""

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def check_uv_available():
    """Check if UV is available"""
    try:
        subprocess.run(["uv", "--version"], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("ERROR: Python 3.8+ required. Current version:", sys.version)
        return False
    return True


def setup_uv_project():
    """Set up UV project and install dependencies"""
    print("Setting up UV project...")

    # Initialize UV project if not exists
    if not Path("pyproject.toml").exists():
        subprocess.run(
            ["uv", "init", "--python", "3.14", "--name", "blackhalo"], check=True
        )

    # Install core dependencies
    deps = [
        "PyQt6",
        "PyQt6-WebEngine",
        "pyzmail39",
        "stopit",
        "pycryptodome",
        "requests",
        "pillow",
        "qrcode",
        "pyinstaller",
    ]

    for dep in deps:
        print(f"Adding {dep}...")
        subprocess.run(["uv", "add", dep], check=True)

    print("Dependencies installed successfully!")


def find_qt_path():
    """Find Qt6 path for PyInstaller bundling"""
    import site

    qt_paths = [
        "/usr/lib/python3/dist-packages/PyQt6/Qt6",
        "/usr/lib64/python3/site-packages/PyQt6/Qt6",
        f"{site.getsitepackages()[0]}/PyQt6/Qt6" if site.getsitepackages() else None,
    ]
    for path in qt_paths:
        if path and Path(path).exists():
            return path
    return None


def build_executable():
    """Build executable using PyInstaller with UV"""
    print("Building executable...")

    platform_name = platform.system().lower()
    script_name = "Halo.py"  # Use Halo.py as main entry point

    cmd = [
        "uv",
        "run",
        "--active",
        "pyinstaller",
        "--onefile",
        "--windowed",
        f"--name=BlackHalo-{platform_name}",
        script_name,
    ]

    qt_path = find_qt_path()
    if qt_path:
        cmd.extend(["--add-data", f"{qt_path}:Qt6"])
        print(f"Found Qt6 at: {qt_path}")
    else:
        print("Warning: Qt6 path not found, skipping Qt bundling")

    try:
        subprocess.run(cmd, check=True)
        print(f"Build successful: BlackHalo-{platform_name}")
        print(f"Executable location: dist/BlackHalo-{platform_name}")
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        return False

    return True


def run_tests():
    """Run basic tests to verify functionality using UV"""
    print("Running tests...")

    # Test imports using UV
    try:
        subprocess.run(
            [
                "uv",
                "run",
                "--active",
                "python3",
                "-c",
                "import PyQt6.QtCore; print('✓ PyQt6 import successful')",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"✗ PyQt6 import failed: {e}")
        return False

    try:
        subprocess.run(
            [
                "uv",
                "run",
                "--active",
                "python3",
                "-c",
                "import highlevelcrypto; print('✓ Crypto module import successful')",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"✗ Crypto module import failed: {e}")
        return False

    return True


def run_lint():
    """Run linting and formatting using UV"""
    print("Running code quality checks...")

    commands = [
        ["uv", "run", "--active", "black", ".", "--line-length=120"],
        ["uv", "run", "--active", "isort", ".", "--profile=black", "--line-length=120"],
        ["uv", "run", "--active", "flake8", ".", "--max-line-length=120"],
    ]

    for cmd in commands:
        try:
            print(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Warning: Linting command failed: {e}")


def main():
    """Main build process"""
    print("BlackHalo Cross-Platform Build Script (UV)")
    print("=" * 50)

    # Check dependencies
    if not check_uv_available():
        print(
            "ERROR: UV is required. Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh"
        )
        sys.exit(1)

    if not check_python_version():
        sys.exit(1)

    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.system()} {platform.release()}")

    # Set up UV project
    try:
        setup_uv_project()
    except Exception as e:
        print(f"Warning: UV project setup failed: {e}")

    # Run tests
    if not run_tests():
        print("Tests failed. Build may not work correctly.")
        # Don't exit - continue build anyway

    # Run linting
    try:
        run_lint()
    except Exception as e:
        print(f"Warning: Linting failed: {e}")

    # Build executable
    if not build_executable():
        print("Build failed!")
        sys.exit(1)

    print("\nBuild completed successfully!")
    print("\nNext steps:")
    print("1. Test the executable on target platforms")
    print("2. Fix any remaining import/compatibility issues")
    print("3. Run pytest tests: uv run --active pytest tests/")


if __name__ == "__main__":
    main()
