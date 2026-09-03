from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellVolumeUsd(SdkBaseModel):
    """Sell volume in USD over various timeframes"""

    m5: Optional[str] = UNSET
    m15: Optional[str] = UNSET
    m30: Optional[str] = UNSET
    h1: Optional[str] = UNSET
    h6: Optional[str] = UNSET
    h24: Optional[str] = UNSET


class SellVolumeUsdDict(TypedDict):
    m5: NotRequired[str]
    m15: NotRequired[str]
    m30: NotRequired[str]
    h1: NotRequired[str]
    h6: NotRequired[str]
    h24: NotRequired[str]
