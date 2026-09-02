from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .attributes8 import Attributes8, Attributes8Dict


class Included3(SdkBaseModel):
    id: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    attributes: Optional[Attributes8] = UNSET


class Included3Dict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[str]
    attributes: NotRequired[Attributes8 | Attributes8Dict]
