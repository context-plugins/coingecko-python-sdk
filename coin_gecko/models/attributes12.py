from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price_change_percentage import PriceChangePercentage, PriceChangePercentageDict
from .transactions import Transactions, TransactionsDict
from .volume_usd import VolumeUsd, VolumeUsdDict


class Attributes12(SdkBaseModel):
    base_token_price_usd: str
    """Base token price in USD"""

    base_token_price_native_currency: str | None
    """Base token price in native currency"""

    quote_token_price_usd: str
    """Quote token price in USD"""

    quote_token_price_native_currency: str | None
    """Quote token price in native currency"""

    base_token_price_quote_token: str | None
    """Base token price in quote token"""

    quote_token_price_base_token: str | None
    """Quote token price in base token"""

    address: str
    """Pool contract address"""

    name: str
    """Pool name"""

    pool_created_at: str
    """Pool creation timestamp"""

    fdv_usd: str | None
    """Fully diluted valuation in USD"""

    market_cap_usd: str | None
    """Market cap in USD"""

    price_change_percentage: PriceChangePercentage
    """Price change percentage over various timeframes"""

    transactions: Transactions
    """Transaction counts over various timeframes"""

    volume_usd: VolumeUsd
    """Volume in USD over various timeframes"""

    reserve_in_usd: str | None
    """Total reserve in USD"""

    token_price_usd: Optional[str] = UNSET
    """Price of the queried token in USD, present when querying pools by token address"""

    sentiment_vote_positive_percentage: Optional[float] = UNSET
    """GeckoTerminal community positive sentiment vote percentage"""

    sentiment_vote_negative_percentage: Optional[float] = UNSET
    """GeckoTerminal community negative sentiment vote percentage"""

    community_sus_report: Optional[int] = UNSET
    """GeckoTerminal community suspicious reports count"""


class Attributes12Dict(TypedDict):
    base_token_price_usd: str
    base_token_price_native_currency: str | None
    quote_token_price_usd: str
    quote_token_price_native_currency: str | None
    base_token_price_quote_token: str | None
    quote_token_price_base_token: str | None
    address: str
    name: str
    pool_created_at: str
    fdv_usd: str | None
    market_cap_usd: str | None
    price_change_percentage: PriceChangePercentage | PriceChangePercentageDict
    transactions: Transactions | TransactionsDict
    volume_usd: VolumeUsd | VolumeUsdDict
    reserve_in_usd: str | None
    token_price_usd: NotRequired[str]
    sentiment_vote_positive_percentage: NotRequired[float]
    sentiment_vote_negative_percentage: NotRequired[float]
    community_sus_report: NotRequired[int]
