from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CoinsList(SdkBaseModel):
    id: str
    """Coin ID"""

    symbol: str
    """Coin symbol"""

    name: str
    """Coin name"""

    platforms: OptionalNullable[dict[str, str]] = UNSET
    """Asset platform and contract address"""


class CoinsListDict(TypedDict):
    id: str
    symbol: str
    name: str
    platforms: NotRequired[dict[str, str] | None]
