from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Nft(SdkBaseModel):
    id: str
    """NFT collection ID"""

    name: str
    """NFT collection name"""

    symbol: str
    """NFT collection symbol"""

    thumb: str
    """NFT collection thumb image URL"""


class NftDict(TypedDict):
    id: str
    name: str
    symbol: str
    thumb: str
