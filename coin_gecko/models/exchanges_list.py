from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ExchangesList(SdkBaseModel):
    id: str
    """Exchange ID"""

    name: str
    """Exchange name"""


class ExchangesListDict(TypedDict):
    id: str
    name: str
