from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Market1(SdkBaseModel):
    """Ticker exchange"""

    name: Optional[str] = UNSET
    """Exchange name"""

    identifier: Optional[str] = UNSET
    """Exchange identifier"""

    has_trading_incentive: Optional[bool] = UNSET
    """Exchange trading incentive"""


class Market1Dict(TypedDict):
    name: NotRequired[str]
    identifier: NotRequired[str]
    has_trading_incentive: NotRequired[bool]
