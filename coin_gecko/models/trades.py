from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data8 import Data8, Data8Dict


class Trades(SdkBaseModel):
    data: list[Data8]


class TradesDict(TypedDict):
    data: list[Data8 | Data8Dict]
