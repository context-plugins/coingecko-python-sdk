from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Market3(SdkBaseModel):
    """Exchange information"""

    name: Optional[str] = UNSET
    """Exchange name"""

    identifier: Optional[str] = UNSET
    """Exchange identifier"""

    has_trading_incentive: Optional[bool] = UNSET
    """Exchange trading incentive"""


class Market3Dict(TypedDict):
    name: NotRequired[str]
    identifier: NotRequired[str]
    has_trading_incentive: NotRequired[bool]
