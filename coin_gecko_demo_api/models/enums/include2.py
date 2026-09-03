from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Include2(str, Enum):
    POOL = "pool"

    __str__ = str.__str__


Include2OrStr: TypeAlias = Annotated[Include2 | str, open_enum_validator(Include2)]
