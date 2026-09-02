from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .attributes13 import Attributes13, Attributes13Dict


class Included6(SdkBaseModel):
    id: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    attributes: Optional[Attributes13] = UNSET


class Included6Dict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[str]
    attributes: NotRequired[Attributes13 | Attributes13Dict]
