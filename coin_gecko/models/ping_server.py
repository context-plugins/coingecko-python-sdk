from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PingServer(SdkBaseModel):
    gecko_says: str
    """API server status message"""


class PingServerDict(TypedDict):
    gecko_says: str
