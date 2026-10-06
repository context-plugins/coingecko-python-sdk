from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Attributes6(SdkBaseModel):
    name: Optional[str] = UNSET
    coingecko_asset_platform_id: Optional[str] = UNSET


class Attributes6Dict(TypedDict):
    name: NotRequired[str]
    coingecko_asset_platform_id: NotRequired[str]
