from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data1 import Data1, Data1Dict


class GlobalDeFi(SdkBaseModel):
    data: Data1


class GlobalDeFiDict(TypedDict):
    data: Data1 | Data1Dict
