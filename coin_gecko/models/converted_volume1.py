from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConvertedVolume1(SdkBaseModel):
    """Ticker converted volume"""

    btc: Optional[float] = UNSET
    eth: Optional[float] = UNSET
    usd: Optional[float] = UNSET


class ConvertedVolume1Dict(TypedDict):
    btc: NotRequired[float]
    eth: NotRequired[float]
    usd: NotRequired[float]
