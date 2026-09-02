from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DerivativesExchange(SdkBaseModel):
    name: str
    """Derivatives exchange name"""

    id: str
    """Derivatives exchange ID"""

    open_interest_btc: float
    """Derivatives exchange open interest in BTC"""

    trade_volume_24h_btc: str
    """Derivatives exchange trade volume in BTC in 24 hours"""

    number_of_perpetual_pairs: int
    """Number of perpetual pairs in the derivatives exchange"""

    number_of_futures_pairs: int
    """Number of futures pairs in the derivatives exchange"""

    image: str
    """Derivatives exchange image URL"""

    year_established: int | None
    """Derivatives exchange established year"""

    country: str | None
    """Derivatives exchange incorporated country"""

    description: str
    """Derivatives exchange description"""

    url: str
    """Derivatives exchange website URL"""


class DerivativesExchangeDict(TypedDict):
    name: str
    id: str
    open_interest_btc: float
    trade_volume_24h_btc: str
    number_of_perpetual_pairs: int
    number_of_futures_pairs: int
    image: str
    year_established: int | None
    country: str | None
    description: str
    url: str
