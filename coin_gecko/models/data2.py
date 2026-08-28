from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .content import Content, ContentDict


class Data2(SdkBaseModel):
    price: float
    """Coin price in USD"""

    price_btc: str
    """Coin price in BTC"""

    price_change_percentage_24h: dict[str, float]
    """Coin price change percentage in 24 hours by currency"""

    market_cap: str
    """Coin market cap in USD"""

    market_cap_btc: str
    """Coin market cap in BTC"""

    total_volume: str
    """Coin total volume in USD"""

    total_volume_btc: str
    """Coin total volume in BTC"""

    sparkline: str
    """Coin sparkline image URL"""

    content: Content | None


class Data2Dict(TypedDict):
    price: float
    price_btc: str
    price_change_percentage_24h: dict[str, float]
    market_cap: str
    market_cap_btc: str
    total_volume: str
    total_volume_btc: str
    sparkline: str
    content: Content | ContentDict | None
