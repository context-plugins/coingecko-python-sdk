from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order4(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    OPEN_INTEREST_BTC_ASC = "open_interest_btc_asc"
    OPEN_INTEREST_BTC_DESC = "open_interest_btc_desc"
    TRADE_VOLUME_24H_BTC_ASC = "trade_volume_24h_btc_asc"
    TRADE_VOLUME_24H_BTC_DESC = "trade_volume_24h_btc_desc"

    __str__ = str.__str__


Order4OrStr: TypeAlias = Annotated[Order4 | str, open_enum_validator(Order4)]
