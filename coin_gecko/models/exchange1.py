from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Exchange1(SdkBaseModel):
    id: str
    """Exchange ID"""

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

    has_trading_incentive: bool
    """Whether the exchange has trading incentive"""

    trust_score: float | None
    """Exchange trust score"""

    trust_score_rank: float | None
    """Exchange trust score rank"""

    trade_volume_24h_btc: float
    """Exchange 24h trading volume in BTC"""


class Exchange1Dict(TypedDict):
    id: str
    name: str
    year_established: float | None
    country: str | None
    description: str
    url: str
    image: str
    has_trading_incentive: bool
    trust_score: float | None
    trust_score_rank: float | None
    trade_volume_24h_btc: float
