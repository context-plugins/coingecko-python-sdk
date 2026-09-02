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
from ..models.enums.order6 import Order6OrStr
from ..models.public_treasury_entity import PublicTreasuryEntity
from ..models.public_treasury_entity_chart import PublicTreasuryEntityChart
from ..models.public_treasury_transaction_history import PublicTreasuryTransactionHistory
from ..server.server import Server


class PublicTreasuryApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PublicTreasuryApiWithRawResponse(client, server, auth)

    def public_treasury_entity(
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
        return self._with_raw_response.public_treasury_entity(
            entity_id=entity_id,
            holding_amount_change=holding_amount_change,
            holding_change_percentage=holding_change_percentage,
            request_options=request_options,
        ).unwrap()

    def public_treasury_entity_chart(
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
        return self._with_raw_response.public_treasury_entity_chart(
            entity_id=entity_id,
            coin_id=coin_id,
            days=days,
            include_empty_intervals=include_empty_intervals,
            request_options=request_options,
        ).unwrap()

    def public_treasury_transaction_history(
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
        return self._with_raw_response.public_treasury_transaction_history(
            entity_id=entity_id,
            per_page=per_page,
            page=page,
            order=order,
            coin_ids=coin_ids,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> PublicTreasuryApiWithRawResponse:
        return self._with_raw_response


class AsyncPublicTreasuryApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPublicTreasuryApiWithRawResponse(client, server, auth)

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
            await self._with_raw_response.public_treasury_entity(
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
            await self._with_raw_response.public_treasury_entity_chart(
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
            await self._with_raw_response.public_treasury_transaction_history(
                entity_id=entity_id,
                per_page=per_page,
                page=page,
                order=order,
                coin_ids=coin_ids,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPublicTreasuryApiWithRawResponse:
        return self._with_raw_response


class PublicTreasuryApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def public_treasury_entity(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/public_treasury/{entity_id}"),
            path_params=[param[str]("entity_id", entity_id)],
            query_params=[
                param[str | None]("holding_amount_change", holding_amount_change),
                param[str | None]("holding_change_percentage", holding_change_percentage),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasuryEntity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def public_treasury_entity_chart(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/public_treasury/{entity_id}/{coin_id}/holding_chart"),
            path_params=[param[str]("entity_id", entity_id), param[str]("coin_id", coin_id)],
            query_params=[
                param[str]("days", days), param[bool | None]("include_empty_intervals", include_empty_intervals)
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasuryEntityChart],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def public_treasury_transaction_history(
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
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/public_treasury/{entity_id}/transaction_history"),
            path_params=[param[str]("entity_id", entity_id)],
            query_params=[
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
                param[Order6OrStr | None]("order", order),
                param[str | None]("coin_ids", coin_ids),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasuryTransactionHistory],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPublicTreasuryApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
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
