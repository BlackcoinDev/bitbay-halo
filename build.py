#!/usr/bin/env python3
"""
Cross-platform build script for BlackHalo
Modernized for Python 3.14+ and PyQt6 using UV
"""


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
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("ERROR: Python 3.8+ required. Current version:", sys.version)
        return False
    return True


def setup_uv_project():
    """Set up UV project and install dependencies"""
    print("Setting up UV project...")

    # Initialize UV project if not exists
    if not Path("pyproject.toml").exists():
        subprocess.run(["uv", "init", "--python", "3.14", "--name", "blackhalo"], check=True)

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

    # Add py2app for macOS builds
    if platform.system().lower() == "darwin":
        deps.append("py2app")
        # Also add create-dmg for DMG creation
        deps.append("create-dmg")

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


def build_macos_app():
    """Build macOS .app bundle using py2app with UV"""
    print("Building macOS app bundle with py2app...")

    platform_name = platform.system().lower()
    if platform_name != "darwin":
        print("ERROR: py2app builds only work on macOS")
        return False

    # Create setup.py for py2app
    setup_content = '''#!/usr/bin/env python3
"""
py2app setup for BlackHalo macOS build
"""
from setuptools import setup

APP = ['Halo.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'bundle_script_name': 'BlackHalo',
    'copy_python_path': True,
    'exclusive': True,
    'iconfile': 'gui/images/BlackHalo.icns',
    'plist': {
        'CFBundleName': 'BlackHalo',
        'CFBundleDisplayName': 'BlackHalo',
        'CFBundleIdentifier': 'org.blackhalo.app',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundlePackageType': 'APPL',
        'CFBundleExecutable': 'BlackHalo',
        'NSHighResolutionCapable': True,
        'LSRequiresIPhoneOS': False,
        'NSPrincipalClass': 'NSApplication',
        'CFBundleURLTypes': [
            {
                'CFBundleURLName': 'org.blackhalo.app',
                'CFBundleURLSchemes': ['blackhalo'],
            },
        ],
    },
    'resources': [
        'gui/images/BlackHalo.icns',
        'gui/images/dmg_background.png',
    ],
    'frameworks': [],
    'private_frameworks': [],
    'strip': True,
    'suppress_error_output': False,
    'use_pythonw': True,
    'verbose': False,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
'''

    setup_path = Path("setup-macOS.py")
    setup_path.write_text(setup_content)
    print(f"Created {setup_path}")

    # Build the app using py2app
    cmd = [
        "uv",
        "run",
        "--active",
        "python3",
        "setup-macOS.py",
        "py2app",
    ]

    try:
        subprocess.run(cmd, check=True)
        print("py2app build successful!")

        # Move app to dist folder if needed
        app_path = Path("dist/BlackHalo.app")
        if app_path.exists():
            dist_dir = Path("dist")
            dist_dir.mkdir(exist_ok=True)
            shutil.move(str(app_path), str(dist_dir / "BlackHalo.app"))
            print("App bundle location: dist/BlackHalo.app")
        else:
            print(f"Warning: Expected app not found at {app_path}")

    except subprocess.CalledProcessError as e:
        print(f"py2app build failed: {e}")
        return False

    return True


def create_macos_dmg():
    """Create DMG from .app bundle using create-dmg"""
    print("Creating DMG file...")

    app_path = Path("dist/BlackHalo.app")
    dmg_path = Path("dist/BlackHalo-macOS-Universal.dmg")

    if not app_path.exists():
        print(f"ERROR: App bundle not found at {app_path}")
        return False

    # Create DMG using create-dmg
    cmd = [
        "uv",
        "run",
        "--active",
        "create-dmg",
        "--volname",
        "BlackHalo",
        "--volicon",
        "gui/images/BlackHalo.icns",
        "--background",
        "gui/images/dmg_background.png",
        "--window-pos",
        "200",
        "120",
        "--window-size",
        "800",
        "500",
        "--app-drop-link",
        "600",
        "185",
        "--format",
        "UDBZ",
        str(dmg_path),
        str(app_path.parent),
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"DMG created successfully: {dmg_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"create-dmg failed: {e}")
        return False


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
        ["uv", "run", "--active", "black", ".", "--line-length=180"],
        ["uv", "run", "--active", "isort", ".", "--profile=black", "--line-length=180"],
        ["uv", "run", "--active", "flake8", ".", "--max-line-length=180"],
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
        print("ERROR: UV is required. Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh")
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
    platform_name = platform.system().lower()

    if platform_name == "darwin":
        # Use py2app for macOS
        if not build_macos_app():
            print("macOS app build failed!")
            sys.exit(1)

        # Create DMG
        if not create_macos_dmg():
            print("DMG creation failed!")
            # Don't exit - app was built successfully

        print("\nBuild completed successfully!")
        print("\nNext steps:")
        print("1. Code sign the app: codesign --deep --sign 'Developer ID' dist/BlackHalo.app")
        print("2. Notarize for distribution: xcrun notarytool submit dist/BlackHalo.app --apple-id 'email' --password 'app-password' --wait")
        print("3. Test the .dmg on target macOS versions")

    else:
        # Use PyInstaller for Windows/Linux
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
