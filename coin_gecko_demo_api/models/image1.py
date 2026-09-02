from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Image1(SdkBaseModel):
    """Coin image URL"""

    thumb: Optional[str] = UNSET
    small: Optional[str] = UNSET
    large: Optional[str] = UNSET


class Image1Dict(TypedDict):
    thumb: NotRequired[str]
    small: NotRequired[str]
    large: NotRequired[str]
