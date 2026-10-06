from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DetailPlatforms1(SdkBaseModel):
    decimal_place: OptionalNullable[int] = UNSET
    """Token decimal place"""

    contract_address: Optional[str] = UNSET
    """Token contract address"""


class DetailPlatforms1Dict(TypedDict):
    decimal_place: NotRequired[int | None]
    contract_address: NotRequired[str]
