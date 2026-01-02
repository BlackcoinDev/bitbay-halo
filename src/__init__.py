"""
BlackHalo 2.0 - Main Application
Type-safe cryptocurrency exchange platform
"""

import sys
import logging
from typing import Any, Dict, Optional, Union
from decimal import Decimal
from datetime import datetime
from pathlib import Path

from .types import (
    CryptoType,
    AppConfig,
    BalanceInfo,
    BlockInfo,
    ContractStatus,
    OrderType,
    UTXO,
)
from .state import StateManager, get_state_manager
from .rpc import RPCClient, BlackCoinClient, create_rpc_client
from .crypto import (
    safe_hexlify,
    safe_unhexlify,
    txhash,
    public_key_to_address,
    private_key_to_wif,
    generate_private_key,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class BlackHaloApplication:
    """
    Main application class for BlackHalo 2.0.
    Replaces the legacy Halo.py with typed, modular architecture.
    """

    def __init__(self, config: Optional[AppConfig] = None) -> None:
        """Initialize application"""
        self.config = config or AppConfig()
        self.state = get_state_manager()
        self.rpc_client: Optional[Union[BlackCoinClient, RPCClient]] = None
        self._running = False

        # Validate configuration
        errors = self.config.validate()
        if errors:
            for error in errors:
                logger.error(f"Configuration error: {error}")
            raise ValueError(f"Invalid configuration: {errors}")

    def initialize(self) -> None:
        """Initialize RPC connections and load state"""
        logger.info("Initializing BlackHalo 2.0...")

        # Create RPC client
        self.rpc_client = create_rpc_client(
            crypto_type=self.config.coin_select.value,
            host=self.config.rpc_host,
            port=self.config.rpc_port,
            username=self.config.rpc_user,
            password=self.config.rpc_password,
        )

        # Load state from disk
        state_path = Path(self.config.data_directory) / "state.json"
        if state_path.exists():
            self.state.load_state(str(state_path))
            logger.info("Loaded state from disk")

        logger.info("Initialization complete")

    def start(self) -> None:
        """Start the application"""
        if self._running:
            logger.warning("Application already running")
            return

        self._running = True
        logger.info("Starting BlackHalo application...")

        try:
            self._main_loop()
        except KeyboardInterrupt:
            logger.info("Received shutdown signal")
        finally:
            self.shutdown()

    def _main_loop(self) -> None:
        """Main application loop"""
        while self._running:
            # Main loop logic would go here
            # In a real implementation, this would handle:
            # - RPC polling
            # - Message scanning
            # - Contract state updates
            # - GUI events
            break  # For now, just exit

    def shutdown(self) -> None:
        """Shutdown the application"""
        logger.info("Shutting down BlackHalo...")
        self._running = False

        # Save state
        state_path = Path(self.config.data_directory) / "state.json"
        state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state.save_state(str(state_path))
        logger.info("State saved to disk")

        logger.info("BlackHalo shutdown complete")

    # =========================================================================
    # Blockchain Operations
    # =========================================================================

    def get_block_info(self) -> Optional[BlockInfo]:
        """Get current block information"""
        if self.rpc_client is None:
            return None

        try:
            height = self.rpc_client.getblockcount()
            block_hash = self.rpc_client.getbestblockhash()
            block = self.rpc_client.getblock(block_hash)

            return BlockInfo(
                height=height,
                hash=block_hash,
                timestamp=block.get("time", 0),
                tx_count=len(block.get("tx", [])),
                difficulty=Decimal(str(block.get("difficulty", 0))),
                size=block.get("size", 0),
            )
        except Exception as e:
            logger.error(f"Error getting block info: {e}")
            return None

    def get_balance(self) -> BalanceInfo:
        """Get wallet balance"""
        if self.rpc_client is None:
            return BalanceInfo(
                confirmed=Decimal("0"),
                unconfirmed=Decimal("0"),
                spendable=Decimal("0"),
                frozen=Decimal("0"),
            )

        try:
            confirmed = self.rpc_client.getbalance(1)  # Confirmed
            unconfirmed = self.rpc_client.getbalance(0) - confirmed  # Unconfirmed

            spendable = self.state.get_total_spendable()

            return BalanceInfo(
                confirmed=confirmed,
                unconfirmed=unconfirmed,
                spendable=spendable,
                frozen=Decimal("0"),
            )
        except Exception as e:
            logger.error(f"Error getting balance: {e}")
            return BalanceInfo(
                confirmed=Decimal("0"),
                unconfirmed=Decimal("0"),
                spendable=Decimal("0"),
                frozen=Decimal("0"),
            )

    def get_utxos(self) -> list[dict[str, Any]]:
        """Get list of spendable UTXOs"""
        if self.rpc_client is None:
            return []

        try:
            utxos = self.rpc_client.listunspent(0)

            for utxo_data in utxos:
                utxo = UTXO(
                    txid=utxo_data.get("txid", ""),
                    vout=utxo_data.get("vout", 0),
                    amount=Decimal(str(utxo_data.get("amount", 0))),
                    address=utxo_data.get("address", ""),
                    confirmations=utxo_data.get("confirmations", 0),
                )
                self.state.add_utxo(utxo)

            return utxos
        except Exception as e:
            logger.error(f"Error getting UTXOs: {e}")
            return []

    # =========================================================================
    # Contract Operations
    # =========================================================================

    def create_contract(
        self, order_id: str, terms: Dict[str, Any], parties: Dict[str, Dict[str, Any]]
    ) -> str:
        """Create a new contract"""
        from .types import Contract, ContractTerms, ContractParty, CryptoType

        # Generate contract ID
        contract_id = safe_hexlify(
            self.state.get("U", "") + str(len(self.state.contracts))
        )

        contract = Contract(
            contract_id=contract_id,
            order_id=order_id,
            status=ContractStatus.PENDING,
            terms=ContractTerms(
                price=Decimal(str(terms.get("price", 0))),
                currency=CryptoType.BLACKCOIN,
                deposit_percentage=Decimal(str(terms.get("deposit", 0.01))),
            ),
            parties={
                role: ContractParty(
                    address=data.get("address", ""),
                    is_seller=(role == "seller"),
                )
                for role, data in parties.items()
            },
        )

        self.state.add_contract(contract)
        logger.info(f"Created contract {contract_id}")

        return contract_id

    def get_contracts(self, status: Optional[ContractStatus] = None) -> list:
        """Get contracts, optionally filtered by status"""
        if status is None:
            return self.state.contracts
        return [c for c in self.state.contracts if c.status == status]

    # =========================================================================
    # Address Operations
    # =========================================================================

    def generate_address(
        self, label: str = "", is_multisig: bool = False
    ) -> Dict[str, Any]:
        """Generate a new receiving address"""
        if self.rpc_client is None:
            return {}

        try:
            address = self.rpc_client.getnewaddress(label)

            return {
                "address": address,
                "label": label,
                "is_multisig": is_multisig,
                "created_at": str(datetime.utcnow()),
            }
        except Exception as e:
            logger.error(f"Error generating address: {e}")
            return {}

    def import_private_key(
        self, private_key: str, label: str = "", rescan: bool = True
    ) -> bool:
        """Import a private key"""
        if self.rpc_client is None:
            return False

        try:
            self.rpc_client.importprivkey(private_key, label, rescan)
            logger.info(f"Imported private key with label: {label}")
            return True
        except Exception as e:
            logger.error(f"Error importing private key: {e}")
            return False

    # =========================================================================
    # Message Operations
    # =========================================================================

    def get_messages(self) -> list:
        """Get all messages"""
        return self.state.messages

    def get_unread_messages(self) -> list:
        """Get unread messages"""
        return self.state.get_unread_messages()


def main() -> int:
    """Main entry point"""
    try:
        app = BlackHaloApplication()
        app.initialize()
        app.start()
        return 0
    except Exception as e:
        logger.exception(f"Fatal error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
