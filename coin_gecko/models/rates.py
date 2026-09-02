from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Rates(SdkBaseModel):
    name: str
    """Currency name"""

    unit: str
    """Currency unit symbol"""

    value: float
    """Exchange rate value relative to BTC"""

    type_: str = Field(alias="type")
    """Currency type: crypto, fiat, or commodity"""


class RatesDict(TypedDict):
    name: str
    unit: str
    value: float
    type_: str
