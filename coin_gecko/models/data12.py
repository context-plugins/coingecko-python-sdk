from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes7 import Attributes7, Attributes7Dict
from .relationships2 import Relationships2, Relationships2Dict


class Data12(SdkBaseModel):
    id: str
    """Token identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes7
    relationships: Relationships2


class Data12Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes7 | Attributes7Dict
    relationships: Relationships2 | Relationships2Dict
