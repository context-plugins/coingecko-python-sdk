from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .included5 import Included5, Included5Dict
from .token_item import TokenItem, TokenItemDict


class TokenData(SdkBaseModel):
    data: TokenItem
    included: Optional[list[Included5]] = UNSET
    """Included top pool data, present when include=top_pools is specified"""


class TokenDataDict(TypedDict):
    data: TokenItem | TokenItemDict
    included: NotRequired[list[Included5 | Included5Dict]]
