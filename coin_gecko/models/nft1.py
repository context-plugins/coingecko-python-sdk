from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data3 import Data3, Data3Dict


class Nft1(SdkBaseModel):
    id: str
    """NFT collection ID"""

    name: str
    """NFT collection name"""

    symbol: str
    """NFT collection symbol"""

    thumb: str
    """NFT collection thumb image URL"""

    nft_contract_id: int
    """NFT contract internal ID"""

    native_currency_symbol: str
    """NFT collection native currency symbol"""

    floor_price_in_native_currency: float
    """NFT collection floor price in native currency"""

    floor_price_24h_percentage_change: float
    """NFT collection floor price 24 hours percentage change"""

    data: Data3


class Nft1Dict(TypedDict):
    id: str
    name: str
    symbol: str
    thumb: str
    nft_contract_id: int
    native_currency_symbol: str
    floor_price_in_native_currency: float
    floor_price_24h_percentage_change: float
    data: Data3 | Data3Dict
