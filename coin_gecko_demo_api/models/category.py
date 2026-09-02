from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Category(SdkBaseModel):
    id: str
    """Category ID"""

    name: str
    """Category name"""


class CategoryDict(TypedDict):
    id: str
    name: str
