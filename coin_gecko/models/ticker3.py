from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .converted_last import ConvertedLast, ConvertedLastDict
from .converted_volume import ConvertedVolume, ConvertedVolumeDict
from .market3 import Market3, Market3Dict


class Ticker3(SdkBaseModel):
    base: Optional[str] = UNSET
    """Ticker base currency"""

    target: Optional[str] = UNSET
    """Ticker target currency"""

    market: Optional[Market3] = UNSET
    """Exchange information"""

    last: Optional[float] = UNSET
    """Last price"""

    volume: Optional[float] = UNSET
    """Trading volume"""

    converted_last: Optional[ConvertedLast] = UNSET
    """Converted last price"""

    converted_volume: Optional[ConvertedVolume] = UNSET
    """Converted trading volume"""

    trust_score: OptionalNullable[str] = UNSET
    """Trust score"""

    bid_ask_spread_percentage: Optional[float] = UNSET
    """Bid-ask spread percentage"""

    timestamp: Optional[str] = UNSET
    """Ticker timestamp"""

    last_traded_at: Optional[str] = UNSET
    """Last traded timestamp"""

    last_fetch_at: Optional[str] = UNSET
    """Last fetch timestamp"""

    is_anomaly: Optional[bool] = UNSET
    """Whether ticker is anomalous"""

    is_stale: Optional[bool] = UNSET
    """Whether ticker is stale"""

    trade_url: Optional[str] = UNSET
    """Trade URL"""

    token_info_url: OptionalNullable[str] = UNSET
    """Token info URL"""

    coin_id: Optional[str] = UNSET
    """Base currency coin ID"""

    target_coin_id: Optional[str] = UNSET
    """Target currency coin ID"""

    coin_mcap_usd: Optional[float] = UNSET
    """Coin market cap in USD"""


class Ticker3Dict(TypedDict):
    base: NotRequired[str]
    target: NotRequired[str]
    market: NotRequired[Market3 | Market3Dict]
    last: NotRequired[float]
    volume: NotRequired[float]
    converted_last: NotRequired[ConvertedLast | ConvertedLastDict]
    converted_volume: NotRequired[ConvertedVolume | ConvertedVolumeDict]
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
