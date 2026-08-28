from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .status_update2 import StatusUpdate2, StatusUpdate2Dict
from .ticker3 import Ticker3, Ticker3Dict


class ExchangesId(SdkBaseModel):
    name: str
    """Exchange name"""

    year_established: float | None
    """Year the exchange was established"""

    country: str | None
    """Country where the exchange is based"""

    description: str
    """Exchange description"""

    url: str
    """Exchange website URL"""

    image: str
    """Exchange logo URL"""

    facebook_url: str
    """Facebook URL"""

    reddit_url: str
    """Reddit URL"""

    telegram_url: str
    """Telegram URL"""

    slack_url: str
    """Slack URL"""

    other_url_1: str
    """Other URL 1"""

    other_url_2: str
    """Other URL 2"""

    twitter_handle: str
    """Twitter handle"""

    has_trading_incentive: bool
    """Whether the exchange has trading incentive"""

    centralized: bool
    """Whether the exchange is centralized"""

    public_notice: str
    """Public notice"""

    alert_notice: str
    """Alert notice"""

    trust_score: float | None
    """Exchange trust score"""

    trust_score_rank: float | None
    """Exchange trust score rank"""

    coins: float
    """Number of coins listed"""

    pairs: float
    """Number of trading pairs"""

    trade_volume_24h_btc: float
    """Exchange 24h trading volume in BTC"""

    tickers: list[Ticker3]
    """Exchange tickers"""

    status_updates: list[StatusUpdate2]
    """Status updates"""


class ExchangesIdDict(TypedDict):
    name: str
    year_established: float | None
    country: str | None
    description: str
    url: str
    image: str
    facebook_url: str
    reddit_url: str
    telegram_url: str
    slack_url: str
    other_url_1: str
    other_url_2: str
    twitter_handle: str
    has_trading_incentive: bool
    centralized: bool
    public_notice: str
    alert_notice: str
    trust_score: float | None
    trust_score_rank: float | None
    coins: float
    pairs: float
    trade_volume_24h_btc: float
    tickers: list[Ticker3 | Ticker3Dict]
    status_updates: list[StatusUpdate2 | StatusUpdate2Dict]
