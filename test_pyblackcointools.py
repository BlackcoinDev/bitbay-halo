import os
import sys

# Add parent directory to path to ensure we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

print("Testing pyblackcointools imports.")
try:
    import pyblackcointools

    print("Imported pyblackcointools")
    from pyblackcointools import main

    print("Imported pyblackcointools.main")
    from pyblackcointools import transaction

    print("Imported pyblackcointools.transaction")
    from pyblackcointools import bci

    print("Imported pyblackcointools.bci")
    from pyblackcointools import deterministic

    print("Imported pyblackcointools.deterministic")
    from pyblackcointools import composite

    print("Imported pyblackcointools.composite")

    # Test safe_hexlify
    print("Testing safe_hexlify.")
    h = main.safe_hexlify(b"\x01\x02")
    print(f"safe_hexlify(b'\\x01\\x02') = {h}")
    assert h == "0102"

    # Test safe_unhexlify
    print("Testing safe_unhexlify.")
    b = main.safe_unhexlify("0102")
    print(f"safe_unhexlify('0102') = {repr(b)}")
    # In my architecture, unhexlify returns latin1 str (which acts as bytes) or bytes?
    # safe_unhexlify: return binascii.unhexlify(s).decode('latin1') (from my edit in main.py)
    # So it returns str.
    assert b == "\x01\x02"

    print("Success!")
except Exception as e:
    print(f"FAILED: {e}")
    import traceback

    traceback.print_exc()
