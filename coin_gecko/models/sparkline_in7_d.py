from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SparklineIn7D(SdkBaseModel):
    """Sparkline price data for the last 7 days"""

    price: Optional[list[float]] = UNSET
    """Array of price values"""


class SparklineIn7DDict(TypedDict):
    price: NotRequired[list[float]]
