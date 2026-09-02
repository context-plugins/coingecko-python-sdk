from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .converted_last import ConvertedLast, ConvertedLastDict
from .converted_volume import ConvertedVolume, ConvertedVolumeDict
from .market import Market, MarketDict


class Ticker(SdkBaseModel):
    base: str
    """Ticker base currency"""

    target: str
    """Ticker target currency"""

    market: Market
    """Exchange information"""

    last: float
    """Last price"""

    volume: float
    """Trading volume"""

    cost_to_move_up_usd: Optional[float] = UNSET
    """Cost to move price up by 2% in USD"""

    cost_to_move_down_usd: Optional[float] = UNSET
    """Cost to move price down by 2% in USD"""

    converted_last: ConvertedLast
    """Converted last price"""

    converted_volume: ConvertedVolume
    """Converted trading volume"""

    trust_score: str | None
    """Trust score"""

    bid_ask_spread_percentage: float
    """Bid-ask spread percentage"""

    timestamp: str
    """Ticker timestamp"""

    last_traded_at: str
    """Last traded timestamp"""

    last_fetch_at: str
    """Last fetch timestamp"""

    is_anomaly: bool
    """Whether ticker is anomalous"""

    is_stale: bool
    """Whether ticker is stale"""

    trade_url: str
    """Trade URL"""

    token_info_url: str | None
    """Token info URL"""

    coin_id: str
    """Base currency coin ID"""

    target_coin_id: str
    """Target currency coin ID"""

    coin_mcap_usd: float
    """Coin market cap in USD"""


class TickerDict(TypedDict):
    base: str
    target: str
    market: Market | MarketDict
    last: float
    volume: float
    cost_to_move_up_usd: NotRequired[float]
    cost_to_move_down_usd: NotRequired[float]
    converted_last: ConvertedLast | ConvertedLastDict
    converted_volume: ConvertedVolume | ConvertedVolumeDict
    trust_score: str | None
    bid_ask_spread_percentage: float
    timestamp: str
    last_traded_at: str
    last_fetch_at: str
    is_anomaly: bool
    is_stale: bool
    trade_url: str
    token_info_url: str | None
    coin_id: str
    target_coin_id: str
    coin_mcap_usd: float
