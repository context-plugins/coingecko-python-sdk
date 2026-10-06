from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConvertedVolume(SdkBaseModel):
    """Converted trading volume"""

    btc: Optional[float] = UNSET
    eth: Optional[float] = UNSET
    usd: Optional[float] = UNSET


class ConvertedVolumeDict(TypedDict):
    btc: NotRequired[float]
    eth: NotRequired[float]
    usd: NotRequired[float]
