from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .price_change_percentage import PriceChangePercentage, PriceChangePercentageDict
from .transactions import Transactions, TransactionsDict
from .volume_usd import VolumeUsd, VolumeUsdDict


class Attributes14(SdkBaseModel):
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


class Attributes14Dict(TypedDict):
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
