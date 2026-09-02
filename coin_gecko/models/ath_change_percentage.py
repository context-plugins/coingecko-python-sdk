from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AthChangePercentage(SdkBaseModel):
    """NFT collection all time highs change percentage"""

    native_currency: Optional[float] = UNSET
    usd: Optional[float] = UNSET


class AthChangePercentageDict(TypedDict):
    native_currency: NotRequired[float]
    usd: NotRequired[float]
