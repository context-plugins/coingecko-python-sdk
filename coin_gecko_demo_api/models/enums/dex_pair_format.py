from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DexPairFormat(str, Enum):
    CONTRACT_ADDRESS = "contract_address"
    SYMBOL = "symbol"

    __str__ = str.__str__


DexPairFormatOrStr: TypeAlias = Annotated[DexPairFormat | str, open_enum_validator(DexPairFormat)]
