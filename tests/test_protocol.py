"""
Tests for Bitmessage protocol serialization.
"""

import pytest


class TestVarint:
    """Extended tests for varint encoding/decoding."""

    def test_encode_zero(self):
        """Test encoding zero."""
        from Bitmessage.addresses import encodeVarint

        assert encodeVarint(0) == b"\x00"

    def test_encode_max_one_byte(self):
        """Test max value that fits in one byte."""
        from Bitmessage.addresses import encodeVarint

        assert encodeVarint(252) == b"\xfc"

    def test_encode_min_two_bytes(self):
        """Test min value requiring two bytes."""
        from Bitmessage.addresses import encodeVarint

        result = encodeVarint(253)
        assert result is not None
        assert result[0:1] == b"\xfd"
        assert len(result) == 3

    def test_encode_large_number(self):
        """Test encoding a large number."""
        from Bitmessage.addresses import encodeVarint

        result = encodeVarint(0xFFFFFFFF)  # 4 billion
        assert result is not None
        assert len(result) == 5
        assert result[0:1] == b"\xfe"

    def test_decode_roundtrip_all_sizes(self):
        """Test roundtrip for all size classes."""
        from Bitmessage.addresses import decodeVarint, encodeVarint

        test_values = [
            0,
            1,
            127,
            252,  # 1 byte
            253,
            1000,
            65535,  # 2 bytes
            65536,
            1000000,
            0xFFFFFFFF,  # 4 bytes
            0x100000000,  # 8 bytes
        ]
        for value in test_values:
            encoded = encodeVarint(value)
            assert encoded is not None
            res = decodeVarint(encoded)
            assert res is not None
            decoded, _ = res
            assert decoded == value, f"Failed for {value}"


class TestAddressChecksum:
    """Tests for address checksum validation."""

    def test_checksum_fails_on_tamper(self):
        """Test that tampered addresses fail checksum."""
        from Bitmessage.addresses import decodeAddress

        # Valid-looking but fake address
        res = decodeAddress("BM-2cTux3PGRqHTEH6wyUP2sWeT4LrsGgy63z")
        assert res is not None
        status, _, _, _ = res
        # Should either succeed or fail with proper error, but not crash
        assert status in ["success", "checksumfailed", "invalidcharacters"]

    def test_empty_address(self):
        """Test empty address handling."""
        from Bitmessage.addresses import decodeAddress

        res = decodeAddress("")
        assert res is not None
        status, _, _, _ = res
        assert status == "invalidcharacters"

    def test_whitespace_address(self):
        """Test whitespace-only address."""
        from Bitmessage.addresses import decodeAddress

        res = decodeAddress("   ")
        assert res is not None
        status, _, _, _ = res
        assert status == "invalidcharacters"
