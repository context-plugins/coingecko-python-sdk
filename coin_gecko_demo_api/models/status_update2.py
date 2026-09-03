from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .project import Project, ProjectDict


class StatusUpdate2(SdkBaseModel):
    description: Optional[str] = UNSET
    """Status update description"""

    category: Optional[str] = UNSET
    """Status update category"""

    created_at: Optional[str] = UNSET
    """Status update creation time"""

    user: Optional[str] = UNSET
    """Status update user"""

    user_title: Optional[str] = UNSET
    """Status update user title"""

    pin: Optional[bool] = UNSET
    """Whether status update is pinned"""

    project: Optional[Project] = UNSET
    """Project information"""


class StatusUpdate2Dict(TypedDict):
    description: NotRequired[str]
    category: NotRequired[str]
    created_at: NotRequired[str]
    user: NotRequired[str]
    user_title: NotRequired[str]
    pin: NotRequired[bool]
    project: NotRequired[Project | ProjectDict]
