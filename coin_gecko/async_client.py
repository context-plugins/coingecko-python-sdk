from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseCoinGeckoClient
from .core import (
    ApiKeyHeaderScheme,
    ApiKeyQueryScheme,
    ApiResult,
    AsyncAnySchemes,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    no_auth,
    param,
    raw_error_response,
)
from .models.asset_platform import AssetPlatform
from .models.categories_list import CategoriesList
from .models.category1 import Category1
from .models.coins_contract_address import CoinsContractAddress
from .models.coins_id import CoinsId
from .models.coins_id_history import CoinsIdHistory
from .models.coins_id_tickers import CoinsIdTickers
from .models.coins_list import CoinsList
from .models.coins_market import CoinsMarket
from .models.coins_market_chart import CoinsMarketChart
from .models.derivatives_exchange import DerivativesExchange
from .models.derivatives_exchanges_id import DerivativesExchangesId
from .models.derivatives_exchanges_list import DerivativesExchangesList
from .models.derivatives_ticker import DerivativesTicker
from .models.dexes_list import DexesList
from .models.entities_list import EntitiesList
from .models.enums.currency import CurrencyOrStr
from .models.enums.days import DaysOrStr
from .models.enums.dex_pair_format import DexPairFormatOrStr
from .models.enums.duration import DurationOrStr
from .models.enums.entity import EntityOrStr
from .models.enums.entity_type import EntityTypeOrStr
from .models.enums.filter import FilterOrStr
from .models.enums.include import IncludeOrStr
from .models.enums.include2 import Include2OrStr
from .models.enums.include3 import Include3OrStr
from .models.enums.include_tickers import IncludeTickersOrStr
from .models.enums.include_tokens import IncludeTokensOrStr
from .models.enums.interval import IntervalOrStr
from .models.enums.locale import LocaleOrStr
from .models.enums.order import OrderOrStr
from .models.enums.order1 import Order1OrStr
from .models.enums.order2 import Order2OrStr
from .models.enums.order3 import Order3OrStr
from .models.enums.order4 import Order4OrStr
from .models.enums.order5 import Order5OrStr
from .models.enums.order6 import Order6OrStr
from .models.enums.order7 import Order7OrStr
from .models.enums.precision import PrecisionOrStr
from .models.enums.sort import SortOrStr
from .models.enums.sort2 import Sort2OrStr
from .models.enums.status import StatusOrStr
from .models.enums.timeframe import TimeframeOrStr
from .models.exchange1 import Exchange1
from .models.exchange_rates import ExchangeRates
from .models.exchanges_id import ExchangesId
from .models.exchanges_list import ExchangesList
from .models.global_de_fi import GlobalDeFi
from .models.global_model import GlobalModel
from .models.multi_pool_address_data import MultiPoolAddressData
from .models.multi_token_data import MultiTokenData
from .models.networks_list import NetworksList
from .models.nftdata import Nftdata
from .models.nfts_list import NftsList
from .models.ohlcv import Ohlcv
from .models.onchain_simple_price import OnchainSimplePrice
from .models.ping_server import PingServer
from .models.pool import Pool
from .models.pool_address_data import PoolAddressData
from .models.pool_search import PoolSearch
from .models.pool_tokens_info import PoolTokensInfo
from .models.public_treasury_entity import PublicTreasuryEntity
from .models.public_treasury_entity_chart import PublicTreasuryEntityChart
from .models.public_treasury_transaction_history import PublicTreasuryTransactionHistory
from .models.search import Search
from .models.simple_price import SimplePrice
from .models.token_data import TokenData
from .models.token_info import TokenInfo
from .models.token_info_recently_updated import TokenInfoRecentlyUpdated
from .models.token_lists import TokenLists
from .models.trades import Trades
from .models.trending_search import TrendingSearch
from .models.unions.exchange_volume_chart import ExchangeVolumeChart
from .models.unions.public_treasury import PublicTreasury
from .server.server import Server


class AsyncCoinGeckoClient(BaseCoinGeckoClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        header_auth: str | None = None,
        query_auth: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
        )
        self._auth = AsyncAuthSchemes(
            header_auth=ApiKeyHeaderScheme("x-cg-demo-api-key", header_auth) if header_auth is not None else no_auth,
            query_auth=ApiKeyQueryScheme("x_cg_demo_api_key", query_auth) if query_auth is not None else no_auth,
        )

    @cached_property
    def with_raw_response(self) -> AsyncApiWithRawResponse:
        return AsyncApiWithRawResponse(self._raw_client, self._server, self._auth)

    async def asset_platforms_list(
        self, *, filter: FilterOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[AssetPlatform]:
        """To query all the supported asset platforms (blockchain networks) on CoinGecko

        Args:
            filter: Apply relevant filters to results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of asset platforms

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.asset_platforms_list(filter=filter, request_options=request_options)
        ).unwrap()

    async def coins_categories(
        self, *, order: Order2OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[Category1]:
        """To query all the coins categories with market data (market cap, volume, etc.) on CoinGecko

        Args:
            order: Sort results by field. Default: ``market_cap_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of coin categories with market data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.coins_categories(order=order, request_options=request_options)).unwrap()

    async def coins_categories_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CategoriesList]:
        """To query all the supported coins categories on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of coin categories

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.coins_categories_list(request_options=request_options)).unwrap()

    async def coins_contract_address(
        self,
        *,
        id: str = "ethereum",
        contract_address: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsContractAddress:
        """To query all the metadata (image, websites, socials, description, contract address, etc.) and market data
        (price, ATH, exchange tickers, etc.) of a coin based on an asset platform and a particular token contract
        address

        Args:
            id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: The contract address of token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin data by token contract address

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_contract_address(
                id=id, contract_address=contract_address, request_options=request_options
            )
        ).unwrap()

    async def coins_id(
        self,
        *,
        id: str = "bitcoin",
        localization: bool | None = None,
        tickers: bool | None = None,
        market_data: bool | None = None,
        community_data: bool | None = None,
        developer_data: bool | None = None,
        sparkline: bool | None = None,
        include_categories_details: bool | None = None,
        dex_pair_format: DexPairFormatOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsId:
        """To query all the metadata (image, websites, socials, description, contract address, etc.) and market data
        (price, ATH, exchange tickers, etc.) of a coin based on a particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list
            localization: Include all localized languages in the response. Default: true
            tickers: Include tickers data. Default: true
            market_data: Include market data. Default: true
            community_data: Include community data. Default: true
            developer_data: Include developer data. Default: true
            sparkline: Include sparkline 7-day data. Default: false
            include_categories_details: Include categories details. Default: false
            dex_pair_format: Set to ``symbol`` to display DEX pair base and target as symbols. Default:
                ``contract_address``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_id(
                id=id,
                localization=localization,
                tickers=tickers,
                market_data=market_data,
                community_data=community_data,
                developer_data=developer_data,
                sparkline=sparkline,
                include_categories_details=include_categories_details,
                dex_pair_format=dex_pair_format,
                request_options=request_options,
            )
        ).unwrap()

    async def coins_id_history(
        self,
        *,
        id: str = "bitcoin",
        date: str = "30-12-2025",
        localization: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsIdHistory:
        """To query the historical data (price, market cap, 24hrs volume, etc.) at a given date for a coin based on a
        particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list.
            date: The date of data snapshot. Format: ``dd-mm-yyyy``
            localization: Include all the localized languages in response. Default: true
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin historical data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_id_history(
                id=id, date=date, localization=localization, request_options=request_options
            )
        ).unwrap()

    async def coins_id_market_chart(
        self,
        *,
        id: str = "bitcoin",
        vs_currency: str = "usd",
        days: str = "1",
        interval: IntervalOrStr | None = None,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsMarketChart:
        """To get the historical chart data of a coin including time in UNIX, price, market cap and 24hrs volume based
        on particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list.
            vs_currency: Target currency of market data. *refers to /reference/simple-supported-currencies.
            days: Data up to number of days ago. You may use any integer or ``max`` for number of days.
            interval: Data interval, leave empty for auto granularity.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin historical chart data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_id_market_chart(
                id=id,
                vs_currency=vs_currency,
                days=days,
                interval=interval,
                precision=precision,
                request_options=request_options,
            )
        ).unwrap()

    async def coins_id_market_chart_range(
        self,
        *,
        id: str = "bitcoin",
        vs_currency: str = "usd",
        from_: int = 1767024000,
        to: int = 1777564800,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsMarketChart:
        """To get the historical chart data of a coin within certain time range in UNIX along with price, market cap and
        24hrs volume based on particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list.
            vs_currency: Target currency of market data. *refers to /reference/simple-supported-currencies.
            from_: Starting date in UNIX timestamp.
            to: Ending date in UNIX timestamp.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin historical chart data within time range

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_id_market_chart_range(
                id=id, vs_currency=vs_currency, from_=from_, to=to, precision=precision, request_options=request_options
            )
        ).unwrap()

    async def coins_id_ohlc(
        self,
        days: DaysOrStr,
        *,
        id: str = "bitcoin",
        vs_currency: str = "usd",
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[list[float]]:
        """To get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin ID

        Args:
            days: Data up to number of days ago.
            id: Coin ID. *refers to /reference/coins-list.
            vs_currency: Target currency of price data. *refers to /reference/simple-supported-currencies.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin OHLC chart data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_id_ohlc(
                days, id=id, vs_currency=vs_currency, precision=precision, request_options=request_options
            )
        ).unwrap()

    async def coins_id_tickers(
        self,
        *,
        id: str = "bitcoin",
        exchange_ids: str | None = None,
        include_exchange_logo: bool | None = None,
        page: int | None = None,
        order: Order1OrStr | None = None,
        depth: bool | None = None,
        dex_pair_format: DexPairFormatOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsIdTickers:
        """To query the coin tickers on both centralized exchange (CEX) and decentralized exchange (DEX) based on a
        particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list
            exchange_ids: Exchange ID. *refers to /reference/exchanges-list
            include_exchange_logo: Include exchange logo. Default: false
            page: Page through results
            order: Sort the order of responses. Default: trust_score_desc
            depth: Include 2% orderbook depth, i.e. ``cost_to_move_up_usd`` and ``cost_to_move_down_usd``. Default:
                false
            dex_pair_format: Set to ``symbol`` to display DEX pair base and target as symbols. Default:
                ``contract_address``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin tickers

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_id_tickers(
                id=id,
                exchange_ids=exchange_ids,
                include_exchange_logo=include_exchange_logo,
                page=page,
                order=order,
                depth=depth,
                dex_pair_format=dex_pair_format,
                request_options=request_options,
            )
        ).unwrap()

    async def coins_list(
        self,
        *,
        include_platform: bool | None = None,
        status: StatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CoinsList]:
        """To query all the supported coins on CoinGecko with coin ID, name and symbol

        Args:
            include_platform: Include platform and token's contract addresses. Default: false
            status: Filter by status of coins. Default: active
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of coins

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_list(
                include_platform=include_platform, status=status, request_options=request_options
            )
        ).unwrap()

    async def coins_markets(
        self,
        *,
        vs_currency: str = "usd",
        ids: str | None = "bitcoin",
        names: str | None = "Bitcoin",
        symbols: str | None = "btc",
        include_tokens: IncludeTokensOrStr | None = None,
        category: str | None = None,
        order: OrderOrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        sparkline: bool | None = None,
        price_change_percentage: str | None = None,
        locale: LocaleOrStr | None = None,
        precision: PrecisionOrStr | None = None,
        include_rehypothecated: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CoinsMarket]:
        """To query all the supported coins with price, market cap, volume and market related data

        Args:
            vs_currency: Target currency of coins and market data. *refers to /reference/simple-supported-currencies
            ids: Coins' IDs, comma-separated if querying more than 1 coin. *refers to /reference/coins-list
            names: Coins' names, comma-separated if querying more than 1 coin.
            symbols: Coins' symbols, comma-separated if querying more than 1 coin.
            include_tokens: For ``symbols`` lookups, specify ``all`` to include all matching tokens. Default ``top``
                returns top-ranked tokens by market cap or volume.
            category: Filter based on coins' category. *refers to /reference/coins-categories-list
            order: Sort result by field. Default: market_cap_desc
            per_page: Total results per page. Default: 100 Valid values: 1...250
            page: Page through results. Default: 1
            sparkline: Include sparkline 7-day data. Default: false
            price_change_percentage: Include price change percentage timeframe, comma-separated if querying more than 1
                timeframe. Valid values: ``1h``, ``24h``, ``7d``, ``14d``, ``30d``, ``200d``, ``1y``
            locale: Language background. Default: en
            precision: Decimal places for currency price value
            include_rehypothecated: Include rehypothecated tokens in results. When true, returns
                ``market_cap_rank_with_rehypothecated`` field. Default: false
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of coins with market data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.coins_markets(
                vs_currency=vs_currency,
                ids=ids,
                names=names,
                symbols=symbols,
                include_tokens=include_tokens,
                category=category,
                order=order,
                per_page=per_page,
                page=page,
                sparkline=sparkline,
                price_change_percentage=price_change_percentage,
                locale=locale,
                precision=precision,
                include_rehypothecated=include_rehypothecated,
                request_options=request_options,
            )
        ).unwrap()

    async def companies_public_treasury(
        self,
        entity: EntityOrStr,
        *,
        coin_id: str = "bitcoin",
        per_page: int | None = None,
        page: int | None = None,
        order: Order5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublicTreasury:
        """To query public companies' and governments' cryptocurrency holdings by coin ID

        Args:
            entity: Public company or government entity.
            coin_id: Coin ID. e.g. ``bitcoin``, ``ethereum``, ``solana``, ``binancecoin``
            per_page: Total results per page. Default value: 250 Valid values: 1...250
            page: Page through results. Default value: 1
            order: Sort order for results. Default: ``total_holdings_usd_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Public companies or governments crypto treasury holdings data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.companies_public_treasury(
                entity, coin_id=coin_id, per_page=per_page, page=page, order=order, request_options=request_options
            )
        ).unwrap()

    async def contract_address_market_chart(
        self,
        *,
        id: str = "ethereum",
        contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
        vs_currency: str = "usd",
        days: str = "1",
        interval: IntervalOrStr | None = None,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsMarketChart:
        """To get the historical chart data including time in UNIX, price, market cap and 24hrs volume based on asset
        platform and particular token contract address

        Args:
            id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: The contract address of token.
            vs_currency: Target currency of market data. *refers to /reference/simple-supported-currencies.
            days: Data up to number of days ago. You may use any integer or ``max`` for number of days.
            interval: Data interval, leave empty for auto granularity.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin historical chart data by token address

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.contract_address_market_chart(
                id=id,
                contract_address=contract_address,
                vs_currency=vs_currency,
                days=days,
                interval=interval,
                precision=precision,
                request_options=request_options,
            )
        ).unwrap()

    async def contract_address_market_chart_range(
        self,
        *,
        id: str = "ethereum",
        contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
        vs_currency: str = "usd",
        from_: int = 1767024000,
        to: int = 1777564800,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsMarketChart:
        """To get the historical chart data within certain time range in UNIX along with price, market cap and 24hrs
        volume based on asset platform and particular token contract address

        Args:
            id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: The contract address of token.
            vs_currency: Target currency of market data. *refers to /reference/simple-supported-currencies.
            from_: Starting date in UNIX timestamp.
            to: Ending date in UNIX timestamp.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin historical chart data within time range by token address

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.contract_address_market_chart_range(
                id=id,
                contract_address=contract_address,
                vs_currency=vs_currency,
                from_=from_,
                to=to,
                precision=precision,
                request_options=request_options,
            )
        ).unwrap()

    async def crypto_global(self, *, request_options: RequestOptionsOrDict | None = None) -> GlobalModel:
        """To query cryptocurrency global data including active cryptocurrencies, markets, total crypto market cap and
        etc

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cryptocurrency global market data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.crypto_global(request_options=request_options)).unwrap()

    async def derivatives_exchanges(
        self,
        *,
        order: Order4OrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DerivativesExchange]:
        """To query all the derivatives exchanges with related data (ID, name, open interest, ...) on CoinGecko

        Args:
            order: Sort order of responses. Default: ``open_interest_btc_desc``
            per_page: Total results per page.
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of derivative exchanges with data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.derivatives_exchanges(
                order=order, per_page=per_page, page=page, request_options=request_options
            )
        ).unwrap()

    async def derivatives_exchanges_id(
        self,
        *,
        id: str = "binance_futures",
        include_tickers: IncludeTickersOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DerivativesExchangesId:
        """To query the derivatives exchange's related data (name, open interest, trade volume, ...) based on the
        exchange's ID

        Args:
            id: Derivative exchange ID. *refers to /reference/derivatives-exchanges-list.
            include_tickers: Include tickers data. Default: tickers data is not included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Derivative exchange data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.derivatives_exchanges_id(
                id=id, include_tickers=include_tickers, request_options=request_options
            )
        ).unwrap()

    async def derivatives_exchanges_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DerivativesExchangesList]:
        """To query all the supported derivatives exchanges with ID and name on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of derivative exchange identifiers and names

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.derivatives_exchanges_list(request_options=request_options)).unwrap()

    async def derivatives_tickers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DerivativesTicker]:
        """To query all the tickers from derivatives exchanges on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of derivative tickers

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.derivatives_tickers(request_options=request_options)).unwrap()

    async def dexes_list(
        self, *, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DexesList:
        """To query all the supported decentralized exchanges (DEXs) based on the provided network on GeckoTerminal

        Args:
            network: Network ID. *refers to /reference/networks-list.
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported DEXs on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.dexes_list(network=network, page=page, request_options=request_options)
        ).unwrap()

    async def entities_list(
        self,
        *,
        entity_type: EntityTypeOrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[EntitiesList]:
        """To query all the supported entities on CoinGecko with entity ID, name, symbol, and country

        Args:
            entity_type: Filter by entity type.
            per_page: Total results per page. Default value: 100 Valid values: 1...250
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of entities with ID, name, symbol, and country

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.entities_list(
                entity_type=entity_type, per_page=per_page, page=page, request_options=request_options
            )
        ).unwrap()

    async def exchange_rates(self, *, request_options: RequestOptionsOrDict | None = None) -> ExchangeRates:
        """To query BTC exchange rates with other currencies

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            BTC exchange rates with other currencies

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.exchange_rates(request_options=request_options)).unwrap()

    async def exchanges(
        self,
        *,
        per_page: float | None = None,
        page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Exchange1]:
        """To query all the supported exchanges with exchanges' data (ID, name, country, etc.) that have active trading
        volumes on CoinGecko

        Args:
            per_page: Total results per page. Default: 100. Valid values: 1...250
            page: Page through results. Default: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of exchanges with data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.exchanges(per_page=per_page, page=page, request_options=request_options)
        ).unwrap()

    async def exchanges_id(
        self,
        *,
        id: str = "binance",
        dex_pair_format: DexPairFormatOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ExchangesId:
        """To query exchange's data (name, year established, country, etc.), exchange volume in BTC and top 100 tickers
        based on exchange's ID

        Args:
            id: Exchange ID. *refers to /reference/exchanges-list.
            dex_pair_format: Set to ``symbol`` to display DEX pair base and target as symbols. Default:
                ``contract_address``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Exchange data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.exchanges_id(
                id=id, dex_pair_format=dex_pair_format, request_options=request_options
            )
        ).unwrap()

    async def exchanges_id_tickers(
        self,
        *,
        id: str = "binance",
        coin_ids: str | None = None,
        include_exchange_logo: bool | None = None,
        page: float | None = None,
        depth: bool | None = None,
        order: Order3OrStr | None = None,
        dex_pair_format: DexPairFormatOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CoinsIdTickers:
        """To query exchange's tickers based on exchange's ID

        Args:
            id: Exchange ID. *refers to /reference/exchanges-list.
            coin_ids: Filter tickers by coin IDs, comma-separated if querying more than 1 coin. *refers to
                /reference/coins-list.
            include_exchange_logo: Include exchange logo. Default: false
            page: Page through results.
            depth: Include 2% orderbook depth (cost_to_move_up_usd and cost_to_move_down_usd). Default: false
            order: Sort the order of responses. Default: ``trust_score_desc``
            dex_pair_format: Set to ``symbol`` to display DEX pair base and target as symbols. Default:
                ``contract_address``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Exchange tickers

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.exchanges_id_tickers(
                id=id,
                coin_ids=coin_ids,
                include_exchange_logo=include_exchange_logo,
                page=page,
                depth=depth,
                order=order,
                dex_pair_format=dex_pair_format,
                request_options=request_options,
            )
        ).unwrap()

    async def exchanges_id_volume_chart(
        self, days: DaysOrStr, *, id: str = "binance", request_options: RequestOptionsOrDict | None = None
    ) -> list[list[ExchangeVolumeChart]]:
        """To query the historical volume chart data with time in UNIX and trading volume data in BTC based on
        exchange's ID

        Args:
            days: Data up to number of days ago.
            id: Exchange ID or derivative exchange ID. *refers to /reference/exchanges-list or
                /reference/derivatives-exchanges-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Exchange volume chart data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.exchanges_id_volume_chart(days, id=id, request_options=request_options)
        ).unwrap()

    async def exchanges_list(
        self, *, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[ExchangesList]:
        """To query all the supported exchanges with ID and name

        Args:
            status: Filter by status of exchanges. Default: ``active``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of exchanges

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.exchanges_list(status=status, request_options=request_options)).unwrap()

    async def global_defi(self, *, request_options: RequestOptionsOrDict | None = None) -> GlobalDeFi:
        """To query top 100 cryptocurrency global decentralized finance (DeFi) data including DeFi market cap, trading
        volume

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Global decentralized finance (DeFi) market data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.global_defi(request_options=request_options)).unwrap()

    async def latest_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the latest pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Latest pools across all networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.latest_pools_list(
                include=include,
                page=page,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def latest_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the latest pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Latest pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.latest_pools_network(
                network=network,
                include=include,
                page=page,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def networks_list(
        self, *, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NetworksList:
        """To retrieve a list of all supported networks on GeckoTerminal

        Args:
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.networks_list(page=page, request_options=request_options)).unwrap()

    async def nfts_contract_address(
        self,
        *,
        asset_platform_id: str = "ethereum",
        contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
        request_options: RequestOptionsOrDict | None = None,
    ) -> Nftdata:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection contract address
        and respective asset platform

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: Contract address of the NFT collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT collection data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.nfts_contract_address(
                asset_platform_id=asset_platform_id, contract_address=contract_address, request_options=request_options
            )
        ).unwrap()

    async def nfts_id(
        self, *, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None
    ) -> Nftdata:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection ID

        Args:
            id: NFT collection ID. *refers to /reference/nfts-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT collection data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.nfts_id(id=id, request_options=request_options)).unwrap()

    async def nfts_list(
        self,
        *,
        order: Order7OrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[NftsList]:
        """To query all supported NFTs with ID, contract address, name, asset platform ID and symbol on CoinGecko

        Args:
            order: Sort order of responses.
            per_page: Total results per page. Valid values: 1...250
            page: Page through results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported NFTs

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.nfts_list(
                order=order, per_page=per_page, page=page, request_options=request_options
            )
        ).unwrap()

    async def onchain_simple_price(
        self,
        *,
        network: str = "eth",
        addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        include_market_cap: bool | None = None,
        mcap_fdv_fallback: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_price_change: bool | None = None,
        include_total_reserve_in_usd: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnchainSimplePrice:
        """To get token price based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include_market_cap: Include market capitalization. Default: ``false``
            mcap_fdv_fallback: Return FDV if market cap is not available. Default: ``false``
            include_24hr_vol: Include 24hr volume. Default: ``false``
            include_24hr_price_change: Include 24hr price change. Default: ``false``
            include_total_reserve_in_usd: Include total reserve in USD. Default: ``false``
            include_inactive_source: Include token price data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token price data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.onchain_simple_price(
                network=network,
                addresses=addresses,
                include_market_cap=include_market_cap,
                mcap_fdv_fallback=mcap_fdv_fallback,
                include_24hr_vol=include_24hr_vol,
                include_24hr_price_change=include_24hr_price_change,
                include_total_reserve_in_usd=include_total_reserve_in_usd,
                include_inactive_source=include_inactive_source,
                request_options=request_options,
            )
        ).unwrap()

    async def ping_server(self, *, request_options: RequestOptionsOrDict | None = None) -> PingServer:
        """To check the API server status

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Server status

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.ping_server(request_options=request_options)).unwrap()

    async def pool_address(
        self,
        *,
        network: str = "eth",
        address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolAddressData:
        """To query the specific pool based on the provided network and pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Pool address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Specific pool data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.pool_address(
                network=network,
                address=address,
                include=include,
                include_volume_breakdown=include_volume_breakdown,
                include_composition=include_composition,
                request_options=request_options,
            )
        ).unwrap()

    async def pool_ohlcv_contract_address(
        self,
        timeframe: TimeframeOrStr,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        aggregate: str | None = None,
        before_timestamp: int | None = None,
        limit: int | None = None,
        currency: CurrencyOrStr | None = None,
        token: str | None = None,
        include_empty_intervals: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Ohlcv:
        """To get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a
        network

        Args:
            timeframe: Timeframe of the OHLCV chart.
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            aggregate: Time period to aggregate each OHLCV. Available values (day): ``1`` Available values (hour):
                ``1``, ``4``, ``12`` Available values (minute): ``1``, ``5``, ``15`` Default value: 1
            before_timestamp: Return OHLCV data before this timestamp (integer seconds since epoch).
            limit: Number of OHLCV results to return, maximum 1000. Default value: 100
            currency: Return OHLCV in USD or quote token. Default: ``usd``
            token: Return OHLCV for token, use this to invert the chart. Available values: ``base``, ``quote``, or token
                address. Default: ``base``
            include_empty_intervals: Include empty intervals with no trade data. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool OHLCV chart data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.pool_ohlcv_contract_address(
                timeframe,
                network=network,
                pool_address=pool_address,
                aggregate=aggregate,
                before_timestamp=before_timestamp,
                limit=limit,
                currency=currency,
                token=token,
                include_empty_intervals=include_empty_intervals,
                request_options=request_options,
            )
        ).unwrap()

    async def pool_token_info_contract_address(
        self,
        *,
        network: str = "solana",
        pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt",
        include: Include2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolTokensInfo:
        """To query pool metadata (base and quote token details, image, socials, websites, description, contract
        address, etc.) based on a provided pool contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            include: Attributes to include.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool tokens info data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.pool_token_info_contract_address(
                network=network, pool_address=pool_address, include=include, request_options=request_options
            )
        ).unwrap()

    async def pool_trades_contract_address(
        self,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        trade_volume_in_usd_greater_than: float | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Trades:
        """To query the last 300 trades in the past 24 hours based on the provided pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            trade_volume_in_usd_greater_than: Filter trades by trade volume in USD greater than this value. Default
                value: 0
            token: Return trades for token, use this to invert the chart. Available values: ``base``, ``quote``, or
                token address. Default: ``base``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Last 300 trades in past 24 hours from a pool

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.pool_trades_contract_address(
                network=network,
                pool_address=pool_address,
                trade_volume_in_usd_greater_than=trade_volume_in_usd_greater_than,
                token=token,
                request_options=request_options,
            )
        ).unwrap()

    async def pools_addresses(
        self,
        *,
        network: str = "eth",
        addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiPoolAddressData:
        """To query multiple pools based on the provided network and pool addresses

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Pool contract address, comma-separated if more than one pool contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multiple pools data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.pools_addresses(
                network=network,
                addresses=addresses,
                include=include,
                include_volume_breakdown=include_volume_breakdown,
                include_composition=include_composition,
                request_options=request_options,
            )
        ).unwrap()

    async def public_treasury_entity(
        self,
        *,
        entity_id: str = "strategy",
        holding_amount_change: str | None = None,
        holding_change_percentage: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublicTreasuryEntity:
        """To query public companies' and governments' cryptocurrency holdings by entity ID

        Args:
            entity_id: Public company or government entity ID. *refers to /reference/entities-list.
            holding_amount_change: Include holding amount change for specified timeframes, comma-separated if querying
                more than 1 timeframe. Valid values: ``7d``, ``14d``, ``30d``, ``90d``, ``1y``, ``ytd``
            holding_change_percentage: Include holding change percentage for specified timeframes, comma-separated if
                querying more than 1 timeframe. Valid values: ``7d``, ``14d``, ``30d``, ``90d``, ``1y``, ``ytd``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Public company or government crypto treasury holdings data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.public_treasury_entity(
                entity_id=entity_id,
                holding_amount_change=holding_amount_change,
                holding_change_percentage=holding_change_percentage,
                request_options=request_options,
            )
        ).unwrap()

    async def public_treasury_entity_chart(
        self,
        *,
        entity_id: str = "strategy",
        coin_id: str = "bitcoin",
        days: str = "365",
        include_empty_intervals: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublicTreasuryEntityChart:
        """To query historical cryptocurrency holdings chart of public companies and governments by entity ID and coin
        ID

        Args:
            entity_id: Public company or government entity ID. *refers to /reference/entities-list.
            coin_id: Coin ID. e.g. ``bitcoin``, ``ethereum``, ``solana``, ``binancecoin``
            days: Data up to number of days ago. Valid values: ``7``, ``14``, ``30``, ``90``, ``180``, ``365``
            include_empty_intervals: Include empty intervals with no transaction data. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Crypto treasury holdings historical chart data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.public_treasury_entity_chart(
                entity_id=entity_id,
                coin_id=coin_id,
                days=days,
                include_empty_intervals=include_empty_intervals,
                request_options=request_options,
            )
        ).unwrap()

    async def public_treasury_transaction_history(
        self,
        *,
        entity_id: str = "strategy",
        per_page: int | None = None,
        page: int | None = None,
        order: Order6OrStr | None = None,
        coin_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublicTreasuryTransactionHistory:
        """To query public companies' and governments' cryptocurrency transaction history by entity ID

        Args:
            entity_id: Public company or government entity ID. *refers to /reference/entities-list.
            per_page: Total results per page. Default value: 100 Valid values: 1...250
            page: Page through results. Default value: 1
            order: Sort order of transactions. Default: ``date_desc``
            coin_ids: Filter transactions by coin IDs, comma-separated if querying more than 1 coin. *refers to
                /reference/coins-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Crypto treasury transaction history data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.public_treasury_transaction_history(
                entity_id=entity_id,
                per_page=per_page,
                page=page,
                order=order,
                coin_ids=coin_ids,
                request_options=request_options,
            )
        ).unwrap()

    async def search_data(self, query: str, *, request_options: RequestOptionsOrDict | None = None) -> Search:
        """To search for coins, categories and markets listed on CoinGecko

        Args:
            query: Search query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Search results

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.search_data(query, request_options=request_options)).unwrap()

    async def search_pools(
        self,
        *,
        query: str | None = "weth",
        network: str | None = None,
        include: str | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolSearch:
        """To search for pools across all networks by pool address, token name, token symbol, or token contract address

        Args:
            query: Search query: pool contract address, token name, token symbol, or token contract address.
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool search results

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.search_pools(
                query=query, network=network, include=include, page=page, request_options=request_options
            )
        ).unwrap()

    async def simple_price(
        self,
        *,
        vs_currencies: str = "usd",
        ids: str | None = "bitcoin",
        names: str | None = "Bitcoin",
        symbols: str | None = "btc",
        include_tokens: IncludeTokensOrStr | None = None,
        include_market_cap: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_change: bool | None = None,
        include_last_updated_at: bool | None = None,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> dict[str, SimplePrice]:
        """To query the prices of one or more coins by using their unique Coin API IDs, symbols, or names

        Args:
            vs_currencies: Target currency of coins, comma-separated if querying more than 1 currency. *refers to
                /reference/simple-supported-currencies
            ids: Coins' IDs, comma-separated if querying more than 1 coin. *refers to /reference/coins-list
            names: Coins' names, comma-separated if querying more than 1 coin.
            symbols: Coins' symbols, comma-separated if querying more than 1 coin.
            include_tokens: For ``symbols`` lookups, specify ``all`` to include all matching tokens. Default ``top``
                returns top-ranked tokens by market cap or volume.
            include_market_cap: Include market capitalization. Default: false
            include_24hr_vol: Include 24-hour trading volume. Default: false
            include_24hr_change: Include 24-hour change percentage. Default: false
            include_last_updated_at: Include last updated price time as a UNIX timestamp. Default: false
            precision: Decimal places for currency price value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Coin prices

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.simple_price(
                vs_currencies=vs_currencies,
                ids=ids,
                names=names,
                symbols=symbols,
                include_tokens=include_tokens,
                include_market_cap=include_market_cap,
                include_24hr_vol=include_24hr_vol,
                include_24hr_change=include_24hr_change,
                include_last_updated_at=include_last_updated_at,
                precision=precision,
                request_options=request_options,
            )
        ).unwrap()

    async def simple_supported_currencies(self, *, request_options: RequestOptionsOrDict | None = None) -> list[str]:
        """To query all the supported currencies on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported currencies

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.simple_supported_currencies(request_options=request_options)).unwrap()

    async def simple_token_price(
        self,
        *,
        id: str = "ethereum",
        contract_addresses: str = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
        vs_currencies: str = "usd",
        include_market_cap: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_change: bool | None = None,
        include_last_updated_at: bool | None = None,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> dict[str, SimplePrice]:
        """To query one or more token prices by using their token contract addresses

        Args:
            id: Asset platform's ID. *refers to /reference/asset-platforms-list
            contract_addresses: Token contract addresses, comma-separated if querying more than 1 token
            vs_currencies: Target currency of coins, comma-separated if querying more than 1 currency. *refers to
                /reference/simple-supported-currencies
            include_market_cap: Include market capitalization. Default: false
            include_24hr_vol: Include 24-hour trading volume. Default: false
            include_24hr_change: Include 24-hour change percentage. Default: false
            include_last_updated_at: Include last updated price time as a UNIX timestamp. Default: false
            precision: Decimal places for currency price value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token prices

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.simple_token_price(
                id=id,
                contract_addresses=contract_addresses,
                vs_currencies=vs_currencies,
                include_market_cap=include_market_cap,
                include_24hr_vol=include_24hr_vol,
                include_24hr_change=include_24hr_change,
                include_last_updated_at=include_last_updated_at,
                precision=precision,
                request_options=request_options,
            )
        ).unwrap()

    async def token_data_contract_address(
        self,
        *,
        network: str = "eth",
        address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenData:
        """To query specific token data based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include token data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.token_data_contract_address(
                network=network,
                address=address,
                include=include,
                include_composition=include_composition,
                include_inactive_source=include_inactive_source,
                request_options=request_options,
            )
        ).unwrap()

    async def token_info_contract_address(
        self,
        *,
        network: str = "solana",
        address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump",
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenInfo:
        """To query token metadata (name, symbol, CoinGecko ID, image, socials, websites, description, etc.) based on a
        provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token info data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.token_info_contract_address(
                network=network, address=address, request_options=request_options
            )
        ).unwrap()

    async def token_lists(
        self, *, asset_platform_id: str = "ethereum", request_options: RequestOptionsOrDict | None = None
    ) -> TokenLists:
        """To get full list of tokens of a blockchain network (asset platform) that is supported by `Ethereum token list
        standard <https://tokenlists.org/>`__

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token list by asset platform

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.token_lists(
                asset_platform_id=asset_platform_id, request_options=request_options
            )
        ).unwrap()

    async def tokens_data_contract_addresses(
        self,
        *,
        network: str = "solana",
        addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiTokenData:
        """To query multiple tokens data based on the provided token contract addresses on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multiple tokens data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.tokens_data_contract_addresses(
                network=network,
                addresses=addresses,
                include=include,
                include_composition=include_composition,
                include_inactive_source=include_inactive_source,
                request_options=request_options,
            )
        ).unwrap()

    async def tokens_info_recent_updated(
        self,
        *,
        include: Include3OrStr | None = None,
        network: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenInfoRecentlyUpdated:
        """To query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal

        Args:
            include: Attributes for related resources to include.
            network: Filter tokens by provided network. *refers to /reference/networks-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Most recently updated tokens info

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.tokens_info_recent_updated(
                include=include, network=network, request_options=request_options
            )
        ).unwrap()

    async def top_pools_contract_address(
        self,
        *,
        network: str = "eth",
        token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: str | None = None,
        include_inactive_source: bool | None = None,
        page: int | None = None,
        sort: Sort2OrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query top pools based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            token_address: Token contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_volume_usd_liquidity_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools for a token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.top_pools_contract_address(
                network=network,
                token_address=token_address,
                include=include,
                include_inactive_source=include_inactive_source,
                page=page,
                sort=sort,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def top_pools_dex(
        self,
        *,
        network: str = "eth",
        dex: str = "sushiswap",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the top pools based on the provided network and decentralized exchange (DEX)

        Args:
            network: Network ID. *refers to /reference/networks-list.
            dex: DEX ID. *refers to /reference/dexes-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools on a network's DEX

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.top_pools_dex(
                network=network,
                dex=dex,
                include=include,
                page=page,
                sort=sort,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def top_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the top pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.top_pools_network(
                network=network,
                include=include,
                page=page,
                sort=sort,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def trending_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the trending pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trending pools across all networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.trending_pools_list(
                include=include,
                page=page,
                duration=duration,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def trending_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query the trending pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trending pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.trending_pools_network(
                network=network,
                include=include,
                page=page,
                duration=duration,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def trending_search(self, *, request_options: RequestOptionsOrDict | None = None) -> TrendingSearch:
        """To query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trending search coins, NFTs and categories

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self.with_raw_response.trending_search(request_options=request_options)).unwrap()

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


class AsyncApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def asset_platforms_list(
        self, *, filter: FilterOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[AssetPlatform], RawError]:
        """To query all the supported asset platforms (blockchain networks) on CoinGecko

        Args:
            filter: Apply relevant filters to results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/asset_platforms"),
            query_params=[param[FilterOrStr | None]("filter", filter)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[AssetPlatform]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_categories(
        self, *, order: Order2OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Category1], RawError]:
        """To query all the coins categories with market data (market cap, volume, etc.) on CoinGecko

        Args:
            order: Sort results by field. Default: ``market_cap_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/categories"),
            query_params=[param[Order2OrStr | None]("order", order)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[Category1]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_categories_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CategoriesList], RawError]:
        """To query all the supported coins categories on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/categories/list"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[CategoriesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_contract_address(
        self,
        *,
        id: str = "ethereum",
        contract_address: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsContractAddress, RawError]:
        """To query all the metadata (image, websites, socials, description, contract address, etc.) and market data
        (price, ATH, exchange tickers, etc.) of a coin based on an asset platform and a particular token contract
        address

        Args:
            id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: The contract address of token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/contract/{contract_address}"),
            path_params=[param[str]("id", id), param[str]("contract_address", contract_address)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsContractAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_id(
        self,
        *,
        id: str = "bitcoin",
        localization: bool | None = None,
        tickers: bool | None = None,
        market_data: bool | None = None,
        community_data: bool | None = None,
        developer_data: bool | None = None,
        sparkline: bool | None = None,
        include_categories_details: bool | None = None,
        dex_pair_format: DexPairFormatOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsId, RawError]:
        """To query all the metadata (image, websites, socials, description, contract address, etc.) and market data
        (price, ATH, exchange tickers, etc.) of a coin based on a particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list
            localization: Include all localized languages in the response. Default: true
            tickers: Include tickers data. Default: true
            market_data: Include market data. Default: true
            community_data: Include community data. Default: true
            developer_data: Include developer data. Default: true
            sparkline: Include sparkline 7-day data. Default: false
            include_categories_details: Include categories details. Default: false
            dex_pair_format: Set to ``symbol`` to display DEX pair base and target as symbols. Default:
                ``contract_address``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[bool | None]("localization", localization),
                param[bool | None]("tickers", tickers),
                param[bool | None]("market_data", market_data),
                param[bool | None]("community_data", community_data),
                param[bool | None]("developer_data", developer_data),
                param[bool | None]("sparkline", sparkline),
                param[bool | None]("include_categories_details", include_categories_details),
                param[DexPairFormatOrStr | None]("dex_pair_format", dex_pair_format),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_id_history(
        self,
        *,
        id: str = "bitcoin",
        date: str = "30-12-2025",
        localization: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsIdHistory, RawError]:
        """To query the historical data (price, market cap, 24hrs volume, etc.) at a given date for a coin based on a
        particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list.
            date: The date of data snapshot. Format: ``dd-mm-yyyy``
            localization: Include all the localized languages in response. Default: true
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/history"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("date", date), param[bool | None]("localization", localization)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsIdHistory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_id_market_chart(
        self,
        *,
        id: str = "bitcoin",
        vs_currency: str = "usd",
        days: str = "1",
        interval: IntervalOrStr | None = None,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsMarketChart, RawError]:
        """To get the historical chart data of a coin including time in UNIX, price, market cap and 24hrs volume based
        on particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list.
            vs_currency: Target currency of market data. *refers to /reference/simple-supported-currencies.
            days: Data up to number of days ago. You may use any integer or ``max`` for number of days.
            interval: Data interval, leave empty for auto granularity.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/market_chart"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[str]("days", days),
                param[IntervalOrStr | None]("interval", interval),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsMarketChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_id_market_chart_range(
        self,
        *,
        id: str = "bitcoin",
        vs_currency: str = "usd",
        from_: int = 1767024000,
        to: int = 1777564800,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsMarketChart, RawError]:
        """To get the historical chart data of a coin within certain time range in UNIX along with price, market cap and
        24hrs volume based on particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list.
            vs_currency: Target currency of market data. *refers to /reference/simple-supported-currencies.
            from_: Starting date in UNIX timestamp.
            to: Ending date in UNIX timestamp.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/market_chart/range"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[int]("from", from_),
                param[int]("to", to),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsMarketChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_id_ohlc(
        self,
        days: DaysOrStr,
        *,
        id: str = "bitcoin",
        vs_currency: str = "usd",
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[list[float]], RawError]:
        """To get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin ID

        Args:
            days: Data up to number of days ago.
            id: Coin ID. *refers to /reference/coins-list.
            vs_currency: Target currency of price data. *refers to /reference/simple-supported-currencies.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/ohlc"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[DaysOrStr]("days", days),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[list[float]]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_id_tickers(
        self,
        *,
        id: str = "bitcoin",
        exchange_ids: str | None = None,
        include_exchange_logo: bool | None = None,
        page: int | None = None,
        order: Order1OrStr | None = None,
        depth: bool | None = None,
        dex_pair_format: DexPairFormatOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsIdTickers, RawError]:
        """To query the coin tickers on both centralized exchange (CEX) and decentralized exchange (DEX) based on a
        particular coin ID

        Args:
            id: Coin ID. *refers to /reference/coins-list
            exchange_ids: Exchange ID. *refers to /reference/exchanges-list
            include_exchange_logo: Include exchange logo. Default: false
            page: Page through results
            order: Sort the order of responses. Default: trust_score_desc
            depth: Include 2% orderbook depth, i.e. ``cost_to_move_up_usd`` and ``cost_to_move_down_usd``. Default:
                false
            dex_pair_format: Set to ``symbol`` to display DEX pair base and target as symbols. Default:
                ``contract_address``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/tickers"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str | None]("exchange_ids", exchange_ids),
                param[bool | None]("include_exchange_logo", include_exchange_logo),
                param[int | None]("page", page),
                param[Order1OrStr | None]("order", order),
                param[bool | None]("depth", depth),
                param[DexPairFormatOrStr | None]("dex_pair_format", dex_pair_format),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsIdTickers],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_list(
        self,
        *,
        include_platform: bool | None = None,
        status: StatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CoinsList], RawError]:
        """To query all the supported coins on CoinGecko with coin ID, name and symbol

        Args:
            include_platform: Include platform and token's contract addresses. Default: false
            status: Filter by status of coins. Default: active
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/list"),
            query_params=[
                param[bool | None]("include_platform", include_platform), param[StatusOrStr | None]("status", status)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[CoinsList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def coins_markets(
        self,
        *,
        vs_currency: str = "usd",
        ids: str | None = "bitcoin",
        names: str | None = "Bitcoin",
        symbols: str | None = "btc",
        include_tokens: IncludeTokensOrStr | None = None,
        category: str | None = None,
        order: OrderOrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        sparkline: bool | None = None,
        price_change_percentage: str | None = None,
        locale: LocaleOrStr | None = None,
        precision: PrecisionOrStr | None = None,
        include_rehypothecated: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CoinsMarket], RawError]:
        """To query all the supported coins with price, market cap, volume and market related data

        Args:
            vs_currency: Target currency of coins and market data. *refers to /reference/simple-supported-currencies
            ids: Coins' IDs, comma-separated if querying more than 1 coin. *refers to /reference/coins-list
            names: Coins' names, comma-separated if querying more than 1 coin.
            symbols: Coins' symbols, comma-separated if querying more than 1 coin.
            include_tokens: For ``symbols`` lookups, specify ``all`` to include all matching tokens. Default ``top``
                returns top-ranked tokens by market cap or volume.
            category: Filter based on coins' category. *refers to /reference/coins-categories-list
            order: Sort result by field. Default: market_cap_desc
            per_page: Total results per page. Default: 100 Valid values: 1...250
            page: Page through results. Default: 1
            sparkline: Include sparkline 7-day data. Default: false
            price_change_percentage: Include price change percentage timeframe, comma-separated if querying more than 1
                timeframe. Valid values: ``1h``, ``24h``, ``7d``, ``14d``, ``30d``, ``200d``, ``1y``
            locale: Language background. Default: en
            precision: Decimal places for currency price value
            include_rehypothecated: Include rehypothecated tokens in results. When true, returns
                ``market_cap_rank_with_rehypothecated`` field. Default: false
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/markets"),
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[str | None]("ids", ids),
                param[str | None]("names", names),
                param[str | None]("symbols", symbols),
                param[IncludeTokensOrStr | None]("include_tokens", include_tokens),
                param[str | None]("category", category),
                param[OrderOrStr | None]("order", order),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
                param[bool | None]("sparkline", sparkline),
                param[str | None]("price_change_percentage", price_change_percentage),
                param[LocaleOrStr | None]("locale", locale),
                param[PrecisionOrStr | None]("precision", precision),
                param[bool | None]("include_rehypothecated", include_rehypothecated),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[CoinsMarket]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def companies_public_treasury(
        self,
        entity: EntityOrStr,
        *,
        coin_id: str = "bitcoin",
        per_page: int | None = None,
        page: int | None = None,
        order: Order5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublicTreasury, RawError]:
        """To query public companies' and governments' cryptocurrency holdings by coin ID

        Args:
            entity: Public company or government entity.
            coin_id: Coin ID. e.g. ``bitcoin``, ``ethereum``, ``solana``, ``binancecoin``
            per_page: Total results per page. Default value: 250 Valid values: 1...250
            page: Page through results. Default value: 1
            order: Sort order for results. Default: ``total_holdings_usd_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/{entity}/public_treasury/{coin_id}"),
            path_params=[param[EntityOrStr]("entity", entity), param[str]("coin_id", coin_id)],
            query_params=[
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
                param[Order5OrStr | None]("order", order),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasury],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def contract_address_market_chart(
        self,
        *,
        id: str = "ethereum",
        contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
        vs_currency: str = "usd",
        days: str = "1",
        interval: IntervalOrStr | None = None,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsMarketChart, RawError]:
        """To get the historical chart data including time in UNIX, price, market cap and 24hrs volume based on asset
        platform and particular token contract address

        Args:
            id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: The contract address of token.
            vs_currency: Target currency of market data. *refers to /reference/simple-supported-currencies.
            days: Data up to number of days ago. You may use any integer or ``max`` for number of days.
            interval: Data interval, leave empty for auto granularity.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/contract/{contract_address}/market_chart"),
            path_params=[param[str]("id", id), param[str]("contract_address", contract_address)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[str]("days", days),
                param[IntervalOrStr | None]("interval", interval),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsMarketChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def contract_address_market_chart_range(
        self,
        *,
        id: str = "ethereum",
        contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
        vs_currency: str = "usd",
        from_: int = 1767024000,
        to: int = 1777564800,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsMarketChart, RawError]:
        """To get the historical chart data within certain time range in UNIX along with price, market cap and 24hrs
        volume based on asset platform and particular token contract address

        Args:
            id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: The contract address of token.
            vs_currency: Target currency of market data. *refers to /reference/simple-supported-currencies.
            from_: Starting date in UNIX timestamp.
            to: Ending date in UNIX timestamp.
            precision: Decimal place for currency price value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/contract/{contract_address}/market_chart/range"),
            path_params=[param[str]("id", id), param[str]("contract_address", contract_address)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[int]("from", from_),
                param[int]("to", to),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsMarketChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def crypto_global(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GlobalModel, RawError]:
        """To query cryptocurrency global data including active cryptocurrencies, markets, total crypto market cap and
        etc

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/global"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[GlobalModel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def derivatives_exchanges(
        self,
        *,
        order: Order4OrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DerivativesExchange], RawError]:
        """To query all the derivatives exchanges with related data (ID, name, open interest, ...) on CoinGecko

        Args:
            order: Sort order of responses. Default: ``open_interest_btc_desc``
            per_page: Total results per page.
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/derivatives/exchanges"),
            query_params=[
                param[Order4OrStr | None]("order", order),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[DerivativesExchange]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def derivatives_exchanges_id(
        self,
        *,
        id: str = "binance_futures",
        include_tickers: IncludeTickersOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DerivativesExchangesId, RawError]:
        """To query the derivatives exchange's related data (name, open interest, trade volume, ...) based on the
        exchange's ID

        Args:
            id: Derivative exchange ID. *refers to /reference/derivatives-exchanges-list.
            include_tickers: Include tickers data. Default: tickers data is not included.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/derivatives/exchanges/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[IncludeTickersOrStr | None]("include_tickers", include_tickers)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[DerivativesExchangesId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def derivatives_exchanges_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DerivativesExchangesList], RawError]:
        """To query all the supported derivatives exchanges with ID and name on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/derivatives/exchanges/list"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[DerivativesExchangesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def derivatives_tickers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DerivativesTicker], RawError]:
        """To query all the tickers from derivatives exchanges on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/derivatives"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[DerivativesTicker]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def dexes_list(
        self, *, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DexesList, RawError]:
        """To query all the supported decentralized exchanges (DEXs) based on the provided network on GeckoTerminal

        Args:
            network: Network ID. *refers to /reference/networks-list.
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/dexes"),
            path_params=[param[str]("network", network)],
            query_params=[param[int | None]("page", page)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[DexesList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def entities_list(
        self,
        *,
        entity_type: EntityTypeOrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[EntitiesList], RawError]:
        """To query all the supported entities on CoinGecko with entity ID, name, symbol, and country

        Args:
            entity_type: Filter by entity type.
            per_page: Total results per page. Default value: 100 Valid values: 1...250
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/entities/list"),
            query_params=[
                param[EntityTypeOrStr | None]("entity_type", entity_type),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[EntitiesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def exchange_rates(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExchangeRates, RawError]:
        """To query BTC exchange rates with other currencies

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchange_rates"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[ExchangeRates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def exchanges(
        self,
        *,
        per_page: float | None = None,
        page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Exchange1], RawError]:
        """To query all the supported exchanges with exchanges' data (ID, name, country, etc.) that have active trading
        volumes on CoinGecko

        Args:
            per_page: Total results per page. Default: 100. Valid values: 1...250
            page: Page through results. Default: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges"),
            query_params=[param[float | None]("per_page", per_page), param[float | None]("page", page)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[Exchange1]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def exchanges_id(
        self,
        *,
        id: str = "binance",
        dex_pair_format: DexPairFormatOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ExchangesId, RawError]:
        """To query exchange's data (name, year established, country, etc.), exchange volume in BTC and top 100 tickers
        based on exchange's ID

        Args:
            id: Exchange ID. *refers to /reference/exchanges-list.
            dex_pair_format: Set to ``symbol`` to display DEX pair base and target as symbols. Default:
                ``contract_address``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[DexPairFormatOrStr | None]("dex_pair_format", dex_pair_format)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[ExchangesId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def exchanges_id_tickers(
        self,
        *,
        id: str = "binance",
        coin_ids: str | None = None,
        include_exchange_logo: bool | None = None,
        page: float | None = None,
        depth: bool | None = None,
        order: Order3OrStr | None = None,
        dex_pair_format: DexPairFormatOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CoinsIdTickers, RawError]:
        """To query exchange's tickers based on exchange's ID

        Args:
            id: Exchange ID. *refers to /reference/exchanges-list.
            coin_ids: Filter tickers by coin IDs, comma-separated if querying more than 1 coin. *refers to
                /reference/coins-list.
            include_exchange_logo: Include exchange logo. Default: false
            page: Page through results.
            depth: Include 2% orderbook depth (cost_to_move_up_usd and cost_to_move_down_usd). Default: false
            order: Sort the order of responses. Default: ``trust_score_desc``
            dex_pair_format: Set to ``symbol`` to display DEX pair base and target as symbols. Default:
                ``contract_address``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges/{id}/tickers"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str | None]("coin_ids", coin_ids),
                param[bool | None]("include_exchange_logo", include_exchange_logo),
                param[float | None]("page", page),
                param[bool | None]("depth", depth),
                param[Order3OrStr | None]("order", order),
                param[DexPairFormatOrStr | None]("dex_pair_format", dex_pair_format),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsIdTickers],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def exchanges_id_volume_chart(
        self, days: DaysOrStr, *, id: str = "binance", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[list[ExchangeVolumeChart]], RawError]:
        """To query the historical volume chart data with time in UNIX and trading volume data in BTC based on
        exchange's ID

        Args:
            days: Data up to number of days ago.
            id: Exchange ID or derivative exchange ID. *refers to /reference/exchanges-list or
                /reference/derivatives-exchanges-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges/{id}/volume_chart"),
            path_params=[param[str]("id", id)],
            query_params=[param[DaysOrStr]("days", days)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[list[ExchangeVolumeChart]]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def exchanges_list(
        self, *, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ExchangesList], RawError]:
        """To query all the supported exchanges with ID and name

        Args:
            status: Filter by status of exchanges. Default: ``active``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges/list"),
            query_params=[param[StatusOrStr | None]("status", status)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[ExchangesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def global_defi(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GlobalDeFi, RawError]:
        """To query top 100 cryptocurrency global decentralized finance (DeFi) data including DeFi market cap, trading
        volume

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/global/decentralized_finance_defi"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[GlobalDeFi],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def latest_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the latest pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/new_pools"),
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def latest_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the latest pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/new_pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def networks_list(
        self, *, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NetworksList, RawError]:
        """To retrieve a list of all supported networks on GeckoTerminal

        Args:
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks"),
            query_params=[param[int | None]("page", page)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[NetworksList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def nfts_contract_address(
        self,
        *,
        asset_platform_id: str = "ethereum",
        contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Nftdata, RawError]:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection contract address
        and respective asset platform

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: Contract address of the NFT collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/{asset_platform_id}/contract/{contract_address}"),
            path_params=[
                param[str]("asset_platform_id", asset_platform_id), param[str]("contract_address", contract_address)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Nftdata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def nfts_id(
        self, *, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Nftdata, RawError]:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection ID

        Args:
            id: NFT collection ID. *refers to /reference/nfts-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Nftdata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def nfts_list(
        self,
        *,
        order: Order7OrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[NftsList], RawError]:
        """To query all supported NFTs with ID, contract address, name, asset platform ID and symbol on CoinGecko

        Args:
            order: Sort order of responses.
            per_page: Total results per page. Valid values: 1...250
            page: Page through results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/list"),
            query_params=[
                param[Order7OrStr | None]("order", order),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[NftsList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def onchain_simple_price(
        self,
        *,
        network: str = "eth",
        addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        include_market_cap: bool | None = None,
        mcap_fdv_fallback: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_price_change: bool | None = None,
        include_total_reserve_in_usd: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnchainSimplePrice, RawError]:
        """To get token price based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include_market_cap: Include market capitalization. Default: ``false``
            mcap_fdv_fallback: Return FDV if market cap is not available. Default: ``false``
            include_24hr_vol: Include 24hr volume. Default: ``false``
            include_24hr_price_change: Include 24hr price change. Default: ``false``
            include_total_reserve_in_usd: Include total reserve in USD. Default: ``false``
            include_inactive_source: Include token price data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/simple/networks/{network}/token_price/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[bool | None]("include_market_cap", include_market_cap),
                param[bool | None]("mcap_fdv_fallback", mcap_fdv_fallback),
                param[bool | None]("include_24hr_vol", include_24hr_vol),
                param[bool | None]("include_24hr_price_change", include_24hr_price_change),
                param[bool | None]("include_total_reserve_in_usd", include_total_reserve_in_usd),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[OnchainSimplePrice],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def ping_server(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PingServer, RawError]:
        """To check the API server status

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ping"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PingServer],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pool_address(
        self,
        *,
        network: str = "eth",
        address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolAddressData, RawError]:
        """To query the specific pool based on the provided network and pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Pool address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{address}"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_volume_breakdown", include_volume_breakdown),
                param[bool | None]("include_composition", include_composition),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolAddressData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pool_ohlcv_contract_address(
        self,
        timeframe: TimeframeOrStr,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        aggregate: str | None = None,
        before_timestamp: int | None = None,
        limit: int | None = None,
        currency: CurrencyOrStr | None = None,
        token: str | None = None,
        include_empty_intervals: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Ohlcv, RawError]:
        """To get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a
        network

        Args:
            timeframe: Timeframe of the OHLCV chart.
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            aggregate: Time period to aggregate each OHLCV. Available values (day): ``1`` Available values (hour):
                ``1``, ``4``, ``12`` Available values (minute): ``1``, ``5``, ``15`` Default value: 1
            before_timestamp: Return OHLCV data before this timestamp (integer seconds since epoch).
            limit: Number of OHLCV results to return, maximum 1000. Default value: 100
            currency: Return OHLCV in USD or quote token. Default: ``usd``
            token: Return OHLCV for token, use this to invert the chart. Available values: ``base``, ``quote``, or token
                address. Default: ``base``
            include_empty_intervals: Include empty intervals with no trade data. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}"),
            path_params=[
                param[str]("network", network),
                param[str]("pool_address", pool_address),
                param[TimeframeOrStr]("timeframe", timeframe),
            ],
            query_params=[
                param[str | None]("aggregate", aggregate),
                param[int | None]("before_timestamp", before_timestamp),
                param[int | None]("limit", limit),
                param[CurrencyOrStr | None]("currency", currency),
                param[str | None]("token", token),
                param[bool | None]("include_empty_intervals", include_empty_intervals),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Ohlcv],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pool_token_info_contract_address(
        self,
        *,
        network: str = "solana",
        pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt",
        include: Include2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolTokensInfo, RawError]:
        """To query pool metadata (base and quote token details, image, socials, websites, description, contract
        address, etc.) based on a provided pool contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            include: Attributes to include.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/info"),
            path_params=[param[str]("network", network), param[str]("pool_address", pool_address)],
            query_params=[param[Include2OrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolTokensInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pool_trades_contract_address(
        self,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        trade_volume_in_usd_greater_than: float | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Trades, RawError]:
        """To query the last 300 trades in the past 24 hours based on the provided pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            trade_volume_in_usd_greater_than: Filter trades by trade volume in USD greater than this value. Default
                value: 0
            token: Return trades for token, use this to invert the chart. Available values: ``base``, ``quote``, or
                token address. Default: ``base``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/trades"),
            path_params=[param[str]("network", network), param[str]("pool_address", pool_address)],
            query_params=[
                param[float | None]("trade_volume_in_usd_greater_than", trade_volume_in_usd_greater_than),
                param[str | None]("token", token),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Trades],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pools_addresses(
        self,
        *,
        network: str = "eth",
        addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiPoolAddressData, RawError]:
        """To query multiple pools based on the provided network and pool addresses

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Pool contract address, comma-separated if more than one pool contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/multi/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_volume_breakdown", include_volume_breakdown),
                param[bool | None]("include_composition", include_composition),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[MultiPoolAddressData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def public_treasury_entity(
        self,
        *,
        entity_id: str = "strategy",
        holding_amount_change: str | None = None,
        holding_change_percentage: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublicTreasuryEntity, RawError]:
        """To query public companies' and governments' cryptocurrency holdings by entity ID

        Args:
            entity_id: Public company or government entity ID. *refers to /reference/entities-list.
            holding_amount_change: Include holding amount change for specified timeframes, comma-separated if querying
                more than 1 timeframe. Valid values: ``7d``, ``14d``, ``30d``, ``90d``, ``1y``, ``ytd``
            holding_change_percentage: Include holding change percentage for specified timeframes, comma-separated if
                querying more than 1 timeframe. Valid values: ``7d``, ``14d``, ``30d``, ``90d``, ``1y``, ``ytd``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/public_treasury/{entity_id}"),
            path_params=[param[str]("entity_id", entity_id)],
            query_params=[
                param[str | None]("holding_amount_change", holding_amount_change),
                param[str | None]("holding_change_percentage", holding_change_percentage),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasuryEntity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def public_treasury_entity_chart(
        self,
        *,
        entity_id: str = "strategy",
        coin_id: str = "bitcoin",
        days: str = "365",
        include_empty_intervals: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublicTreasuryEntityChart, RawError]:
        """To query historical cryptocurrency holdings chart of public companies and governments by entity ID and coin
        ID

        Args:
            entity_id: Public company or government entity ID. *refers to /reference/entities-list.
            coin_id: Coin ID. e.g. ``bitcoin``, ``ethereum``, ``solana``, ``binancecoin``
            days: Data up to number of days ago. Valid values: ``7``, ``14``, ``30``, ``90``, ``180``, ``365``
            include_empty_intervals: Include empty intervals with no transaction data. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/public_treasury/{entity_id}/{coin_id}/holding_chart"),
            path_params=[param[str]("entity_id", entity_id), param[str]("coin_id", coin_id)],
            query_params=[
                param[str]("days", days), param[bool | None]("include_empty_intervals", include_empty_intervals)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasuryEntityChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def public_treasury_transaction_history(
        self,
        *,
        entity_id: str = "strategy",
        per_page: int | None = None,
        page: int | None = None,
        order: Order6OrStr | None = None,
        coin_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublicTreasuryTransactionHistory, RawError]:
        """To query public companies' and governments' cryptocurrency transaction history by entity ID

        Args:
            entity_id: Public company or government entity ID. *refers to /reference/entities-list.
            per_page: Total results per page. Default value: 100 Valid values: 1...250
            page: Page through results. Default value: 1
            order: Sort order of transactions. Default: ``date_desc``
            coin_ids: Filter transactions by coin IDs, comma-separated if querying more than 1 coin. *refers to
                /reference/coins-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/public_treasury/{entity_id}/transaction_history"),
            path_params=[param[str]("entity_id", entity_id)],
            query_params=[
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
                param[Order6OrStr | None]("order", order),
                param[str | None]("coin_ids", coin_ids),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasuryTransactionHistory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_data(
        self, query: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Search, RawError]:
        """To search for coins, categories and markets listed on CoinGecko

        Args:
            query: Search query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search"),
            query_params=[param[str]("query", query)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Search],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_pools(
        self,
        *,
        query: str | None = "weth",
        network: str | None = None,
        include: str | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolSearch, RawError]:
        """To search for pools across all networks by pool address, token name, token symbol, or token contract address

        Args:
            query: Search query: pool contract address, token name, token symbol, or token contract address.
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/search/pools"),
            query_params=[
                param[str | None]("query", query),
                param[str | None]("network", network),
                param[str | None]("include", include),
                param[int | None]("page", page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolSearch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def simple_price(
        self,
        *,
        vs_currencies: str = "usd",
        ids: str | None = "bitcoin",
        names: str | None = "Bitcoin",
        symbols: str | None = "btc",
        include_tokens: IncludeTokensOrStr | None = None,
        include_market_cap: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_change: bool | None = None,
        include_last_updated_at: bool | None = None,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[dict[str, SimplePrice], RawError]:
        """To query the prices of one or more coins by using their unique Coin API IDs, symbols, or names

        Args:
            vs_currencies: Target currency of coins, comma-separated if querying more than 1 currency. *refers to
                /reference/simple-supported-currencies
            ids: Coins' IDs, comma-separated if querying more than 1 coin. *refers to /reference/coins-list
            names: Coins' names, comma-separated if querying more than 1 coin.
            symbols: Coins' symbols, comma-separated if querying more than 1 coin.
            include_tokens: For ``symbols`` lookups, specify ``all`` to include all matching tokens. Default ``top``
                returns top-ranked tokens by market cap or volume.
            include_market_cap: Include market capitalization. Default: false
            include_24hr_vol: Include 24-hour trading volume. Default: false
            include_24hr_change: Include 24-hour change percentage. Default: false
            include_last_updated_at: Include last updated price time as a UNIX timestamp. Default: false
            precision: Decimal places for currency price value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/simple/price"),
            query_params=[
                param[str]("vs_currencies", vs_currencies),
                param[str | None]("ids", ids),
                param[str | None]("names", names),
                param[str | None]("symbols", symbols),
                param[IncludeTokensOrStr | None]("include_tokens", include_tokens),
                param[bool | None]("include_market_cap", include_market_cap),
                param[bool | None]("include_24hr_vol", include_24hr_vol),
                param[bool | None]("include_24hr_change", include_24hr_change),
                param[bool | None]("include_last_updated_at", include_last_updated_at),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[dict[str, SimplePrice]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def simple_supported_currencies(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """To query all the supported currencies on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/simple/supported_vs_currencies"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def simple_token_price(
        self,
        *,
        id: str = "ethereum",
        contract_addresses: str = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
        vs_currencies: str = "usd",
        include_market_cap: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_change: bool | None = None,
        include_last_updated_at: bool | None = None,
        precision: PrecisionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[dict[str, SimplePrice], RawError]:
        """To query one or more token prices by using their token contract addresses

        Args:
            id: Asset platform's ID. *refers to /reference/asset-platforms-list
            contract_addresses: Token contract addresses, comma-separated if querying more than 1 token
            vs_currencies: Target currency of coins, comma-separated if querying more than 1 currency. *refers to
                /reference/simple-supported-currencies
            include_market_cap: Include market capitalization. Default: false
            include_24hr_vol: Include 24-hour trading volume. Default: false
            include_24hr_change: Include 24-hour change percentage. Default: false
            include_last_updated_at: Include last updated price time as a UNIX timestamp. Default: false
            precision: Decimal places for currency price value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/simple/token_price/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("contract_addresses", contract_addresses),
                param[str]("vs_currencies", vs_currencies),
                param[bool | None]("include_market_cap", include_market_cap),
                param[bool | None]("include_24hr_vol", include_24hr_vol),
                param[bool | None]("include_24hr_change", include_24hr_change),
                param[bool | None]("include_last_updated_at", include_last_updated_at),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[dict[str, SimplePrice]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def token_data_contract_address(
        self,
        *,
        network: str = "eth",
        address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenData, RawError]:
        """To query specific token data based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include token data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{address}"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            query_params=[
                param[IncludeOrStr | None]("include", include),
                param[bool | None]("include_composition", include_composition),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def token_info_contract_address(
        self,
        *,
        network: str = "solana",
        address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenInfo, RawError]:
        """To query token metadata (name, symbol, CoinGecko ID, image, socials, websites, description, etc.) based on a
        provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{address}/info"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def token_lists(
        self, *, asset_platform_id: str = "ethereum", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TokenLists, RawError]:
        """To get full list of tokens of a blockchain network (asset platform) that is supported by `Ethereum token list
        standard <https://tokenlists.org/>`__

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/token_lists/{asset_platform_id}/all.json"),
            path_params=[param[str]("asset_platform_id", asset_platform_id)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenLists],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def tokens_data_contract_addresses(
        self,
        *,
        network: str = "solana",
        addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiTokenData, RawError]:
        """To query multiple tokens data based on the provided token contract addresses on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/multi/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[IncludeOrStr | None]("include", include),
                param[bool | None]("include_composition", include_composition),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[MultiTokenData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def tokens_info_recent_updated(
        self,
        *,
        include: Include3OrStr | None = None,
        network: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenInfoRecentlyUpdated, RawError]:
        """To query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal

        Args:
            include: Attributes for related resources to include.
            network: Filter tokens by provided network. *refers to /reference/networks-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/tokens/info_recently_updated"),
            query_params=[param[Include3OrStr | None]("include", include), param[str | None]("network", network)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenInfoRecentlyUpdated],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def top_pools_contract_address(
        self,
        *,
        network: str = "eth",
        token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: str | None = None,
        include_inactive_source: bool | None = None,
        page: int | None = None,
        sort: Sort2OrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query top pools based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            token_address: Token contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_volume_usd_liquidity_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{token_address}/pools"),
            path_params=[param[str]("network", network), param[str]("token_address", token_address)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_inactive_source", include_inactive_source),
                param[int | None]("page", page),
                param[Sort2OrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def top_pools_dex(
        self,
        *,
        network: str = "eth",
        dex: str = "sushiswap",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the top pools based on the provided network and decentralized exchange (DEX)

        Args:
            network: Network ID. *refers to /reference/networks-list.
            dex: DEX ID. *refers to /reference/dexes-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/dexes/{dex}/pools"),
            path_params=[param[str]("network", network), param[str]("dex", dex)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[SortOrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def top_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the top pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[SortOrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def trending_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the trending pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/trending_pools"),
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[DurationOrStr | None]("duration", duration),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def trending_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query the trending pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/trending_pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[DurationOrStr | None]("duration", duration),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def trending_search(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrendingSearch, RawError]:
        """To query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/trending"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TrendingSearch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


AsyncClient = AsyncCoinGeckoClient
