from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HoldingAmountChange(SdkBaseModel):
    """Holding amount changes over different timeframes"""

    d7: Optional[float] = Field(default=UNSET, alias="7d")
    d14: Optional[float] = Field(default=UNSET, alias="14d")
    d30: Optional[float] = Field(default=UNSET, alias="30d")
    d90: Optional[float] = Field(default=UNSET, alias="90d")
    y1: Optional[float] = Field(default=UNSET, alias="1y")
    ytd: Optional[float] = UNSET


class HoldingAmountChangeDict(TypedDict):
    d7: NotRequired[float]
    d14: NotRequired[float]
    d30: NotRequired[float]
    d90: NotRequired[float]
    y1: NotRequired[float]
    ytd: NotRequired[float]
