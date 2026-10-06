from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Ath(SdkBaseModel):
    """NFT collection all time highs"""

    native_currency: Optional[float] = UNSET
    usd: Optional[float] = UNSET


class AthDict(TypedDict):
    native_currency: NotRequired[float]
    usd: NotRequired[float]
