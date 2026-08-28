from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Timeframe(str, Enum):
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"

    __str__ = str.__str__


TimeframeOrStr: TypeAlias = Annotated[Timeframe | str, open_enum_validator(Timeframe)]
