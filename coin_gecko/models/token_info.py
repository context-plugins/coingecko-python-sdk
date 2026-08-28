from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .token_info_item import TokenInfoItem, TokenInfoItemDict


class TokenInfo(SdkBaseModel):
    data: TokenInfoItem


class TokenInfoDict(TypedDict):
    data: TokenInfoItem | TokenInfoItemDict
