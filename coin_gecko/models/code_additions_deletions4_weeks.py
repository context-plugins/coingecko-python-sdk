from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CodeAdditionsDeletions4Weeks(SdkBaseModel):
    """Code additions and deletions in the last 4 weeks"""

    additions: OptionalNullable[float] = UNSET
    """Lines added"""

    deletions: OptionalNullable[float] = UNSET
    """Lines deleted"""


class CodeAdditionsDeletions4WeeksDict(TypedDict):
    additions: NotRequired[float | None]
    deletions: NotRequired[float | None]
