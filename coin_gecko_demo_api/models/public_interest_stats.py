from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PublicInterestStats(SdkBaseModel):
    """Public interest statistics"""

    alexa_rank: OptionalNullable[float] = UNSET
    """Alexa rank"""

    bing_matches: OptionalNullable[float] = UNSET
    """Bing search matches"""


class PublicInterestStatsDict(TypedDict):
    alexa_rank: NotRequired[float | None]
    bing_matches: NotRequired[float | None]
