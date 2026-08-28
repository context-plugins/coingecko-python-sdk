from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .community_data import CommunityData, CommunityDataDict
from .developer_data import DeveloperData, DeveloperDataDict
from .image import Image, ImageDict
from .market_data import MarketData, MarketDataDict
from .public_interest_stats import PublicInterestStats, PublicInterestStatsDict


class CoinsIdHistory(SdkBaseModel):
    id: str
    """Coin ID"""

    symbol: str
    """Coin symbol"""

    name: str
    """Coin name"""

    localization: Optional[dict[str, str]] = UNSET
    """Localized coin names keyed by locale code"""

    image: Image
    """Coin image URLs"""

    market_data: MarketData
    """Market data at the given date"""

    community_data: CommunityData
    """Community engagement data"""

    developer_data: DeveloperData
    """Developer activity data"""

    public_interest_stats: PublicInterestStats
    """Public interest statistics"""


class CoinsIdHistoryDict(TypedDict):
    id: str
    symbol: str
    name: str
    localization: NotRequired[dict[str, str]]
    image: Image | ImageDict
    market_data: MarketData | MarketDataDict
    community_data: CommunityData | CommunityDataDict
    developer_data: DeveloperData | DeveloperDataDict
    public_interest_stats: PublicInterestStats | PublicInterestStatsDict
