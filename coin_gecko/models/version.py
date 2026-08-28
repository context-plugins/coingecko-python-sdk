from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Version(SdkBaseModel):
    """Token list version"""

    major: Optional[float] = UNSET
    """Major version"""

    minor: Optional[float] = UNSET
    """Minor version"""

    patch: Optional[float] = UNSET
    """Patch version"""


class VersionDict(TypedDict):
    major: NotRequired[float]
    minor: NotRequired[float]
    patch: NotRequired[float]
