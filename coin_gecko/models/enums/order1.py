from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order1(str, Enum):
    TRUST_SCORE_DESC = "trust_score_desc"
    TRUST_SCORE_ASC = "trust_score_asc"
    VOLUME_DESC = "volume_desc"
    VOLUME_ASC = "volume_asc"

    __str__ = str.__str__


Order1OrStr: TypeAlias = Annotated[Order1 | str, open_enum_validator(Order1)]
