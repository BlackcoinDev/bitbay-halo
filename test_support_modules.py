import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import base58

try:
    import password
    HAS_PASSWORD_DEPS = True
except ImportError:
    print("WARNING: 'Crypto' library not found. Skipping password.py tests.")
    HAS_PASSWORD_DEPS = False

import highlevelcrypto

def test_base58():
    print("Testing base58.")
    data = b'Hello Base58'
    encoded = base58.b58encode(data)
    print(f"Encoded: {encoded}")
    decoded = base58.b58decode(encoded, len(data))
    print(f"Decoded: {decoded}")
    assert decoded == data
    
    # Test with padding (leading zeros)
    data_pad = b'\x00\x00Hello'
    encoded_pad = base58.b58encode(data_pad)
    print(f"Encoded (pad): {encoded_pad}")
    decoded_pad = base58.b58decode(encoded_pad, len(data_pad))
    print(f"Decoded (pad): {decoded_pad}")
    assert decoded_pad == data_pad
    print("Base58 Success!")

def test_password():
    if not HAS_PASSWORD_DEPS:
        return

    print("Testing password (AES).")
    secret = "my_secret_password"
    plaintext = "Sensitive Data to Encrypt"
    
    # Encrypt
    encrypted_base64 = password.EncryptWithAES(secret, plaintext)
    print(f"Encrypted (b64): {encrypted_base64}")
    
    # Decrypt
    decrypted = password.DecryptWithAES(secret, encrypted_base64)
    print(f"Decrypted: {decrypted}")
    
    assert decrypted == plaintext
    print("Password Success!")

def test_highlevelcrypto():
    print("Testing highlevelcrypto.")
    # This might fail if pyelliptic is not fully working or OpenSSL issues
    try:
        alice_key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
        cryptor = highlevelcrypto.makeCryptor(alice_key)
        
        msg = b"Secret Message"
        sig = cryptor.sign(msg)
        print(f"Signature generated: {len(sig)} bytes")
        
        pub = highlevelcrypto.privToPub(alice_key)
        print(f"Public Key: {pub}")
        
        valid = highlevelcrypto.verify(msg, sig, pub)
        print(f"Verify: {valid}")
        assert valid is True
        
        # Encrypt/Decrypt
        ciphertext = highlevelcrypto.encrypt(msg, pub)
        decrypted = highlevelcrypto.decrypt(msg=ciphertext, hexPrivkey=alice_key)
        print(f"Decrypted: {decrypted}")
        assert decrypted == msg
        
        print("HighLevelCrypto Success!")
    except Exception as e:
        print(f"HighLevelCrypto FAILED: {e}")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    try:
        test_base58()
        test_password()
        test_highlevelcrypto()
        print("ALL TESTS PASSED")
    except Exception as e:
        print("TEST FAILED")
        sys.exit(1)
