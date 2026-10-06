from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Data5(SdkBaseModel):
    id: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")


class Data5Dict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[str]
