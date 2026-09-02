from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data21 import Data21, Data21Dict
from .included6 import Included6, Included6Dict


class Pool(SdkBaseModel):
    data: list[Data21]
    included: Optional[list[Included6]] = UNSET
    """Included related resources, present when include parameter is specified"""


class PoolDict(TypedDict):
    data: list[Data21 | Data21Dict]
    included: NotRequired[list[Included6 | Included6Dict]]
