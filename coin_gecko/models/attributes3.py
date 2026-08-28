from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Attributes3(SdkBaseModel):
    block_number: int
    """Block number of the trade"""

    tx_hash: str
    """Transaction hash"""

    tx_from_address: str
    """Transaction sender address"""

    from_token_amount: str
    """Amount of token sent"""

    to_token_amount: str
    """Amount of token received"""

    price_from_in_currency_token: str
    """Price of from-token in currency token"""

    price_to_in_currency_token: str
    """Price of to-token in currency token"""

    price_from_in_usd: str
    """Price of from-token in USD"""

    price_to_in_usd: str
    """Price of to-token in USD"""

    block_timestamp: str
    """Block timestamp"""

    kind: str
    """Trade kind (buy or sell)"""

    volume_in_usd: str
    """Trade volume in USD"""

    from_token_address: str
    """From-token contract address"""

    to_token_address: str
    """To-token contract address"""


class Attributes3Dict(TypedDict):
    block_number: int
    tx_hash: str
    tx_from_address: str
    from_token_amount: str
    to_token_amount: str
    price_from_in_currency_token: str
    price_to_in_currency_token: str
    price_from_in_usd: str
    price_to_in_usd: str
    block_timestamp: str
    kind: str
    volume_in_usd: str
    from_token_address: str
    to_token_address: str
