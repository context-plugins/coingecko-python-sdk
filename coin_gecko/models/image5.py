from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Image5(SdkBaseModel):
    """NFT collection image URLs"""

    small: Optional[str] = UNSET
    small_2x: Optional[str] = UNSET


class Image5Dict(TypedDict):
    small: NotRequired[str]
    small_2x: NotRequired[str]
