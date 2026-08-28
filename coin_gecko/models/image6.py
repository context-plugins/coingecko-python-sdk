from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Image6(SdkBaseModel):
    """Token image URLs in different sizes"""

    thumb: Optional[str] = UNSET
    small: Optional[str] = UNSET
    large: Optional[str] = UNSET


class Image6Dict(TypedDict):
    thumb: NotRequired[str]
    small: NotRequired[str]
    large: NotRequired[str]
