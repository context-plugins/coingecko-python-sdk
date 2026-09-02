from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReposUrl(SdkBaseModel):
    """Repository URL"""

    github: Optional[list[str]] = UNSET
    """GitHub repository URL"""

    bitbucket: Optional[list[str]] = UNSET
    """Bitbucket repository URL"""


class ReposUrlDict(TypedDict):
    github: NotRequired[list[str]]
    bitbucket: NotRequired[list[str]]
