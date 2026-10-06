from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SimplePrice(SdkBaseModel):
    usd: Optional[float] = UNSET
    """Price in the target currency"""

    usd_market_cap: Optional[float] = UNSET
    """Market capitalization in the target currency"""

    usd_24h_vol: Optional[float] = UNSET
    """24-hour trading volume in the target currency"""

    usd_24h_change: Optional[float] = UNSET
    """24-hour price change percentage in the target currency"""

    last_updated_at: Optional[float] = UNSET
    """Last updated timestamp in UNIX seconds"""


class SimplePriceDict(TypedDict):
    usd: NotRequired[float]
    usd_market_cap: NotRequired[float]
    usd_24h_vol: NotRequired[float]
    usd_24h_change: NotRequired[float]
    last_updated_at: NotRequired[float]
