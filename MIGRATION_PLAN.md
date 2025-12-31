# BlackHalo Python 2.7 → 3.14 & PyQt4 → PyQt6 Migration Plan

> [!CAUTION]
> **CRITICAL CONSTRAINT**: Only make changes REQUIRED for Python 2→3 or PyQt4→6 migration.
>
> - ❌ NO architecture changes
> - ❌ NO refactoring or "improvements"
> - ❌ NO "nice to have" changes
> - ✅ ONLY syntax/API compatibility fixes

## Executive Summary

BlackHalo is a multi-cryptocurrency smart contract application supporting **3 currencies**. The migration target is **Python 3.14** and **PyQt6**.

| Currency | Crypto Module | Import Alias | Notes |
|----------|---------------|--------------|-------|
| **Bitcoin (BTC)** | pybitcointools/ | `pybit` | 14 files |
| **BitBay (BAY)** | pybitcoincashtools/ | `pybit2` | **Identical** to pybitcointools |
| **BlackCoin (BLK)** | pyblackcointools/ | `pyblackcointools` | 7 files, unique PoS implementation |

---

## Project Architecture & Status

| File/Component | Lines | Status | Complexity |
|----------------|-------|--------|------------|
| **Halo.py** | **38,027** | ✅ **Done** | **High** (Core Logic) |
| **ANewBitHalo.py** | 6,705 | ⏳ Pending | **High** (Legacy UI) |
| **ATemplates.py** | 5,116 | ⏳ Pending | **High** (Legacy Templates) |
| **gui/mainwindow.py** | 1,507 | ⏳ Pending | **Medium** (Modern UI) |
| **pybitcointools/** | ~14 files | ✅ **Done** | High (Crypto) |
| **pybitcoincashtools/**| ~14 files | ✅ **Done** | High (Crypto) |
| **pyblackcointools/** | ~7 files | ✅ **Done** | High (Crypto) |
| **pyelliptic/** | ~6 files | ✅ **Done** | High (Crypto Bindings) |
| **highlevelcrypto.py** | 84 | ✅ **Done** | Medium (Wrappers) |
| **password.py** | 117 | ✅ **Done** | Low (AES) |
| **base58.py** | 88 | ✅ **Done** | Low (Encoding) |
| **ripemd.py** | 400 | ✅ **Done** | Low (Hashing) |
| **testblock.py** | 177 | ✅ **Done** | Medium (API) |
| **electrumaccessor.py**| 401 | ✅ **Done** | Medium (Network) |
| **electrumaccessor.py**| 401 | ✅ **Done** | Medium (Network) |
| **APIdemo.py** | 123 | ✅ **Done** | Low (Example) |
| **gtranslate.py** | 191 | ✅ **Done** | Low (Translation) |
| **stepic.py** | 125 | ✅ **Done** | Low (Steganography) |
| **BitMHalo.py** | ~926 | ⏳ Pending | **High** (Bitmessage Bridge) |
| **Bitmessage/** | ~50 files | ⏳ Pending | **High** (Separate Subproject) |

---

## Migration Phases

### ✅ Phase 1: Crypto Foundation (Completed)

**Goal**: Ensure all cryptographic operations work in Python 3.

- **pybitcointools/pybitcoincashtools**: Fixed explicit relative imports, removed Py2/3 dual import confusion, fixed hex encoding.
- **pyblackcointools**: Full migration from `long` types, `xrange`, and string-based hex to `bytes`.
- **pyelliptic**: Updated OpenSSL bindings, fixed `ctypes` argument types for Py3, fixed `arithmetic.py` division.
- **Support Modules**: `base58`, `ripemd`, `password` (AES), `highlevelcrypto` (ECC) all updated to handle `bytes` correctly.

### ✅ Phase 2: Support Infrastructure (Completed)

**Goal**: Ensure external network and API handling works in Python 3.

- **testblock.py**: Migrated `urllib2` -> `urllib.request`/`error`. Fixed exception syntax (`as e`).
- **electrumaccessor.py**: Updated `socket` handling to send/recv `bytes`. Removed `ord()` usage.
- **APIdemo.py**: Updated `xmlrpclib` -> `xmlrpc.client`, fixed `print`.
- **gtranslate.py**: Fixed `urllib` imports and `xrange` usage.
- **stepic.py**: Fixed `xrange` -> `range`, `imdata.next()` -> `next()`, and bytes/string handling.

### ✅ Phase 3: Core Application (Completed)

**Goal**: Migrate the massive `Halo.py` core logic.

- **Dependencies**:
  - `xmlrpc.server` / `xmlrpc.client`
  - `urllib.request`
  - `configparser`
  - `io.StringIO`
- **Syntax Fixes**:
  - `print` statements
  - `except Exception, e` -> `as e`
  - `unicode()` -> `str()` / `.encode()`
  - Integer division `//`
  - `long` type removal
- **Key Risk**: 38k+ lines means high chance of missing subtle logic changes. Verification will need to be section-by-section.

### ⏳ Phase 4: GUI Migration

**Goal**: Migrate from PyQt4 to PyQt6.

- **Imports**: `PyQt4` -> `PyQt6`
- **Widgets**: `QtGui` -> `QtWidgets` (mostly)
- **Signals**: `QtCore.SIGNAL()` -> `object.signal.connect()`
- **Web**: `QtWebKit` -> `QtWebEngineWidgets` (Major API difference)

### ⏳ Phase 5: Bitmessage & Integration

**Goal**: Migrate the Bitmessage subproject and run full integration tests.

- **Bitmessage**: Separate migration project (~50 files).
- **Integration**: Testing cross-currency contracts and full UI flows.

---

## Strict Migration Rules (Cross-Check Verified)

This plan adheres strictly to the user's constraints:

1. **No Refactoring**: Code structure in `Halo.py` and others will remain exactly as-is.
2. **No New Features**: Only existing functionality is preserved.
3. **Compatibility Only**: Changes are limited to those required by the interpreter (Python 3) or the library (PyQt6).

---

## External Dependencies Status

| Package | Purpose | Status |
|---------|---------|--------|
| **PyQt6** | GUI | ✅ Installed |
| **Pillow** | Imaging | ✅ Installed (replaces PIL) |
| **pyzmail39** | Email | ✅ Installed (replaces pyzmail) |
| **ujson** | JSON | ✅ Installed |
| **requests** | HTTP | ✅ Installed |
| **pysocks** | Proxy | ✅ Installed |
| **mechanize** | Web | ⚠️ Check Py3 compatibility during Halo migration |
