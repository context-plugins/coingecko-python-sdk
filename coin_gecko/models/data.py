from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data(SdkBaseModel):
    active_cryptocurrencies: int
    """Number of active cryptocurrencies"""

    upcoming_icos: int
    """Number of upcoming ICOs"""

    ongoing_icos: int
    """Number of ongoing ICOs"""

    ended_icos: int
    """Number of ended ICOs"""

    markets: int
    """Number of exchanges"""

    total_market_cap: dict[str, float]
    """Total cryptocurrency market cap by currency"""

    total_volume: dict[str, float]
    """Total cryptocurrency volume by currency"""

    market_cap_percentage: dict[str, float]
    """Market cap percentage by coin"""

    market_cap_change_percentage_24h_usd: float
    """Market cap change percentage in 24 hours in USD"""

    volume_change_percentage_24h_usd: float
    """Volume change percentage in 24 hours in USD"""

    updated_at: int
    """Last updated time in UNIX timestamp"""


class DataDict(TypedDict):
    active_cryptocurrencies: int
    upcoming_icos: int
    ongoing_icos: int
    ended_icos: int
    markets: int
    total_market_cap: dict[str, float]
    total_volume: dict[str, float]
    market_cap_percentage: dict[str, float]
    market_cap_change_percentage_24h_usd: float
    volume_change_percentage_24h_usd: float
    updated_at: int
