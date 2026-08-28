from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .base_token import BaseToken, BaseTokenDict
from .dex import Dex, DexDict
from .quote_token import QuoteToken, QuoteTokenDict


class Relationships(SdkBaseModel):
    """Related resources"""

    base_token: Optional[BaseToken] = UNSET
    quote_token: Optional[QuoteToken] = UNSET
    dex: Optional[Dex] = UNSET


class RelationshipsDict(TypedDict):
    base_token: NotRequired[BaseToken | BaseTokenDict]
    quote_token: NotRequired[QuoteToken | QuoteTokenDict]
    dex: NotRequired[Dex | DexDict]
