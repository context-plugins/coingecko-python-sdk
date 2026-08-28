from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .attributes6 import Attributes6, Attributes6Dict


class Included2(SdkBaseModel):
    id: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    attributes: Optional[Attributes6] = UNSET


class Included2Dict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[str]
    attributes: NotRequired[Attributes6 | Attributes6Dict]
