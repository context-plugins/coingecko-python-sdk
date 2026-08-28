from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EntitiesList(SdkBaseModel):
    id: str
    """Entity ID"""

    symbol: str
    """Ticker symbol of public company"""

    name: str
    """Entity name"""

    country: str
    """Country code"""


class EntitiesListDict(TypedDict):
    id: str
    symbol: str
    name: str
    country: str
