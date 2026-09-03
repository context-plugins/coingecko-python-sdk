from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Include3(str, Enum):
    NETWORK = "network"

    __str__ = str.__str__


Include3OrStr: TypeAlias = Annotated[Include3 | str, open_enum_validator(Include3)]
