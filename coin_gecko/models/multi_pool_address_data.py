from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .included import Included, IncludedDict
from .pool_address_item import PoolAddressItem, PoolAddressItemDict


class MultiPoolAddressData(SdkBaseModel):
    data: list[PoolAddressItem]
    included: Optional[list[Included]] = UNSET
    """Included related resources, present when include parameter is specified"""


class MultiPoolAddressDataDict(TypedDict):
    data: list[PoolAddressItem | PoolAddressItemDict]
    included: NotRequired[list[Included | IncludedDict]]
