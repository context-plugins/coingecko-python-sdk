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
    raw_error_response,
)
from ..models.global_de_fi import GlobalDeFi
from ..models.global_model import GlobalModel
from ..server.server import Server


class GlobalApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GlobalApiWithRawResponse(client, server, auth)

    def crypto_global(self, *, request_options: RequestOptionsOrDict | None = None) -> GlobalModel:
        """To query cryptocurrency global data including active cryptocurrencies, markets, total crypto market cap and
        etc

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cryptocurrency global market data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.crypto_global(request_options=request_options).unwrap()

    def global_defi(self, *, request_options: RequestOptionsOrDict | None = None) -> GlobalDeFi:
        """To query top 100 cryptocurrency global decentralized finance (DeFi) data including DeFi market cap, trading
        volume

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Global decentralized finance (DeFi) market data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.global_defi(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GlobalApiWithRawResponse:
        return self._with_raw_response


class AsyncGlobalApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGlobalApiWithRawResponse(client, server, auth)

    async def crypto_global(self, *, request_options: RequestOptionsOrDict | None = None) -> GlobalModel:
        """To query cryptocurrency global data including active cryptocurrencies, markets, total crypto market cap and
        etc

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Cryptocurrency global market data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.crypto_global(request_options=request_options)).unwrap()

    async def global_defi(self, *, request_options: RequestOptionsOrDict | None = None) -> GlobalDeFi:
        """To query top 100 cryptocurrency global decentralized finance (DeFi) data including DeFi market cap, trading
        volume

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Global decentralized finance (DeFi) market data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.global_defi(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncGlobalApiWithRawResponse:
        return self._with_raw_response


class GlobalApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def crypto_global(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GlobalModel, RawError]:
        """To query cryptocurrency global data including active cryptocurrencies, markets, total crypto market cap and
        etc

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/global"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[GlobalModel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def global_defi(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GlobalDeFi, RawError]:
        """To query top 100 cryptocurrency global decentralized finance (DeFi) data including DeFi market cap, trading
        volume

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/global/decentralized_finance_defi"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[GlobalDeFi],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncGlobalApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
