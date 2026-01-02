"""
Cryptographic utilities for BlackHalo 2.0
Type-safe cryptographic operations
"""

from typing import Any, Tuple, Optional
from decimal import Decimal
from dataclasses import dataclass
import hashlib
import secrets
import struct

from ..types import Address, TxHash, HexString, PrivateKey, PublicKey


def sha256(data: bytes) -> bytes:
    """Compute SHA-256 hash"""
    return hashlib.sha256(data).digest()


def sha512(data: bytes) -> bytes:
    """Compute SHA-512 hash"""
    return hashlib.sha512(data).digest()


def double_sha256(data: bytes) -> bytes:
    """Compute double SHA-256 hash"""
    return sha256(sha256(data))


def ripemd160(data: bytes) -> bytes:
    """Compute RIPEMD-160 hash"""
    h = hashlib.new("ripemd160")
    h.update(data)
    return h.digest()


def hash160(data: bytes) -> bytes:
    """Compute RIPEMD-160(SHA-256(data))"""
    return ripemd160(sha256(data))


def hash256(data: bytes) -> bytes:
    """Alias for double_sha256"""
    return double_sha256(data)


def hex_to_bytes(hex_string: str) -> bytes:
    """Convert hex string to bytes"""
    return bytes.fromhex(hex_string)


def bytes_to_hex(data: bytes) -> str:
    """Convert bytes to hex string"""
    return data.hex()


def safe_hexlify(data: Any) -> str:
    """Convert bytes to hex string (legacy compatible)"""
    if isinstance(data, str):
        return data
    if isinstance(data, bytes):
        return data.hex()
    return str(data)


def safe_unhexlify(hex_string: str | bytes) -> bytes:
    """Convert hex string to bytes (legacy compatible)"""
    if isinstance(hex_string, bytes):
        return hex_string
    return bytes.fromhex(hex_string)


def num_to_var_int(n: int) -> bytes:
    """Encode integer as Bitcoin-style variable-length integer"""
    if n < 0xFD:
        return bytes([n])
    elif n < 0xFFFF:
        return bytes([0xFD]) + struct.pack("<H", n)
    elif n < 0xFFFFFFFF:
        return bytes([0xFE]) + struct.pack("<L", n)
    else:
        return bytes([0xFF]) + struct.pack("<Q", n)


def var_int_to_num(data: bytes, offset: int = 0) -> Tuple[int, int]:
    """Decode Bitcoin-style variable-length integer"""
    if data[offset] < 0xFD:
        return data[offset], offset + 1
    elif data[offset] == 0xFD:
        return struct.unpack("<H", data[offset + 1 : offset + 3])[0], offset + 3
    elif data[offset] == 0xFE:
        return struct.unpack("<L", data[offset + 1 : offset + 5])[0], offset + 5
    else:
        return struct.unpack("<Q", data[offset + 1 : offset + 9])[0], offset + 9


@dataclass
class KeyPair:
    """Public/private key pair"""

    private_key: bytes
    public_key: bytes

    @property
    def private_hex(self) -> str:
        return self.private_key.hex()

    @property
    def public_hex(self) -> str:
        return self.public_key.hex()


def generate_private_key() -> bytes:
    """Generate a random 32-byte private key"""
    return secrets.token_bytes(32)


def private_to_public_key(private_key: bytes) -> bytes:
    """
    Derive public key from private key using SECP256k1.
    This is a placeholder - real implementation would use ecdsa.
    """
    # Placeholder: In real implementation, use ecdsa or similar library
    # to compute public key from private key on SECP256k1 curve
    return sha256(private_key) + sha256(private_key + b"pub")


def private_key_to_wif(
    private_key: bytes,
    compressed: bool = True,
    magic_byte: int = 0xBD,  # BlackCoin magic byte
) -> str:
    """
    Convert private key to WIF (Wallet Import Format)

    Args:
        private_key: 32-byte private key
        compressed: Whether to use compressed public key
        magic_byte: Network magic byte (0xbd for BlackCoin)
    """
    # Add magic byte and compressed flag
    if compressed:
        data = bytes([magic_byte]) + private_key + bytes([0x01])
    else:
        data = bytes([magic_byte]) + private_key

    # Double SHA256 for checksum
    checksum = double_sha256(data)[:4]
    return safe_hexlify(data + checksum)


def wif_to_private_key(wif: str, magic_byte: int = 0xBD) -> bytes:
    """Convert WIF to private key"""
    data = safe_unhexlify(wif)

    # Remove checksum
    data = data[:-4]

    # Remove magic byte and compressed flag
    if data[-1] == 0x01:
        data = data[1:-1]
    else:
        data = data[1:]

    return data


@dataclass
class AddressResult:
    """Result of address generation"""

    address: str
    public_key_hash: bytes
    private_key: bytes


def public_key_to_address(
    public_key: bytes,
    magic_byte: int = 25,  # BlackCoin P2PKH
) -> str:
    """
    Convert public key to address

    Args:
        public_key: Compressed public key (33 bytes)
        magic_byte: Network magic byte (25 for BlackCoin)
    """
    # Hash public key
    pub_hash = hash160(public_key)

    # Add magic byte
    data = bytes([magic_byte]) + pub_hash

    # Double SHA256 for checksum
    checksum = double_sha256(data)[:4]

    # Base58 encode
    result = base58_encode(data + checksum)
    return result


def public_key_hash_to_address(pub_hash: bytes, magic_byte: int = 25) -> str:
    """Convert public key hash to address"""
    data = bytes([magic_byte]) + pub_hash
    checksum = double_sha256(data)[:4]
    return base58_encode(data + checksum)


def script_to_address(script: bytes, magic_byte: int = 25) -> str:
    """Convert script to P2SH address"""
    pub_hash = hash160(script)
    data = bytes([magic_byte]) + pub_hash
    checksum = double_sha256(data)[:4]
    return base58_encode(data + checksum)


def address_to_public_key_hash(address: str) -> Optional[bytes]:
    """Extract public key hash from address"""
    try:
        decoded = base58_decode(address)
        if len(decoded) < 25:
            return None
        # Remove magic byte and checksum
        return decoded[1:-4]
    except Exception:
        return None


def txhash(tx: str) -> str:
    """Compute transaction hash"""
    tx_bytes = safe_unhexlify(tx)
    return bytes_to_hex(double_sha256(tx_bytes))


# Base58 encoding/decoding
BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> str:
    """Encode bytes to Base58"""
    # Handle leading zeros
    leading_zeros = len(data)
    data = data.lstrip(b"\x00")

    # Encode
    num = int.from_bytes(data, "big") if data else 0
    result = []
    while num > 0:
        num, remainder = divmod(num, 58)
        result.append(BASE58_ALPHABET[remainder])

    # Add leading zeros back
    result.extend([BASE58_ALPHABET[0]] * leading_zeros)

    return "".join(reversed(result))


def base58_decode(s: str) -> bytes:
    """Decode Base58 to bytes"""
    if not s:
        return b""

    # Handle leading zeros
    leading_zeros = len(s) - len(s.lstrip(BASE58_ALPHABET[0]))

    # Decode
    num = 0
    for char in s:
        if char not in BASE58_ALPHABET:
            raise ValueError(f"Invalid Base58 character: {char}")
        num = num * 58 + BASE58_ALPHABET.index(char)

    # Convert to bytes
    result = num.to_bytes((num.bit_length() + 7) // 8, "big") if num else b""

    # Add leading zeros back
    return b"\x00" * leading_zeros + result


def deserialize(data: Any) -> dict:
    """Deserialize transaction data (placeholder)"""
    if isinstance(data, str):
        data = safe_unhexlify(data)

    result: dict = {
        "version": 1,
        "locktime": 0,
        "vin": [],
        "vout": [],
    }

    # This is a simplified placeholder
    # Real implementation would parse Bitcoin transaction format
    return result


def serialize_transaction(
    version: int, inputs: list, outputs: list, locktime: int = 0
) -> str:
    """Serialize transaction to hex"""
    # Simplified placeholder
    result = struct.pack("<L", version)
    result += var_int_to_bytes(len(inputs))

    for inp in inputs:
        result += inp["txid"]
        result += struct.pack("<L", inp["vout"])
        result += inp["script"]
        result += struct.pack("<L", inp["sequence"])

    result += var_int_to_bytes(len(outputs))
    for out in outputs:
        result += struct.pack("<Q", int(out["value"] * 100000000))
        result += out["script"]

    result += struct.pack("<L", locktime)

    return result.hex()


def var_int_to_bytes(n: int) -> bytes:
    """Encode integer as bytes (variable length)"""
    if n < 0xFD:
        return bytes([n])
    elif n < 0xFFFF:
        return bytes([0xFD]) + struct.pack("<H", n)
    elif n < 0xFFFFFFFF:
        return bytes([0xFE]) + struct.pack("<L", n)
    else:
        return bytes([0xFF]) + struct.pack("<Q", n)


# Import base58 for address encoding
import base58  # noqa: F401


@dataclass
class MultiSigInfo:
    """Multisignature address information"""

    address: str
    redeem_script: bytes
    required_signers: int
    total_signers: int


def create_multisig_address(
    public_keys: list[bytes], required_signers: int
) -> MultiSigInfo:
    """
    Create multisignature address

    Args:
        public_keys: List of public keys
        required_signers: Number of signatures required

    Returns:
        MultisigInfo with address and redeem script
    """
    n = len(public_keys)

    if required_signers > n or required_signers < 1:
        raise ValueError("Invalid number of required signers")

    # Create redeem script: OP_M <pubkey1> ... <pubkeyN> OP_N OP_CHECKMULTISIG
    script = bytes([required_signers]) + b"".join(public_keys) + bytes([n, 0xAE])

    # Get address
    pub_hash = hash160(script)
    address = public_key_hash_to_address(pub_hash, magic_byte=0x05)  # P2SH

    return MultiSigInfo(
        address=address,
        redeem_script=script,
        required_signers=required_signers,
        total_signers=n,
    )
