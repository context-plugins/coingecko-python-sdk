from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PublicTreasuryEntityChart(SdkBaseModel):
    holdings: list[list[float]]
    """Historical holdings data as [timestamp, amount] pairs"""

    holding_value_in_usd: list[list[float]]
    """Historical holdings value in USD as [timestamp, value_usd] pairs"""


class PublicTreasuryEntityChartDict(TypedDict):
    holdings: list[list[float]]
    holding_value_in_usd: list[list[float]]
