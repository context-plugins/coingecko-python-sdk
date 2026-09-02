from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FloorPrice1YPercentageChange(SdkBaseModel):
    """NFT collection floor price 1 year percentage change"""

    usd: Optional[float] = UNSET
    native_currency: Optional[float] = UNSET


class FloorPrice1YPercentageChangeDict(TypedDict):
    usd: NotRequired[float]
    native_currency: NotRequired[float]
