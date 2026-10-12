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
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.search import Search
from ..models.trending_search import TrendingSearch
from ..server.server import Server


class SearchApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SearchApiWithRawResponse(client, server, auth)

    def search_data(self, query: str, *, request_options: RequestOptionsOrDict | None = None) -> Search:
        """To search for coins, categories and markets listed on CoinGecko

        Args:
            query: Search query
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Search results

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.search_data(query, request_options=request_options))

    def trending_search(self, *, request_options: RequestOptionsOrDict | None = None) -> TrendingSearch:
        """To query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Trending search coins, NFTs and categories

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.trending_search(request_options=request_options))

    @property
    def with_raw_response(self) -> SearchApiWithRawResponse:
        return self._with_raw_response


class AsyncSearchApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSearchApiWithRawResponse(client, server, auth)

    async def search_data(self, query: str, *, request_options: RequestOptionsOrDict | None = None) -> Search:
        """To search for coins, categories and markets listed on CoinGecko

        Args:
            query: Search query
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Search results

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.search_data(query, request_options=request_options))

    async def trending_search(self, *, request_options: RequestOptionsOrDict | None = None) -> TrendingSearch:
        """To query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Trending search coins, NFTs and categories

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.trending_search(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncSearchApiWithRawResponse:
        return self._with_raw_response


class SearchApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def search_data(
        self, query: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Search, RawError]:
        """To search for coins, categories and markets listed on CoinGecko

        Args:
            query: Search query
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search"),
            query_params=[param[str]("query", query)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Search],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def trending_search(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrendingSearch, RawError]:
        """To query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/trending"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TrendingSearch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSearchApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def search_data(
        self, query: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Search, RawError]:
        """To search for coins, categories and markets listed on CoinGecko

        Args:
            query: Search query
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search"),
            query_params=[param[str]("query", query)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=async_json_decoder[Search],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def trending_search(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TrendingSearch, RawError]:
        """To query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/trending"),
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=async_json_decoder[TrendingSearch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
