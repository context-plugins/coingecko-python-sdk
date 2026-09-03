from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data4(SdkBaseModel):
    market_cap: float
    """Category market cap"""

    market_cap_btc: float
    """Category market cap in BTC"""

    total_volume: float
    """Category total volume"""

    total_volume_btc: float
    """Category total volume in BTC"""

    market_cap_change_percentage_24h: dict[str, float]
    """Category market cap change percentage in 24 hours by currency"""

    sparkline: str
    """Category sparkline image URL"""


class Data4Dict(TypedDict):
    market_cap: float
    market_cap_btc: float
    total_volume: float
    total_volume_btc: float
    market_cap_change_percentage_24h: dict[str, float]
    sparkline: str
