from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort2(str, Enum):
    H24_VOLUME_USD_LIQUIDITY_DESC = "h24_volume_usd_liquidity_desc"
    H24_TX_COUNT_DESC = "h24_tx_count_desc"
    H24_VOLUME_USD_DESC = "h24_volume_usd_desc"

    __str__ = str.__str__


Sort2OrStr: TypeAlias = Annotated[Sort2 | str, open_enum_validator(Sort2)]
