from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes12 import Attributes12, Attributes12Dict
from .relationships6 import Relationships6, Relationships6Dict


class Data21(SdkBaseModel):
    id: str
    """Pool identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes12
    relationships: Relationships6
    """Related resources"""


class Data21Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes12 | Attributes12Dict
    relationships: Relationships6 | Relationships6Dict
