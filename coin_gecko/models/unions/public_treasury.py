from __future__ import annotations

from typing import TypeAlias

from ..company_treasury import CompanyTreasury, CompanyTreasuryDict
from ..government_treasury import GovernmentTreasury, GovernmentTreasuryDict

PublicTreasury: TypeAlias = CompanyTreasury | GovernmentTreasury

PublicTreasuryDict: TypeAlias = CompanyTreasuryDict | GovernmentTreasuryDict
