from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .top_pools import TopPools, TopPoolsDict


class Relationships3(SdkBaseModel):
    top_pools: Optional[TopPools] = UNSET


class Relationships3Dict(TypedDict):
    top_pools: NotRequired[TopPools | TopPoolsDict]
