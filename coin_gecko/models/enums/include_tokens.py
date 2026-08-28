from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludeTokens(str, Enum):
    TOP = "top"
    ALL = "all"

    __str__ = str.__str__


IncludeTokensOrStr: TypeAlias = Annotated[IncludeTokens | str, open_enum_validator(IncludeTokens)]
