from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .rates import Rates, RatesDict


class ExchangeRates(SdkBaseModel):
    rates: dict[str, Rates]
    """Exchange rates keyed by currency code"""


class ExchangeRatesDict(TypedDict):
    rates: dict[str, Rates | RatesDict]
