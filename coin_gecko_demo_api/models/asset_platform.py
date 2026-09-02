from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .image3 import Image3, Image3Dict


class AssetPlatform(SdkBaseModel):
    id: str
    """Asset platform ID"""

    chain_identifier: float | None
    """Chainlist's chain ID"""

    name: str
    """Chain name"""

    shortname: str
    """Chain shortname"""

    native_coin_id: str | None
    """Chain native coin ID"""

    image: Image3
    """Asset platform image URLs"""


class AssetPlatformDict(TypedDict):
    id: str
    chain_identifier: float | None
    name: str
    shortname: str
    native_coin_id: str | None
    image: Image3 | Image3Dict
