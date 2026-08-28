from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .base_token import BaseToken, BaseTokenDict
from .dex import Dex, DexDict
from .network import Network, NetworkDict
from .quote_token import QuoteToken, QuoteTokenDict


class Relationships6(SdkBaseModel):
    """Related resources"""

    base_token: Optional[BaseToken] = UNSET
    quote_token: Optional[QuoteToken] = UNSET
    network: Optional[Network] = UNSET
    dex: Optional[Dex] = UNSET


class Relationships6Dict(TypedDict):
    base_token: NotRequired[BaseToken | BaseTokenDict]
    quote_token: NotRequired[QuoteToken | QuoteTokenDict]
    network: NotRequired[Network | NetworkDict]
    dex: NotRequired[Dex | DexDict]
