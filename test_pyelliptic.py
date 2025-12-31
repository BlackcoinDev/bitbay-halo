import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

print("Testing pyelliptic.")
try:
    import pyelliptic
    print(f"pyelliptic imported. OpenSSL version: {pyelliptic.OpenSSL._version}")
    
    # Test ECC
    print("Testing ECC generation.")
    alice = pyelliptic.ECC()
    bob = pyelliptic.ECC()
    print("Keys generated.")

    # Test Sign/Verify
    print("Testing Sign/Verify.")
    msg = b"Hello Crypto World"
    sig = alice.sign(msg)
    print(f"Signature length: {len(sig)}")
    valid = alice.verify(sig, msg)
    print(f"Signature valid: {valid}")
    assert valid is True

    # Test Encrypt/Decrypt (ECIES)
    print("Testing Encrypt/Decrypt.")
    ciphertext = alice.encrypt(msg, bob.get_pubkey())
    print(f"Ciphertext length: {len(ciphertext)}")
    decrypted = bob.decrypt(ciphertext)
    print(f"Decrypted: {decrypted}")
    assert decrypted == msg

    print("Success!")
except Exception as e:
    print(f"FAILED: {e}")
    import traceback
    traceback.print_exc()
