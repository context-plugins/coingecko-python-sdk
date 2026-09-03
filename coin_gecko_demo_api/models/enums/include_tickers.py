from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludeTickers(str, Enum):
    ALL = "all"
    UNEXPIRED = "unexpired"

    __str__ = str.__str__


IncludeTickersOrStr: TypeAlias = Annotated[IncludeTickers | str, open_enum_validator(IncludeTickers)]
