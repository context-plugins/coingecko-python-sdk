from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ticker4 import Ticker4, Ticker4Dict


class DerivativesExchangesId(SdkBaseModel):
    name: str
    """Derivatives exchange name"""

    open_interest_btc: float | None
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

    tickers: Optional[list[Ticker4]] = UNSET
    """Derivative tickers data, available when include_tickers is specified"""


class DerivativesExchangesIdDict(TypedDict):
    name: str
    open_interest_btc: float | None
    trade_volume_24h_btc: str
    number_of_perpetual_pairs: int
    number_of_futures_pairs: int
    image: str
    year_established: int | None
    country: str | None
    description: str
    url: str
    tickers: NotRequired[list[Ticker4 | Ticker4Dict]]
