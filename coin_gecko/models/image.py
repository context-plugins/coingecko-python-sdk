from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Image(SdkBaseModel):
    """Coin image URLs"""

    thumb: Optional[str] = UNSET
    """Thumbnail image URL"""

    small: Optional[str] = UNSET
    """Small image URL"""


class ImageDict(TypedDict):
    thumb: NotRequired[str]
    small: NotRequired[str]
