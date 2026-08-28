from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .included4 import Included4, Included4Dict
from .token_item import TokenItem, TokenItemDict


class MultiTokenData(SdkBaseModel):
    data: list[TokenItem]
    included: Optional[list[Included4]] = UNSET
    """Included top pool data, present when include=top_pools is specified"""


class MultiTokenDataDict(TypedDict):
    data: list[TokenItem | TokenItemDict]
    included: NotRequired[list[Included4 | Included4Dict]]
