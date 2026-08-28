from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .h1 import H1, H1Dict
from .m5 import M5, M5Dict


class Transactions(SdkBaseModel):
    """Transaction counts over various timeframes"""

    m5: Optional[M5] = UNSET
    m15: Optional[M5] = UNSET
    m30: Optional[M5] = UNSET
    h1: Optional[H1] = UNSET
    h6: Optional[H1] = UNSET
    h24: Optional[H1] = UNSET


class TransactionsDict(TypedDict):
    m5: NotRequired[M5 | M5Dict]
    m15: NotRequired[M5 | M5Dict]
    m30: NotRequired[M5 | M5Dict]
    h1: NotRequired[H1 | H1Dict]
    h6: NotRequired[H1 | H1Dict]
    h24: NotRequired[H1 | H1Dict]
