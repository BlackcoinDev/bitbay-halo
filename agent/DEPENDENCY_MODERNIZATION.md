# BlackHalo Dependency Modernization Assessment

**Date:** January 2026
**Purpose:** Assess crypto libraries and identify outdated packages for modernization

---

## Executive Summary

**Current State:**
- 85 packages installed via UV
- Core crypto libraries (pycryptodome, cryptography) are reasonably current
- Several legacy/unmaintained packages identified

**Recommendations:**
- **Keep:** pycryptodome, cryptography (modern and well-maintained)
- **Replace:** 7 legacy packages identified
- **OpenSSL 3.5.4:** Compatible with current cryptography library

---

## Crypto Libraries Assessment

### pycryptodome

| Aspect | Current | Assessment |
|--------|---------|------------|
| **Version** | 3.23.0 | Good (latest is 3.25.x) |
| **Status** | ✅ Actively maintained | Strong |
| **OpenSSL** | Built-in (no external deps) | Excellent |
| **Python 3.14** | ✅ Full support | Excellent |
| **Use Case** | AES encryption, hashing | Core crypto operations |

**Recommendation:** ✅ KEEP - No replacement needed
- Modern, well-maintained
- No external OpenSSL dependency (self-contained)
- Excellent Python 3.14 support

### cryptography (pyca)

| Aspect | Current | Assessment |
|--------|---------|------------|
| **Version** | 46.0.3 | Good (latest is ~46.x) |
| **Status** | ✅ Very actively maintained | Strong |
| **OpenSSL** | Uses system OpenSSL | Good |
| **Python 3.14** | ✅ Full support | Excellent |
| **Use Case** | OpenSSL bindings, X.509, RSA | Advanced crypto |

**OpenSSL Compatibility:**
```
cryptography 46.x → OpenSSL 1.1.1, 3.0.x, 3.5.x ✅
```

**Recommendation:** ✅ KEEP - No replacement needed
- One of the best-maintained Python crypto libraries
- Works with OpenSSL 3.5.4
- Strong security track record

### OpenSSL 3.5.4 Compatibility

| Package | OpenSSL 3.5.4 Support |
|---------|----------------------|
| cryptography 46.x | ✅ Yes |
| pycryptodome | ✅ Yes (bundled) |
| cffi | ✅ Yes |
| pyOpenSSL | ✅ Yes (via cryptography) |

**Note:** OpenSSL 3.5.4 is very new (April 2025). System packages may still be on 3.0.x or 3.3.x.

---

## Legacy/Unmaintained Packages Identified

### 1. html5lib (HIGH PRIORITY - Replace)

| Aspect | Details |
|--------|---------|
| **Current** | 0.999999999 (999999999 = unmaintained placeholder) |
| **Status** | ⚠️ Abandoned - no updates since ~2017 |
| **Why problematic** | Security vulnerabilities, no Python 3.14 guarantees |
| **Usage** | mechanize dependency |
| **Replacement** | `lxml` or `beautifulsoup4` (already installed) |

**Replacement:**
```python
# Instead of html5lib
from bs4 import BeautifulSoup

# Already installed: beautifulsoup4 4.14.3 ✅
```

### 2. mechanize (HIGH PRIORITY - Replace)

| Aspect | Details |
|--------|---------|
| **Current** | 0.4.10 |
| **Status** | ⚠️ Unmaintained since ~2018 |
| **Why problematic** | HTML parsing issues, Python 3 compatibility concerns |
| **Usage** | `Halo.py:244,294,19883` (web scraping) |
| **Replacement** | `requests` + `beautifulsoup4` or `httpx` |

**Replacement:**
```python
# Instead of mechanize
import requests
from bs4 import BeautifulSoup

# More modern, actively maintained
```

### 3. webencodings (MEDIUM PRIORITY - Remove)

| Aspect | Details |
|--------|---------|
| **Current** | 0.5.1 |
| **Status** | ⚠️ Very old (2014) |
| **Why problematic** | html5lib dependency, outdated encoding handling |
| **Usage** | Indirect (html5lib dep) |
| **Replacement** | Python's built-in `codecs` module |

**Note:** Will be auto-removed when html5lib is removed.

### 4. pyzmail39 (MEDIUM PRIORITY - Consider)

| Aspect | Details |
|--------|---------|
| **Current** | 0.0.2 |
| **Status** | ⚠️ Low activity |
| **Why problematic** | Complex API, email composition only |
| **Usage** | `BitMHalo.py:38,354` (email sending) |
| **Replacement** | `email` (built-in) or `fastmail` |

**Recommendation:** Consider replacing with built-in `email` module for simpler use cases.

### 5. yandex-translate (LOW PRIORITY - Remove)

| Aspect | Details |
|--------|---------|
| **Current** | 0.3.5 |
| **Status** | ⚠️ API likely changed |
| **Why problematic** | Yandex Translate API v1.0 deprecated |
| **Usage** | `Halo.py:258,305` (translation) |
| **Replacement** | `googletrans` or direct Google Translate API |

**Recommendation:** Remove or replace with modern translation library.

### 6. stepic (LOW PRIORITY - Replace)

| Aspect | Details |
|--------|---------|
| **Current** | 0.5.0 |
| **Status** | ⚠️ Unmaintained |
| **Why problematic** | Old steganography library |
| **Usage** | `Halo.py:265` (hidden data in images) |
| **Replacement** | Custom implementation or `stegano` |

**Recommendation:** Replace with active steganography library.

### 7. python-bsonjs (LOW PRIORITY - Replace)

| Aspect | Details |
|--------|---------|
| **Current** | 0.7.0 |
| **Status** | ⚠️ Low activity |
| **Why problematic** | C extension, pymongo has built-in BSON |
| **Usage** | `Halo.py:262,308` (BSON serialization) |
| **Replacement** | `pymongo.bson` (built-in) |

**Replacement:**
```python
# Instead of python-bsonjs
from pymongo import bson
# or simply use built-in json for most cases
```

### 8. pydenticon (LOW PRIORITY - Review)

| Aspect | Details |
|--------|---------|
| **Current** | 0.3.1 |
| **Status** | ⚠️ Low activity |
| **Usage** | Identicon generation |
| **Replacement** | `identicon` or custom implementation |

**Recommendation:** Review if actively used, otherwise replace.

---

## Well-Maintained Packages (No Action Needed)

| Package | Version | Status |
|---------|---------|--------|
| PyQt6 | 6.10.1 | ✅ Current |
| requests | 2.32.5 | ✅ Current |
| urllib3 | 2.6.2 | ✅ Current |
| pytest | 9.0.2 | ✅ Current |
| black | 25.12.0 | ✅ Current |
| pillow | 12.0.0 | ✅ Current |
| selenium | 4.39.0 | ✅ Current |
| attrs | 25.4.0 | ✅ Current |
| cryptography | 46.0.3 | ✅ Current |
| pycryptodome | 3.23.0 | ✅ Current |
| trio | 0.32.0 | ✅ Current |
| click | 8.3.1 | ✅ Current |
| packaging | 25.0 | ✅ Current |

---

## Replacement Plan

### Phase 1: Critical Replacements (Week 1)

| Package | Replace With | Effort | Risk |
|---------|-------------|--------|------|
| html5lib | beautifulsoup4 (already installed) | Low | Low |
| mechanize | requests + beautifulsoup4 | Medium | Medium |

### Phase 2: Email/Translation (Week 2)

| Package | Replace With | Effort | Risk |
|---------|-------------|--------|------|
| pyzmail39 | built-in `email` module | Medium | Medium |
| yandex-translate | googletrans or remove | Low | Low |

### Phase 3: Optional Enhancements (Week 3)

| Package | Replace With | Effort | Risk |
|---------|-------------|--------|------|
| stepic | stegano library | Low | Low |
| python-bsonjs | pymongo.bson or json | Low | Low |
| pydenticon | identicon or custom | Low | Low |

---

## Code Migration Examples

### mechanize → requests + BeautifulSoup

```python
# OLD (mechanize)
import mechanize
browser = mechanize.Browser()
browser.open(url)
response = browser.read()

# NEW (requests + beautifulsoup4)
import requests
from bs4 import BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
```

### pyzmail39 → built-in email

```python
# OLD (pyzmail39)
import pyzmail
payload, mail_from, rcpt_to, msg_id = pyzmail.compose_mail(...)

# NEW (built-in email)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg.attach(MIMEText(body, 'plain'))
```

### python-bsonjs → pymongo.bson or json

```python
# OLD (python-bsonjs)
import bsonjs
data = bsonjs.loads(bson_data)

# NEW (pymongo.bson or json)
import json  # Most cases
data = json.loads(bson_data.decode('utf-8'))
# or
from pymongo import bson
data = bson.BSON(bson_data).decode()
```

---

## Security Considerations

### Packages with Security Implications

| Package | Current Version | Security Notes |
|---------|-----------------|----------------|
| pycryptodome | 3.23.0 | ✅ Good - no known CVEs |
| cryptography | 46.0.3 | ✅ Good - actively audited |
| requests | 2.32.5 | ✅ Good - no known CVEs |
| urllib3 | 2.6.2 | ✅ Good - patched past CVEs |
| html5lib | 0.999999999 | ⚠️ Risk - unmaintained |
| mechanize | 0.4.10 | ⚠️ Risk - unmaintained |

**Recommendation:** Prioritize removing html5lib and mechanize due to security concerns.

---

## Testing After Migration

After replacing packages, verify:

1. ✅ Web scraping functionality works
2. ✅ Email sending works
3. ✅ Translation (if kept) works
4. ✅ All tests pass (uv run --active pytest tests/)
5. ✅ No new linting errors

---

## Summary

| Action | Count | Estimated Effort |
|--------|-------|------------------|
| Keep (no change) | 77 | - |
| Replace | 4-6 | 1-2 weeks |
| Remove | 1-2 | 1-2 days |

**Crypto libraries (pycryptodome, cryptography) are in good shape** - no replacement needed. Focus modernization efforts on the legacy HTML/email packages.
