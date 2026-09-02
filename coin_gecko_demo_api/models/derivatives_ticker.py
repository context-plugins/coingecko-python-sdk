from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DerivativesTicker(SdkBaseModel):
    market: str
    """Derivative market name"""

    symbol: str
    """Derivative ticker symbol"""

    index_id: str
    """Derivative underlying asset"""

    price: str
    """Derivative ticker price"""

    price_percentage_change_24h: float
    """Derivative ticker price percentage change in 24 hours"""

    contract_type: str
    """Derivative contract type"""

    index: float
    """Derivative underlying asset price"""

    basis: float
    """Difference of derivative price and index price"""

    spread: float
    """Derivative bid-ask spread"""

    funding_rate: float
    """Derivative funding rate"""

    open_interest: float
    """Derivative open interest"""

    volume_24h: float
    """Derivative trading volume in 24 hours"""

    last_traded_at: float
    """Derivative last traded time in UNIX timestamp"""

    expired_at: float | None
    """Derivative expiry time in UNIX timestamp"""


class DerivativesTickerDict(TypedDict):
    market: str
    symbol: str
    index_id: str
    price: str
    price_percentage_change_24h: float
    contract_type: str
    index: float
    basis: float
    spread: float
    funding_rate: float
    open_interest: float
    volume_24h: float
    last_traded_at: float
    expired_at: float | None
