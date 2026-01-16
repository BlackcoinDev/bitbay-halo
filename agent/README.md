# BlackHalo - Smart Contracts & Decentralized Exchange

BlackHalo is a revolutionary cryptocurrency platform that enables trustless smart contracts and decentralized marketplaces through double deposit escrow systems.

## Overview

BlackHalo eliminates middlemen by using cryptographic enforcement of contracts rather than traditional escrow services. Released July 4th, 2014 by David Zimbeck, it offers "unbreakable contracts" where theft is impossible thanks to advanced deposit mechanisms.

## Core Architecture

### Main Components
- **BlackHalo Core** - Smart contracting engine with double deposit escrow
- **BlackCoin Currency** - Official modern cryptocurrency (Bitcoin Core v26.2.0 + PoS v3.1)
- **BitBay Currency** - PoS-based cryptocurrency with dynamic inflation/deflation controls
- **Bitmessage Integration** - Decentralized encrypted communication
- **PyElliptic Cryptography** - ECC, AES, and cryptographic operations
- **GUI Layer** - Qt-based user interface with naming conventions

### Cryptocurrency Support
- **Blackcoin** - Official modern cryptocurrency (Bitcoin Core v26.2.0 + PoS v3.1)
- **BitBay** - Dynamic currency with algorithmic interest rates
- **Bitcoin** - Legacy support (not recommended)
- **USD Integration** - Real-time exchange rate synchronization

## Key Features

### Unbreakable Contracts
- Double deposit escrow system prevents theft
- No middlemen or escrow services required
- Cryptographic enforcement of agreements
- Timeout transactions destroy escrows on expiration

### Decentralized Marketplace
- Zero fees, no chargebacks, no arbiters
- International peer-to-peer trading
- Like combining E-Bay, Alibaba, and Freelancer
- No servers or centralized infrastructure

### Advanced Security
- Multisignature accounts with two-key authentication
- 2FA support through separate key locations
- Key hiding within images for additional security
- Automated signature verification and broken link repair

### Smart Contract Types
- **Employment Contracts** - Guaranteed work performance and payment
- **Cash for Coins** - Global wire and Western Union alternatives
- **Barter Trading** - Exchange any commodities or assets
- **Joint Accounts** - Shared wallets with approval requirements
- **Python Contracts** - Custom smart contract automation
- **Micro-trading** - Incremental trust building for large transactions

### Communication & Integration
- **Bitmessage Integration** - Decentralized encrypted messaging
- **Pay to Email** - Send crypto to non-crypto users
- **Gmail/Hotmail Support** - Receive market orders via traditional email
- **Decentralized Email** - Server-free encrypted communication

## Technical Implementation

### GUI Structure
```
gui/
├── fonts/          # Default Roboto font
├── forms/          # All UI forms
├── icons/          # Base + per-style icons
├── images/         # Base + per-style images
└── styles/         # Qt Style Sheets (QSS)
```

### Python Naming Conventions
- `variableName` - Class/object members/properties
- `var_name` - Temporary scope variables
- `i,j,k` - Short names for small scope loops
- UI forms: `type_variableName` (e.g., `le_firstName` for line edit)

### Development Process
- Feature branches for major developments
- Regular master branch builds and testing
- Pull request workflow with 15-day stale issue closure
- Coding conventions adherence required
- PGP-signed commits for contributions

## Installation & Setup

### Dependencies
- Python 2.7+
- PyQt4 (python-qt4 on Debian/Ubuntu)
- OpenSSL with compatibility libraries
- Git for version control

### Running BlackHalo
```bash
# From source
python src/bitmessagemain.py

# Or use provided scripts
./bitmhalo.sh
```

### Configuration Files
- `Halo.cfg` - Main configuration
- `Halo - BlackHalo Config.cfg` - BlackHalo-specific settings
- `keys.dat` - API keys and user settings

## Security Model

### Safeguards
1. **Signature Verification** - Confirms proper escrow signing
2. **Destruction Transactions** - Timeout mechanisms prevent dishonest profit
3. **Instant Refunds** - Circumvents transaction malleability
4. **Auto-backup** - Contract history backup to secondary locations
5. **Reputation System** - Decentralized peer-to-peer moderation
6. **Broken Link Repair** - Automatic transaction ID re-signing

### Multi-Layer Security
- Two-key account system
- Separate password requirements per key
- Cold staking capabilities
- Image-based key hiding
- Automated backup systems

## Advanced Features

### Python Contract Automation
- Custom Python code execution within contracts
- No blockchain bloat like Ethereum
- Protocol-agnostic contract evolution
- Perfect for derivatives and price checking

### Dynamic Currency (BitBay)
- Inflation/deflation controls through voting
- Algorithmic interest rate management
- Bond-like instruments and advanced contracts
- Self-banking capabilities

### Decentralized Governance
- Community-driven moderation
- Reputation-based trust systems
- Voluntary participation in market cleaning
- Peer-to-peer dispute resolution

## Integration Points

### Bitmessage Protocol
- P2P encrypted communication
- No reliance on certificate authorities
- Strong authentication prevents spoofing
- Metadata protection from passive surveillance

### PyElliptic Cryptography
- ECC key agreement (ECDH)
- Digital signatures (ECDSA)
- Hybrid encryption (ECIES)
- AES-256 symmetric encryption
- CSPRNG and HMAC-SHA512

## Development Guidelines

### Code Contributions
- Follow PEP8 coding standards
- Target v0.6 branch for pull requests
- Ensure fast-forward merge capability
- PGP-sign all commits
- Explain code functionality clearly

### Translation Support
- Use Transifex for localization
- Consult Microsoft Language Portal for technical terms
- No pull requests needed for translations

## File Structure
```
/home/blackcoindev/Development/blackhalo/
├── agent/                    # This documentation
├── gui/                      # User interface components
├── Bitmessage/              # Encrypted messaging integration
├── Bitmessage-BitMHalo-v0.6/ # Bitmessage core
├── pyelliptic/              # Cryptographic library
├── pybitcoincashtools/      # Bitcoin cash utilities
├── pybitcointools/          # Bitcoin utilities
├── pyblackcointools/        # Blackcoin utilities
├── BUILD SCRIPTS ETC/       # Build and deployment scripts
└── translations/            # Localization files
```

## Use Cases

### Business Applications

- International wire transfers without intermediaries
- Employment contracts with guaranteed performance
- Supply chain verification and automation
- Decentralized freelancer marketplace

### Financial Services

- Peer-to-peer currency exchange
- Collateralized lending with smart contracts
- Automated market making
- Cross-chain atomic swaps

### Social Applications

- Community cooperative management
- Reputation-based social networks
- Decentralized voting systems
- Trust-building through micro-transactions

## Community & Support

### Developer Contact
- DevTalk pseudo-mailing list: BM-2D9QKN4teYRvoq2fyzpiftPh9WP9qggtzh
- GitHub pull requests for code contributions
- NightTrader exchange community: https://nighttrader.org/

### Documentation
- Whitepaper: Available in repository
- Protocol specification and API references
- Installation guides for multiple platforms
- Community-driven wiki and forums

This platform represents a foundational shift toward trustless economic interactions, enabling global commerce without traditional financial intermediaries while maintaining security through cryptographic enforcement mechanisms.