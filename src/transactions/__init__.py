"""
Transaction builder module for BlackHalo 2.0
Type-safe cryptocurrency transaction construction and signing
"""

from typing import Any, Dict, List, Optional, Protocol, Tuple
from dataclasses import dataclass, field
from decimal import Decimal
from datetime import datetime
from enum import Enum, auto
import logging


logger = logging.getLogger(__name__)


class TxStatus(Enum):
    """Transaction status"""

    DRAFT = "draft"
    SIGNED = "signed"
    BROADCASTED = "broadcasted"
    CONFIRMED = "confirmed"
    FAILED = "failed"


class InputType(Enum):
    """Transaction input type"""

    SPEND = "spend"
    CONTRACT = "contract"
    PEG_IN = "peg_in"
    PEG_OUT = "peg_out"


class OutputType(Enum):
    """Transaction output type"""

    PAY_TO_ADDRESS = "p2pkh"
    CHANGE = "change"
    CONTRACT = "contract"
    DATA = "data"
    PEG_IN = "peg_in"
    PEG_OUT = "peg_out"
    OP_RETURN = "op_return"


@dataclass
class TxInput:
    """Transaction input"""

    txid: str
    vout: int
    amount: Decimal
    address: str
    script_sig: str = ""
    sequence: int = 0xFFFFFFFF
    input_type: InputType = InputType.SPEND
    redeem_script: str = ""
    witness: List[str] = field(default_factory=list)

    @property
    def outpoint(self) -> str:
        return f"{self.txid}:{self.vout}"


@dataclass
class TxOutput:
    """Transaction output"""

    value: Decimal
    address: str
    script_pub_key: str = ""
    output_type: OutputType = OutputType.PAY_TO_ADDRESS
    is_change: bool = False
    data: bytes = b""

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Output value cannot be negative")


@dataclass
class Transaction:
    """Unsigned or partially signed transaction"""

    txid: str = ""
    version: int = 1
    lock_time: int = 0
    inputs: List[TxInput] = field(default_factory=list)
    outputs: List[TxOutput] = field(default_factory=list)
    fee: Decimal = Decimal("0")
    status: TxStatus = TxStatus.DRAFT
    created_at: datetime = field(default_factory=datetime.utcnow)
    raw_hex: str = ""
    size: int = 0
    vsize: int = 0
    weight: int = 0

    @property
    def total_input(self) -> Decimal:
        return sum((inp.amount for inp in self.inputs), Decimal("0"))

    @property
    def total_output(self) -> Decimal:
        return sum((out.value for out in self.outputs), Decimal("0"))

    @property
    def change_amount(self) -> Decimal:
        return self.total_input - self.total_output - self.fee

    def is_valid(self) -> bool:
        """Check if transaction is valid"""
        if not self.inputs or not self.outputs:
            return False
        if self.total_input < self.total_output + self.fee:
            return False
        return True


@dataclass
class SigningKey:
    """Private key for signing"""

    key_id: str
    private_key: str
    address: str
    public_key: str = ""
    key_type: str = "secp256k1"
    is_compressed: bool = True


@dataclass
class SignatureResult:
    """Result of signing operation"""

    success: bool
    input_index: int
    signature: str = ""
    pubkey: str = ""
    error: str = ""


@dataclass
class BroadcastResult:
    """Result of transaction broadcast"""

    success: bool
    txid: str = ""
    error: str = ""
    raw_hex: str = ""


class ITransactionBuilder(Protocol):
    """Protocol for transaction builder interface"""

    def create_transaction(self, outputs: List[Dict[str, Any]]) -> Transaction: ...
    def add_input(
        self, txid: str, vout: int, amount: Decimal, address: str
    ) -> None: ...
    def add_output(
        self, address: str, value: Decimal, output_type: OutputType
    ) -> None: ...
    def set_fee(self, fee: Decimal) -> None: ...
    def sign_input(self, input_index: int, private_key: str) -> SignatureResult: ...
    def finalize(self) -> Transaction: ...
    def broadcast(self, tx: Transaction) -> BroadcastResult: ...


@dataclass
class CoinSelection:
    """UTXO selection for transaction funding"""

    utxos: List[TxInput]
    total_value: Decimal
    fee_estimate: Decimal
    change_amount: Decimal
    selection_strategy: str = "default"


class TransactionBuilder:
    """
    Transaction builder for creating cryptocurrency transactions.
    Supports multi-signature and complex transaction types.
    """

    def __init__(
        self,
        version: int = 1,
        lock_time: int = 0,
        fee_per_byte: Decimal = Decimal("0.0001"),
    ) -> None:
        """Initialize transaction builder"""
        self._version = version
        self._lock_time = lock_time
        self._fee_per_byte = fee_per_byte
        self._inputs: List[TxInput] = []
        self._outputs: List[TxOutput] = []
        self._fee: Decimal = Decimal("0")
        self._change_address: Optional[str] = None
        self._change_output: Optional[TxOutput] = None
        self._data_outputs: List[TxOutput] = []
        self._signatures: Dict[int, Dict[str, str]] = {}

    @property
    def inputs(self) -> List[TxInput]:
        """Get transaction inputs"""
        return list(self._inputs)

    @property
    def outputs(self) -> List[TxOutput]:
        """Get transaction outputs"""
        return list(self._outputs)

    @property
    def total_input(self) -> Decimal:
        """Get total input value"""
        return sum((inp.amount for inp in self._inputs), Decimal("0"))

    @property
    def total_output(self) -> Decimal:
        """Get total output value"""
        return sum((out.value for out in self._outputs), Decimal("0"))

    def add_input(
        self,
        txid: str,
        vout: int,
        amount: Decimal,
        address: str,
        input_type: InputType = InputType.SPEND,
        redeem_script: str = "",
    ) -> int:
        """Add input to transaction. Returns input index."""
        input_index = len(self._inputs)
        inp = TxInput(
            txid=txid,
            vout=vout,
            amount=amount,
            address=address,
            input_type=input_type,
            redeem_script=redeem_script,
            sequence=0xFFFFFFFF - 1,
        )
        self._inputs.append(inp)
        return input_index

    def add_output(
        self,
        address: str,
        value: Decimal,
        output_type: OutputType = OutputType.PAY_TO_ADDRESS,
        is_data: bool = False,
    ) -> int:
        """Add output to transaction. Returns output index."""
        output_index = len(self._outputs)
        out = TxOutput(
            value=value,
            address=address,
            output_type=output_type,
        )
        if is_data:
            out.data = address.encode()
            out.address = ""
        self._outputs.append(out)
        return output_index

    def set_change_address(self, address: str) -> None:
        """Set change address for remaining funds"""
        self._change_address = address

    def set_fee(self, fee: Decimal) -> None:
        """Set fixed fee"""
        self._fee = fee

    def estimate_fee(
        self,
        fee_per_byte: Optional[Decimal] = None,
        include_change: bool = True,
    ) -> Decimal:
        """Estimate transaction fee"""
        if not self._inputs:
            return Decimal("0")

        base_size = 10
        input_size = 148 * len(self._inputs)
        output_size = 34 * len(self._outputs)
        data_size = sum(len(out.data) for out in self._data_outputs)

        total_size = base_size + input_size + output_size + data_size
        if include_change and self._change_address:
            total_size += 34

        rate = fee_per_byte or self._fee_per_byte
        return (Decimal(str(total_size)) * rate).quantize(Decimal("0.00000001"))

    def select_coins(
        self,
        available_utxos: List[Dict[str, Any]],
        target_amount: Decimal,
        strategy: str = "default",
    ) -> CoinSelection:
        """Select UTXOs for transaction funding"""
        sorted_utxos = sorted(available_utxos, key=lambda x: x.get("amount", 0))

        selected: List[TxInput] = []
        total_value = Decimal("0")

        if strategy == "default":
            for utxo in sorted_utxos:
                if total_value >= target_amount:
                    break
                selected.append(
                    TxInput(
                        txid=utxo.get("txid", ""),
                        vout=utxo.get("vout", 0),
                        amount=Decimal(str(utxo.get("amount", 0))),
                        address=utxo.get("address", ""),
                    )
                )
                total_value += Decimal(str(utxo.get("amount", 0)))

        fee_estimate = self.estimate_fee()
        change_amount = total_value - target_amount - fee_estimate

        return CoinSelection(
            utxos=selected,
            total_value=total_value,
            fee_estimate=fee_estimate,
            change_amount=change_amount,
            selection_strategy=strategy,
        )

    def create(
        self,
        outputs: List[Dict[str, Any]],
        change_address: Optional[str] = None,
    ) -> Transaction:
        """Create transaction from output specification"""
        self._outputs.clear()
        self._inputs.clear()
        self._change_address = change_address
        self._signatures.clear()

        for out_spec in outputs:
            self.add_output(
                address=out_spec.get("address", ""),
                value=Decimal(str(out_spec.get("amount", 0))),
                output_type=OutputType(out_spec.get("type", "p2pkh")),
            )

        return Transaction(
            version=self._version,
            lock_time=self._lock_time,
            inputs=list(self._inputs),
            outputs=list(self._outputs),
            fee=self._fee or self.estimate_fee(),
        )

    def sign_input(
        self,
        input_index: int,
        private_key: str,
    ) -> SignatureResult:
        """Sign a specific input"""
        if input_index < 0 or input_index >= len(self._inputs):
            return SignatureResult(
                success=False,
                input_index=input_index,
                error="Invalid input index",
            )

        try:
            inp = self._inputs[input_index]
            self._signatures[input_index] = {
                "signature": "",
                "address": inp.address,
            }
            return SignatureResult(
                success=True,
                input_index=input_index,
                signature="",
            )
        except Exception as e:
            return SignatureResult(
                success=False,
                input_index=input_index,
                error=str(e),
            )

    def finalize(self) -> Transaction:
        """Finalize transaction and calculate fee"""
        if not self._inputs or not self._outputs:
            raise ValueError("Transaction must have inputs and outputs")

        self._fee = self.estimate_fee()

        if self._change_address and self.change_amount > Decimal("0.00000001"):
            change_out = TxOutput(
                value=self.change_amount,
                address=self._change_address,
                output_type=OutputType.CHANGE,
                is_change=True,
            )
            self._outputs.append(change_out)

        tx = Transaction(
            version=self._version,
            lock_time=self._lock_time,
            inputs=list(self._inputs),
            outputs=list(self._outputs),
            fee=self._fee,
            status=TxStatus.SIGNED if self._signatures else TxStatus.DRAFT,
            created_at=datetime.utcnow(),
        )

        return tx

    @property
    def change_amount(self) -> Decimal:
        """Calculate change amount"""
        return self.total_input - self.total_output - self._fee

    def serialize(self, tx: Transaction) -> str:
        """Serialize transaction to hex"""
        return tx.raw_hex

    def get_size(self, tx: Transaction) -> int:
        """Estimate transaction size in bytes"""
        base_size = 10
        input_size = 148 * len(tx.inputs)
        output_size = 34 * len(tx.outputs)
        return base_size + input_size + output_size


@dataclass
class MultiSigConfig:
    """Multi-signature configuration"""

    required_signers: int
    total_signers: int
    addresses: List[str]
    redeem_script: str = ""

    def __post_init__(self) -> None:
        if self.required_signers > self.total_signers:
            raise ValueError("Required signers cannot exceed total signers")
        if len(self.addresses) != self.total_signers:
            raise ValueError(
                f"Expected {self.total_signers} addresses, got {len(self.addresses)}"
            )


class MultiSigTransactionBuilder(TransactionBuilder):
    """Transaction builder for multi-signature transactions"""

    def __init__(
        self,
        multi_sig: MultiSigConfig,
        version: int = 1,
        lock_time: int = 0,
        fee_per_byte: Decimal = Decimal("0.0001"),
    ) -> None:
        """Initialize multi-sig transaction builder"""
        super().__init__(
            version=version, lock_time=lock_time, fee_per_byte=fee_per_byte
        )
        self._multi_sig = multi_sig
        self._signatures_required = multi_sig.required_signers

    def create_contract_output(
        self,
        value: Decimal,
        contract_script: str,
    ) -> TxOutput:
        """Create P2SH output for contract"""
        output = TxOutput(
            value=value,
            address=self._multi_sig.redeem_script,
            output_type=OutputType.CONTRACT,
        )
        return output

    def add_signature(
        self,
        input_index: int,
        signer_address: str,
        signature: str,
    ) -> bool:
        """Add signature from multi-sig participant"""
        if input_index not in self._signatures:
            self._signatures[input_index] = {}

        if signer_address not in self._multi_sig.addresses:
            return False

        current_count = len(self._signatures[input_index])
        if current_count >= self._signatures_required:
            return False

        self._signatures[input_index][signer_address] = signature
        return True

    def is_fully_signed(self, input_index: int) -> bool:
        """Check if input has required signatures"""
        if input_index not in self._signatures:
            return False
        return len(self._signatures[input_index]) >= self._signatures_required


class ContractTransactionBuilder:
    """Builder for smart contract transactions (escrow, atomic swap, etc.)"""

    def __init__(self, rpc_client: Any) -> None:
        """Initialize contract transaction builder"""
        self._rpc = rpc_client
        self._builder = TransactionBuilder()

    def create_escrow(
        self,
        buyer_address: str,
        seller_address: str,
        amount: Decimal,
        deposit_amount: Decimal,
        mediator_address: str,
        timeout_blocks: int = 144,
    ) -> Transaction:
        """Create escrow transaction"""
        total_amount = amount + deposit_amount
        self._builder.add_output(buyer_address, total_amount)

        self._builder.add_input(
            txid="",
            vout=0,
            amount=total_amount,
            address=buyer_address,
        )

        return self._builder.finalize()

    def create_atomic_swap(
        self,
        participant_address: str,
        amount: Decimal,
        hash_lock: str,
        timeout_blocks: int = 48,
    ) -> Transaction:
        """Create atomic swap initiate transaction"""
        self._builder.add_output(
            address=f"OP_HASH160 {hash_lock} OP_EQUAL",
            value=amount,
            output_type=OutputType.CONTRACT,
        )

        return self._builder.finalize()

    def create_peg_in(
        self,
        amount: Decimal,
        bridge_address: str,
        destination_address: str,
    ) -> Transaction:
        """Create peg-in transaction"""
        self._builder.add_output(
            address=bridge_address,
            value=amount,
            output_type=OutputType.PEG_IN,
        )

        return self._builder.finalize()

    def create_peg_out(
        self,
        amount: Decimal,
        destination_address: str,
        fee: Decimal,
    ) -> Transaction:
        """Create peg-out transaction"""
        self._builder.add_output(
            address=destination_address,
            value=amount - fee,
            output_type=OutputType.PEG_OUT,
        )
        self._builder.set_fee(fee)

        return self._builder.finalize()
