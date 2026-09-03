from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .roi import Roi, RoiDict


class MarketData1(SdkBaseModel):
    """Market data"""

    current_price: Optional[dict[str, float]] = UNSET
    """Current price in target currency"""

    total_value_locked: OptionalNullable[float] = UNSET
    """Total value locked"""

    mcap_to_tvl_ratio: OptionalNullable[float] = UNSET
    """Market cap to TVL ratio"""

    fdv_to_tvl_ratio: OptionalNullable[float] = UNSET
    """FDV to TVL ratio"""

    roi: OptionalNullable[Roi] = UNSET
    """Return on investment"""

    ath: Optional[dict[str, float]] = UNSET
    """All-time high in target currency"""

    ath_change_percentage: Optional[dict[str, float]] = UNSET
    """All-time high change percentage"""

    ath_date: Optional[dict[str, str]] = UNSET
    """All-time high date"""

    atl: Optional[dict[str, float]] = UNSET
    """All-time low in target currency"""

    atl_change_percentage: Optional[dict[str, float]] = UNSET
    """All-time low change percentage"""

    atl_date: Optional[dict[str, str]] = UNSET
    """All-time low date"""

    market_cap: Optional[dict[str, float]] = UNSET
    """Market cap in target currency"""

    fully_diluted_valuation: Optional[dict[str, float]] = UNSET
    """Fully diluted valuation in target currency"""

    market_cap_fdv_ratio: Optional[float] = UNSET
    """Market cap to FDV ratio"""

    market_cap_rank: OptionalNullable[int] = UNSET
    """Market cap rank"""

    outstanding_token_value_usd: OptionalNullable[float] = UNSET
    """Outstanding token value in USD"""

    market_cap_rank_with_rehypothecated: OptionalNullable[int] = UNSET
    """Market cap rank including rehypothecated tokens"""

    total_volume: Optional[dict[str, float]] = UNSET
    """Total trading volume in target currency"""

    high_24h: Optional[dict[str, float]] = UNSET
    """24h price high in target currency"""

    low_24h: Optional[dict[str, float]] = UNSET
    """24h price low in target currency"""

    price_change_24h: Optional[float] = UNSET
    """24h price change in target currency"""

    price_change_percentage_24h: Optional[float] = UNSET
    """24h price change percentage"""

    price_change_percentage_7d: Optional[float] = UNSET
    """7d price change percentage"""

    price_change_percentage_14d: Optional[float] = UNSET
    """14d price change percentage"""

    price_change_percentage_30d: Optional[float] = UNSET
    """30d price change percentage"""

    price_change_percentage_60d: Optional[float] = UNSET
    """60d price change percentage"""

    price_change_percentage_200d: Optional[float] = UNSET
    """200d price change percentage"""

    price_change_percentage_1y: Optional[float] = UNSET
    """1y price change percentage"""

    market_cap_change_24h: Optional[float] = UNSET
    """24h market cap change in target currency"""

    market_cap_change_percentage_24h: Optional[float] = UNSET
    """24h market cap change percentage"""

    price_change_24h_in_currency: Optional[dict[str, float]] = UNSET
    """24h price change in target currency"""

    price_change_percentage_1h_in_currency: Optional[dict[str, float]] = UNSET
    """1h price change percentage per currency"""

    price_change_percentage_24h_in_currency: Optional[dict[str, float]] = UNSET
    """24h price change percentage per currency"""

    price_change_percentage_7d_in_currency: Optional[dict[str, float]] = UNSET
    """7d price change percentage per currency"""

    price_change_percentage_14d_in_currency: Optional[dict[str, float]] = UNSET
    """14d price change percentage per currency"""

    price_change_percentage_30d_in_currency: Optional[dict[str, float]] = UNSET
    """30d price change percentage per currency"""

    price_change_percentage_60d_in_currency: Optional[dict[str, float]] = UNSET
    """60d price change percentage per currency"""

    price_change_percentage_200d_in_currency: Optional[dict[str, float]] = UNSET
    """200d price change percentage per currency"""

    price_change_percentage_1y_in_currency: Optional[dict[str, float]] = UNSET
    """1y price change percentage per currency"""

    market_cap_change_24h_in_currency: Optional[dict[str, float]] = UNSET
    """24h market cap change in target currency"""

    market_cap_change_percentage_24h_in_currency: Optional[dict[str, float]] = UNSET
    """24h market cap change percentage per currency"""

    total_supply: Optional[float] = UNSET
    """Total supply"""

    max_supply: OptionalNullable[float] = UNSET
    """Max supply"""

    max_supply_infinite: Optional[bool] = UNSET
    """Max supply infinite"""

    circulating_supply: Optional[float] = UNSET
    """Circulating supply"""

    outstanding_supply: OptionalNullable[float] = UNSET
    """Tokens outstanding in the market"""

    last_updated: Optional[str] = UNSET
    """Market data last updated timestamp"""

    sparkline_7d: Optional[list[float]] = UNSET
    """Sparkline 7-day price data"""


class MarketData1Dict(TypedDict):
    current_price: NotRequired[dict[str, float]]
    total_value_locked: NotRequired[float | None]
    mcap_to_tvl_ratio: NotRequired[float | None]
    fdv_to_tvl_ratio: NotRequired[float | None]
    roi: NotRequired[Roi | RoiDict | None]
    ath: NotRequired[dict[str, float]]
    ath_change_percentage: NotRequired[dict[str, float]]
    ath_date: NotRequired[dict[str, str]]
    atl: NotRequired[dict[str, float]]
    atl_change_percentage: NotRequired[dict[str, float]]
    atl_date: NotRequired[dict[str, str]]
    market_cap: NotRequired[dict[str, float]]
    fully_diluted_valuation: NotRequired[dict[str, float]]
    market_cap_fdv_ratio: NotRequired[float]
    market_cap_rank: NotRequired[int | None]
    outstanding_token_value_usd: NotRequired[float | None]
    market_cap_rank_with_rehypothecated: NotRequired[int | None]
    total_volume: NotRequired[dict[str, float]]
    high_24h: NotRequired[dict[str, float]]
    low_24h: NotRequired[dict[str, float]]
    price_change_24h: NotRequired[float]
    price_change_percentage_24h: NotRequired[float]
    price_change_percentage_7d: NotRequired[float]
    price_change_percentage_14d: NotRequired[float]
    price_change_percentage_30d: NotRequired[float]
    price_change_percentage_60d: NotRequired[float]
    price_change_percentage_200d: NotRequired[float]
    price_change_percentage_1y: NotRequired[float]
    market_cap_change_24h: NotRequired[float]
    market_cap_change_percentage_24h: NotRequired[float]
    price_change_24h_in_currency: NotRequired[dict[str, float]]
    price_change_percentage_1h_in_currency: NotRequired[dict[str, float]]
    price_change_percentage_24h_in_currency: NotRequired[dict[str, float]]
    price_change_percentage_7d_in_currency: NotRequired[dict[str, float]]
    price_change_percentage_14d_in_currency: NotRequired[dict[str, float]]
    price_change_percentage_30d_in_currency: NotRequired[dict[str, float]]
    price_change_percentage_60d_in_currency: NotRequired[dict[str, float]]
    price_change_percentage_200d_in_currency: NotRequired[dict[str, float]]
    price_change_percentage_1y_in_currency: NotRequired[dict[str, float]]
    market_cap_change_24h_in_currency: NotRequired[dict[str, float]]
    market_cap_change_percentage_24h_in_currency: NotRequired[dict[str, float]]
    total_supply: NotRequired[float]
    max_supply: NotRequired[float | None]
    max_supply_infinite: NotRequired[bool]
    circulating_supply: NotRequired[float]
    outstanding_supply: NotRequired[float | None]
    last_updated: NotRequired[str]
    sparkline_7d: NotRequired[list[float]]
