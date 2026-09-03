from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data33 import Data33, Data33Dict


class NetworksList(SdkBaseModel):
    data: list[Data33]


class NetworksListDict(TypedDict):
    data: list[Data33 | Data33Dict]
