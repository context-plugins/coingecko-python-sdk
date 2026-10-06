from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CodeAdditionsDeletions4Weeks1(SdkBaseModel):
    """Code additions and deletions in 4 weeks"""

    additions: Optional[float] = UNSET
    deletions: Optional[float] = UNSET


class CodeAdditionsDeletions4Weeks1Dict(TypedDict):
    additions: NotRequired[float]
    deletions: NotRequired[float]
