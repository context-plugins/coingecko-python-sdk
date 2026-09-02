from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Category1(SdkBaseModel):
    id: str
    """Category ID"""

    name: str
    """Category name"""

    market_cap: float
    """Category market cap"""

    market_cap_change_24h: float
    """Category market cap change in 24 hours"""

    content: str
    """Category description"""

    top_3_coins_id: list[str]
    """IDs of top 3 coins in the category"""

    top_3_coins: list[str]
    """Image URLs of top 3 coins in the category"""

    volume_24h: float
    """Category trading volume in 24 hours"""

    updated_at: str
    """Category last updated timestamp"""


class Category1Dict(TypedDict):
    id: str
    name: str
    market_cap: float
    market_cap_change_24h: float
    content: str
    top_3_coins_id: list[str]
    top_3_coins: list[str]
    volume_24h: float
    updated_at: str
