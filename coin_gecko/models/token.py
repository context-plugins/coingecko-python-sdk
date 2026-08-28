from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Token(SdkBaseModel):
    chain_id: float = Field(alias="chainId")
    """Chainlist's chain ID"""

    address: str
    """Token contract address"""

    name: str
    """Token name"""

    symbol: str
    """Token symbol"""

    decimals: float
    """Token decimals"""

    logo_uri: str = Field(alias="logoURI")
    """Token image URL"""


class TokenDict(TypedDict):
    chain_id: float
    address: str
    name: str
    symbol: str
    decimals: float
    logo_uri: str
