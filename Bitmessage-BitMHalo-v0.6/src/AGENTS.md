# Bitmessage-BitMHalo-v0.6/src/ Development Guide

**Updated:** January 2026  
**Status:** Legacy PyBitmessage codebase (Python 2.7 → 3.14 migration)

## OVERVIEW
Legacy Bitmessage protocol implementation with PyQt6 UI, networking, and crypto components being modernized from Python 2.7.

## STRUCTURE
- **bitmessageqt/** - PyQt6 GUI components, message views, address management
- **network/** - TCP/UDP connections, SOCKS proxy support, connection pooling
- **pyelliptic/** - Elliptic curve cryptography wrapper
- **bitmsghash/** - C++ proof-of-work acceleration (OpenCL)
- **translations/** - Qt translation files (.ts/.qm) for 15+ languages
- **storage/** - SQLite database abstraction layer
- **socks/** - SOCKS4/4a/5 proxy implementation

## WHERE TO LOOK
- **bitmessagemain.py** - Entry point, daemon initialization
- **protocol.py** - Bitmessage wire protocol constants and packet creation
- **shared.py** - Global state, configuration, thread locks
- **network/connectionpool.py** - Connection management singleton
- **class_singleWorker.py** - Message processing worker thread
- **api.py** - XML-RPC API server implementation

## CONVENTIONS
- **Python 2 heritage**: `ConfigParser`, `print` statements, `except E, e:` patterns
- **Threading model**: Classes prefixed with `class_` contain threaded workers
- **Crypto**: `highlevelcrypto.py` wraps OpenSSL via `pyelliptic`
- **Config**: `BMConfigParser` extends ConfigParser with safeGet methods
- **Debugging**: `debug.py` provides logger instance, state tracking

## ANTI-PATTERNS
- **Python 2 syntax**: `print "msg"`, `except Exception, e:`, `unicode()` calls
- **Legacy imports**: `ConfigParser` (use `configparser`), `urllib2` (use `urllib.request`)
- **Empty excepts**: `except:` without specific exception types
- **Threading locks**: Manual lock management instead of context managers
- **Global state**: Heavy use of module-level globals in `shared.py`