from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CommunityData1(SdkBaseModel):
    """Community data"""

    facebook_likes: OptionalNullable[float] = UNSET
    """Facebook likes"""

    reddit_average_posts_48h: Optional[float] = UNSET
    """Reddit average posts in 48 hours"""

    reddit_average_comments_48h: Optional[float] = UNSET
    """Reddit average comments in 48 hours"""

    reddit_subscribers: Optional[float] = UNSET
    """Reddit subscribers"""

    reddit_accounts_active_48h: Optional[float] = UNSET
    """Reddit active accounts in 48 hours"""

    telegram_channel_user_count: OptionalNullable[float] = UNSET
    """Telegram channel user count"""


class CommunityData1Dict(TypedDict):
    facebook_likes: NotRequired[float | None]
    reddit_average_posts_48h: NotRequired[float]
    reddit_average_comments_48h: NotRequired[float]
    reddit_subscribers: NotRequired[float]
    reddit_accounts_active_48h: NotRequired[float]
    telegram_channel_user_count: NotRequired[float | None]
