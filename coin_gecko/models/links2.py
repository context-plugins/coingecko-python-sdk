from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Links2(SdkBaseModel):
    """NFT collection links"""

    homepage: Optional[str] = UNSET
    twitter: Optional[str] = UNSET
    discord: Optional[str] = UNSET


class Links2Dict(TypedDict):
    homepage: NotRequired[str]
    twitter: NotRequired[str]
    discord: NotRequired[str]
