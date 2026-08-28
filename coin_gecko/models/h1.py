from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class H1(SdkBaseModel):
    buys: Optional[int] = UNSET
    sells: Optional[int] = UNSET
    buyers: Optional[int] = UNSET
    sellers: Optional[int] = UNSET


class H1Dict(TypedDict):
    buys: NotRequired[int]
    sells: NotRequired[int]
    buyers: NotRequired[int]
    sellers: NotRequired[int]
