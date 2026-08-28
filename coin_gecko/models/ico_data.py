from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IcoData(SdkBaseModel):
    """ICO data"""

    ico_start_date: Optional[str] = UNSET
    """ICO start date"""

    ico_end_date: Optional[str] = UNSET
    """ICO end date"""

    short_desc: Optional[str] = UNSET
    """Short description"""

    description: Optional[str] = UNSET
    """Detailed description"""

    links: Optional[dict[str, str]] = UNSET
    """ICO related links"""

    softcap_currency: Optional[str] = UNSET
    """Softcap currency"""

    hardcap_currency: Optional[str] = UNSET
    """Hardcap currency"""

    total_raised_currency: Optional[str] = UNSET
    """Total raised currency"""

    softcap_amount: Optional[float] = UNSET
    """Softcap amount"""

    hardcap_amount: Optional[float] = UNSET
    """Hardcap amount"""

    total_raised: Optional[float] = UNSET
    """Total raised amount"""

    quote_pre_sale_currency: Optional[str] = UNSET
    """Quote pre-sale currency"""

    base_pre_sale_amount: Optional[float] = UNSET
    """Base pre-sale amount"""

    quote_pre_sale_amount: Optional[float] = UNSET
    """Quote pre-sale amount"""

    quote_public_sale_currency: Optional[str] = UNSET
    """Quote public sale currency"""

    base_public_sale_amount: Optional[float] = UNSET
    """Base public sale amount"""

    quote_public_sale_amount: Optional[float] = UNSET
    """Quote public sale amount"""

    accepting_currencies: Optional[str] = UNSET
    """Accepting currencies"""

    country_origin: Optional[str] = UNSET
    """Country of origin"""

    pre_sale_start_date: Optional[str] = UNSET
    """Pre-sale start date"""

    pre_sale_end_date: Optional[str] = UNSET
    """Pre-sale end date"""

    whitelist_url: Optional[str] = UNSET
    """Whitelist URL"""

    whitelist_start_date: Optional[str] = UNSET
    """Whitelist start date"""

    whitelist_end_date: Optional[str] = UNSET
    """Whitelist end date"""

    bounty_detail_url: Optional[str] = UNSET
    """Bounty detail URL"""

    amount_for_sale: Optional[float] = UNSET
    """Amount for sale"""

    kyc_required: Optional[bool] = UNSET
    """KYC required"""

    whitelist_available: Optional[bool] = UNSET
    """Whitelist available"""

    pre_sale_available: Optional[bool] = UNSET
    """Pre-sale available"""

    pre_sale_ended: Optional[bool] = UNSET
    """Pre-sale ended"""


class IcoDataDict(TypedDict):
    ico_start_date: NotRequired[str]
    ico_end_date: NotRequired[str]
    short_desc: NotRequired[str]
    description: NotRequired[str]
    links: NotRequired[dict[str, str]]
    softcap_currency: NotRequired[str]
    hardcap_currency: NotRequired[str]
    total_raised_currency: NotRequired[str]
    softcap_amount: NotRequired[float]
    hardcap_amount: NotRequired[float]
    total_raised: NotRequired[float]
    quote_pre_sale_currency: NotRequired[str]
    base_pre_sale_amount: NotRequired[float]
    quote_pre_sale_amount: NotRequired[float]
    quote_public_sale_currency: NotRequired[str]
    base_public_sale_amount: NotRequired[float]
    quote_public_sale_amount: NotRequired[float]
    accepting_currencies: NotRequired[str]
    country_origin: NotRequired[str]
    pre_sale_start_date: NotRequired[str]
    pre_sale_end_date: NotRequired[str]
    whitelist_url: NotRequired[str]
    whitelist_start_date: NotRequired[str]
    whitelist_end_date: NotRequired[str]
    bounty_detail_url: NotRequired[str]
    amount_for_sale: NotRequired[float]
    kyc_required: NotRequired[bool]
    whitelist_available: NotRequired[bool]
    pre_sale_available: NotRequired[bool]
    pre_sale_ended: NotRequired[bool]
