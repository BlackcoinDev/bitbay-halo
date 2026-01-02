"""
GUI module for BlackHalo 2.0
Type-safe PyQt6 interface components
"""

from typing import Any, Dict, Optional, Protocol, runtime_checkable
from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import datetime
import logging


logger = logging.getLogger(__name__)


class Theme(Enum):
    """GUI theme options"""

    DARK = "dark"
    LIGHT = "light"
    SYSTEM = "system"


@dataclass
class WindowState:
    """Main window state"""

    width: int = 1024
    height: int = 768
    x: int = 100
    y: int = 100
    isMaximized: bool = False
    isFullScreen: bool = False


@dataclass
class GUISettings:
    """GUI configuration settings"""

    theme: Theme = Theme.SYSTEM
    language: str = "en"
    tray_enabled: bool = True
    notifications_enabled: bool = True
    sound_enabled: bool = True
    animation_enabled: bool = True
    font_size: int = 10
    font_family: str = "Sans Serif"


@dataclass
class Notification:
    """Toast notification"""

    title: str
    message: str
    level: str = "info"
    duration_ms: int = 3000
    callback: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class ProgressUpdate:
    """Progress indicator update"""

    task_name: str
    current: int
    total: int
    message: str = ""
    is_indeterminate: bool = False


@runtime_checkable
class IGUIController(Protocol):
    """Protocol for GUI controller interface"""

    def show_window(self) -> None: ...
    def hide_window(self) -> None: ...
    def close_window(self) -> None: ...
    def show_notification(self, notification: Notification) -> None: ...
    def show_progress(self, progress: ProgressUpdate) -> None: ...
    def hide_progress(self) -> None: ...
    def update_status_bar(self, message: str) -> None: ...
    def set_cursor(self, cursor_type: str) -> None: ...
    def refresh_ui(self) -> None: ...


@dataclass
class TabInfo:
    """Information about a UI tab"""

    id: str
    name: str
    icon: str = ""
    tooltip: str = ""
    is_visible: bool = True
    order: int = 0


@dataclass
class ActionShortcut:
    """Menu action with keyboard shortcut"""

    id: str
    text: str
    shortcut: str = ""
    icon: str = ""
    tooltip: str = ""
    is_checkable: bool = False
    is_checked: bool = False
    is_enabled: bool = True


@dataclass
class TableColumn:
    """Data table column definition"""

    id: str
    header: str
    width: int = 100
    is_sortable: bool = True
    is_visible: bool = True
    alignment: str = "left"


@dataclass
class TableRow:
    """Data table row"""

    data: Dict[str, Any]
    is_selected: bool = False
    is_editable: bool = False


@dataclass
class FormField:
    """Form input field definition"""

    id: str
    label: str
    field_type: str = "text"
    placeholder: str = ""
    is_required: bool = False
    is_password: bool = False
    validation_regex: str = ""
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    choices: list[tuple[str, str]] = field(default_factory=list)


@dataclass
class DialogResult:
    """Dialog/ modal result"""

    accepted: bool = False
    data: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MenuItem:
    """Menu tree item"""

    id: str
    text: str
    parent_id: Optional[str] = None
    icon: str = ""
    shortcut: str = ""
    is_separator: bool = False
    is_checkable: bool = False
    is_checked: bool = False
    is_enabled: bool = True
    order: int = 0
    children: list["MenuItem"] = field(default_factory=list)


@dataclass
class ToolbarItem:
    """Toolbar button definition"""

    id: str
    text: str
    icon: str = ""
    tooltip: str = ""
    is_separator: bool = False
    is_enabled: bool = True
    order: int = 0
