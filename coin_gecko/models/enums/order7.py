from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order7(str, Enum):
    H24_VOLUME_USD_ASC = "h24_volume_usd_asc"
    H24_VOLUME_USD_DESC = "h24_volume_usd_desc"
    H24_VOLUME_NATIVE_ASC = "h24_volume_native_asc"
    H24_VOLUME_NATIVE_DESC = "h24_volume_native_desc"
    FLOOR_PRICE_NATIVE_ASC = "floor_price_native_asc"
    FLOOR_PRICE_NATIVE_DESC = "floor_price_native_desc"
    MARKET_CAP_NATIVE_ASC = "market_cap_native_asc"
    MARKET_CAP_NATIVE_DESC = "market_cap_native_desc"
    MARKET_CAP_USD_ASC = "market_cap_usd_asc"
    MARKET_CAP_USD_DESC = "market_cap_usd_desc"

    __str__ = str.__str__


Order7OrStr: TypeAlias = Annotated[Order7 | str, open_enum_validator(Order7)]
