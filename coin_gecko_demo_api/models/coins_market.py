from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .roi2 import Roi2, Roi2Dict
from .sparkline_in7_d import SparklineIn7D, SparklineIn7DDict


class CoinsMarket(SdkBaseModel):
    id: str
    """Coin ID"""

    symbol: str
    """Coin symbol"""

    name: str
    """Coin name"""

    image: str
    """Coin image URL"""

    current_price: float | None
    """Current price in target currency"""

    market_cap: float | None
    """Market cap in target currency"""

    market_cap_rank: int | None
    """Market cap rank"""

    fully_diluted_valuation: float | None
    """Fully diluted valuation in target currency"""

    total_volume: float | None
    """Total trading volume in target currency"""

    high_24h: float | None
    """24-hour price high in target currency"""

    low_24h: float | None
    """24-hour price low in target currency"""

    price_change_24h: float | None
    """24-hour price change in target currency"""

    price_change_percentage_24h: float | None
    """24-hour price change percentage"""

    market_cap_change_24h: float | None
    """24-hour market cap change in target currency"""

    market_cap_change_percentage_24h: float | None
    """24-hour market cap change percentage"""

    circulating_supply: float | None
    """Circulating supply"""

    total_supply: float | None
    """Total supply"""

    max_supply: float | None
    """Max supply"""

    ath: float | None
    """All-time high price in target currency"""

    ath_change_percentage: float | None
    """All-time high change percentage"""

    ath_date: RFC3339DateTime | None
    """All-time high date"""

    atl: float | None
    """All-time low price in target currency"""

    atl_change_percentage: float | None
    """All-time low change percentage"""

    atl_date: RFC3339DateTime | None
    """All-time low date"""

    roi: Roi2 | None
    """Return on investment data"""

    last_updated: RFC3339DateTime
    """Last updated timestamp"""

    market_cap_rank_with_rehypothecated: OptionalNullable[int] = UNSET
    """Market cap rank including rehypothecated tokens"""

    sparkline_in_7d: Optional[SparklineIn7D] = UNSET
    """Sparkline price data for the last 7 days"""

    price_change_percentage_1h_in_currency: OptionalNullable[float] = UNSET
    """1-hour price change percentage in target currency"""

    price_change_percentage_24h_in_currency: OptionalNullable[float] = UNSET
    """24-hour price change percentage in target currency"""

    price_change_percentage_7d_in_currency: OptionalNullable[float] = UNSET
    """7-day price change percentage in target currency"""

    price_change_percentage_14d_in_currency: OptionalNullable[float] = UNSET
    """14-day price change percentage in target currency"""

    price_change_percentage_30d_in_currency: OptionalNullable[float] = UNSET
    """30-day price change percentage in target currency"""

    price_change_percentage_200d_in_currency: OptionalNullable[float] = UNSET
    """200-day price change percentage in target currency"""

    price_change_percentage_1y_in_currency: OptionalNullable[float] = UNSET
    """1-year price change percentage in target currency"""


class CoinsMarketDict(TypedDict):
    id: str
    symbol: str
    name: str
    image: str
    current_price: float | None
    market_cap: float | None
    market_cap_rank: int | None
    fully_diluted_valuation: float | None
    total_volume: float | None
    high_24h: float | None
    low_24h: float | None
    price_change_24h: float | None
    price_change_percentage_24h: float | None
    market_cap_change_24h: float | None
    market_cap_change_percentage_24h: float | None
    circulating_supply: float | None
    total_supply: float | None
    max_supply: float | None
    ath: float | None
    ath_change_percentage: float | None
    ath_date: RFC3339DateTime | None
    atl: float | None
    atl_change_percentage: float | None
    atl_date: RFC3339DateTime | None
    roi: Roi2 | Roi2Dict | None
    last_updated: RFC3339DateTime
    market_cap_rank_with_rehypothecated: NotRequired[int | None]
    sparkline_in_7d: NotRequired[SparklineIn7D | SparklineIn7DDict]
    price_change_percentage_1h_in_currency: NotRequired[float | None]
    price_change_percentage_24h_in_currency: NotRequired[float | None]
    price_change_percentage_7d_in_currency: NotRequired[float | None]
    price_change_percentage_14d_in_currency: NotRequired[float | None]
    price_change_percentage_30d_in_currency: NotRequired[float | None]
    price_change_percentage_200d_in_currency: NotRequired[float | None]
    price_change_percentage_1y_in_currency: NotRequired[float | None]
