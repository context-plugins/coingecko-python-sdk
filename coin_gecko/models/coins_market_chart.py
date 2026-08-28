from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CoinsMarketChart(SdkBaseModel):
    prices: list[list[float]]
    """Price data points as [timestamp, price] pairs"""

    market_caps: list[list[float]]
    """Market cap data points as [timestamp, market_cap] pairs"""

    total_volumes: list[list[float]]
    """Total volume data points as [timestamp, volume] pairs"""


class CoinsMarketChartDict(TypedDict):
    prices: list[list[float]]
    market_caps: list[list[float]]
    total_volumes: list[list[float]]
