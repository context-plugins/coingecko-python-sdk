from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order2(str, Enum):
    MARKET_CAP_DESC = "market_cap_desc"
    MARKET_CAP_ASC = "market_cap_asc"
    NAME_DESC = "name_desc"
    NAME_ASC = "name_asc"
    MARKET_CAP_CHANGE_24H_DESC = "market_cap_change_24h_desc"
    MARKET_CAP_CHANGE_24H_ASC = "market_cap_change_24h_asc"

    __str__ = str.__str__


Order2OrStr: TypeAlias = Annotated[Order2 | str, open_enum_validator(Order2)]
