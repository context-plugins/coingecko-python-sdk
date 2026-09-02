from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ticker import Ticker, TickerDict


class CoinsIdTickers(SdkBaseModel):
    name: str
    """Coin name"""

    tickers: list[Ticker]
    """List of tickers"""


class CoinsIdTickersDict(TypedDict):
    name: str
    tickers: list[Ticker | TickerDict]
