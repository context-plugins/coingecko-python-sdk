from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transaction import Transaction, TransactionDict


class PublicTreasuryTransactionHistory(SdkBaseModel):
    transactions: list[Transaction]


class PublicTreasuryTransactionHistoryDict(TypedDict):
    transactions: list[Transaction | TransactionDict]
