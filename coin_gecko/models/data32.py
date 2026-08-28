from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes17 import Attributes17, Attributes17Dict


class Data32(SdkBaseModel):
    id: str
    """DEX identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes17


class Data32Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes17 | Attributes17Dict
