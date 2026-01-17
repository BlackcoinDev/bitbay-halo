"""
BitMessage client module for BlackHalo 2.0
Type-safe PyBitmessage API integration
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Protocol

logger = logging.getLogger(__name__)


@dataclass
class BMAddress:
    """BitMessage address"""

    address: str
    label: str = ""
    stream: int = 1
    is_deterministic: bool = False
    is_chan: bool = False
    is_mail_gateway: bool = False
    gateway: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    enabled: bool = True

    def is_valid(self) -> bool:
        """Validate BitMessage address format"""
        return self.address.startswith("BM-") and len(self.address) == 36


@dataclass
class BMInboxMessage:
    """BitMessage inbox message"""

    msg_id: str
    to_address: str
    from_address: str
    subject: str
    body: str
    received_at: datetime = field(default_factory=datetime.utcnow)
    read: bool = False
    archived: bool = False
    message_encoding: str = "UTF-8"
    ack_data: str = ""
    payload_length: int = 0

    @property
    def is_unread(self) -> bool:
        return not self.read


@dataclass
class BMOutboxMessage:
    """BitMessage outbox entry"""

    msg_id: str
    to_address: str
    from_address: str
    subject: str
    body: str
    status: str = "pending"
    ack_data: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    sent_at: Optional[datetime] = None
    last_attempt: Optional[datetime] = None
    retry_count: int = 0
    message_encoding: str = "UTF-8"

    def is_sent(self) -> bool:
        return self.status in ("sent", "delivered", "ack")


@dataclass
class BMBroadcast:
    """BitMessage broadcast"""

    address: str
    subject: str
    body: str
    encoding: int = 2
    version: int = 2
    TTL: int = 4320


@dataclass
class BMLocalStream:
    """Local BitMessage stream"""

    stream_number: int
    address_count: int
    last_updated: datetime = field(default_factory=datetime.utcnow)


@dataclass
class BMNetworkStatus:
    """BitMessage network status"""

    is_connected: bool = False
    incoming_connections: int = 0
    outgoing_connections: int = 0
    host: str = "127.0.0.1"
    port: int = 8878
    api_port: int = 8442
    uptime_seconds: int = 0


@dataclass
class BMStats:
    """BitMessage statistics"""

    total_sent: int = 0
    total_received: int = 0
    total_acknowledged: int = 0
    total_failed: int = 0
    number_of_processed_objects: int = 0
    pending_messages: int = 0
    pending_acks: int = 0


class IBMDaemon(Protocol):
    """Protocol for BitMessage daemon interface"""

    def start_daemon(self, config_dir: str = "") -> Dict[str, Any]: ...

    def stop_daemon(self) -> Dict[str, Any]: ...

    def get_status(self) -> Dict[str, Any]: ...

    def add_subscription(self, address: str, label: str) -> Dict[str, Any]: ...

    def delete_subscription(self, address: str) -> Dict[str, Any]: ...

    def list_subscriptions(self) -> List[Dict[str, Any]]: ...

    def create_address(self, deterministic: bool = False, num_addresses: int = 1) -> Dict[str, Any]: ...

    def create_deterministic_address(self, passphrase: str, num_addresses: int = 1, is_chan: bool = False) -> Dict[str, Any]: ...

    def list_addresses(self) -> List[Dict[str, Any]]: ...

    def decode_address(self, address: str) -> Dict[str, Any]: ...

    def send_message(
        self,
        to_address: str,
        from_address: str,
        subject: str,
        message: str,
        encoding: int = 2,
    ) -> Dict[str, Any]: ...

    def send_broadcast(self, from_address: str, subject: str, message: str, encoding: int = 2) -> Dict[str, Any]: ...

    def get_inbox_messages(self) -> List[Dict[str, Any]]: ...

    def get_all_inbox_messages(self) -> List[Dict[str, Any]]: ...

    def get_sent_messages(self) -> List[Dict[str, Any]]: ...

    def get_all_sent_messages(self) -> List[Dict[str, Any]]: ...

    def trash_message(self, msg_id: str) -> bool: ...

    def trash_sent_message(self, msg_id: str) -> bool: ...

    def mark_message_as_read(self, msg_id: str) -> bool: ...

    def mark_message_as_unread(self, msg_id: str) -> bool: ...

    def get_address_messages(self, address: str) -> List[Dict[str, Any]]: ...

    def decrypt_message(self, msg_id: str) -> Dict[str, Any]: ...

    def get_network_status(self) -> Dict[str, Any]: ...

    def add_black_list(self, address: str, enabled: bool = True) -> Dict[str, Any]: ...

    def delete_black_list(self, address: str) -> Dict[str, Any]: ...

    def get_black_list(self) -> List[Dict[str, Any]]: ...

    def get_white_list(self) -> List[Dict[str, Any]]: ...

    def add_white_list(self, address: str, enabled: bool = True) -> Dict[str, Any]: ...

    def delete_white_list(self, address: str) -> Dict[str, Any]: ...


class PyBitmessageClient:
    """
    PyBitmessage API client.
    Communicates with BitMessage daemon via JSON-RPC API.
    """

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 8442,
        username: str = "",
        password: str = "",
    ) -> None:
        """Initialize BitMessage client"""
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.auth_string = f"{username}:{password}"
        self._is_connected = False

    def _make_request(self, method: str, params: Optional[List[Any]] = None) -> Dict[str, Any]:
        """Make JSON-RPC request to BitMessage API"""
        import base64
        import json as json_lib
        import urllib.error
        import urllib.request

        url = f"http://{self.host}:{self.port}"
        headers: Dict[str, str] = {
            "Authorization": f"Basic {base64.b64encode(self.auth_string.encode()).decode()}",
            "Content-Type": "application/json",
        }
        request_data: Dict[str, Any] = {
            "method": method,
            "params": params or [],
            "id": 1,
        }

        try:
            req = urllib.request.Request(
                url,
                data=json_lib.dumps(request_data).encode(),
                headers=headers,
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json_lib.loads(response.read().decode())
                return result.get("result", {})
        except urllib.error.HTTPError as e:
            logger.error(f"BitMessage HTTP error {e.code}: {e.read().decode()}")
            return {"error": str(e)}
        except urllib.error.URLError as e:
            logger.error(f"BitMessage connection error: {e.reason}")
            return {"error": str(e)}
        except Exception as e:
            logger.exception(f"BitMessage request error: {e}")
            return {"error": str(e)}

    def start_daemon(self, config_dir: str = "") -> Dict[str, Any]:
        """Start the BitMessage daemon"""
        params = [config_dir] if config_dir else []
        return self._make_request("startDaemon", params)

    def stop_daemon(self) -> Dict[str, Any]:
        """Stop the BitMessage daemon"""
        return self._make_request("stopDaemon")

    def get_status(self) -> Dict[str, Any]:
        """Get daemon status"""
        return self._make_request("getStatus")

    def add_subscription(self, address: str, label: str) -> Dict[str, Any]:
        """Add address to subscriptions"""
        return self._make_request("addSubscription", [address, label])

    def delete_subscription(self, address: str) -> Dict[str, Any]:
        """Remove address from subscriptions"""
        return self._make_request("deleteSubscription", [address])

    def list_subscriptions(self) -> List[Dict[str, Any]]:
        """List all subscriptions"""
        result = self._make_request("listSubscriptions")
        return result.get("subscriptions", [])

    def create_address(self, deterministic: bool = False, num_addresses: int = 1) -> Dict[str, Any]:
        """Create new address(es)"""
        return self._make_request("createRandomAddress", ["", deterministic, num_addresses])

    def create_deterministic_address(self, passphrase: str, num_addresses: int = 1, is_chan: bool = False) -> Dict[str, Any]:
        """Create deterministic address from passphrase"""
        return self._make_request(
            "createDeterministicAddresses",
            [
                passphrase,
                num_addresses,
                is_chan,
                1,
                0,
                0,
            ],
        )

    def list_addresses(self) -> List[Dict[str, Any]]:
        """List all addresses"""
        result = self._make_request("listAddresses")
        return result.get("addresses", [])

    def decode_address(self, address: str) -> Dict[str, Any]:
        """Decode and validate address"""
        return self._make_request("decodeAddress", [address])

    def send_message(
        self,
        to_address: str,
        from_address: str,
        subject: str,
        message: str,
        encoding: int = 2,
    ) -> Dict[str, Any]:
        """Send a message"""
        return self._make_request(
            "sendMessage",
            [
                to_address,
                from_address,
                subject,
                message,
                encoding,
            ],
        )

    def send_broadcast(self, from_address: str, subject: str, message: str, encoding: int = 2) -> Dict[str, Any]:
        """Send a broadcast"""
        return self._make_request("sendBroadcast", [from_address, subject, message, encoding])

    def get_inbox_messages(self) -> List[Dict[str, Any]]:
        """Get inbox messages"""
        result = self._make_request("getInboxMessages", [False])
        return result.get("inboxMessages", [])

    def get_all_inbox_messages(self) -> List[Dict[str, Any]]:
        """Get all inbox messages including archived"""
        result = self._make_request("getInboxMessages", [True])
        return result.get("inboxMessages", [])

    def get_sent_messages(self) -> List[Dict[str, Any]]:
        """Get sent messages"""
        result = self._make_request("getSentMessages", [False, "", ""])
        return result.get("sentMessages", [])

    def get_all_sent_messages(self) -> List[Dict[str, Any]]:
        """Get all sent messages including those awaiting ack"""
        result = self._make_request("getSentMessages", [True, "", ""])
        return result.get("sentMessages", [])

    def trash_message(self, msg_id: str) -> bool:
        """Delete message from inbox"""
        result = self._make_request("trashMessage", [msg_id])
        return isinstance(result, bool) and result

    def trash_sent_message(self, msg_id: str) -> bool:
        """Delete message from sent folder"""
        result = self._make_request("trashSentMessage", [msg_id])
        return isinstance(result, bool) and result

    def mark_message_as_read(self, msg_id: str) -> bool:
        """Mark message as read"""
        result = self._make_request("markMessageAsRead", [msg_id])
        return result is True

    def mark_message_as_unread(self, msg_id: str) -> bool:
        """Mark message as unread"""
        result = self._make_request("markMessageAsUnread", [msg_id])
        return result is True

    def get_address_messages(self, address: str) -> List[Dict[str, Any]]:
        """Get messages for specific address"""
        result = self._make_request("getInboxMessagesByReceiver", [address])
        return result.get("inboxMessages", []) if isinstance(result, dict) else []

    def decrypt_message(self, msg_id: str) -> Dict[str, Any]:
        """Decrypt encrypted message"""
        return self._make_request("decryptMessage", [msg_id])

    def get_network_status(self) -> Dict[str, Any]:
        """Get network connection status"""
        return self._make_request("getNetworkStatus")

    def add_black_list(self, address: str, enabled: bool = True) -> Dict[str, Any]:
        """Add address to blacklist"""
        return self._make_request("addToBlacklist", [address, "black", enabled])

    def delete_black_list(self, address: str) -> Dict[str, Any]:
        """Remove address from blacklist"""
        return self._make_request("deleteFromBlacklist", [address])

    def get_black_list(self) -> List[Dict[str, Any]]:
        """Get blacklist entries"""
        result = self._make_request("getBlackList")
        return result.get("blacklist", []) if isinstance(result, dict) else []

    def get_white_list(self) -> List[Dict[str, Any]]:
        """Get whitelist entries"""
        result = self._make_request("getWhiteList")
        return result.get("whitelist", []) if isinstance(result, dict) else []

    def add_white_list(self, address: str, enabled: bool = True) -> Dict[str, Any]:
        """Add address to whitelist"""
        return self._make_request("addToWhitelist", [address, "white", enabled])

    def delete_white_list(self, address: str) -> Dict[str, Any]:
        """Remove address from whitelist"""
        return self._make_request("deleteFromWhitelist", [address])


class BitMessageManager:
    """
    High-level BitMessage manager.
    Combines API client with local state management.
    """

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 8442,
        api_username: str = "",
        api_password: str = "",
    ) -> None:
        """Initialize BitMessage manager"""
        self.client = PyBitmessageClient(
            host=host,
            port=port,
            username=api_username,
            password=api_password,
        )
        self._addresses: List[BMAddress] = []
        self._inbox: List[BMInboxMessage] = []
        self._outbox: List[BMOutboxMessage] = []
        self._subscriptions: List[Dict[str, Any]] = []
        self._network_status: Optional[BMNetworkStatus] = None

    def initialize(self) -> bool:
        """Initialize connection to BitMessage daemon"""
        try:
            status = self.client.get_status()
            self._is_connected = "status" in status
            if self._is_connected:
                self.refresh_addresses()
                self.refresh_messages()
            return self._is_connected
        except Exception as e:
            logger.error(f"Failed to initialize BitMessage: {e}")
            return False

    @property
    def is_connected(self) -> bool:
        """Check if connected to daemon"""
        return self._is_connected

    def refresh_addresses(self) -> None:
        """Refresh local address list"""
        try:
            addresses = self.client.list_addresses()
            self._addresses = [
                BMAddress(
                    address=a["address"],
                    label=a.get("label", ""),
                    stream=a.get("streamNumber", 1),
                    is_deterministic=a.get("deterministic", False),
                    is_chan=a.get("chan", False),
                    enabled=a.get("enabled", True),
                    created_at=datetime.fromtimestamp(a.get("timeCreated", 0)),
                )
                for a in addresses
            ]
        except Exception as e:
            logger.error(f"Failed to refresh addresses: {e}")

    def refresh_messages(self) -> None:
        """Refresh inbox and outbox"""
        try:
            inbox_messages = self.client.get_inbox_messages()
            self._inbox = [
                BMInboxMessage(
                    msg_id=m["msgid"],
                    to_address=m["toAddress"],
                    from_address=m["fromAddress"],
                    subject=m.get("subject", ""),
                    body=m.get("message", ""),
                    read=m.get("read", False),
                    received_at=datetime.fromtimestamp(m.get("receivedTime", 0)),
                )
                for m in inbox_messages
            ]

            sent_messages = self.client.get_sent_messages()
            self._outbox = [
                BMOutboxMessage(
                    msg_id=m["msgid"],
                    to_address=m["toAddress"],
                    from_address=m["fromAddress"],
                    subject=m.get("subject", ""),
                    body=m.get("message", ""),
                    status=m.get("status", "unknown"),
                    ack_data=m.get("ackData", ""),
                    sent_at=datetime.fromtimestamp(m.get("lastActionTime", 0)) if m.get("lastActionTime", 0) > 0 else None,
                )
                for m in sent_messages
            ]
        except Exception as e:
            logger.error(f"Failed to refresh messages: {e}")

    @property
    def addresses(self) -> List[BMAddress]:
        """Get all addresses"""
        return list(self._addresses)

    @property
    def inbox(self) -> List[BMInboxMessage]:
        """Get inbox messages"""
        return list(self._inbox)

    @property
    def outbox(self) -> List[BMOutboxMessage]:
        """Get outbox messages"""
        return list(self._outbox)

    def get_unread_count(self) -> int:
        """Get count of unread messages"""
        return sum(1 for m in self._inbox if not m.read)

    def create_new_address(self, label: str = "", deterministic: bool = False) -> Optional[str]:
        """Create new address"""
        result = self.client.create_address(deterministic)
        if "address" in result:
            address = result["address"]
            if label:
                self._update_address_label(address, label)
            self.refresh_addresses()
            return address
        return None

    def create_deterministic_address(self, passphrase: str, is_chan: bool = False) -> Optional[str]:
        """Create deterministic address from passphrase"""
        result = self.client.create_deterministic_address(passphrase, num_addresses=1, is_chan=is_chan)
        if "addresses" in result and len(result["addresses"]) > 0:
            address = result["addresses"][0]
            self.refresh_addresses()
            return address
        return None

    def _update_address_label(self, address: str, label: str) -> None:
        """Update address label"""
        for addr in self._addresses:
            if addr.address == address:
                addr.label = label
                break

    def send_message(
        self,
        to_address: str,
        from_address: str,
        subject: str,
        body: str,
    ) -> bool:
        """Send a message"""
        try:
            result = self.client.send_message(
                to_address=to_address,
                from_address=from_address,
                subject=subject,
                message=body,
            )
            if "msgid" in result:
                self.refresh_messages()
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
            return False

    def send_broadcast(self, from_address: str, subject: str, body: str) -> bool:
        """Send a broadcast"""
        try:
            result = self.client.send_broadcast(
                from_address=from_address,
                subject=subject,
                message=body,
            )
            if "msgid" in result:
                self.refresh_messages()
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to send broadcast: {e}")
            return False

    def mark_as_read(self, msg_id: str) -> bool:
        """Mark message as read"""
        result = self.client.mark_message_as_read(msg_id)
        if result:
            for msg in self._inbox:
                if msg.msg_id == msg_id:
                    msg.read = True
                    break
        return result

    def delete_message(self, msg_id: str) -> bool:
        """Delete message from inbox"""
        result = self.client.trash_message(msg_id)
        if result:
            self._inbox = [m for m in self._inbox if m.msg_id != msg_id]
        return result

    def get_network_status(self) -> Optional[BMNetworkStatus]:
        """Get network status"""
        try:
            status = self.client.get_network_status()
            return BMNetworkStatus(
                is_connected=status.get("networkStatus", "") == "connected",
                incoming_connections=status.get("incomingConnections", 0),
                outgoing_connections=status.get("outgoingConnections", 0),
                host=status.get("host", self.client.host),
                port=status.get("port", self.client.port),
                api_port=status.get("apiPort", self.client.port),
                uptime_seconds=status.get("uptime", 0),
            )
        except Exception as e:
            logger.error(f"Failed to get network status: {e}")
            return None
