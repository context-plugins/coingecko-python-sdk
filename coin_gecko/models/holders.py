from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Holders(SdkBaseModel):
    """Token holder information"""

    count: Optional[int] = UNSET
    """Number of holders"""

    distribution_percentage: Optional[dict[str, str]] = UNSET
    """Holder distribution percentage (keys vary by chain, e.g. top_10, 11_30, 31_50, rest)"""

    last_updated: Optional[str] = UNSET
    """Last updated timestamp"""


class HoldersDict(TypedDict):
    count: NotRequired[int]
    distribution_percentage: NotRequired[dict[str, str]]
    last_updated: NotRequired[str]
