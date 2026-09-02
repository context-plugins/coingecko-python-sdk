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
from ..models.coins_id_tickers import CoinsIdTickers
from ..models.enums.days import DaysOrStr
from ..models.enums.dex_pair_format import DexPairFormatOrStr
from ..models.enums.order3 import Order3OrStr
from ..models.enums.status import StatusOrStr
from ..models.exchange1 import Exchange1
from ..models.exchange_rates import ExchangeRates
from ..models.exchanges_id import ExchangesId
from ..models.exchanges_list import ExchangesList
from ..models.unions.exchange_volume_chart import ExchangeVolumeChart
from ..server.server import Server


class Exchanges:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ExchangesWithRawResponse(client, server, auth)

    def exchange_rates(self, *, request_options: RequestOptionsOrDict | None = None) -> ExchangeRates:
        """To query BTC exchange rates with other currencies

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            BTC exchange rates with other currencies

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.exchange_rates(request_options=request_options).unwrap()

    def exchanges(
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
        return self._with_raw_response.exchanges(per_page=per_page, page=page, request_options=request_options).unwrap()

    def exchanges_id(
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
        return self._with_raw_response.exchanges_id(
            id=id, dex_pair_format=dex_pair_format, request_options=request_options
        ).unwrap()

    def exchanges_id_tickers(
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
        return self._with_raw_response.exchanges_id_tickers(
            id=id,
            coin_ids=coin_ids,
            include_exchange_logo=include_exchange_logo,
            page=page,
            depth=depth,
            order=order,
            dex_pair_format=dex_pair_format,
            request_options=request_options,
        ).unwrap()

    def exchanges_id_volume_chart(
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
        return self._with_raw_response.exchanges_id_volume_chart(days, id=id, request_options=request_options).unwrap()

    def exchanges_list(
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
        return self._with_raw_response.exchanges_list(status=status, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ExchangesWithRawResponse:
        return self._with_raw_response


class AsyncExchanges:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncExchangesWithRawResponse(client, server, auth)

    async def exchange_rates(self, *, request_options: RequestOptionsOrDict | None = None) -> ExchangeRates:
        """To query BTC exchange rates with other currencies

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            BTC exchange rates with other currencies

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.exchange_rates(request_options=request_options)).unwrap()

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
            await self._with_raw_response.exchanges(per_page=per_page, page=page, request_options=request_options)
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
            await self._with_raw_response.exchanges_id(
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
            await self._with_raw_response.exchanges_id_tickers(
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
            await self._with_raw_response.exchanges_id_volume_chart(days, id=id, request_options=request_options)
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
        return (await self._with_raw_response.exchanges_list(status=status, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncExchangesWithRawResponse:
        return self._with_raw_response


class ExchangesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def exchange_rates(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExchangeRates, RawError]:
        """To query BTC exchange rates with other currencies

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchange_rates"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[ExchangeRates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def exchanges(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges"),
            query_params=[param[float | None]("per_page", per_page), param[float | None]("page", page)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[Exchange1]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def exchanges_id(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[DexPairFormatOrStr | None]("dex_pair_format", dex_pair_format)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[ExchangesId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def exchanges_id_tickers(
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
        return self._client.execute(
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
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[CoinsIdTickers],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def exchanges_id_volume_chart(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges/{id}/volume_chart"),
            path_params=[param[str]("id", id)],
            query_params=[param[DaysOrStr]("days", days)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[list[ExchangeVolumeChart]]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def exchanges_list(
        self, *, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ExchangesList], RawError]:
        """To query all the supported exchanges with ID and name

        Args:
            status: Filter by status of exchanges. Default: ``active``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/exchanges/list"),
            query_params=[param[StatusOrStr | None]("status", status)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[ExchangesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncExchangesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
