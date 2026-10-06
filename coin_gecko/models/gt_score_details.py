from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GtScoreDetails(SdkBaseModel):
    """GeckoTerminal trust score breakdown"""

    pool: Optional[float] = UNSET
    transaction: Optional[float] = UNSET
    creation: Optional[float] = UNSET
    info: Optional[float] = UNSET
    holders: Optional[float] = UNSET


class GtScoreDetailsDict(TypedDict):
    pool: NotRequired[float]
    transaction: NotRequired[float]
    creation: NotRequired[float]
    info: NotRequired[float]
    holders: NotRequired[float]
