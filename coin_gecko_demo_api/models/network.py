from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data5 import Data5, Data5Dict


class Network(SdkBaseModel):
    data: Optional[Data5] = UNSET


class NetworkDict(TypedDict):
    data: NotRequired[Data5 | Data5Dict]
