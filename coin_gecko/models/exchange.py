from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Exchange(SdkBaseModel):
    id: str
    """Exchange ID"""

    name: str
    """Exchange name"""

    market_type: str
    """Exchange market type"""

    thumb: str
    """Exchange thumb image URL"""

    large: str
    """Exchange large image URL"""


class ExchangeDict(TypedDict):
    id: str
    name: str
    market_type: str
    thumb: str
    large: str
