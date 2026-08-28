from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes3 import Attributes3, Attributes3Dict


class Data8(SdkBaseModel):
    id: str
    """Trade identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes3


class Data8Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes3 | Attributes3Dict
