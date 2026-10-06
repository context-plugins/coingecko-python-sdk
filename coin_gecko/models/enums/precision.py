from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Precision(str, Enum):
    FULL = "full"
    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"
    _8 = "8"
    _9 = "9"
    _10 = "10"
    _11 = "11"
    _12 = "12"
    _13 = "13"
    _14 = "14"
    _15 = "15"
    _16 = "16"
    _17 = "17"
    _18 = "18"

    __str__ = str.__str__


PrecisionOrStr: TypeAlias = Annotated[Precision | str, open_enum_validator(Precision)]
