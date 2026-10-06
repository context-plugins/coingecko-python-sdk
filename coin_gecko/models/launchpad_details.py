from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class LaunchpadDetails(SdkBaseModel):
    """Launchpad details for pump-style tokens"""

    graduation_percentage: Optional[float] = UNSET
    completed: Optional[bool] = UNSET
    completed_at: OptionalNullable[str] = UNSET
    migrated_destination_pool_address: OptionalNullable[str] = UNSET


class LaunchpadDetailsDict(TypedDict):
    graduation_percentage: NotRequired[float]
    completed: NotRequired[bool]
    completed_at: NotRequired[str | None]
    migrated_destination_pool_address: NotRequired[str | None]
