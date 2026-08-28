from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order5(str, Enum):
    TOTAL_HOLDINGS_USD_DESC = "total_holdings_usd_desc"
    TOTAL_HOLDINGS_USD_ASC = "total_holdings_usd_asc"

    __str__ = str.__str__


Order5OrStr: TypeAlias = Annotated[Order5 | str, open_enum_validator(Order5)]
