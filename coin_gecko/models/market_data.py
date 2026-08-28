from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketData(SdkBaseModel):
    """Market data at the given date"""

    current_price: Optional[dict[str, float]] = UNSET
    """Current price keyed by currency"""

    market_cap: Optional[dict[str, float]] = UNSET
    """Market capitalization keyed by currency"""

    total_volume: Optional[dict[str, float]] = UNSET
    """Total trading volume keyed by currency"""


class MarketDataDict(TypedDict):
    current_price: NotRequired[dict[str, float]]
    market_cap: NotRequired[dict[str, float]]
    total_volume: NotRequired[dict[str, float]]
