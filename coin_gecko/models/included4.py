from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .attributes10 import Attributes10, Attributes10Dict
from .relationships4 import Relationships4, Relationships4Dict


class Included4(SdkBaseModel):
    id: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    attributes: Optional[Attributes10] = UNSET
    relationships: Optional[Relationships4] = UNSET


class Included4Dict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[str]
    attributes: NotRequired[Attributes10 | Attributes10Dict]
    relationships: NotRequired[Relationships4 | Relationships4Dict]
