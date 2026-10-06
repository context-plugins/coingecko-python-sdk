from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Content(SdkBaseModel):
    title: Optional[str] = UNSET
    description: Optional[str] = UNSET


class ContentDict(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
