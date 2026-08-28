from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .item import Item, ItemDict


class Coin1(SdkBaseModel):
    item: Item


class Coin1Dict(TypedDict):
    item: Item | ItemDict
