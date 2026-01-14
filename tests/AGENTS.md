# BlackHalo Test Suite

**Updated:** January 2026
**Python:** 3.14+ | **Framework:** pytest

## OVERVIEW
Comprehensive test coverage for BlackHalo's core cryptographic and protocol modules.

## TEST STRUCTURE

| Module | File | Test Focus |
|--------|------|------------|
| Crypto | `test_crypto.py` | ECDSA sign/verify, point multiplication |
| PyElliptic | `test_pyelliptic.py` | Key generation, ECDH, encrypt/decrypt |
| Addresses | `test_addresses.py` | Varint encoding, address validation |
| Protocol | `test_protocol.py` | Message serialization, checksums |
| API | `test_api.py` | Helper functions, address verification |

## RUN COMMANDS

```bash
uv run pytest tests/                    # All tests
uv run pytest tests/test_crypto.py      # Single module
uv run pytest -k "test_sign_verify"     # Pattern match
uv run pytest --cov=Bitmessage --cov=highlevelcrypto  # Coverage
uv run python tests/scripts/lint.py     # Style check
```

## CONVENTIONS

- **Test classes:** `Test*` prefix, one per module function
- **Test methods:** `test_*` prefix, descriptive names
- **Fixtures:** Defined in `conftest.py`, shared across tests
- **Mocking:** Use `unittest.mock` for external dependencies
- **Coverage:** Target 100% for crypto/protocol modules