from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category2 import Category2, Category2Dict
from .coin1 import Coin1, Coin1Dict
from .nft1 import Nft1, Nft1Dict


class TrendingSearch(SdkBaseModel):
    coins: list[Coin1]
    nfts: list[Nft1]
    categories: list[Category2]


class TrendingSearchDict(TypedDict):
    coins: list[Coin1 | Coin1Dict]
    nfts: list[Nft1 | Nft1Dict]
    categories: list[Category2 | Category2Dict]
