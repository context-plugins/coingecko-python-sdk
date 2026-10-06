from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Volume24H(SdkBaseModel):
    """NFT collection volume in 24 hours"""

    native_currency: Optional[float] = UNSET
    usd: Optional[float] = UNSET


class Volume24HDict(TypedDict):
    native_currency: NotRequired[float]
    usd: NotRequired[float]
