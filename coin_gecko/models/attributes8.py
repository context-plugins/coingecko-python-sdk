from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Attributes8(SdkBaseModel):
    base_token_address: Optional[str] = UNSET
    """Base token contract address"""

    quote_token_address: Optional[str] = UNSET
    """Quote token contract address"""

    quote_token_addresses: Optional[list[str]] = UNSET
    """Quote token contract addresses, present for pools with more than 2 tokens"""

    sentiment_vote_positive_percentage: Optional[float] = UNSET
    """GeckoTerminal community positive sentiment vote percentage"""

    sentiment_vote_negative_percentage: Optional[float] = UNSET
    """GeckoTerminal community negative sentiment vote percentage"""

    community_sus_report: Optional[int] = UNSET
    """GeckoTerminal community suspicious reports count"""


class Attributes8Dict(TypedDict):
    base_token_address: NotRequired[str]
    quote_token_address: NotRequired[str]
    quote_token_addresses: NotRequired[list[str]]
    sentiment_vote_positive_percentage: NotRequired[float]
    sentiment_vote_negative_percentage: NotRequired[float]
    community_sus_report: NotRequired[int]
