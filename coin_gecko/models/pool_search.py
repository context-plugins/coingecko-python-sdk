from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data26 import Data26, Data26Dict
from .included6 import Included6, Included6Dict


class PoolSearch(SdkBaseModel):
    data: list[Data26]
    included: Optional[list[Included6]] = UNSET
    """Included related resources, present when include parameter is specified"""


class PoolSearchDict(TypedDict):
    data: list[Data26 | Data26Dict]
    included: NotRequired[list[Included6 | Included6Dict]]
