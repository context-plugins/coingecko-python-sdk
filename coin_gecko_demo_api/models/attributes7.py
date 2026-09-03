from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .gt_score_details import GtScoreDetails, GtScoreDetailsDict
from .holders import Holders, HoldersDict
from .image6 import Image6, Image6Dict
from .unions.is_honeypot import IsHoneypot, IsHoneypotDict


class Attributes7(SdkBaseModel):
    address: str
    """Token contract address"""

    name: str
    """Token name"""

    symbol: str
    """Token symbol"""

    decimals: int
    """Token decimals"""

    image_url: str | None
    """Token image URL"""

    image: Image6
    """Token image URLs in different sizes"""

    banner_image_url: str | None
    """Token banner image URL"""

    coingecko_coin_id: str | None
    """CoinGecko coin ID"""

    websites: list[str]
    """Token websites"""

    discord_url: str | None
    """Discord URL"""

    farcaster_url: str | None
    """Farcaster URL"""

    zora_url: str | None
    """Zora URL"""

    telegram_handle: str | None
    """Telegram handle"""

    twitter_handle: str | None
    """Twitter handle"""

    description: str | None
    """Token description"""

    gt_score: float
    """GeckoTerminal trust score"""

    gt_score_details: GtScoreDetails
    """GeckoTerminal trust score breakdown"""

    gt_verified: bool
    """Whether the token is verified on GeckoTerminal"""

    categories: list[str]
    """Token categories"""

    gt_category_ids: list[str]
    """GeckoTerminal category IDs"""

    holders: Holders
    """Token holder information"""

    mint_authority: str | None
    """Mint authority status"""

    freeze_authority: str | None
    """Freeze authority status"""

    is_honeypot: IsHoneypot
    """Whether the token is a honeypot (boolean or 'unknown')"""

    developer_address: str | None
    """Developer wallet address"""

    developer_holding_percentage: str | None
    """Developer holding as a percentage of total supply"""


class Attributes7Dict(TypedDict):
    address: str
    name: str
    symbol: str
    decimals: int
    image_url: str | None
    image: Image6 | Image6Dict
    banner_image_url: str | None
    coingecko_coin_id: str | None
    websites: list[str]
    discord_url: str | None
    farcaster_url: str | None
    zora_url: str | None
    telegram_handle: str | None
    twitter_handle: str | None
    description: str | None
    gt_score: float
    gt_score_details: GtScoreDetails | GtScoreDetailsDict
    gt_verified: bool
    categories: list[str]
    gt_category_ids: list[str]
    holders: Holders | HoldersDict
    mint_authority: str | None
    freeze_authority: str | None
    is_honeypot: IsHoneypot | IsHoneypotDict
    developer_address: str | None
    developer_holding_percentage: str | None
