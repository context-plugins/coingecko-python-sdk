from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CategoriesList(SdkBaseModel):
    category_id: str
    """Category ID"""

    name: str
    """Category name"""


class CategoriesListDict(TypedDict):
    category_id: str
    name: str
