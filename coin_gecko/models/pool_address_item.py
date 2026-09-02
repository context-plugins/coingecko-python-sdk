from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attributes import Attributes, AttributesDict
from .relationships import Relationships, RelationshipsDict


class PoolAddressItem(SdkBaseModel):
    id: str
    """Pool identifier"""

    type_: str = Field(alias="type")
    """Resource type"""

    attributes: Attributes
    relationships: Relationships
    """Related resources"""


class PoolAddressItemDict(TypedDict):
    id: str
    type_: str
    attributes: Attributes | AttributesDict
    relationships: Relationships | RelationshipsDict
