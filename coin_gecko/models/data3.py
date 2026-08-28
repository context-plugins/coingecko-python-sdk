from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .content import Content, ContentDict


class Data3(SdkBaseModel):
    floor_price: str
    """NFT collection floor price"""

    floor_price_in_usd_24h_percentage_change: str
    """NFT collection floor price in USD 24 hours percentage change"""

    h24_volume: str
    """NFT collection volume in 24 hours"""

    h24_average_sale_price: str
    """NFT collection 24 hours average sale price"""

    sparkline: str
    """NFT collection sparkline image URL"""

    content: Content | None


class Data3Dict(TypedDict):
    floor_price: str
    floor_price_in_usd_24h_percentage_change: str
    h24_volume: str
    h24_average_sale_price: str
    sparkline: str
    content: Content | ContentDict | None
