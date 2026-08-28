from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data4 import Data4, Data4Dict


class Category2(SdkBaseModel):
    id: int
    """Category ID"""

    name: str
    """Category name"""

    top_3_coins_images: list[str]
    """Top 3 coins image URLs in the category"""

    market_cap_1h_change: float
    """Category market cap 1 hour change"""

    slug: str
    """Category web slug"""

    coins_count: str
    """Number of coins in the category"""

    data: Data4


class Category2Dict(TypedDict):
    id: int
    name: str
    top_3_coins_images: list[str]
    market_cap_1h_change: float
    slug: str
    coins_count: str
    data: Data4 | Data4Dict
