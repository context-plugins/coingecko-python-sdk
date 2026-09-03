from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Locale(str, Enum):
    AR = "ar"
    BG = "bg"
    CS = "cs"
    DA = "da"
    DE = "de"
    EL = "el"
    EN = "en"
    ES = "es"
    FI = "fi"
    FR = "fr"
    HE = "he"
    HI = "hi"
    HR = "hr"
    HU = "hu"
    ID = "id"
    IT = "it"
    JA = "ja"
    KO = "ko"
    LT = "lt"
    NL = "nl"
    NO = "no"
    PL = "pl"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    SK = "sk"
    SL = "sl"
    SV = "sv"
    TH = "th"
    TR = "tr"
    UK = "uk"
    VI = "vi"
    ZH = "zh"
    ZH_TW = "zh-tw"

    __str__ = str.__str__


LocaleOrStr: TypeAlias = Annotated[Locale | str, open_enum_validator(Locale)]
