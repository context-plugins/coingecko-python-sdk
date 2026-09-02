from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Attributes18(SdkBaseModel):
    name: str
    """Network name"""

    coingecko_asset_platform_id: str
    """Corresponding CoinGecko asset platform ID"""


class Attributes18Dict(TypedDict):
    name: str
    coingecko_asset_platform_id: str
