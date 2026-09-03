from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes5 import Attributes5, Attributes5Dict
from .relationships1 import Relationships1, Relationships1Dict


class Data10(SdkBaseModel):
    id: str
    """Token identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes5
    relationships: Relationships1


class Data10Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes5 | Attributes5Dict
    relationships: Relationships1 | Relationships1Dict
