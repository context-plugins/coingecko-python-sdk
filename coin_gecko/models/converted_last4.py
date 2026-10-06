from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConvertedLast4(SdkBaseModel):
    """Derivative converted last price"""

    btc: Optional[str] = UNSET
    eth: Optional[str] = UNSET
    usd: Optional[str] = UNSET


class ConvertedLast4Dict(TypedDict):
    btc: NotRequired[str]
    eth: NotRequired[str]
    usd: NotRequired[str]
