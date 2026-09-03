from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .base import Base, BaseDict
from .quote import Quote, QuoteDict


class Meta(SdkBaseModel):
    base: Optional[Base] = UNSET
    """Base token metadata"""

    quote: Optional[Quote] = UNSET
    """Quote token metadata"""


class MetaDict(TypedDict):
    base: NotRequired[Base | BaseDict]
    quote: NotRequired[Quote | QuoteDict]
