"""
State management for BlackHalo 2.0
Type-safe global state with proper encapsulation
"""

from typing import Any, Dict, List, Optional, Protocol, runtime_checkable
from decimal import Decimal
from datetime import datetime
from dataclasses import dataclass, field
import threading
import json

from ..types import (
    CryptoType,
    Contract,
    Order,
    Market,
    UTXO,
    BMAddress,
    BMMessage,
    BridgeState,
    AppConfig,
    LogLevel,
    LogEntry,
    ThreadState,
    BalanceInfo,
    ContractStatus,
    MessageStatus,
)


class IStateManager(Protocol):
    """Protocol for state management interface"""

    @property
    def advance_array(self) -> Dict[str, Any]: ...
    @property
    def markets(self) -> Dict[str, Any]: ...
    @property
    def contracts(self) -> List[Contract]: ...
    @property
    def messages(self) -> List[BMMessage]: ...
    @property
    def spendable(self) -> List[UTXO]: ...
    @property
    def bitmessage_addresses(self) -> List[BMAddress]: ...
    @property
    def is_locked(self) -> bool: ...

    def lock(self) -> None: ...
    def unlock(self) -> None: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def set(self, key: str, value: Any) -> None: ...
    def save_state(self, path: str) -> None: ...
    def load_state(self, path: str) -> None: ...


@dataclass
class StateManager:
    """
    Thread-safe state management for BlackHalo.
    Replaces the dynamic AdvanceArray pattern with typed accessors.
    """

    # Core state dictionaries
    _advance_array: Dict[str, Any] = field(default_factory=dict)
    _markets: Dict[str, Any] = field(default_factory=dict)
    _contracts: List[Contract] = field(default_factory=list)
    _messages: List[BMMessage] = field(default_factory=list)
    _spendable: List[UTXO] = field(default_factory=list)
    _bitmessage_addresses: List[BMAddress] = field(default_factory=list)
    _outbox: List[Dict[str, Any]] = field(default_factory=list)

    # Thread synchronization
    _lock: threading.RLock = field(default_factory=threading.RLock)
    _is_locked: bool = False

    # Metadata
    _last_saved: datetime | None = None
    _dirty: bool = False

    def __post_init__(self) -> None:
        """Initialize default state"""
        self._ensure_defaults()

    def _ensure_defaults(self) -> None:
        """Ensure default values exist"""
        with self._lock:
            if "MySettings" not in self._advance_array:
                self._advance_array["MySettings"] = {
                    "Proxy": "",
                    "AntiLogger": False,
                    "ManualLogin": False,
                    "ClearLocation": False,
                    "CreateDebug": False,
                    "Staking": False,
                    "ColdStake": "",
                    "PeggingVote": 0,
                    "Voting": [],
                    "EnableBridge": False,
                }

            if "bridgedb" not in self._advance_array:
                self._advance_array["bridgedb"] = {
                    "TrustedStakers1": [],
                    "TrustedStakers2": [],
                    "PendingStakes": [],
                }

            if "InboxCleanTime" not in self._advance_array:
                self._advance_array["InboxCleanTime"] = datetime.utcnow()

            if "clearnotxid" not in self._advance_array:
                self._advance_array["clearnotxid"] = 1

    # =========================================================================
    # Thread Safety
    # =========================================================================

    @property
    def is_locked(self) -> bool:
        """Check if state is locked for modification"""
        return self._is_locked

    def lock(self) -> None:
        """Acquire lock for batch operations"""
        self._lock.acquire()
        self._is_locked = True

    def unlock(self) -> None:
        """Release lock"""
        self._is_locked = False
        self._lock.release()

    def __enter__(self) -> "StateManager":
        """Context manager entry"""
        self.lock()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit"""
        self.unlock()

    # =========================================================================
    # Dictionary Access Pattern (compatible with AdvanceArray)
    # =========================================================================

    def get(self, key: str, default: Any = None) -> Any:
        """Get value from advance array (compatible with legacy code)"""
        with self._lock:
            return self._advance_array.get(key, default)

    def __getitem__(self, key: str) -> Any:
        """Dict-style access"""
        with self._lock:
            return self._advance_array[key]

    def __setitem__(self, key: str, value: Any) -> None:
        """Dict-style assignment"""
        with self._lock:
            self._advance_array[key] = value
            self._dirty = True

    def __contains__(self, key: str) -> bool:
        """Check if key exists"""
        with self._lock:
            return key in self._advance_array

    def get_nested(self, *keys: str, default: Any = None) -> Any:
        """Get nested value, e.g., get_nested('MySettings', 'Staking')"""
        with self._lock:
            current = self._advance_array
            for key in keys:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                else:
                    return default
            return current

    def set_nested(self, *keys: str, value: Any) -> None:
        """Set nested value, creating intermediate dicts"""
        with self._lock:
            current = self._advance_array
            for key in keys[:-1]:
                if key not in current:
                    current[key] = {}
                current = current[key]
            current[keys[-1]] = value
            self._dirty = True

    # =========================================================================
    # Contracts
    # =========================================================================

    @property
    def contracts(self) -> List[Contract]:
        """Get all contracts"""
        with self._lock:
            return list(self._contracts)

    def add_contract(self, contract: Contract) -> None:
        """Add a new contract"""
        with self._lock:
            self._contracts.append(contract)
            self._dirty = True

    def get_contract(self, contract_id: str) -> Contract | None:
        """Get contract by ID"""
        with self._lock:
            for c in self._contracts:
                if c.contract_id == contract_id:
                    return c
            return None

    def update_contract_status(self, contract_id: str, status: ContractStatus) -> bool:
        """Update contract status"""
        with self._lock:
            for contract in self._contracts:
                if contract.contract_id == contract_id:
                    contract.status = status
                    contract.updated_at = datetime.utcnow()
                    self._dirty = True
                    return True
            return False

    def get_active_contracts(self) -> List[Contract]:
        """Get all active contracts"""
        with self._lock:
            return [
                c
                for c in self._contracts
                if c.status in (ContractStatus.PENDING, ContractStatus.ACTIVE)
            ]

    # =========================================================================
    # Messages (BitMessage)
    # =========================================================================

    @property
    def messages(self) -> List[BMMessage]:
        """Get all messages"""
        with self._lock:
            return list(self._messages)

    def add_message(self, message: BMMessage) -> None:
        """Add a new message"""
        with self._lock:
            self._messages.append(message)
            self._dirty = True

    def get_unread_messages(self) -> List[BMMessage]:
        """Get unread messages"""
        with self._lock:
            return [m for m in self._messages if not m.read]

    def archive_message(self, msg_id: str) -> bool:
        """Archive a message"""
        with self._lock:
            for msg in self._messages:
                if msg.msg_id == msg_id:
                    msg.archived = True
                    self._dirty = True
                    return True
            return False

    @property
    def outbox(self) -> List[Dict[str, Any]]:
        """Get outbox entries"""
        with self._lock:
            return list(self._outbox)

    def add_outbox_entry(self, entry: Dict[str, Any]) -> None:
        """Add entry to outbox"""
        with self._lock:
            self._outbox.append(entry)
            self._dirty = True

    def update_outbox_status(self, msg_id: str, status: MessageStatus) -> bool:
        """Update outbox entry status"""
        with self._lock:
            for entry in self._outbox:
                if entry.get("msg_id") == msg_id:
                    entry["status"] = status
                    if status == MessageStatus.SENT:
                        entry["sent_at"] = datetime.utcnow()
                    self._dirty = True
                    return True
            return False

    # =========================================================================
    # BitMessage Addresses
    # =========================================================================

    @property
    def bitmessage_addresses(self) -> List[BMAddress]:
        """Get all BitMessage addresses"""
        with self._lock:
            return list(self._bitmessage_addresses)

    def add_bitmessage_address(self, address: BMAddress) -> None:
        """Add BitMessage address"""
        with self._lock:
            self._bitmessage_addresses.append(address)
            self._dirty = True

    def get_bitmessage_address(self, address: str) -> BMAddress | None:
        """Get BitMessage address by address string"""
        with self._lock:
            for addr in self._bitmessage_addresses:
                if addr.address == address:
                    return addr
            return None

    # =========================================================================
    # UTXO Management
    # =========================================================================

    @property
    def spendable(self) -> List[UTXO]:
        """Get spendable UTXOs"""
        with self._lock:
            return [u for u in self._spendable if u.spendable]

    def add_utxo(self, utxo: UTXO) -> None:
        """Add UTXO"""
        with self._lock:
            self._spendable.append(utxo)
            self._dirty = True

    def mark_utxo_spent(self, txid: str, vout: int) -> bool:
        """Mark UTXO as spent"""
        with self._lock:
            for utxo in self._spendable:
                if utxo.txid == txid and utxo.vout == vout:
                    utxo.spendable = False
                    self._dirty = True
                    return True
            return False

    def get_total_spendable(self) -> Decimal:
        """Get total spendable amount"""
        with self._lock:
            total = sum(
                (u.amount for u in self._spendable if u.spendable), Decimal("0")
            )
            return Decimal(str(total))

    # =========================================================================
    # Markets
    # =========================================================================

    @property
    def markets(self) -> Dict[str, Any]:
        """Get markets data (compatible with legacy Markets dict)"""
        with self._lock:
            return dict(self._markets)

    def update_market_list(self, market_data: Dict[str, Any]) -> None:
        """Update market list from network"""
        with self._lock:
            self._markets.update(market_data)
            self._dirty = True

    def add_order(self, order: Order) -> None:
        """Add order to market"""
        with self._lock:
            if "Orders" not in self._markets:
                self._markets["Orders"] = []
            self._markets["Orders"].append(order.__dict__)
            self._dirty = True

    def get_orders(self, market: str | None = None) -> List[Order]:
        """Get orders, optionally filtered by market"""
        with self._lock:
            orders = self._markets.get("Orders", [])
            if market:
                return [Order(**o) for o in orders if o.get("market") == market]
            return [Order(**o) for o in orders]

    # =========================================================================
    # Settings
    # =========================================================================

    @property
    def my_settings(self) -> Dict[str, Any]:
        """Get MySettings (compatible with legacy)"""
        with self._lock:
            return dict(self._advance_array.get("MySettings", {}))

    def update_settings(self, settings: Dict[str, Any]) -> None:
        """Update settings"""
        with self._lock:
            self._advance_array["MySettings"].update(settings)
            self._dirty = True

    # =========================================================================
    # Persistence
    # =========================================================================

    def save_state(self, path: str) -> None:
        """Save state to file"""
        with self._lock:
            state = {
                "advance_array": self._advance_array,
                "contracts": [c.__dict__ for c in self._contracts],
                "messages": [m.__dict__ for m in self._messages],
                "spendable": [u.__dict__ for u in self._spendable],
                "bitmessage_addresses": [
                    a.__dict__ for a in self._bitmessage_addresses
                ],
                "outbox": self._outbox,
                "markets": self._markets,
                "saved_at": datetime.utcnow().isoformat(),
            }
            with open(path, "w") as f:
                json.dump(state, f, indent=2, default=str)
            self._last_saved = datetime.utcnow()
            self._dirty = False

    def load_state(self, path: str) -> bool:
        """Load state from file"""
        try:
            with open(path, "r") as f:
                state = json.load(f)

            with self._lock:
                self._advance_array = state.get("advance_array", {})
                self._contracts = [Contract(**c) for c in state.get("contracts", [])]
                self._messages = [BMMessage(**m) for m in state.get("messages", [])]
                self._spendable = [UTXO(**u) for u in state.get("spendable", [])]
                self._bitmessage_addresses = [
                    BMAddress(**a) for a in state.get("bitmessage_addresses", [])
                ]
                self._outbox = state.get("outbox", [])
                self._markets = state.get("markets", {})

            self._ensure_defaults()
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            return False

    # =========================================================================
    # Logging
    # =========================================================================

    def log(
        self, level: LogLevel, message: str, module: str = "", **extra: Any
    ) -> None:
        """Log an entry"""
        entry = LogEntry(
            level=level,
            message=message,
            module=module,
            extra=extra,
        )
        with self._lock:
            if "logs" not in self._advance_array:
                self._advance_array["logs"] = []
            self._advance_array["logs"].append(entry.to_dict())
            # Keep only last 1000 entries
            if len(self._advance_array["logs"]) > 1000:
                self._advance_array["logs"] = self._advance_array["logs"][-1000:]

    def get_logs(
        self, level: LogLevel | None = None, limit: int = 100
    ) -> List[LogEntry]:
        """Get log entries"""
        with self._lock:
            logs = self._advance_array.get("logs", [])
            if level:
                logs = [l for l in logs if l["level"] == level.value]
            return [LogEntry(**l) for l in logs[-limit:]]


# Global state instance
_state_manager: StateManager | None = None
_state_lock = threading.Lock()


def get_state_manager() -> StateManager:
    """Get the global state manager instance"""
    global _state_manager
    if _state_manager is None:
        with _state_lock:
            if _state_manager is None:
                _state_manager = StateManager()
    return _state_manager


def reset_state_manager() -> None:
    """Reset the global state manager (for testing)"""
    global _state_manager
    with _state_lock:
        _state_manager = StateManager()
