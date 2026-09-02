from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pool2 import Pool2, Pool2Dict


class Relationships2(SdkBaseModel):
    pool: Optional[Pool2] = UNSET


class Relationships2Dict(TypedDict):
    pool: NotRequired[Pool2 | Pool2Dict]
