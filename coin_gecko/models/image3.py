from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Image3(SdkBaseModel):
    """Asset platform image URLs"""

    thumb: Optional[str] = UNSET
    """Thumbnail image URL"""

    small: Optional[str] = UNSET
    """Small image URL"""

    large: Optional[str] = UNSET
    """Large image URL"""


class Image3Dict(TypedDict):
    thumb: NotRequired[str]
    small: NotRequired[str]
    large: NotRequired[str]
