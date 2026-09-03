from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .converted_last4 import ConvertedLast4, ConvertedLast4Dict
from .converted_volume4 import ConvertedVolume4, ConvertedVolume4Dict


class Ticker4(SdkBaseModel):
    symbol: str
    """Derivative ticker symbol"""

    base: str
    """Derivative base asset"""

    target: str
    """Derivative target asset"""

    coin_id: str
    """Derivative base asset coin ID"""

    target_coin_id: str
    """Derivative target asset coin ID"""

    trade_url: str
    """Derivative trade URL"""

    contract_type: str
    """Derivative contract type"""

    last: float
    """Derivative last price"""

    h24_percentage_change: float
    """Derivative price percentage change in 24 hours"""

    index: float
    """Derivative underlying asset price"""

    index_basis_percentage: float
    """Difference of derivative price and index price in percentage"""

    bid_ask_spread: float
    """Derivative bid-ask spread"""

    funding_rate: float
    """Derivative funding rate"""

    open_interest_usd: float
    """Derivative open interest in USD"""

    h24_volume: float
    """Derivative volume in 24 hours"""

    converted_volume: ConvertedVolume4
    """Derivative converted volume"""

    converted_last: ConvertedLast4
    """Derivative converted last price"""

    last_traded: float
    """Derivative last traded time in UNIX timestamp"""

    expired_at: float | None
    """Derivative expiry time in UNIX timestamp"""


class Ticker4Dict(TypedDict):
    symbol: str
    base: str
    target: str
    coin_id: str
    target_coin_id: str
    trade_url: str
    contract_type: str
    last: float
    h24_percentage_change: float
    index: float
    index_basis_percentage: float
    bid_ask_spread: float
    funding_rate: float
    open_interest_usd: float
    h24_volume: float
    converted_volume: ConvertedVolume4 | ConvertedVolume4Dict
    converted_last: ConvertedLast4 | ConvertedLast4Dict
    last_traded: float
    expired_at: float | None
