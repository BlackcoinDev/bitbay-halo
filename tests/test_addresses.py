"""
Tests for Bitmessage address encoding and decoding.
"""

import pytest


class TestEncodeVarint:
    """Tests for the encodeVarint function."""

    def test_small_integer(self):
        """Test encoding integers < 253."""
        from Bitmessage.addresses import encodeVarint

        result = encodeVarint(0)
        assert result == b"\x00"

        result = encodeVarint(252)
        assert result == b"\xfc"

    def test_medium_integer(self):
        """Test encoding integers 253-65535."""
        from Bitmessage.addresses import encodeVarint

        result = encodeVarint(253)
        assert result is not None
        assert result[0:1] == b"\xfd"

        result = encodeVarint(65535)
        assert result is not None
        assert len(result) == 3

    def test_negative_raises(self):
        """Test that negative integers raise an error."""
        from Bitmessage.addresses import encodeVarint

        with pytest.raises(SystemExit):
            encodeVarint(-1)


class TestDecodeVarint:
    """Tests for the decodeVarint function."""

    def test_roundtrip(self):
        """Test that encode/decode roundtrip works."""
        from Bitmessage.addresses import decodeVarint, encodeVarint

        for value in [0, 1, 252, 253, 65535, 65536, 4294967295]:
            encoded = encodeVarint(value)
            assert encoded is not None
            res = decodeVarint(encoded)
            assert res is not None
            decoded, length = res
            assert decoded == value


class TestDecodeAddress:
    """Tests for the decodeAddress function."""

    def test_invalid_address(self):
        """Test that invalid addresses return error status."""
        from Bitmessage.addresses import decodeAddress

        res = decodeAddress("invalid")
        assert res is not None
        status, _, _, _ = res
        assert status != "success"

    def test_valid_prefix(self):
        """Test that BM- prefix is handled."""
        from Bitmessage.addresses import decodeAddress

        # This should at least not crash
        res = decodeAddress("BM-")
        assert res is not None
        status, _, _, _ = res
        assert status in ["invalidcharacters", "checksumfailed", "success"]
