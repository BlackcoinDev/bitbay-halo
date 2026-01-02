"""
Type definitions for BlackHalo 2.0
Comprehensive type annotations for type-safe cryptocurrency exchange platform
"""

from typing import TypeAlias, TypedDict, Literal, NotRequired
from decimal import Decimal
from datetime import datetime
from enum import Enum, auto
from dataclasses import dataclass, field
import json


class CryptoType(Enum):
    """Supported cryptocurrency types"""

    BLACKCOIN = "BLK"
    BITBAY = "BAY"
    BITCOIN = "BTC"


class OrderType(Enum):
    """Order types for exchange"""

    BUY = "buy"
    SELL = "sell"
    ESCROW = "escrow"


class ContractStatus(Enum):
    """Contract lifecycle status"""

    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    DISPUTED = "disputed"


class MessageStatus(Enum):
    """Message transmission status"""

    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    FAILED = "failed"


# ============================================================================
# Address and Transaction Types
# ============================================================================

Address: TypeAlias = str
TxHash: TypeAlias = str
PrivateKey: TypeAlias = str
PublicKey: TypeAlias = str
HexString: TypeAlias = str
Base64String: TypeAlias = str


@dataclass
class CryptoAddress:
    """Cryptocurrency address with metadata"""

    address: Address
    crypto_type: CryptoType
    label: str = ""
    is_multisig: bool = False
    required_signers: int = 1
    total_signers: int = 1
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_used: datetime | None = None

    def __str__(self) -> str:
        return self.address


@dataclass
class UTXO:
    """Unspent transaction output"""

    txid: TxHash
    vout: int
    amount: Decimal
    address: Address
    confirmations: int = 0
    spendable: bool = True
    script_pub_key: HexString = ""

    @property
    def outpoint(self) -> str:
        return f"{self.txid}:{self.vout}"


@dataclass
class Transaction:
    """Cryptocurrency transaction"""

    txid: TxHash
    hex: HexString
    fee: Decimal = Decimal("0")
    confirmations: int = 0
    timestamp: datetime = field(default_factory=datetime.utcnow)
    inputs: list["TxInput"] = field(default_factory=list)
    outputs: list["TxOutput"] = field(default_factory=list)

    def is_confirmed(self, confirmations_required: int = 6) -> bool:
        return self.confirmations >= confirmations_required


@dataclass
class TxInput:
    """Transaction input"""

    txid: TxHash
    vout: int
    script_sig: HexString = ""
    amount: Decimal = Decimal("0")
    address: Address = ""


@dataclass
class TxOutput:
    """Transaction output"""

    value: Decimal
    address: Address
    script_pub_key: HexString = ""
    spent: bool = False


# ============================================================================
# Exchange and Market Types
# ============================================================================


@dataclass
class Market:
    """Trading market configuration"""

    name: str
    base_currency: CryptoType
    quote_currency: CryptoType
    fee_percentage: Decimal = Decimal("0.01")
    min_trade_amount: Decimal = Decimal("0.0001")
    max_trade_amount: Decimal = Decimal("10000")
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def pair(self) -> str:
        return f"{self.base_currency.value}/{self.quote_currency.value}"


@dataclass
class OrderBookEntry:
    """Order book listing"""

    order_id: str
    order_type: OrderType
    price: Decimal
    amount: Decimal
    total: Decimal
    maker_address: Address
    timestamp: datetime = field(default_factory=datetime.utcnow)
    is_mine: bool = False


@dataclass
class Order:
    """Exchange order"""

    order_id: str
    order_type: OrderType
    market: str
    price: Decimal
    amount: Decimal
    filled_amount: Decimal = Decimal("0")
    status: str = "open"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def total(self) -> Decimal:
        return self.price * self.amount

    @property
    def remaining(self) -> Decimal:
        return self.amount - self.filled_amount

    @property
    def is_filled(self) -> bool:
        return self.filled_amount >= self.amount


# ============================================================================
# Contract and Escrow Types
# ============================================================================


@dataclass
class ContractParty:
    """Party in a contract"""

    address: Address
    btc_address: Address | None = None
    public_key: PublicKey | None = None
    is_seller: bool = False
    has_signed: bool = False


@dataclass
class ContractTerms:
    """Contract terms and conditions"""

    price: Decimal
    currency: CryptoType
    deposit_percentage: Decimal = Decimal("0.01")
    arbitration_fee: Decimal = Decimal("0.005")
    release_conditions: str = ""
    dispute_resolution: str = ""
    expires_at: datetime | None = None


@dataclass
class Contract:
    """Smart contract for exchange"""

    contract_id: str
    order_id: str | None
    status: ContractStatus
    terms: ContractTerms
    parties: dict[str, ContractParty]
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: datetime | None = None
    metadata: dict = field(default_factory=dict)

    @property
    def seller(self) -> ContractParty | None:
        return self.parties.get("seller")

    @property
    def buyer(self) -> ContractParty | None:
        return self.parties.get("buyer")

    def add_party(self, role: str, party: ContractParty) -> None:
        self.parties[role] = party
        self.updated_at = datetime.utcnow()


@dataclass
class EscrowTransaction:
    """Escrow transaction state"""

    txid: TxHash
    amount: Decimal
    address: Address
    status: str = "pending"
    release_conditions: dict = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)
    released_at: datetime | None = None


# ============================================================================
# Message Types (BitMessage)
# =========================================================================()


@dataclass
class BMAddress:
    """BitMessage address"""

    address: str
    label: str = ""
    stream: int = 1
    is_deterministic: bool = False
    is_chan: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)

    def is_valid(self) -> bool:
        return self.address.startswith("BM-")


@dataclass
class BMMessage:
    """BitMessage message"""

    msg_id: str
    to_address: str
    from_address: str
    subject: str
    body: str
    received_at: datetime = field(default_factory=datetime.utcnow)
    read: bool = False
    archived: bool = False
    ack_data: str = ""


@dataclass
class BMOutboxEntry:
    """Outbox entry for tracking sent messages"""

    msg_id: str
    to_address: str
    subject: str
    body: str
    status: MessageStatus
    ack_data: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    sent_at: datetime | None = None


# ============================================================================
# Peg and Bridge Types
# ============================================================================


@dataclass
class PegRate:
    """Exchange rate for pegged currency"""

    rate: Decimal
    base_currency: CryptoType
    quote_currency: CryptoType
    timestamp: datetime = field(default_factory=datetime.utcnow)
    block_height: int = 0

    def to_json(self) -> str:
        return json.dumps(
            {
                "rate": str(self.rate),
                "base": self.base_currency.value,
                "quote": self.quote_currency.value,
                "timestamp": self.timestamp.isoformat(),
            }
        )


@dataclass
class BridgeState:
    """Bridge state for cross-chain operations"""

    current_rate: PegRate | None
    pending_transactions: list[str] = field(default_factory=list)
    frozen_outputs: list[str] = field(default_factory=list)
    last_update: datetime = field(default_factory=datetime.utcnow)


# ============================================================================
# Configuration Types
# ============================================================================


@dataclass
class AppConfig:
    """Application configuration"""

    coin_select: CryptoType = CryptoType.BLACKCOIN
    data_directory: str = "./data"
    keys_directory: str = "./keys"
    network: Literal["mainnet", "testnet"] = "mainnet"
    rpc_host: str = "127.0.0.1"
    rpc_port: int = 15715
    rpc_user: str = ""
    rpc_password: str = ""
    bitmessage_enabled: bool = True
    bitmessage_port: int = 8878
    gui_style: str = "modern"
    language: str = "en"
    log_level: str = "INFO"

    def validate(self) -> list[str]:
        """Validate configuration, return list of errors"""
        errors = []
        if not self.rpc_user:
            errors.append("RPC user is required")
        if not self.rpc_password:
            errors.append("RPC password is required")
        if self.rpc_port < 1 or self.rpc_port > 65535:
            errors.append("RPC port must be between 1 and 65535")
        return errors


@dataclass
class MarketSettings:
    """Market-specific settings"""

    default_market: str = "BLK/BTC"
    enable_market: bool = True
    spam_filter: bool = True
    max_orders_display: int = 100
    refresh_interval: int = 30


# ============================================================================
# API Response Types
# ============================================================================


@dataclass
class APIResponse:
    """Generic API response"""

    success: bool
    data: dict | None = None
    error: str | None = None
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "data": self.data,
            "error": self.error,
            "timestamp": self.timestamp.isoformat(),
        }


@dataclass
class BalanceInfo:
    """Wallet balance information"""

    confirmed: Decimal
    unconfirmed: Decimal
    spendable: Decimal
    frozen: Decimal

    @property
    def total(self) -> Decimal:
        return self.confirmed + self.unconfirmed


@dataclass
class BlockInfo:
    """Blockchain block information"""

    height: int
    hash: TxHash
    timestamp: datetime
    tx_count: int
    difficulty: Decimal
    size: int

    @property
    def age(self) -> float:
        return (datetime.utcnow() - self.timestamp).total_seconds()


# ============================================================================
# Event and Logging Types
# ============================================================================


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class LogEntry:
    """Log entry"""

    level: LogLevel
    message: str
    module: str = ""
    timestamp: datetime = field(default_factory=datetime.utcnow)
    extra: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "level": self.level.value,
            "message": self.message,
            "module": self.module,
            "timestamp": self.timestamp.isoformat(),
            **self.extra,
        }


# ============================================================================
# Thread and Process Types
# ============================================================================


@dataclass
class ThreadState:
    """Thread state tracking"""

    name: str
    is_running: bool = False
    is_stopping: bool = False
    last_error: str | None = None
    start_time: datetime | None = None
    stop_time: datetime | None = None
    iterations: int = 0

    def start(self) -> None:
        self.is_running = True
        self.is_stopping = False
        self.start_time = datetime.utcnow()
        self.last_error = None

    def stop(self) -> None:
        self.is_running = False
        self.is_stopping = True
        self.stop_time = datetime.utcnow()

    def record_iteration(self) -> None:
        self.iterations += 1


@dataclass
class DaemonStatus:
    """Daemon process status"""

    is_running: bool
    pid: int | None
    uptime_seconds: float
    memory_usage_mb: float
    last_heartbeat: datetime

    @property
    def is_responsive(self) -> bool:
        return (datetime.utcnow() - self.last_heartbeat).total_seconds() < 60
