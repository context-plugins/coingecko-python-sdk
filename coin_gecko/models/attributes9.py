from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .launchpad_details import LaunchpadDetails, LaunchpadDetailsDict
from .volume_usd1 import VolumeUsd1, VolumeUsd1Dict


class Attributes9(SdkBaseModel):
    address: str
    """Token contract address"""

    name: str
    """Token name"""

    symbol: str
    """Token symbol"""

    decimals: int
    """Token decimals"""

    image_url: str | None
    """Token image URL"""

    coingecko_coin_id: str | None
    """CoinGecko coin ID"""

    total_supply: str
    """Token total supply"""

    normalized_total_supply: str
    """Normalized token total supply"""

    price_usd: str | None
    """Token price in USD"""

    fdv_usd: str | None
    """Fully diluted valuation in USD"""

    total_reserve_in_usd: str
    """Total reserve in USD across all pools"""

    volume_usd: VolumeUsd1
    """Volume in USD"""

    market_cap_usd: str | None
    """Market cap in USD"""

    last_trade_timestamp: Optional[str] = UNSET
    """Last trade timestamp in UNIX"""

    launchpad_details: Optional[LaunchpadDetails] = UNSET
    """Launchpad details for pump-style tokens"""


class Attributes9Dict(TypedDict):
    address: str
    name: str
    symbol: str
    decimals: int
    image_url: str | None
    coingecko_coin_id: str | None
    total_supply: str
    normalized_total_supply: str
    price_usd: str | None
    fdv_usd: str | None
    total_reserve_in_usd: str
    volume_usd: VolumeUsd1 | VolumeUsd1Dict
    market_cap_usd: str | None
    last_trade_timestamp: NotRequired[str]
    launchpad_details: NotRequired[LaunchpadDetails | LaunchpadDetailsDict]
