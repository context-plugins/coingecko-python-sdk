from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FloorPrice14DPercentageChange(SdkBaseModel):
    """NFT collection floor price 14 days percentage change"""

    usd: Optional[float] = UNSET
    native_currency: Optional[float] = UNSET


class FloorPrice14DPercentageChangeDict(TypedDict):
    usd: NotRequired[float]
    native_currency: NotRequired[float]
