from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Attributes16(SdkBaseModel):
    token_prices: dict[str, str]
    """Token prices keyed by contract address"""

    market_cap_usd: Optional[dict[str, str]] = UNSET
    """Market cap in USD keyed by contract address"""

    h24_volume_usd: Optional[dict[str, str]] = UNSET
    """24hr volume in USD keyed by contract address"""

    h24_price_change_percentage: Optional[dict[str, str]] = UNSET
    """24hr price change percentage keyed by contract address"""

    total_reserve_in_usd: Optional[dict[str, str]] = UNSET
    """Total reserve in USD keyed by contract address"""

    last_trade_timestamp: Optional[dict[str, str]] = UNSET
    """Last trade timestamp keyed by contract address"""


class Attributes16Dict(TypedDict):
    token_prices: dict[str, str]
    market_cap_usd: NotRequired[dict[str, str]]
    h24_volume_usd: NotRequired[dict[str, str]]
    h24_price_change_percentage: NotRequired[dict[str, str]]
    total_reserve_in_usd: NotRequired[dict[str, str]]
    last_trade_timestamp: NotRequired[dict[str, str]]
