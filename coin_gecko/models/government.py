from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Government(SdkBaseModel):
    name: str
    """Government name"""

    symbol: str | None
    """Government ticker symbol"""

    country: str
    """Country code"""

    total_holdings: float
    """Total crypto holdings"""

    total_entry_value_usd: float
    """Total entry value in USD"""

    total_current_value_usd: float
    """Total current value of crypto holdings in USD"""

    percentage_of_total_supply: float
    """Percentage of total crypto supply"""


class GovernmentDict(TypedDict):
    name: str
    symbol: str | None
    country: str
    total_holdings: float
    total_entry_value_usd: float
    total_current_value_usd: float
    percentage_of_total_supply: float
