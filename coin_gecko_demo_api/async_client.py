from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.coins import AsyncCoins
from .apis.derivatives import AsyncDerivatives
from .apis.entities import AsyncEntities
from .apis.exchanges import AsyncExchanges
from .apis.global_api import AsyncGlobalApi
from .apis.misc import AsyncMisc
from .apis.nfts import AsyncNfts
from .apis.onchain import AsyncOnchain
from .apis.public_treasury_api import AsyncPublicTreasuryApi
from .apis.search_api import AsyncSearchApi
from .apis.simple import AsyncSimple
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseCoinGeckoDemoApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    ApiKeyQueryScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    no_auth,
    param,
)


class AsyncCoinGeckoDemoApiClient(BaseCoinGeckoDemoApiClient[AsyncRawClient]):
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
            global_headers=[
                param[str]("User-Agent", "CoinGeckoDemoApiClient/3.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "3.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            header_auth=ApiKeyHeaderScheme("x-cg-demo-api-key", header_auth) if header_auth is not None else no_auth,
            query_auth=ApiKeyQueryScheme("x_cg_demo_api_key", query_auth) if query_auth is not None else no_auth,
        )

    @cached_property
    def coins(self) -> AsyncCoins:
        return AsyncCoins(self._raw_client, self._server, self._auth)

    @cached_property
    def derivatives(self) -> AsyncDerivatives:
        return AsyncDerivatives(self._raw_client, self._server, self._auth)

    @cached_property
    def entities(self) -> AsyncEntities:
        return AsyncEntities(self._raw_client, self._server, self._auth)

    @cached_property
    def exchanges(self) -> AsyncExchanges:
        return AsyncExchanges(self._raw_client, self._server, self._auth)

    @cached_property
    def global_api(self) -> AsyncGlobalApi:
        return AsyncGlobalApi(self._raw_client, self._server, self._auth)

    @cached_property
    def misc(self) -> AsyncMisc:
        return AsyncMisc(self._raw_client, self._server, self._auth)

    @cached_property
    def nfts(self) -> AsyncNfts:
        return AsyncNfts(self._raw_client, self._server, self._auth)

    @cached_property
    def onchain(self) -> AsyncOnchain:
        return AsyncOnchain(self._raw_client, self._server, self._auth)

    @cached_property
    def public_treasury_api(self) -> AsyncPublicTreasuryApi:
        return AsyncPublicTreasuryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def search_api(self) -> AsyncSearchApi:
        return AsyncSearchApi(self._raw_client, self._server, self._auth)

    @cached_property
    def simple(self) -> AsyncSimple:
        return AsyncSimple(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncCoinGeckoDemoApiClient
