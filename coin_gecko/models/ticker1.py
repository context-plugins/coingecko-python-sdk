from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .converted_last1 import ConvertedLast1, ConvertedLast1Dict
from .converted_volume1 import ConvertedVolume1, ConvertedVolume1Dict
from .market1 import Market1, Market1Dict


class Ticker1(SdkBaseModel):
    base: Optional[str] = UNSET
    """Ticker base currency"""

    target: Optional[str] = UNSET
    """Ticker target currency"""

    market: Optional[Market1] = UNSET
    """Ticker exchange"""

    last: Optional[float] = UNSET
    """Ticker last price"""

    volume: Optional[float] = UNSET
    """Ticker volume"""

    converted_last: Optional[ConvertedLast1] = UNSET
    """Ticker converted last price"""

    converted_volume: Optional[ConvertedVolume1] = UNSET
    """Ticker converted volume"""

    trust_score: OptionalNullable[str] = UNSET
    """Ticker trust score"""

    bid_ask_spread_percentage: Optional[float] = UNSET
    """Ticker bid-ask spread percentage"""

    timestamp: Optional[str] = UNSET
    """Ticker timestamp"""

    last_traded_at: Optional[str] = UNSET
    """Ticker last traded timestamp"""

    last_fetch_at: Optional[str] = UNSET
    """Ticker last fetch timestamp"""

    is_anomaly: Optional[bool] = UNSET
    """Ticker anomaly"""

    is_stale: Optional[bool] = UNSET
    """Ticker stale"""

    trade_url: Optional[str] = UNSET
    """Ticker trade URL"""

    token_info_url: OptionalNullable[str] = UNSET
    """Ticker token info URL"""

    coin_id: Optional[str] = UNSET
    """Ticker base currency coin ID"""

    target_coin_id: Optional[str] = UNSET
    """Ticker target currency coin ID"""

    coin_mcap_usd: Optional[float] = UNSET
    """Market cap in USD"""


class Ticker1Dict(TypedDict):
    base: NotRequired[str]
    target: NotRequired[str]
    market: NotRequired[Market1 | Market1Dict]
    last: NotRequired[float]
    volume: NotRequired[float]
    converted_last: NotRequired[ConvertedLast1 | ConvertedLast1Dict]
    converted_volume: NotRequired[ConvertedVolume1 | ConvertedVolume1Dict]
    trust_score: NotRequired[str | None]
    bid_ask_spread_percentage: NotRequired[float]
    timestamp: NotRequired[str]
    last_traded_at: NotRequired[str]
    last_fetch_at: NotRequired[str]
    is_anomaly: NotRequired[bool]
    is_stale: NotRequired[bool]
    trade_url: NotRequired[str]
    token_info_url: NotRequired[str | None]
    coin_id: NotRequired[str]
    target_coin_id: NotRequired[str]
    coin_mcap_usd: NotRequired[float]
