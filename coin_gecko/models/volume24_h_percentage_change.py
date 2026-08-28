from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Volume24HPercentageChange(SdkBaseModel):
    """NFT collection volume in 24 hours percentage change"""

    usd: Optional[float] = UNSET
    native_currency: Optional[float] = UNSET


class Volume24HPercentageChangeDict(TypedDict):
    usd: NotRequired[float]
    native_currency: NotRequired[float]
