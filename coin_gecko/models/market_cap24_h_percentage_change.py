from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketCap24HPercentageChange(SdkBaseModel):
    """NFT collection market cap 24 hours percentage change"""

    usd: Optional[float] = UNSET
    native_currency: Optional[float] = UNSET


class MarketCap24HPercentageChangeDict(TypedDict):
    usd: NotRequired[float]
    native_currency: NotRequired[float]
