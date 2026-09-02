from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data9 import Data9, Data9Dict
from .meta import Meta, MetaDict


class Ohlcv(SdkBaseModel):
    data: Data9
    meta: Meta


class OhlcvDict(TypedDict):
    data: Data9 | Data9Dict
    meta: Meta | MetaDict
