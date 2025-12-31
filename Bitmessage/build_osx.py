from setuptools import setup

name = "Bitmessage"
version = "0.4.4"
mainscript = ["bitmessagemain.py"]

setup(
    name = name,
    version = version,
    app = mainscript,
    setup_requires = ["py2app"],
    options = dict(
        py2app = dict(
            resources = ["images", "translations"],
            includes = ['sip', 'PyQt6._qt'],
            iconfile = "images/bitmessage.icns"
        )
    )
)
