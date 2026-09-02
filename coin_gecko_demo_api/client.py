from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.coins import Coins
from .apis.derivatives import Derivatives
from .apis.entities import Entities
from .apis.exchanges import Exchanges
from .apis.global_api import GlobalApi
from .apis.misc import Misc
from .apis.nfts import Nfts
from .apis.onchain import Onchain
from .apis.public_treasury_api import PublicTreasuryApi
from .apis.search_api import SearchApi
from .apis.simple import Simple
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseCoinGeckoDemoApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    ApiKeyQueryScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    no_auth,
    param,
)


class CoinGeckoDemoApiClient(BaseCoinGeckoDemoApiClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        header_auth: str | None = None,
        query_auth: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "CoinGeckoDemoApiClient/3.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "3.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            header_auth=ApiKeyHeaderScheme("x-cg-demo-api-key", header_auth) if header_auth is not None else no_auth,
            query_auth=ApiKeyQueryScheme("x_cg_demo_api_key", query_auth) if query_auth is not None else no_auth,
        )

    @cached_property
    def coins(self) -> Coins:
        return Coins(self._raw_client, self._server, self._auth)

    @cached_property
    def derivatives(self) -> Derivatives:
        return Derivatives(self._raw_client, self._server, self._auth)

    @cached_property
    def entities(self) -> Entities:
        return Entities(self._raw_client, self._server, self._auth)

    @cached_property
    def exchanges(self) -> Exchanges:
        return Exchanges(self._raw_client, self._server, self._auth)

    @cached_property
    def global_api(self) -> GlobalApi:
        return GlobalApi(self._raw_client, self._server, self._auth)

    @cached_property
    def misc(self) -> Misc:
        return Misc(self._raw_client, self._server, self._auth)

    @cached_property
    def nfts(self) -> Nfts:
        return Nfts(self._raw_client, self._server, self._auth)

    @cached_property
    def onchain(self) -> Onchain:
        return Onchain(self._raw_client, self._server, self._auth)

    @cached_property
    def public_treasury_api(self) -> PublicTreasuryApi:
        return PublicTreasuryApi(self._raw_client, self._server, self._auth)

    @cached_property
    def search_api(self) -> SearchApi:
        return SearchApi(self._raw_client, self._server, self._auth)

    @cached_property
    def simple(self) -> Simple:
        return Simple(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = CoinGeckoDemoApiClient
