from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Roi(SdkBaseModel):
    """Return on investment"""

    times: Optional[float] = UNSET
    """ROI multiplier"""

    currency: Optional[str] = UNSET
    """ROI currency"""

    percentage: Optional[float] = UNSET
    """ROI percentage"""


class RoiDict(TypedDict):
    times: NotRequired[float]
    currency: NotRequired[str]
    percentage: NotRequired[float]
