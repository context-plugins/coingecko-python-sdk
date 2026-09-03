from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FloorPrice(SdkBaseModel):
    """NFT collection floor price"""

    native_currency: Optional[float] = UNSET
    usd: Optional[float] = UNSET


class FloorPriceDict(TypedDict):
    native_currency: NotRequired[float]
    usd: NotRequired[float]
