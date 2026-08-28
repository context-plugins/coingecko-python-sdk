from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Attributes5(SdkBaseModel):
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

    gt_score: float | None
    """GeckoTerminal trust score"""

    metadata_updated_at: str
    """Metadata last updated timestamp"""


class Attributes5Dict(TypedDict):
    address: str
    name: str
    symbol: str
    decimals: int
    image_url: str | None
    coingecko_coin_id: str | None
    websites: list[str]
    discord_url: str | None
    farcaster_url: str | None
    zora_url: str | None
    telegram_handle: str | None
    twitter_handle: str | None
    description: str | None
    gt_score: float | None
    metadata_updated_at: str
