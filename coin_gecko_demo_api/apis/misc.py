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
from ..models.asset_platform import AssetPlatform
from ..models.enums.filter import FilterOrStr
from ..models.ping_server import PingServer
from ..models.token_lists import TokenLists
from ..server.server import Server


class Misc:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MiscWithRawResponse(client, server, auth)

    def asset_platforms_list(
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
        return self._with_raw_response.asset_platforms_list(filter=filter, request_options=request_options).unwrap()

    def ping_server(self, *, request_options: RequestOptionsOrDict | None = None) -> PingServer:
        """To check the API server status

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Server status

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.ping_server(request_options=request_options).unwrap()

    def token_lists(
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
        return self._with_raw_response.token_lists(
            asset_platform_id=asset_platform_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MiscWithRawResponse:
        return self._with_raw_response


class AsyncMisc:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMiscWithRawResponse(client, server, auth)

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
            await self._with_raw_response.asset_platforms_list(filter=filter, request_options=request_options)
        ).unwrap()

    async def ping_server(self, *, request_options: RequestOptionsOrDict | None = None) -> PingServer:
        """To check the API server status

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Server status

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.ping_server(request_options=request_options)).unwrap()

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
            await self._with_raw_response.token_lists(
                asset_platform_id=asset_platform_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMiscWithRawResponse:
        return self._with_raw_response


class MiscWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def asset_platforms_list(
        self, *, filter: FilterOrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[AssetPlatform], RawError]:
        """To query all the supported asset platforms (blockchain networks) on CoinGecko

        Args:
            filter: Apply relevant filters to results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/asset_platforms"),
            query_params=[param[FilterOrStr | None]("filter", filter)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[AssetPlatform]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def ping_server(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PingServer, RawError]:
        """To check the API server status

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ping"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PingServer],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def token_lists(
        self, *, asset_platform_id: str = "ethereum", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TokenLists, RawError]:
        """To get full list of tokens of a blockchain network (asset platform) that is supported by `Ethereum token list
        standard <https://tokenlists.org/>`__

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/token_lists/{asset_platform_id}/all.json"),
            path_params=[param[str]("asset_platform_id", asset_platform_id)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenLists],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMiscWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
