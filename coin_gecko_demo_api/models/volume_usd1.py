from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VolumeUsd1(SdkBaseModel):
    """Volume in USD"""

    h24: Optional[str] = UNSET


class VolumeUsd1Dict(TypedDict):
    h24: NotRequired[str]
