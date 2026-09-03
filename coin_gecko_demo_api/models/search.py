from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category import Category, CategoryDict
from .coin import Coin, CoinDict
from .exchange import Exchange, ExchangeDict
from .nft import Nft, NftDict


class Search(SdkBaseModel):
    coins: list[Coin]
    exchanges: list[Exchange]
    icos: list[Any]
    categories: list[Category]
    nfts: list[Nft]


class SearchDict(TypedDict):
    coins: list[Coin | CoinDict]
    exchanges: list[Exchange | ExchangeDict]
    icos: list[Any]
    categories: list[Category | CategoryDict]
    nfts: list[Nft | NftDict]
