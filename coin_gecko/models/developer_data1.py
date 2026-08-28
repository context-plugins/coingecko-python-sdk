from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .code_additions_deletions4_weeks1 import CodeAdditionsDeletions4Weeks1, CodeAdditionsDeletions4Weeks1Dict


class DeveloperData1(SdkBaseModel):
    """Developer data"""

    forks: Optional[float] = UNSET
    """Repository forks"""

    stars: Optional[float] = UNSET
    """Repository stars"""

    subscribers: Optional[float] = UNSET
    """Repository subscribers"""

    total_issues: Optional[float] = UNSET
    """Repository total issues"""

    closed_issues: Optional[float] = UNSET
    """Repository closed issues"""

    pull_requests_merged: Optional[float] = UNSET
    """Repository pull requests merged"""

    pull_request_contributors: Optional[float] = UNSET
    """Repository pull request contributors"""

    code_additions_deletions_4_weeks: Optional[CodeAdditionsDeletions4Weeks1] = UNSET
    """Code additions and deletions in 4 weeks"""

    commit_count_4_weeks: Optional[float] = UNSET
    """Repository commit count in 4 weeks"""

    last_4_weeks_commit_activity_series: Optional[list[float]] = UNSET
    """Repository last 4 weeks commit activity series"""


class DeveloperData1Dict(TypedDict):
    forks: NotRequired[float]
    stars: NotRequired[float]
    subscribers: NotRequired[float]
    total_issues: NotRequired[float]
    closed_issues: NotRequired[float]
    pull_requests_merged: NotRequired[float]
    pull_request_contributors: NotRequired[float]
    code_additions_deletions_4_weeks: NotRequired[CodeAdditionsDeletions4Weeks1 | CodeAdditionsDeletions4Weeks1Dict]
    commit_count_4_weeks: NotRequired[float]
    last_4_weeks_commit_activity_series: NotRequired[list[float]]
