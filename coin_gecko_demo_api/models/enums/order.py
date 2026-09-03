from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order(str, Enum):
    MARKET_CAP_ASC = "market_cap_asc"
    MARKET_CAP_DESC = "market_cap_desc"
    VOLUME_ASC = "volume_asc"
    VOLUME_DESC = "volume_desc"
    ID_ASC = "id_asc"
    ID_DESC = "id_desc"

    __str__ = str.__str__


OrderOrStr: TypeAlias = Annotated[Order | str, open_enum_validator(Order)]
