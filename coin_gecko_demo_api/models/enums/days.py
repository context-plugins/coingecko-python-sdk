from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Days(str, Enum):
    _1 = "1"
    _7 = "7"
    _14 = "14"
    _30 = "30"
    _90 = "90"
    _180 = "180"
    _365 = "365"

    __str__ = str.__str__


DaysOrStr: TypeAlias = Annotated[Days | str, open_enum_validator(Days)]
