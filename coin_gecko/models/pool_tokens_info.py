from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data12 import Data12, Data12Dict
from .included3 import Included3, Included3Dict


class PoolTokensInfo(SdkBaseModel):
    data: list[Data12]
    included: Optional[list[Included3]] = UNSET
    """Included pool data, present when include=pool is specified"""


class PoolTokensInfoDict(TypedDict):
    data: list[Data12 | Data12Dict]
    included: NotRequired[list[Included3 | Included3Dict]]
