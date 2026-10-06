from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order6(str, Enum):
    DATE_DESC = "date_desc"
    DATE_ASC = "date_asc"
    HOLDING_NET_CHANGE_DESC = "holding_net_change_desc"
    HOLDING_NET_CHANGE_ASC = "holding_net_change_asc"
    TRANSACTION_VALUE_USD_DESC = "transaction_value_usd_desc"
    TRANSACTION_VALUE_USD_ASC = "transaction_value_usd_asc"
    AVERAGE_COST_DESC = "average_cost_desc"
    AVERAGE_COST_ASC = "average_cost_asc"

    __str__ = str.__str__


Order6OrStr: TypeAlias = Annotated[Order6 | str, open_enum_validator(Order6)]
