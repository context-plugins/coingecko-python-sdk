from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .holding import Holding, HoldingDict


class PublicTreasuryEntity(SdkBaseModel):
    name: str
    """Entity name"""

    id: str
    """Entity ID"""

    type_: str = Field(alias="type")
    """Entity type: company or government"""

    symbol: str | None
    """Stock market ticker symbol"""

    country: str
    """Country code"""

    website_url: str
    """Official website URL"""

    twitter_screen_name: str
    """Official Twitter handle"""

    total_treasury_value_usd: float
    """Total current value of all holdings in USD"""

    unrealized_pnl: float
    """Unrealized profit and loss (current value minus total entry value)"""

    m_nav: float
    """Market to net asset value ratio"""

    total_asset_value_per_share_usd: float
    """Total asset value per share in USD"""

    holdings: list[Holding]
    """List of cryptocurrency assets held by the entity"""


class PublicTreasuryEntityDict(TypedDict):
    name: str
    id: str
    type_: str
    symbol: str | None
    country: str
    website_url: str
    twitter_screen_name: str
    total_treasury_value_usd: float
    unrealized_pnl: float
    m_nav: float
    total_asset_value_per_share_usd: float
    holdings: list[Holding | HoldingDict]
