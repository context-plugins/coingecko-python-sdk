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
from ..models.entities_list import EntitiesList
from ..models.enums.entity import EntityOrStr
from ..models.enums.entity_type import EntityTypeOrStr
from ..models.enums.order5 import Order5OrStr
from ..models.unions.public_treasury import PublicTreasury
from ..server.server import Server


class Entities:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EntitiesWithRawResponse(client, server, auth)

    def companies_public_treasury(
        self,
        entity: EntityOrStr,
        *,
        coin_id: str = "bitcoin",
        per_page: int | None = None,
        page: int | None = None,
        order: Order5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublicTreasury:
        """To query public companies' and governments' cryptocurrency holdings by coin ID

        Args:
            entity: Public company or government entity.
            coin_id: Coin ID. e.g. ``bitcoin``, ``ethereum``, ``solana``, ``binancecoin``
            per_page: Total results per page. Default value: 250 Valid values: 1...250
            page: Page through results. Default value: 1
            order: Sort order for results. Default: ``total_holdings_usd_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Public companies or governments crypto treasury holdings data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.companies_public_treasury(
            entity, coin_id=coin_id, per_page=per_page, page=page, order=order, request_options=request_options
        ).unwrap()

    def entities_list(
        self,
        *,
        entity_type: EntityTypeOrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[EntitiesList]:
        """To query all the supported entities on CoinGecko with entity ID, name, symbol, and country

        Args:
            entity_type: Filter by entity type.
            per_page: Total results per page. Default value: 100 Valid values: 1...250
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of entities with ID, name, symbol, and country

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.entities_list(
            entity_type=entity_type, per_page=per_page, page=page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EntitiesWithRawResponse:
        return self._with_raw_response


class AsyncEntities:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEntitiesWithRawResponse(client, server, auth)

    async def companies_public_treasury(
        self,
        entity: EntityOrStr,
        *,
        coin_id: str = "bitcoin",
        per_page: int | None = None,
        page: int | None = None,
        order: Order5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublicTreasury:
        """To query public companies' and governments' cryptocurrency holdings by coin ID

        Args:
            entity: Public company or government entity.
            coin_id: Coin ID. e.g. ``bitcoin``, ``ethereum``, ``solana``, ``binancecoin``
            per_page: Total results per page. Default value: 250 Valid values: 1...250
            page: Page through results. Default value: 1
            order: Sort order for results. Default: ``total_holdings_usd_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Public companies or governments crypto treasury holdings data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.companies_public_treasury(
                entity, coin_id=coin_id, per_page=per_page, page=page, order=order, request_options=request_options
            )
        ).unwrap()

    async def entities_list(
        self,
        *,
        entity_type: EntityTypeOrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[EntitiesList]:
        """To query all the supported entities on CoinGecko with entity ID, name, symbol, and country

        Args:
            entity_type: Filter by entity type.
            per_page: Total results per page. Default value: 100 Valid values: 1...250
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of entities with ID, name, symbol, and country

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.entities_list(
                entity_type=entity_type, per_page=per_page, page=page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEntitiesWithRawResponse:
        return self._with_raw_response


class EntitiesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def companies_public_treasury(
        self,
        entity: EntityOrStr,
        *,
        coin_id: str = "bitcoin",
        per_page: int | None = None,
        page: int | None = None,
        order: Order5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublicTreasury, RawError]:
        """To query public companies' and governments' cryptocurrency holdings by coin ID

        Args:
            entity: Public company or government entity.
            coin_id: Coin ID. e.g. ``bitcoin``, ``ethereum``, ``solana``, ``binancecoin``
            per_page: Total results per page. Default value: 250 Valid values: 1...250
            page: Page through results. Default value: 1
            order: Sort order for results. Default: ``total_holdings_usd_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/{entity}/public_treasury/{coin_id}"),
            path_params=[param[EntityOrStr]("entity", entity), param[str]("coin_id", coin_id)],
            query_params=[
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
                param[Order5OrStr | None]("order", order),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasury],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def entities_list(
        self,
        *,
        entity_type: EntityTypeOrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[EntitiesList], RawError]:
        """To query all the supported entities on CoinGecko with entity ID, name, symbol, and country

        Args:
            entity_type: Filter by entity type.
            per_page: Total results per page. Default value: 100 Valid values: 1...250
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/entities/list"),
            query_params=[
                param[EntityTypeOrStr | None]("entity_type", entity_type),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[EntitiesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEntitiesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def companies_public_treasury(
        self,
        entity: EntityOrStr,
        *,
        coin_id: str = "bitcoin",
        per_page: int | None = None,
        page: int | None = None,
        order: Order5OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublicTreasury, RawError]:
        """To query public companies' and governments' cryptocurrency holdings by coin ID

        Args:
            entity: Public company or government entity.
            coin_id: Coin ID. e.g. ``bitcoin``, ``ethereum``, ``solana``, ``binancecoin``
            per_page: Total results per page. Default value: 250 Valid values: 1...250
            page: Page through results. Default value: 1
            order: Sort order for results. Default: ``total_holdings_usd_desc``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/{entity}/public_treasury/{coin_id}"),
            path_params=[param[EntityOrStr]("entity", entity), param[str]("coin_id", coin_id)],
            query_params=[
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
                param[Order5OrStr | None]("order", order),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PublicTreasury],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def entities_list(
        self,
        *,
        entity_type: EntityTypeOrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[EntitiesList], RawError]:
        """To query all the supported entities on CoinGecko with entity ID, name, symbol, and country

        Args:
            entity_type: Filter by entity type.
            per_page: Total results per page. Default value: 100 Valid values: 1...250
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/entities/list"),
            query_params=[
                param[EntityTypeOrStr | None]("entity_type", entity_type),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[EntitiesList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
