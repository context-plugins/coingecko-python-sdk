from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buy_volume_usd import BuyVolumeUsd, BuyVolumeUsdDict
from .net_buy_volume_usd import NetBuyVolumeUsd, NetBuyVolumeUsdDict
from .price_change_percentage import PriceChangePercentage, PriceChangePercentageDict
from .sell_volume_usd import SellVolumeUsd, SellVolumeUsdDict
from .transactions import Transactions, TransactionsDict
from .volume_usd import VolumeUsd, VolumeUsdDict


class Attributes(SdkBaseModel):
    base_token_price_usd: str
    """Base token price in USD"""

    base_token_price_native_currency: str
    """Base token price in native currency"""

    base_token_balance: Optional[str] = UNSET
    """Base token balance in pool"""

    base_token_liquidity_usd: Optional[str] = UNSET
    """Base token liquidity in USD"""

    quote_token_price_usd: str
    """Quote token price in USD"""

    quote_token_price_native_currency: str
    """Quote token price in native currency"""

    quote_token_balance: Optional[str] = UNSET
    """Quote token balance in pool"""

    quote_token_liquidity_usd: Optional[str] = UNSET
    """Quote token liquidity in USD"""

    base_token_price_quote_token: str
    """Base token price in quote token"""

    quote_token_price_base_token: str
    """Quote token price in base token"""

    address: str
    """Pool contract address"""

    name: str
    """Pool name with fee tier"""

    pool_name: str
    """Pool name without fee tier"""

    pool_fee_percentage: str
    """Pool fee percentage"""

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

    net_buy_volume_usd: Optional[NetBuyVolumeUsd] = UNSET
    """Net buy volume in USD over various timeframes"""

    buy_volume_usd: Optional[BuyVolumeUsd] = UNSET
    """Buy volume in USD over various timeframes"""

    sell_volume_usd: Optional[SellVolumeUsd] = UNSET
    """Sell volume in USD over various timeframes"""

    reserve_in_usd: str
    """Total reserve in USD"""

    locked_liquidity_percentage: str
    """Locked liquidity percentage"""


class AttributesDict(TypedDict):
    base_token_price_usd: str
    base_token_price_native_currency: str
    base_token_balance: NotRequired[str]
    base_token_liquidity_usd: NotRequired[str]
    quote_token_price_usd: str
    quote_token_price_native_currency: str
    quote_token_balance: NotRequired[str]
    quote_token_liquidity_usd: NotRequired[str]
    base_token_price_quote_token: str
    quote_token_price_base_token: str
    address: str
    name: str
    pool_name: str
    pool_fee_percentage: str
    pool_created_at: str
    fdv_usd: str | None
    market_cap_usd: str | None
    price_change_percentage: PriceChangePercentage | PriceChangePercentageDict
    transactions: Transactions | TransactionsDict
    volume_usd: VolumeUsd | VolumeUsdDict
    net_buy_volume_usd: NotRequired[NetBuyVolumeUsd | NetBuyVolumeUsdDict]
    buy_volume_usd: NotRequired[BuyVolumeUsd | BuyVolumeUsdDict]
    sell_volume_usd: NotRequired[SellVolumeUsd | SellVolumeUsdDict]
    reserve_in_usd: str
    locked_liquidity_percentage: str
