from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes4 import Attributes4, Attributes4Dict


class Data9(SdkBaseModel):
    id: str
    """Request ID"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes4


class Data9Dict(TypedDict):
    id: str
    type_: str
    attributes: Attributes4 | Attributes4Dict
