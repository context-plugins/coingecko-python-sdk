from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .repos_url import ReposUrl, ReposUrlDict


class Links(SdkBaseModel):
    """Links"""

    homepage: Optional[list[str]] = UNSET
    """Website URL"""

    whitepaper: Optional[str] = UNSET
    """Whitepaper URL"""

    blockchain_site: Optional[list[str]] = UNSET
    """Block explorer URL"""

    official_forum_url: Optional[list[str]] = UNSET
    """Official forum URL"""

    chat_url: Optional[list[str]] = UNSET
    """Chat URL"""

    announcement_url: Optional[list[str]] = UNSET
    """Announcement URL"""

    snapshot_url: OptionalNullable[str] = UNSET
    """Snapshot URL"""

    twitter_screen_name: Optional[str] = UNSET
    """Twitter handle"""

    facebook_username: Optional[str] = UNSET
    """Facebook username"""

    bitcointalk_thread_identifier: OptionalNullable[int] = UNSET
    """Bitcointalk thread identifier"""

    telegram_channel_identifier: Optional[str] = UNSET
    """Telegram channel identifier"""

    subreddit_url: Optional[str] = UNSET
    """Subreddit URL"""

    repos_url: Optional[ReposUrl] = UNSET
    """Repository URL"""


class LinksDict(TypedDict):
    homepage: NotRequired[list[str]]
    whitepaper: NotRequired[str]
    blockchain_site: NotRequired[list[str]]
    official_forum_url: NotRequired[list[str]]
    chat_url: NotRequired[list[str]]
    announcement_url: NotRequired[list[str]]
    snapshot_url: NotRequired[str | None]
    twitter_screen_name: NotRequired[str]
    facebook_username: NotRequired[str]
    bitcointalk_thread_identifier: NotRequired[int | None]
    telegram_channel_identifier: NotRequired[str]
    subreddit_url: NotRequired[str]
    repos_url: NotRequired[ReposUrl | ReposUrlDict]
