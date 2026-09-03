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
from ..models.derivatives_exchange import DerivativesExchange
from ..models.derivatives_exchanges_id import DerivativesExchangesId
from ..models.derivatives_exchanges_list import DerivativesExchangesList
from ..models.derivatives_ticker import DerivativesTicker
from ..models.enums.include_tickers import IncludeTickersOrStr
from ..models.enums.order4 import Order4OrStr
from ..server.server import Server


class Derivatives:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DerivativesWithRawResponse(client, server, auth)

    def derivatives_exchanges(
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
        return self._with_raw_response.derivatives_exchanges(
            order=order, per_page=per_page, page=page, request_options=request_options
        ).unwrap()

    def derivatives_exchanges_id(
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
        return self._with_raw_response.derivatives_exchanges_id(
            id=id, include_tickers=include_tickers, request_options=request_options
        ).unwrap()

    def derivatives_exchanges_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DerivativesExchangesList]:
        """To query all the supported derivatives exchanges with ID and name on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of derivative exchange identifiers and names

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.derivatives_exchanges_list(request_options=request_options).unwrap()

    def derivatives_tickers(self, *, request_options: RequestOptionsOrDict | None = None) -> list[DerivativesTicker]:
        """To query all the tickers from derivatives exchanges on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of derivative tickers

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.derivatives_tickers(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DerivativesWithRawResponse:
        return self._with_raw_response


class AsyncDerivatives:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDerivativesWithRawResponse(client, server, auth)

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
            await self._with_raw_response.derivatives_exchanges(
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
            await self._with_raw_response.derivatives_exchanges_id(
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
        return (await self._with_raw_response.derivatives_exchanges_list(request_options=request_options)).unwrap()

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
        return (await self._with_raw_response.derivatives_tickers(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDerivativesWithRawResponse:
        return self._with_raw_response


class DerivativesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def derivatives_exchanges(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/derivatives/exchanges"),
            query_params=[
                param[Order4OrStr | None]("order", order),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[DerivativesExchange]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def derivatives_exchanges_id(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/derivatives/exchanges/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[IncludeTickersOrStr | None]("include_tickers", include_tickers)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[DerivativesExchangesId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def derivatives_exchanges_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DerivativesExchangesList], RawError]:
        """To query all the supported derivatives exchanges with ID and name on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/derivatives/exchanges/list"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[DerivativesExchangesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def derivatives_tickers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DerivativesTicker], RawError]:
        """To query all the tickers from derivatives exchanges on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/derivatives"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[DerivativesTicker]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDerivativesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
