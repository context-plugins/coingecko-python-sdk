from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StatusUpdate(SdkBaseModel):
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


class StatusUpdateDict(TypedDict):
    description: NotRequired[str]
    category: NotRequired[str]
    created_at: NotRequired[str]
    user: NotRequired[str]
    user_title: NotRequired[str]
