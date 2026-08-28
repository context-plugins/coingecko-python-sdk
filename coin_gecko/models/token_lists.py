from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .token import Token, TokenDict
from .version import Version, VersionDict


class TokenLists(SdkBaseModel):
    name: str
    """Token list name"""

    logo_uri: str = Field(alias="logoURI")
    """Token list logo URL"""

    keywords: list[str]
    """Token list keywords"""

    timestamp: RFC3339DateTime
    """Token list generation timestamp"""

    tokens: list[Token]
    """List of tokens"""

    version: Version
    """Token list version"""


class TokenListsDict(TypedDict):
    name: str
    logo_uri: str
    keywords: list[str]
    timestamp: RFC3339DateTime
    tokens: list[Token | TokenDict]
    version: Version | VersionDict
