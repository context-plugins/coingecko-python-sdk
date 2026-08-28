from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CommunityData(SdkBaseModel):
    """Community engagement data"""

    facebook_likes: OptionalNullable[float] = UNSET
    """Number of Facebook likes"""

    reddit_average_posts_48h: Optional[float] = UNSET
    """Average Reddit posts in 48 hours"""

    reddit_average_comments_48h: Optional[float] = UNSET
    """Average Reddit comments in 48 hours"""

    reddit_subscribers: OptionalNullable[float] = UNSET
    """Number of Reddit subscribers"""

    reddit_accounts_active_48h: Optional[float] = UNSET
    """Active Reddit accounts in 48 hours"""


class CommunityDataDict(TypedDict):
    facebook_likes: NotRequired[float | None]
    reddit_average_posts_48h: NotRequired[float]
    reddit_average_comments_48h: NotRequired[float]
    reddit_subscribers: NotRequired[float | None]
    reddit_accounts_active_48h: NotRequired[float]
