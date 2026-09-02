from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes9 import Attributes9, Attributes9Dict
from .relationships3 import Relationships3, Relationships3Dict


class TokenItem(SdkBaseModel):
    id: str
    """Token identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes9
    relationships: Relationships3


class TokenItemDict(TypedDict):
    id: str
    type_: str
    attributes: Attributes9 | Attributes9Dict
    relationships: Relationships3 | Relationships3Dict
