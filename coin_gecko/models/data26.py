from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes14 import Attributes14, Attributes14Dict
from .relationships6 import Relationships6, Relationships6Dict


class Data26(SdkBaseModel):
    id: str
    """Pool identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes14
    relationships: Relationships6
    """Related resources"""


class Data26Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes14 | Attributes14Dict
    relationships: Relationships6 | Relationships6Dict
