from typing import Any, Dict

from setuptools import setup

name = "Bitmessage"
version = "0.4.4"
mainscript = ["bitmessagemain.py"]

OPTIONS: Dict[str, Any] = {
    "py2app": {
        "resources": ["images", "translations"],
        "includes": ["sip", "PyQt6._qt"],
        "iconfile": "images/bitmessage.icns",
    }
}

setup(
    name=name,
    version=version,
    app=mainscript,
    setup_requires=["py2app"],
    options=OPTIONS,
)
