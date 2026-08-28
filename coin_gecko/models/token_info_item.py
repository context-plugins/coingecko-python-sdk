from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes7 import Attributes7, Attributes7Dict


class TokenInfoItem(SdkBaseModel):
    id: str
    """Token identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes7


class TokenInfoItemDict(TypedDict):
    id: str
    type_: str
    attributes: Attributes7 | Attributes7Dict
