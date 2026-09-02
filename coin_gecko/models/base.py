from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Base(SdkBaseModel):
    """Base token metadata"""

    name: Optional[str] = UNSET
    symbol: Optional[str] = UNSET
    coingecko_coin_id: OptionalNullable[str] = UNSET
    address: Optional[str] = UNSET


class BaseDict(TypedDict):
    name: NotRequired[str]
    symbol: NotRequired[str]
    coingecko_coin_id: NotRequired[str | None]
    address: NotRequired[str]
