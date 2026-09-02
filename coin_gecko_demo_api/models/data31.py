from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes16 import Attributes16, Attributes16Dict


class Data31(SdkBaseModel):
    id: str
    """Request ID"""

    type_: str = Field(alias="type")
    """Response type"""

    attributes: Attributes16


class Data31Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes16 | Attributes16Dict
