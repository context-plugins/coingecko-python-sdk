from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Attributes4(SdkBaseModel):
    ohlcv_list: list[list[float]]
    """OHLCV data as [timestamp, open, high, low, close, volume] arrays"""


class Attributes4Dict(TypedDict):
    ohlcv_list: list[list[float]]
