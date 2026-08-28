from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data31 import Data31, Data31Dict


class OnchainSimplePrice(SdkBaseModel):
    data: Data31


class OnchainSimplePriceDict(TypedDict):
    data: Data31 | Data31Dict
