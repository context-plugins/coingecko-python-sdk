from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DetailPlatforms(SdkBaseModel):
    decimal_place: OptionalNullable[int] = UNSET
    """Token decimal place"""

    contract_address: Optional[str] = UNSET
    """Token contract address"""

    geckoterminal_url: Optional[str] = UNSET
    """GeckoTerminal URL"""


class DetailPlatformsDict(TypedDict):
    decimal_place: NotRequired[int | None]
    contract_address: NotRequired[str]
    geckoterminal_url: NotRequired[str]
