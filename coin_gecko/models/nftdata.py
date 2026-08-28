from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ath import Ath, AthDict
from .ath_change_percentage import AthChangePercentage, AthChangePercentageDict
from .ath_date import AthDate, AthDateDict
from .explorer import Explorer, ExplorerDict
from .floor_price import FloorPrice, FloorPriceDict
from .floor_price1_y_percentage_change import FloorPrice1YPercentageChange, FloorPrice1YPercentageChangeDict
from .floor_price7_d_percentage_change import FloorPrice7DPercentageChange, FloorPrice7DPercentageChangeDict
from .floor_price14_d_percentage_change import FloorPrice14DPercentageChange, FloorPrice14DPercentageChangeDict
from .floor_price24_h_percentage_change import FloorPrice24HPercentageChange, FloorPrice24HPercentageChangeDict
from .floor_price30_d_percentage_change import FloorPrice30DPercentageChange, FloorPrice30DPercentageChangeDict
from .floor_price60_d_percentage_change import FloorPrice60DPercentageChange, FloorPrice60DPercentageChangeDict
from .image5 import Image5, Image5Dict
from .links2 import Links2, Links2Dict
from .market_cap import MarketCap, MarketCapDict
from .market_cap24_h_percentage_change import MarketCap24HPercentageChange, MarketCap24HPercentageChangeDict
from .volume24_h import Volume24H, Volume24HDict
from .volume24_h_percentage_change import Volume24HPercentageChange, Volume24HPercentageChangeDict


class Nftdata(SdkBaseModel):
    id: str
    """NFT collection ID"""

    web_slug: str
    """NFT collection web slug"""

    contract_address: str
    """NFT collection contract address"""

    asset_platform_id: str
    """NFT collection asset platform ID"""

    name: str
    """NFT collection name"""

    symbol: str
    """NFT collection symbol"""

    image: Image5
    """NFT collection image URLs"""

    banner_image: str
    """NFT collection banner image URL"""

    description: str
    """NFT collection description"""

    native_currency: str
    """NFT collection native currency"""

    native_currency_symbol: str
    """NFT collection native currency symbol"""

    market_cap_rank: int | None
    """NFT collection market cap rank"""

    floor_price: FloorPrice
    """NFT collection floor price"""

    market_cap: MarketCap
    """NFT collection market cap"""

    volume_24h: Volume24H
    """NFT collection volume in 24 hours"""

    floor_price_in_usd_24h_percentage_change: float
    """NFT collection floor price in USD 24 hours percentage change"""

    floor_price_24h_percentage_change: FloorPrice24HPercentageChange
    """NFT collection floor price 24 hours percentage change"""

    market_cap_24h_percentage_change: MarketCap24HPercentageChange
    """NFT collection market cap 24 hours percentage change"""

    volume_24h_percentage_change: Volume24HPercentageChange
    """NFT collection volume in 24 hours percentage change"""

    number_of_unique_addresses: float
    """Number of unique addresses owning the NFTs"""

    number_of_unique_addresses_24h_percentage_change: float
    """Number of unique addresses 24 hours percentage change"""

    volume_in_usd_24h_percentage_change: float
    """NFT collection volume in USD 24 hours percentage change"""

    total_supply: float
    """NFT collection total supply"""

    one_day_sales: float | None
    """NFT collection one day sales"""

    one_day_sales_24h_percentage_change: float
    """NFT collection one day sales 24 hours percentage change"""

    one_day_average_sale_price: float | None
    """NFT collection one day average sale price"""

    one_day_average_sale_price_24h_percentage_change: float
    """NFT collection one day average sale price 24 hours percentage change"""

    links: Links2
    """NFT collection links"""

    floor_price_7d_percentage_change: FloorPrice7DPercentageChange
    """NFT collection floor price 7 days percentage change"""

    floor_price_14d_percentage_change: FloorPrice14DPercentageChange
    """NFT collection floor price 14 days percentage change"""

    floor_price_30d_percentage_change: FloorPrice30DPercentageChange
    """NFT collection floor price 30 days percentage change"""

    floor_price_60d_percentage_change: FloorPrice60DPercentageChange
    """NFT collection floor price 60 days percentage change"""

    floor_price_1y_percentage_change: FloorPrice1YPercentageChange
    """NFT collection floor price 1 year percentage change"""

    explorers: list[Explorer]
    """NFT collection block explorer links"""

    user_favorites_count: int
    """NFT collection user favorites count"""

    ath: Ath
    """NFT collection all time highs"""

    ath_change_percentage: AthChangePercentage
    """NFT collection all time highs change percentage"""

    ath_date: AthDate
    """NFT collection all time highs date"""


class NftdataDict(TypedDict):
    id: str
    web_slug: str
    contract_address: str
    asset_platform_id: str
    name: str
    symbol: str
    image: Image5 | Image5Dict
    banner_image: str
    description: str
    native_currency: str
    native_currency_symbol: str
    market_cap_rank: int | None
    floor_price: FloorPrice | FloorPriceDict
    market_cap: MarketCap | MarketCapDict
    volume_24h: Volume24H | Volume24HDict
    floor_price_in_usd_24h_percentage_change: float
    floor_price_24h_percentage_change: FloorPrice24HPercentageChange | FloorPrice24HPercentageChangeDict
    market_cap_24h_percentage_change: MarketCap24HPercentageChange | MarketCap24HPercentageChangeDict
    volume_24h_percentage_change: Volume24HPercentageChange | Volume24HPercentageChangeDict
    number_of_unique_addresses: float
    number_of_unique_addresses_24h_percentage_change: float
    volume_in_usd_24h_percentage_change: float
    total_supply: float
    one_day_sales: float | None
    one_day_sales_24h_percentage_change: float
    one_day_average_sale_price: float | None
    one_day_average_sale_price_24h_percentage_change: float
    links: Links2 | Links2Dict
    floor_price_7d_percentage_change: FloorPrice7DPercentageChange | FloorPrice7DPercentageChangeDict
    floor_price_14d_percentage_change: FloorPrice14DPercentageChange | FloorPrice14DPercentageChangeDict
    floor_price_30d_percentage_change: FloorPrice30DPercentageChange | FloorPrice30DPercentageChangeDict
    floor_price_60d_percentage_change: FloorPrice60DPercentageChange | FloorPrice60DPercentageChangeDict
    floor_price_1y_percentage_change: FloorPrice1YPercentageChange | FloorPrice1YPercentageChangeDict
    explorers: list[Explorer | ExplorerDict]
    user_favorites_count: int
    ath: Ath | AthDict
    ath_change_percentage: AthChangePercentage | AthChangePercentageDict
    ath_date: AthDate | AthDateDict
