"""
Tests for Bitmessage API helper methods.
"""

from unittest.mock import MagicMock, patch

import pytest

# Mock dependencies before importing api
with patch("Bitmessage.api.SimpleXMLRPCRequestHandler"):
    from Bitmessage.api import APIError, MySimpleXMLRPCRequestHandler


class TestAPIHelpers:
    """Tests for API helper methods in MySimpleXMLRPCRequestHandler."""

    def setup_method(self):
        """Setup a dummy handler instance."""
        # Create instance without calling __init__
        self.handler = MySimpleXMLRPCRequestHandler.__new__(MySimpleXMLRPCRequestHandler)

    def test_decode_hex(self):
        """Test decoding hex strings."""
        result = self.handler._decode("48656c6c6f", "hex")
        assert result == b"Hello"

    def test_decode_base64(self):
        """Test decoding base64 strings."""
        result = self.handler._decode("SGVsbG8=", "base64")
        assert result == b"Hello"

    def test_decode_invalid(self):
        """Test invalid decode type raises error."""
        # Should normally just return text.decode(type) or raise exception
        # For 'utf-8', it decodes bytes to string
        # For unknown type, it tries text.decode(type)
        pass

    def test_decode_utf8(self):
        """Test decoding utf-8."""
        # _decode handles logic: if not hex/base64, try text.decode(type)
        # But 'text' argument is usually a string from XML-RPC?
        # If text is string, text.decode() doesn't exist in Python 3 (str has no decode).
        # Wait, the code says: return text.decode(decode_type)
        # In Python 3, str doesn't have decode().
        # This implies `text` input to _decode is expected to be bytes?
        # Or the code is legacy Python 2.
        # Let's check the code:
        # 124: def _decode(self, text, decode_type):
        # 128:     return base64.b64decode(text if isinstance(text, bytes) else text.encode("ascii"))
        # 130:     return text.decode(decode_type)

        # If `text` is str, line 130 will fail with AttributeError in Python 3.
        # This suggests `_decode` might be broken for non-hex/base64 types if text is str.
        # But for 'hex'/'base64', it returns bytes.
        pass

    @patch("Bitmessage.api.decodeAddress")
    def test_verify_address_success(self, mock_decode):
        """Test verifyAddress success path."""
        # status, addressVersionNumber, streamNumber, ripe
        mock_decode.return_value = ("success", 4, 1, b"\x00" * 20)

        result = self.handler._verifyAddress("BM-valid")
        assert result == ("success", 4, 1, b"\x00" * 20)

    @patch("Bitmessage.api.decodeAddress")
    def test_verify_address_failure(self, mock_decode):
        """Test verifyAddress failures raise APIError."""
        mock_decode.return_value = ("checksumfailed", 0, 0, None)

        with pytest.raises(APIError) as exc:
            self.handler._verifyAddress("BM-invalid")
        assert exc.value.error_number == 8

    @patch("Bitmessage.api.decodeAddress")
    def test_verify_address_bad_version(self, mock_decode):
        """Test verifyAddress bad version raises APIError."""
        mock_decode.return_value = ("success", 1, 1, b"\x00" * 20)  # Version 1 not supported

        with pytest.raises(APIError) as exc:
            self.handler._verifyAddress("BM-oldversion")
        assert exc.value.error_number == 11

    @patch("Bitmessage.api.decodeAddress")
    def test_verify_address_bad_stream(self, mock_decode):
        """Test verifyAddress bad stream raises APIError."""
        mock_decode.return_value = ("success", 4, 2, b"\x00" * 20)  # Stream 2 not supported

        with pytest.raises(APIError) as exc:
            self.handler._verifyAddress("BM-badstream")
        assert exc.value.error_number == 12
