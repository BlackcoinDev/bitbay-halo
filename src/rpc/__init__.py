"""
RPC client for BlackCoin and other cryptocurrencies
Type-safe RPC communication
"""

from typing import Any, Dict, List, Optional, Protocol, Union
from decimal import Decimal
from dataclasses import dataclass, field
import base64
import json
import logging

import urllib.request
import urllib.error


logger = logging.getLogger(__name__)


@dataclass
class RPCResponse:
    """RPC response wrapper"""

    result: Optional[Any] = None
    error: Optional[Dict[str, Any]] = None
    id: Optional[str] = None

    @property
    def is_success(self) -> bool:
        return self.error is None


@dataclass
class RPCClient:
    """
    Generic JSON-RPC client for cryptocurrency daemons.
    Compatible with Bitcoin Core RPC interface.
    """

    host: str = "127.0.0.1"
    port: int = 15715
    username: str = ""
    password: str = ""
    timeout: int = 30
    _id_counter: int = 0

    def __post_init__(self) -> None:
        """Initialize RPC client"""
        self._auth_header: str = base64.b64encode(f"{self.username}:{self.password}".encode()).decode()

    def _next_id(self) -> str:
        """Generate next request ID"""
        self._id_counter += 1
        return str(self._id_counter)

    def _make_request(self, method: str, params: Optional[List[Any]] = None) -> RPCResponse:
        """Make JSON-RPC request"""
        request_data: Dict[str, Any] = {
            "jsonrpc": "2.0",
            "method": method,
            "id": self._next_id(),
        }
        if params is not None:
            request_data["params"] = params

        url = f"http://{self.host}:{self.port}"
        headers: Dict[str, str] = {
            "Authorization": f"Basic {self._auth_header}",
            "Content-Type": "application/json",
        }

        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(request_data).encode(),
                headers=headers,
                method="POST",
            )

            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                response_data = json.loads(response.read().decode())
                return RPCResponse(
                    result=response_data.get("result"),
                    error=response_data.get("error"),
                    id=response_data.get("id"),
                )

        except urllib.error.HTTPError as e:
            error_body = e.read().decode() if e.fp else ""
            logger.error(f"RPC HTTP error {e.code}: {error_body}")
            return RPCResponse(
                error={"code": e.code, "message": error_body},
            )
        except urllib.error.URLError as e:
            logger.error(f"RPC connection error: {e.reason}")
            return RPCResponse(
                error={"code": -1, "message": str(e.reason)},
            )
        except Exception as e:
            logger.exception(f"RPC unexpected error: {e}")
            return RPCResponse(
                error={"code": -1, "message": str(e)},
            )

    # =========================================================================
    # Blockchain Queries
    # =========================================================================

    def getblockcount(self) -> int:
        """Get current block height"""
        response = self._make_request("getblockcount")
        return int(response.result) if response.result is not None else 0

    def getconnectioncount(self) -> int:
        """Get number of network connections"""
        response = self._make_request("getconnectioncount")
        return int(response.result) if response.result is not None else 0

    def getbestblockhash(self) -> str:
        """Get hash of best block"""
        response = self._make_request("getbestblockhash")
        return str(response.result) if response.result is not None else ""

    def getblockhash(self, height: int) -> str:
        """Get block hash at height"""
        response = self._make_request("getblockhash", [height])
        return str(response.result) if response.result is not None else ""

    def getblock(self, hash: str) -> Dict[str, Any]:
        """Get block data by hash"""
        response = self._make_request("getblock", [hash])
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    def getblockbyheight(self, height: int) -> Dict[str, Any]:
        """Get block data by height"""
        block_hash = self.getblockhash(height)
        if block_hash:
            return self.getblock(block_hash)
        return {}

    # =========================================================================
    # Transaction Queries
    # =========================================================================

    def getrawtransaction(self, txid: str, verbose: bool = False) -> str:
        """Get raw transaction hex"""
        response = self._make_request("getrawtransaction", [txid, verbose])
        return str(response.result) if response.result is not None else ""

    def gettransaction(self, txid: str) -> Dict[str, Any]:
        """Get transaction details"""
        response = self._make_request("gettransaction", [txid])
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    def sendrawtransaction(self, hex: str) -> str:
        """Broadcast raw transaction"""
        response = self._make_request("sendrawtransaction", [hex])
        if response.is_success:
            return str(response.result) if response.result is not None else ""
        logger.error(f"Failed to send transaction: {response.error}")
        raise ValueError(f"Transaction broadcast failed: {response.error}")

    def decoderawtransaction(self, hex: str) -> Dict[str, Any]:
        """Decode raw transaction"""
        response = self._make_request("decoderawtransaction", [hex])
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    # =========================================================================
    # Wallet Queries
    # =========================================================================

    def listunspent(self, minconf: int = 0) -> List[Dict[str, Any]]:
        """List unspent outputs"""
        response = self._make_request("listunspent", [minconf])
        result = response.result
        return list(result) if isinstance(result, list) else []

    def getwalletinfo(self) -> Dict[str, Any]:
        """Get wallet information"""
        response = self._make_request("getwalletinfo")
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    def getbalance(self, minconf: int = 0) -> Decimal:
        """Get wallet balance"""
        response = self._make_request("getbalance", [minconf])
        try:
            return Decimal(str(response.result)) if response.result is not None else Decimal("0")
        except (TypeError, ValueError):
            return Decimal("0")

    def getnewaddress(self, label: str = "") -> str:
        """Generate new receiving address"""
        params = [label] if label else []
        response = self._make_request("getnewaddress", params)
        return str(response.result) if response.result is not None else ""

    def importprivkey(self, privkey: str, label: str = "", rescan: bool = True) -> None:
        """Import private key"""
        params = [privkey, label, rescan]
        self._make_request("importprivkey", params)

    def dumpprivkey(self, address: str) -> str:
        """Export private key"""
        response = self._make_request("dumpprivkey", [address])
        return str(response.result) if response.result is not None else ""

    def walletpassphrase(self, passphrase: str, timeout: int) -> None:
        """Unlock wallet"""
        self._make_request("walletpassphrase", [passphrase, timeout])

    # =========================================================================
    # Network Queries
    # =========================================================================

    def getnetworkinfo(self) -> Dict[str, Any]:
        """Get network information"""
        response = self._make_request("getnetworkinfo")
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    def getpeerinfo(self) -> List[Dict[str, Any]]:
        """Get peer information"""
        response = self._make_request("getpeerinfo")
        result = response.result
        return list(result) if isinstance(result, list) else []

    # =========================================================================
    # Control
    # =========================================================================

    def stop(self) -> None:
        """Stop the daemon"""
        self._make_request("stop")

    def help(self, command: str = "") -> str:
        """Get help for command"""
        params = [command] if command else []
        response = self._make_request("help", params)
        return str(response.result) if response.result is not None else ""

    def estimatefee(self, nblocks: int = 6) -> Decimal:
        """Estimate fee for confirmation in nblocks"""
        response = self._make_request("estimatefee", [nblocks])
        try:
            return Decimal(str(response.result)) if response.result is not None else Decimal("0.0001")
        except (TypeError, ValueError):
            return Decimal("0.0001")


@dataclass
class BlackCoinClient(RPCClient):
    """
    BlackCoin-specific RPC client.
    Adds peg and bridge functionality.
    """

    def __post_init__(self) -> None:
        """Initialize BlackCoin client"""
        super().__post_init__()
        self.host = "127.0.0.1"
        self.port = 15715

    # =========================================================================
    # Peg Functions (BlackHalo specific)
    # =========================================================================

    def getpeginfo(self) -> Dict[str, Any]:
        """Get peg status information"""
        response = self._make_request("getpeginfo")
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    def bridges(self) -> List[Dict[str, Any]]:
        """Get bridge information"""
        response = self._make_request("bridges")
        result = response.result
        return list(result) if isinstance(result, list) else []

    def merklesin(self, stream: int = 1) -> Dict[str, Any]:
        """Get Merkle proof for incoming transfers"""
        response = self._make_request("merklesin", [stream])
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    def merklesout(self, stream: int = 1) -> Dict[str, Any]:
        """Get Merkle proof for outgoing transfers"""
        response = self._make_request("merklesout", [stream])
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    def getfractions(self, txid: str) -> Dict[str, Any]:
        """Get exchange fractions for transaction"""
        response = self._make_request("getfractions", [txid])
        result = response.result
        return dict(result) if isinstance(result, dict) else {}

    def listfrozen(self) -> List[str]:
        """List frozen outputs"""
        response = self._make_request("listfrozen")
        result = response.result
        return list(result) if isinstance(result, list) else []

    def freeze(self, txid: str, vout: int) -> None:
        """Freeze an output"""
        self._make_request("freeze", [txid, vout])

    def unfreeze(self, txid: str, vout: int) -> None:
        """Unfreeze an output"""
        self._make_request("unfreeze", [txid, vout])

    def getstakesplitthreshold(self) -> Decimal:
        """Get stake split threshold"""
        response = self._make_request("getstakesplitthreshold")
        try:
            return Decimal(str(response.result)) if response.result is not None else Decimal("1000")
        except (TypeError, ValueError):
            return Decimal("1000")

    def getstakinginfo(self) -> Dict[str, Any]:
        """Get staking information"""
        response = self._make_request("getstakinginfo")
        result = response.result
        return dict(result) if isinstance(result, dict) else {}


# Factory function
def create_rpc_client(
    crypto_type: str = "BLK",
    host: str = "127.0.0.1",
    port: int = 15715,
    username: str = "",
    password: str = "",
) -> Union[BlackCoinClient, RPCClient]:
    """Create appropriate RPC client based on cryptocurrency type"""
    if crypto_type.upper() == "BLK":
        return BlackCoinClient(
            host=host,
            port=port,
            username=username,
            password=password,
        )
    return RPCClient(
        host=host,
        port=port,
        username=username,
        password=password,
    )
