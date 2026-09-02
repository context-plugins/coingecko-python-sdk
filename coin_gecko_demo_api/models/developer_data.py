from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .code_additions_deletions4_weeks import CodeAdditionsDeletions4Weeks, CodeAdditionsDeletions4WeeksDict


class DeveloperData(SdkBaseModel):
    """Developer activity data"""

    forks: OptionalNullable[float] = UNSET
    """Repository forks"""

    stars: OptionalNullable[float] = UNSET
    """Repository stars"""

    subscribers: OptionalNullable[float] = UNSET
    """Repository subscribers"""

    total_issues: OptionalNullable[float] = UNSET
    """Total issues"""

    closed_issues: OptionalNullable[float] = UNSET
    """Closed issues"""

    pull_requests_merged: OptionalNullable[float] = UNSET
    """Pull requests merged"""

    pull_request_contributors: OptionalNullable[float] = UNSET
    """Pull request contributors"""

    code_additions_deletions_4_weeks: Optional[CodeAdditionsDeletions4Weeks] = UNSET
    """Code additions and deletions in the last 4 weeks"""

    commit_count_4_weeks: OptionalNullable[float] = UNSET
    """Commit count in the last 4 weeks"""


class DeveloperDataDict(TypedDict):
    forks: NotRequired[float | None]
    stars: NotRequired[float | None]
    subscribers: NotRequired[float | None]
    total_issues: NotRequired[float | None]
    closed_issues: NotRequired[float | None]
    pull_requests_merged: NotRequired[float | None]
    pull_request_contributors: NotRequired[float | None]
    code_additions_deletions_4_weeks: NotRequired[CodeAdditionsDeletions4Weeks | CodeAdditionsDeletions4WeeksDict]
    commit_count_4_weeks: NotRequired[float | None]
