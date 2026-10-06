from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Attributes13(SdkBaseModel):
    address: Optional[str] = UNSET
    name: Optional[str] = UNSET
    symbol: Optional[str] = UNSET
    decimals: Optional[int] = UNSET
    image_url: OptionalNullable[str] = UNSET
    coingecko_coin_id: OptionalNullable[str] = UNSET
    coingecko_asset_platform_id: Optional[str] = UNSET


class Attributes13Dict(TypedDict):
    address: NotRequired[str]
    name: NotRequired[str]
    symbol: NotRequired[str]
    decimals: NotRequired[int]
    image_url: NotRequired[str | None]
    coingecko_coin_id: NotRequired[str | None]
    coingecko_asset_platform_id: NotRequired[str]
