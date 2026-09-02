from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .data import Data, DataDict


class GlobalModel(SdkBaseModel):
    data: Data


class GlobalModelDict(TypedDict):
    data: Data | DataDict
