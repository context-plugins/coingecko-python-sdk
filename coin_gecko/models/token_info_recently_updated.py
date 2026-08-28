from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data10 import Data10, Data10Dict
from .included2 import Included2, Included2Dict


class TokenInfoRecentlyUpdated(SdkBaseModel):
    data: list[Data10]
    included: Optional[list[Included2]] = UNSET
    """Included network data, present when include=network is specified"""


class TokenInfoRecentlyUpdatedDict(TypedDict):
    data: list[Data10 | Data10Dict]
    included: NotRequired[list[Included2 | Included2Dict]]
