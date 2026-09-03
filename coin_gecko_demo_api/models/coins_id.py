from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .categories_detail import CategoriesDetail, CategoriesDetailDict
from .community_data1 import CommunityData1, CommunityData1Dict
from .detail_platforms1 import DetailPlatforms1, DetailPlatforms1Dict
from .developer_data1 import DeveloperData1, DeveloperData1Dict
from .ico_data import IcoData, IcoDataDict
from .image1 import Image1, Image1Dict
from .links import Links, LinksDict
from .market_data1 import MarketData1, MarketData1Dict
from .status_update import StatusUpdate, StatusUpdateDict
from .ticker1 import Ticker1, Ticker1Dict


class CoinsId(SdkBaseModel):
    id: str
    """Coin ID"""

    symbol: str
    """Coin symbol"""

    name: str
    """Coin name"""

    web_slug: str
    """Coin web slug"""

    asset_platform_id: str | None
    """Coin asset platform ID"""

    platforms: dict[str, str]
    """Coin asset platform and contract address"""

    detail_platforms: dict[str, DetailPlatforms1]
    """Detailed coin asset platform and contract address"""

    block_time_in_minutes: float
    """Blockchain block time in minutes"""

    hashing_algorithm: str | None
    """Blockchain hashing algorithm"""

    categories: list[str]
    """Coin categories"""

    categories_details: Optional[list[CategoriesDetail]] = UNSET
    """Detailed coin categories"""

    preview_listing: bool
    """Preview listing coin"""

    public_notice: str | None
    """Public notice"""

    additional_notices: list[str]
    """Additional notices"""

    has_supply_breakdown: bool
    """Whether detailed supply breakdown data is available via /coins/supply_breakdown"""

    localization: Optional[dict[str, str]] = UNSET
    """Coin name localization"""

    description: dict[str, str]
    """Coin description"""

    links: Links
    """Links"""

    image: Image1
    """Coin image URL"""

    country_origin: str
    """Country of origin"""

    genesis_date: str | None
    """Genesis date"""

    sentiment_votes_up_percentage: float | None
    """Sentiment votes up percentage"""

    sentiment_votes_down_percentage: float | None
    """Sentiment votes down percentage"""

    ico_data: OptionalNullable[IcoData] = UNSET
    """ICO data"""

    watchlist_portfolio_users: float
    """Number of users watching this coin in portfolio"""

    market_cap_rank: int | None
    """Market cap rank"""

    market_cap_rank_with_rehypothecated: int | None
    """Market cap rank including rehypothecated tokens"""

    market_data: Optional[MarketData1] = UNSET
    """Market data"""

    community_data: Optional[CommunityData1] = UNSET
    """Community data"""

    developer_data: Optional[DeveloperData1] = UNSET
    """Developer data"""

    status_updates: list[StatusUpdate]
    """Status updates"""

    last_updated: str
    """Last updated timestamp"""

    tickers: Optional[list[Ticker1]] = UNSET
    """Tickers"""


class CoinsIdDict(TypedDict):
    id: str
    symbol: str
    name: str
    web_slug: str
    asset_platform_id: str | None
    platforms: dict[str, str]
    detail_platforms: dict[str, DetailPlatforms1 | DetailPlatforms1Dict]
    block_time_in_minutes: float
    hashing_algorithm: str | None
    categories: list[str]
    categories_details: NotRequired[list[CategoriesDetail | CategoriesDetailDict]]
    preview_listing: bool
    public_notice: str | None
    additional_notices: list[str]
    has_supply_breakdown: bool
    localization: NotRequired[dict[str, str]]
    description: dict[str, str]
    links: Links | LinksDict
    image: Image1 | Image1Dict
    country_origin: str
    genesis_date: str | None
    sentiment_votes_up_percentage: float | None
    sentiment_votes_down_percentage: float | None
    ico_data: NotRequired[IcoData | IcoDataDict | None]
    watchlist_portfolio_users: float
    market_cap_rank: int | None
    market_cap_rank_with_rehypothecated: int | None
    market_data: NotRequired[MarketData1 | MarketData1Dict]
    community_data: NotRequired[CommunityData1 | CommunityData1Dict]
    developer_data: NotRequired[DeveloperData1 | DeveloperData1Dict]
    status_updates: list[StatusUpdate | StatusUpdateDict]
    last_updated: str
    tickers: NotRequired[list[Ticker1 | Ticker1Dict]]
