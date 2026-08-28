from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data2 import Data2, Data2Dict


class Item(SdkBaseModel):
    id: str
    """Coin ID"""

    coin_id: int
    """Coin internal ID"""

    name: str
    """Coin name"""

    symbol: str
    """Coin symbol"""

    market_cap_rank: int
    """Coin market cap rank"""

    thumb: str
    """Coin thumb image URL"""

    small: str
    """Coin small image URL"""

    large: str
    """Coin large image URL"""

    slug: str
    """Coin web slug"""

    price_btc: float
    """Coin price in BTC"""

    score: int
    """Coin trending rank (0-based)"""

    data: Data2


class ItemDict(TypedDict):
    id: str
    coin_id: int
    name: str
    symbol: str
    market_cap_rank: int
    thumb: str
    small: str
    large: str
    slug: str
    price_btc: float
    score: int
    data: Data2 | Data2Dict
