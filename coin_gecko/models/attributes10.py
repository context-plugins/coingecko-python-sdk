from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .price_change_percentage1 import PriceChangePercentage1, PriceChangePercentage1Dict
from .transactions1 import Transactions1, Transactions1Dict
from .volume_usd2 import VolumeUsd2, VolumeUsd2Dict


class Attributes10(SdkBaseModel):
    base_token_price_usd: Optional[str] = UNSET
    base_token_price_native_currency: Optional[str] = UNSET
    quote_token_price_usd: Optional[str] = UNSET
    quote_token_price_native_currency: Optional[str] = UNSET
    base_token_price_quote_token: Optional[str] = UNSET
    quote_token_price_base_token: Optional[str] = UNSET
    address: Optional[str] = UNSET
    name: Optional[str] = UNSET
    pool_created_at: Optional[str] = UNSET
    fdv_usd: OptionalNullable[str] = UNSET
    market_cap_usd: OptionalNullable[str] = UNSET
    price_change_percentage: Optional[PriceChangePercentage1] = UNSET
    transactions: Optional[Transactions1] = UNSET
    volume_usd: Optional[VolumeUsd2] = UNSET
    reserve_in_usd: Optional[str] = UNSET


class Attributes10Dict(TypedDict):
    base_token_price_usd: NotRequired[str]
    base_token_price_native_currency: NotRequired[str]
    quote_token_price_usd: NotRequired[str]
    quote_token_price_native_currency: NotRequired[str]
    base_token_price_quote_token: NotRequired[str]
    quote_token_price_base_token: NotRequired[str]
    address: NotRequired[str]
    name: NotRequired[str]
    pool_created_at: NotRequired[str]
    fdv_usd: NotRequired[str | None]
    market_cap_usd: NotRequired[str | None]
    price_change_percentage: NotRequired[PriceChangePercentage1 | PriceChangePercentage1Dict]
    transactions: NotRequired[Transactions1 | Transactions1Dict]
    volume_usd: NotRequired[VolumeUsd2 | VolumeUsd2Dict]
    reserve_in_usd: NotRequired[str]
