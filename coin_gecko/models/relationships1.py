from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .network import Network, NetworkDict


class Relationships1(SdkBaseModel):
    network: Optional[Network] = UNSET


class Relationships1Dict(TypedDict):
    network: NotRequired[Network | NetworkDict]
