from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data32 import Data32, Data32Dict


class DexesList(SdkBaseModel):
    data: list[Data32]


class DexesListDict(TypedDict):
    data: list[Data32 | Data32Dict]
