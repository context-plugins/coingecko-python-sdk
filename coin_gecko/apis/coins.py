from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.categories_list import CategoriesList
from ..models.category1 import Category1
from ..models.coins_contract_address import CoinsContractAddress
from ..models.coins_id import CoinsId
from ..models.coins_id_history import CoinsIdHistory
from ..models.coins_id_tickers import CoinsIdTickers
from ..models.coins_list import CoinsList
from ..models.coins_market import CoinsMarket
from ..models.coins_market_chart import CoinsMarketChart
from ..models.enums.days import DaysOrStr
from ..models.enums.dex_pair_format import DexPairFormatOrStr
from ..models.enums.include_tokens import IncludeTokensOrStr
from ..models.enums.interval import IntervalOrStr
from ..models.enums.locale import LocaleOrStr
from ..models.enums.order import OrderOrStr
from ..models.enums.order1 import Order1OrStr
from ..models.enums.order2 import Order2OrStr
from ..models.enums.precision import PrecisionOrStr
from ..models.enums.status import StatusOrStr
from ..server.server import Server


class Coins:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CoinsWithRawResponse(client, server, auth)

    def coins_categories(
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
        return self._with_raw_response.coins_categories(order=order, request_options=request_options).unwrap()

    def coins_categories_list(self, *, request_options: RequestOptionsOrDict | None = None) -> list[CategoriesList]:
        """To query all the supported coins categories on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of coin categories

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.coins_categories_list(request_options=request_options).unwrap()

    def coins_contract_address(
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
        return self._with_raw_response.coins_contract_address(
            id=id, contract_address=contract_address, request_options=request_options
        ).unwrap()

    def coins_id(
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
        return self._with_raw_response.coins_id(
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
        ).unwrap()

    def coins_id_history(
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
        return self._with_raw_response.coins_id_history(
            id=id, date=date, localization=localization, request_options=request_options
        ).unwrap()

    def coins_id_market_chart(
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
        return self._with_raw_response.coins_id_market_chart(
            id=id,
            vs_currency=vs_currency,
            days=days,
            interval=interval,
            precision=precision,
            request_options=request_options,
        ).unwrap()

    def coins_id_market_chart_range(
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
        return self._with_raw_response.coins_id_market_chart_range(
            id=id, vs_currency=vs_currency, from_=from_, to=to, precision=precision, request_options=request_options
        ).unwrap()

    def coins_id_ohlc(
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
        return self._with_raw_response.coins_id_ohlc(
            days, id=id, vs_currency=vs_currency, precision=precision, request_options=request_options
        ).unwrap()

    def coins_id_tickers(
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
        return self._with_raw_response.coins_id_tickers(
            id=id,
            exchange_ids=exchange_ids,
            include_exchange_logo=include_exchange_logo,
            page=page,
            order=order,
            depth=depth,
            dex_pair_format=dex_pair_format,
            request_options=request_options,
        ).unwrap()

    def coins_list(
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
        return self._with_raw_response.coins_list(
            include_platform=include_platform, status=status, request_options=request_options
        ).unwrap()

    def coins_markets(
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
        return self._with_raw_response.coins_markets(
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
        ).unwrap()

    def contract_address_market_chart(
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
        return self._with_raw_response.contract_address_market_chart(
            id=id,
            contract_address=contract_address,
            vs_currency=vs_currency,
            days=days,
            interval=interval,
            precision=precision,
            request_options=request_options,
        ).unwrap()

    def contract_address_market_chart_range(
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
        return self._with_raw_response.contract_address_market_chart_range(
            id=id,
            contract_address=contract_address,
            vs_currency=vs_currency,
            from_=from_,
            to=to,
            precision=precision,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> CoinsWithRawResponse:
        return self._with_raw_response


class AsyncCoins:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCoinsWithRawResponse(client, server, auth)

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
        return (await self._with_raw_response.coins_categories(order=order, request_options=request_options)).unwrap()

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
        return (await self._with_raw_response.coins_categories_list(request_options=request_options)).unwrap()

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
            await self._with_raw_response.coins_contract_address(
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
            await self._with_raw_response.coins_id(
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
            await self._with_raw_response.coins_id_history(
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
            await self._with_raw_response.coins_id_market_chart(
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
            await self._with_raw_response.coins_id_market_chart_range(
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
            await self._with_raw_response.coins_id_ohlc(
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
            await self._with_raw_response.coins_id_tickers(
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
            await self._with_raw_response.coins_list(
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
            await self._with_raw_response.coins_markets(
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
            await self._with_raw_response.contract_address_market_chart(
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
            await self._with_raw_response.contract_address_market_chart_range(
                id=id,
                contract_address=contract_address,
                vs_currency=vs_currency,
                from_=from_,
                to=to,
                precision=precision,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCoinsWithRawResponse:
        return self._with_raw_response


class CoinsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def coins_categories(
        self, *, order: Order2OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Category1], RawError]:
        """To query all the coins categories with market data (market cap, volume, etc.) on CoinGecko

        Args:
            order: Sort results by field. Default: ``market_cap_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/categories"),
            query_params=[param[Order2OrStr | None]("order", order)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[Category1]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_categories_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CategoriesList], RawError]:
        """To query all the supported coins categories on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/categories/list"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[CategoriesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_contract_address(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/contract/{contract_address}"),
            path_params=[param[str]("id", id), param[str]("contract_address", contract_address)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsContractAddress],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_id(
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
        return self._client.execute(
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
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_id_history(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/history"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("date", date), param[bool | None]("localization", localization)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsIdHistory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_id_market_chart(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/market_chart"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[str]("days", days),
                param[IntervalOrStr | None]("interval", interval),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsMarketChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_id_market_chart_range(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/market_chart/range"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[int]("from", from_),
                param[int]("to", to),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsMarketChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_id_ohlc(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/ohlc"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[DaysOrStr]("days", days),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[list[float]]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_id_tickers(
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
        return self._client.execute(
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
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsIdTickers],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_list(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/list"),
            query_params=[
                param[bool | None]("include_platform", include_platform), param[StatusOrStr | None]("status", status)
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[CoinsList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def coins_markets(
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
        return self._client.execute(
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
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[CoinsMarket]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def contract_address_market_chart(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/contract/{contract_address}/market_chart"),
            path_params=[param[str]("id", id), param[str]("contract_address", contract_address)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[str]("days", days),
                param[IntervalOrStr | None]("interval", interval),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsMarketChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def contract_address_market_chart_range(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/coins/{id}/contract/{contract_address}/market_chart/range"),
            path_params=[param[str]("id", id), param[str]("contract_address", contract_address)],
            query_params=[
                param[str]("vs_currency", vs_currency),
                param[int]("from", from_),
                param[int]("to", to),
                param[PrecisionOrStr | None]("precision", precision),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsMarketChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCoinsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
