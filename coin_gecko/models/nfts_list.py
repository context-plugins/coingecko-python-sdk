from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NftsList(SdkBaseModel):
    id: str
    """NFT collection ID"""

    contract_address: str
    """NFT collection contract address"""

    name: str
    """NFT collection name"""

    asset_platform_id: str
    """NFT collection asset platform ID"""

    symbol: str
    """NFT collection symbol"""


class NftsListDict(TypedDict):
    id: str
    contract_address: str
    name: str
    asset_platform_id: str
    symbol: str
