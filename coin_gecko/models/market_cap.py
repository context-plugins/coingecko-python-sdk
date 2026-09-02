from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketCap(SdkBaseModel):
    """NFT collection market cap"""

    native_currency: Optional[float] = UNSET
    usd: Optional[float] = UNSET


class MarketCapDict(TypedDict):
    native_currency: NotRequired[float]
    usd: NotRequired[float]
