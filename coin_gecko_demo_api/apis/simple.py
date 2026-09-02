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
from ..models.enums.include_tokens import IncludeTokensOrStr
from ..models.enums.precision import PrecisionOrStr
from ..models.simple_price import SimplePrice
from ..server.server import Server


class Simple:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SimpleWithRawResponse(client, server, auth)

    def simple_price(
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
        return self._with_raw_response.simple_price(
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
        ).unwrap()

    def simple_supported_currencies(self, *, request_options: RequestOptionsOrDict | None = None) -> list[str]:
        """To query all the supported currencies on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported currencies

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.simple_supported_currencies(request_options=request_options).unwrap()

    def simple_token_price(
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
        return self._with_raw_response.simple_token_price(
            id=id,
            contract_addresses=contract_addresses,
            vs_currencies=vs_currencies,
            include_market_cap=include_market_cap,
            include_24hr_vol=include_24hr_vol,
            include_24hr_change=include_24hr_change,
            include_last_updated_at=include_last_updated_at,
            precision=precision,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SimpleWithRawResponse:
        return self._with_raw_response


class AsyncSimple:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSimpleWithRawResponse(client, server, auth)

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
            await self._with_raw_response.simple_price(
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
        return (await self._with_raw_response.simple_supported_currencies(request_options=request_options)).unwrap()

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
            await self._with_raw_response.simple_token_price(
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

    @property
    def with_raw_response(self) -> AsyncSimpleWithRawResponse:
        return self._with_raw_response


class SimpleWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def simple_price(
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
        return self._client.execute(
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
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[dict[str, SimplePrice]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def simple_supported_currencies(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """To query all the supported currencies on CoinGecko

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/simple/supported_vs_currencies"),
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def simple_token_price(
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
        return self._client.execute(
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
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[dict[str, SimplePrice]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSimpleWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
