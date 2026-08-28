from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .attributes11 import Attributes11, Attributes11Dict
from .relationships4 import Relationships4, Relationships4Dict


class Included5(SdkBaseModel):
    id: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    attributes: Optional[Attributes11] = UNSET
    relationships: Optional[Relationships4] = UNSET


class Included5Dict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[str]
    attributes: NotRequired[Attributes11 | Attributes11Dict]
    relationships: NotRequired[Relationships4 | Relationships4Dict]
