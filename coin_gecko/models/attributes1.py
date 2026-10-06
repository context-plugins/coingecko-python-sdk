from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Attributes1(SdkBaseModel):
    address: Optional[str] = UNSET
    name: Optional[str] = UNSET
    symbol: Optional[str] = UNSET
    decimals: Optional[int] = UNSET
    image_url: Optional[str] = UNSET
    coingecko_coin_id: Optional[str] = UNSET


class Attributes1Dict(TypedDict):
    address: NotRequired[str]
    name: NotRequired[str]
    symbol: NotRequired[str]
    decimals: NotRequired[int]
    image_url: NotRequired[str]
    coingecko_coin_id: NotRequired[str]
