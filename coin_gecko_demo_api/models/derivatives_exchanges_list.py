from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DerivativesExchangesList(SdkBaseModel):
    id: str
    """Derivatives exchange ID"""

    name: str
    """Derivatives exchange name"""


class DerivativesExchangesListDict(TypedDict):
    id: str
    name: str
