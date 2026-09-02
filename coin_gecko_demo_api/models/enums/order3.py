from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order3(str, Enum):
    MARKET_CAP_ASC = "market_cap_asc"
    MARKET_CAP_DESC = "market_cap_desc"
    TRUST_SCORE_DESC = "trust_score_desc"
    TRUST_SCORE_ASC = "trust_score_asc"
    VOLUME_DESC = "volume_desc"
    VOLUME_ASC = "volume_asc"
    BASE_TARGET = "base_target"

    __str__ = str.__str__


Order3OrStr: TypeAlias = Annotated[Order3 | str, open_enum_validator(Order3)]
