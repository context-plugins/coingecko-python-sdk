from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type import TypeOrStr


class Transaction(SdkBaseModel):
    date: float
    """Transaction date in UNIX timestamp"""

    source_url: str
    """Source document URL"""

    coin_id: str
    """Coin ID"""

    type_: TypeOrStr = Field(alias="type")
    """Transaction type"""

    holding_net_change: float
    """Net change in holdings after the transaction"""

    transaction_value_usd: float
    """Transaction value in USD"""

    holding_balance: float
    """Total holding balance after the transaction"""

    average_entry_value_usd: float
    """Average entry value in USD after the transaction"""


class TransactionDict(TypedDict):
    date: float
    source_url: str
    coin_id: str
    type_: TypeOrStr
    holding_net_change: float
    transaction_value_usd: float
    holding_balance: float
    average_entry_value_usd: float
