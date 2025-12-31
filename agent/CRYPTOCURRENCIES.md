# BlackHalo Supported Cryptocurrencies

## Overview

BlackHalo supports **3 different cryptocurrencies** through a unified smart contract platform. Each cryptocurrency has its own application variant and specific features.

## Supported Cryptocurrencies

### 1. **BlackCoin (BLK)** - PRIMARY FOCUS
**Application:** BlackHalo  
**Symbol:** BLK  
**Daemon:** `blackmored` (Official BlackCoin Node)  
**RPC Port:** 15715  
**Network Port:** 15714  

**Key Features:**
- **Official BlackCoin Node Software** (based on Bitcoin Core v26.2.0)
- **BlackCoin PoS v3.1** (mature Proof-of-Stake implementation)
- **Segwit Activation** (modern Bitcoin protocol features)
- **Staking enabled** (500 confirmations required)
- **Primary development focus** for BlackHalo
- **64-second block times**
- **Multi-signature support**
- **Native staking integration**

**Configuration:**
```python
NewCoin["daemon"] = "blackmored"  # Official BlackCoin node (Bitcoin Core v26.2.0)
NewCoin["name"] = "Blackcoin"
NewCoin["HaloName"] = "BlackHalo"
NewCoin["staking"] = True
NewCoin["stakeconfirmations"] = 500
NewCoin["blocktime"] = "64"
```

**Important Note:** This uses the **official modern BlackCoin node software**, not a custom fork. Based on Bitcoin Core v26.2.0 with BlackCoin PoS v3.1 and segwit activation, making it a legitimate, up-to-date cryptocurrency implementation.

**Network:** 70+ active nodes worldwide
**Website:** https://blackcoinmore.org

---

### 2. **BitBay (BAY)** - SECONDARY SUPPORT
**Application:** BitBay  
**Symbol:** BAY  
**Daemon:** `bitbayd`  
**RPC Port:** 19915  
**Network Port:** 19914  

**Key Features:**
- **Dynamic pegged currency system**
- **Advanced market features**
- **Algorithmic interest rates**
- **Cross-chain bridge capabilities**
- **64-second block times**
- **Modern GUI** (moderngui = 1)
- **Enhanced smart contract features**

**Configuration:**
```python
NewCoin1["daemon"] = "bitbayd"
NewCoin1["name"] = "BitBay"
NewCoin1["HaloName"] = "BitBay"
NewCoin1["pegging"] = True
NewCoin1["staking"] = True
NewCoin1["stakeconfirmations"] = 120
NewCoin1["moderngui"] = 1
```

**Special Features:**
- **Pegged Currency System:** Dynamic inflation/deflation controls
- **Market Making:** Automated market operations
- **Bridge Operations:** Cross-chain interoperability
- **Advanced Contracts:** Enhanced smart contract capabilities

**Network:** 100+ active nodes worldwide
**Website:** https://bitbay.market/

---

### 3. **Bitcoin (BTC)** - LEGACY SUPPORT
**Application:** BitHalo  
**Symbol:** BTC  
**Daemon:** `blackmored` (uses BlackCoin daemon)  
**RPC Port:** 15715  
**Network Port:** 15714  

**Key Features:**
- **Legacy Bitcoin support** 
- **Uses BlackCoin daemon** (not actual Bitcoin Core)
- **Proof-of-Stake** (not Bitcoin's PoW)
- **64-second block times** (not Bitcoin's 10 minutes)
- **Basic smart contract support**

**Configuration:**
```python
NewCoin2["daemon"] = "blackmored"  # Uses BlackCoin daemon!
NewCoin2["name"] = "Bitcoin"
NewCoin2["HaloName"] = "BitHalo"
NewCoin2["staking"] = True
NewCoin2["checksequenceverify"] = False
```

**Important Note:** This is **NOT real Bitcoin** - it uses the BlackCoin daemon for compatibility. The block time, consensus mechanism, and network are all BlackCoin-based.

---

## Migration Priority

### Phase 1: BlackCoin/BlackHalo (PRIMARY)
**Focus:** Complete BlackHalo migration for BlackCoin
- **Why:** Primary use case and most complete implementation
- **Scope:** Full Python 3.14 + PyQt6 migration
- **Timeline:** Complete first

### Phase 2: BitBay (SECONDARY)  
**Focus:** Migrate BitBay functionality
- **Why:** Advanced features and active development
- **Scope:** Pegged currency system and market features
- **Timeline:** After BlackHalo is stable

### Phase 3: Bitcoin (LEGACY)
**Focus:** Decide on Bitcoin support
- **Why:** Not real Bitcoin, uses BlackCoin daemon
- **Options:** 
  - Remove Bitcoin support entirely
  - Implement real Bitcoin Core integration
  - Keep as-is for backward compatibility

## Code Architecture for Multi-Currency

### Dynamic Currency Selection
```python
# Configuration determines which version runs
CoinSelect = {
    'BTC': {'name': 'Bitcoin', 'version': 'BitHalo'},
    'BAY': {'name': 'BitBay', 'version': 'Halo'}, 
    'BLK': {'name': 'BlackCoin', 'version': 'BlackHalo'}
}
```

### Single Codebase, Multiple Applications
- **One Halo.py** (49,664 lines) handles all 3 currencies
- **Configuration-driven** currency selection
- **Runtime coin switching** via config files
- **Shared smart contract engine** across all currencies

### File Structure Impact
```
├── pyblackcointools/      # BlackCoin integration - KEEP
├── pybitcointools/        # Bitcoin tools - MAYBE REMOVE
├── pybitcoincashtools/    # Bitcoin Cash - IGNORE (not used)
├── gui/styles/
│   ├── blk.py            # BlackCoin theme - KEEP
│   ├── bay.py            # BitBay theme - KEEP  
│   └── btc.py            # Bitcoin theme - MAYBE REMOVE
└── Config files:
    ├── Halo - BlackHalo Config.cfg
    ├── Halo - BitBay Config.cfg
    └── Halo - BitHalo Config.cfg
```

## Modernization Strategy

### For BlackCoin/BlackHalo:
1. **Keep all BlackCoin-specific code**
2. **Modernize pyblackcointools/** library
3. **Migrate PyQt4→PyQt6 for BlackCoin GUI**
4. **Test staking and smart contracts**

### For BitBay:
1. **Keep pegged currency system**
2. **Modernize market features**
3. **Update bridge operations**
4. **Test dynamic currency features**

### For Bitcoin:
1. **Decision needed:** Keep, remove, or replace
2. **If keeping:** Implement real Bitcoin Core RPC
3. **If removing:** Clean up related code and dependencies
4. **Focus resources** on BlackCoin and BitBay

## Testing Strategy

### BlackCoin Testing (Priority 1):
- [ ] Smart contract creation and execution
- [ ] Multi-signature operations  
- [ ] Staking functionality
- [ ] Transaction signing and broadcasting
- [ ] Address generation and validation

### BitBay Testing (Priority 2):
- [ ] Pegged currency operations
- [ ] Market maker functionality
- [ ] Bridge operations
- [ ] Dynamic interest rates
- [ ] Advanced smart contracts

### Bitcoin Testing (Priority 3):
- [ ] Basic functionality (if kept)
- [ ] Real Bitcoin Core integration (if implemented)
- [ ] Decision on legacy support

## Conclusion

**BlackHalo is fundamentally a BlackCoin platform** with BitBay as a advanced variant. Bitcoin support appears to be legacy/compatibility code that doesn't provide real Bitcoin functionality.

**Recommendation:** Focus modernization efforts on **BlackCoin (primary)** and **BitBay (secondary)**, with a clear decision needed on Bitcoin support.