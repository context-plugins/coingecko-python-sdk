from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .holding_amount_change import HoldingAmountChange, HoldingAmountChangeDict
from .holding_change_percentage import HoldingChangePercentage, HoldingChangePercentageDict


class Holding(SdkBaseModel):
    coin_id: str
    """Coin ID"""

    amount: float
    """Amount of cryptocurrency held"""

    percentage_of_total_supply: float
    """Percentage of total crypto supply"""

    amount_per_share: float
    """Amount of cryptocurrency per share"""

    entity_value_usd_percentage: float
    """Percentage of entity's total treasury value"""

    current_value_usd: float
    """Current value of holdings in USD"""

    total_entry_value_usd: float
    """Total entry cost in USD"""

    average_entry_value_usd: float
    """Average entry cost per unit in USD"""

    unrealized_pnl: float
    """Unrealized profit and loss for this holding"""

    holding_amount_change: Optional[HoldingAmountChange] = UNSET
    """Holding amount changes over different timeframes"""

    holding_change_percentage: Optional[HoldingChangePercentage] = UNSET
    """Holding change percentages over different timeframes"""


class HoldingDict(TypedDict):
    coin_id: str
    amount: float
    percentage_of_total_supply: float
    amount_per_share: float
    entity_value_usd_percentage: float
    current_value_usd: float
    total_entry_value_usd: float
    average_entry_value_usd: float
    unrealized_pnl: float
    holding_amount_change: NotRequired[HoldingAmountChange | HoldingAmountChangeDict]
    holding_change_percentage: NotRequired[HoldingChangePercentage | HoldingChangePercentageDict]
