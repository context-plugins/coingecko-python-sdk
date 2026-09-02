from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort(str, Enum):
    H24_TX_COUNT_DESC = "h24_tx_count_desc"
    H24_VOLUME_USD_DESC = "h24_volume_usd_desc"

    __str__ = str.__str__


SortOrStr: TypeAlias = Annotated[Sort | str, open_enum_validator(Sort)]
