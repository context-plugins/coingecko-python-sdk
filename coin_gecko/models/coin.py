from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Coin(SdkBaseModel):
    id: str
    """Coin ID"""

    name: str
    """Coin name"""

    api_symbol: str
    """Coin API symbol"""

    symbol: str
    """Coin symbol"""

    market_cap_rank: int | None
    """Coin market cap rank"""

    thumb: str
    """Coin thumb image URL"""

    large: str
    """Coin large image URL"""


class CoinDict(TypedDict):
    id: str
    name: str
    api_symbol: str
    symbol: str
    market_cap_rank: int | None
    thumb: str
    large: str
