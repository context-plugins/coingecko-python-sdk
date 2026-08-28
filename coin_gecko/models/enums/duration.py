from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Duration(str, Enum):
    _5M = "5m"
    _1H = "1h"
    _6H = "6h"
    _24H = "24h"

    __str__ = str.__str__


DurationOrStr: TypeAlias = Annotated[Duration | str, open_enum_validator(Duration)]
