from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FloorPrice24HPercentageChange(SdkBaseModel):
    """NFT collection floor price 24 hours percentage change"""

    usd: Optional[float] = UNSET
    native_currency: Optional[float] = UNSET


class FloorPrice24HPercentageChangeDict(TypedDict):
    usd: NotRequired[float]
    native_currency: NotRequired[float]
