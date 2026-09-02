from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .image4 import Image4, Image4Dict


class Project(SdkBaseModel):
    """Project information"""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Project type"""

    id: Optional[str] = UNSET
    """Project ID"""

    name: Optional[str] = UNSET
    """Project name"""

    image: Optional[Image4] = UNSET
    """Project image URLs"""


class ProjectDict(TypedDict):
    type_: NotRequired[str]
    id: NotRequired[str]
    name: NotRequired[str]
    image: NotRequired[Image4 | Image4Dict]
