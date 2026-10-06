from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FloorPrice7DPercentageChange(SdkBaseModel):
    """NFT collection floor price 7 days percentage change"""

    usd: Optional[float] = UNSET
    native_currency: Optional[float] = UNSET


class FloorPrice7DPercentageChangeDict(TypedDict):
    usd: NotRequired[float]
    native_currency: NotRequired[float]
