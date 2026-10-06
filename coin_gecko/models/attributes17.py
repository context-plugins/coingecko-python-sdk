from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Attributes17(SdkBaseModel):
    name: str
    """DEX name"""


class Attributes17Dict(TypedDict):
    name: str
