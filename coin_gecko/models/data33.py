from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes18 import Attributes18, Attributes18Dict


class Data33(SdkBaseModel):
    id: str
    """Network identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes18


class Data33Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes18 | Attributes18Dict
