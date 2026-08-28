from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .government import Government, GovernmentDict


class GovernmentTreasury(SdkBaseModel):
    total_holdings: float
    """Total crypto holdings"""

    total_value_usd: float
    """Total crypto holdings value in USD"""

    market_cap_dominance: float
    """Market cap dominance percentage"""

    governments: list[Government]
    """List of governments holding crypto"""


class GovernmentTreasuryDict(TypedDict):
    total_holdings: float
    total_value_usd: float
    market_cap_dominance: float
    governments: list[Government | GovernmentDict]
