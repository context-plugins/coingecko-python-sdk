from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data1(SdkBaseModel):
    defi_market_cap: str
    """DeFi market cap"""

    eth_market_cap: str
    """ETH market cap"""

    defi_to_eth_ratio: str
    """DeFi to ETH ratio"""

    trading_volume_24h: str
    """DeFi trading volume in 24 hours"""

    defi_dominance: str
    """DeFi dominance percentage"""

    top_coin_name: str
    """DeFi top coin name"""

    top_coin_defi_dominance: float
    """DeFi top coin dominance percentage"""


class Data1Dict(TypedDict):
    defi_market_cap: str
    eth_market_cap: str
    defi_to_eth_ratio: str
    trading_volume_24h: str
    defi_dominance: str
    top_coin_name: str
    top_coin_defi_dominance: float
