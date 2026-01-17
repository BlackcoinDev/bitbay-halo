"""
Tests for cryptographic operations (highlevelcrypto, pyelliptic).
"""


class TestPointMult:
    """Tests for EC point multiplication."""

    def test_point_mult_returns_bytes(self):
        """Test that pointMult returns bytes."""
        from highlevelcrypto import pointMult

        # 32-byte secret key
        secret = b"\x01" * 32
        result = pointMult(secret)
        assert isinstance(result, bytes)
        assert len(result) == 65  # Uncompressed public key


class TestSignVerify:
    """Tests for signing and verification."""

    def test_sign_verify_roundtrip(self):
        """Test that signed messages can be verified."""
        from highlevelcrypto import privToPub, sign, verify

        # Test private key (32 bytes hex = 64 chars)
        privkey = "0123456789abcdef" * 4
        pubkey = privToPub(privkey)

        message = b"Hello, World!"
        signature = sign(message, privkey)

        assert verify(message, signature, pubkey) is True

    def test_verify_fails_on_tamper(self):
        """Test that verification fails on tampered message."""
        from highlevelcrypto import privToPub, sign, verify

        privkey = "0123456789abcdef" * 4
        pubkey = privToPub(privkey)

        message = b"Hello, World!"
        signature = sign(message, privkey)

        tampered = b"Hello, World?"
        assert verify(tampered, signature, pubkey) is False
