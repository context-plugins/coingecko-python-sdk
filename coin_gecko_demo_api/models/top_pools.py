from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data5 import Data5, Data5Dict


class TopPools(SdkBaseModel):
    data: Optional[list[Data5]] = UNSET


class TopPoolsDict(TypedDict):
    data: NotRequired[list[Data5 | Data5Dict]]
