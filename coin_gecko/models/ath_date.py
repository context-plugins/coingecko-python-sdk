from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class AthDate(SdkBaseModel):
    """NFT collection all time highs date"""

    native_currency: Optional[RFC3339DateTime] = UNSET
    usd: Optional[RFC3339DateTime] = UNSET


class AthDateDict(TypedDict):
    native_currency: NotRequired[RFC3339DateTime]
    usd: NotRequired[RFC3339DateTime]
