from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Explorer(SdkBaseModel):
    name: Optional[str] = UNSET
    link: Optional[str] = UNSET


class ExplorerDict(TypedDict):
    name: NotRequired[str]
    link: NotRequired[str]
