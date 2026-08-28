from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConvertedVolume4(SdkBaseModel):
    """Derivative converted volume"""

    btc: Optional[str] = UNSET
    eth: Optional[str] = UNSET
    usd: Optional[str] = UNSET


class ConvertedVolume4Dict(TypedDict):
    btc: NotRequired[str]
    eth: NotRequired[str]
    usd: NotRequired[str]
