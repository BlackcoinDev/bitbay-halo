"""
Tests for pyelliptic cryptographic operations.
"""

import pytest


class TestKeyGeneration:
    """Tests for ECC key generation."""

    def test_generate_key_returns_ecc_instance(self):
        """Test that key generation returns an ECC object."""
        from Bitmessage.pyelliptic.ecc import ECC

        key = ECC(curve="secp256k1")
        assert key is not None
        assert hasattr(key, "get_pubkey")

    def test_generated_keys_are_unique(self):
        """Test that two generated keys are different."""
        from Bitmessage.pyelliptic.ecc import ECC

        key1 = ECC(curve="secp256k1")
        key2 = ECC(curve="secp256k1")
        assert key1.get_pubkey() != key2.get_pubkey()

    def test_pubkey_format(self):
        """Test public key format (custom pyelliptic format)."""
        from Bitmessage.pyelliptic.ecc import ECC

        key = ECC(curve="secp256k1")
        pubkey = key.get_pubkey()
        assert isinstance(pubkey, bytes)
        # Custom format: curve(2) + lenX(2) + X(32) + lenY(2) + Y(32) = 70 bytes for secp256k1
        # However, default curve is sect283r1 which produces 78 bytes.
        # Ensure we are using secp256k1.
        assert len(pubkey) == 70
        assert pubkey[2:4] == b"\x00\x20"  # Length of X should be 32 bytes


class TestEncryptDecrypt:
    """Tests for ECIES encryption/decryption."""

    def test_encrypt_decrypt_roundtrip(self):
        """Test that encrypted data can be decrypted."""
        from Bitmessage.pyelliptic.ecc import ECC

        alice = ECC()
        bob = ECC()

        message = b"Hello from Alice!"
        encrypted = alice.encrypt(message, bob.get_pubkey())

        decrypted = bob.decrypt(encrypted)
        assert decrypted == message

    def test_wrong_key_fails_decrypt(self):
        """Test that wrong key cannot decrypt."""
        from Bitmessage.pyelliptic.ecc import ECC

        alice = ECC()
        bob = ECC()
        charlie = ECC()

        message = b"Secret message"
        encrypted = alice.encrypt(message, bob.get_pubkey())

        # Charlie should not be able to decrypt
        with pytest.raises(Exception):
            charlie.decrypt(encrypted)


class TestECDH:
    """Tests for ECDH key exchange."""

    def test_ecdh_shared_secret_matches(self):
        """Test that both parties derive the same shared secret."""
        from Bitmessage.pyelliptic.ecc import ECC

        alice = ECC()
        bob = ECC()

        # Both should derive the same shared secret
        secret_alice = alice.get_ecdh_key(bob.get_pubkey())
        secret_bob = bob.get_ecdh_key(alice.get_pubkey())

        assert secret_alice == secret_bob

    def test_ecdh_different_pairs_different_secrets(self):
        """Test that different key pairs give different secrets."""
        from Bitmessage.pyelliptic.ecc import ECC

        alice = ECC()
        bob = ECC()
        charlie = ECC()

        secret_ab = alice.get_ecdh_key(bob.get_pubkey())
        secret_ac = alice.get_ecdh_key(charlie.get_pubkey())

        assert secret_ab != secret_ac
