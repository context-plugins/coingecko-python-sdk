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
from ..models.enums.order7 import Order7OrStr
from ..models.nftdata import Nftdata
from ..models.nfts_list import NftsList
from ..server.server import Server


class Nfts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NftsWithRawResponse(client, server, auth)

    def nfts_contract_address(
        self,
        *,
        asset_platform_id: str = "ethereum",
        contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
        request_options: RequestOptionsOrDict | None = None,
    ) -> Nftdata:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection contract address
        and respective asset platform

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: Contract address of the NFT collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT collection data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.nfts_contract_address(
            asset_platform_id=asset_platform_id, contract_address=contract_address, request_options=request_options
        ).unwrap()

    def nfts_id(self, *, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None) -> Nftdata:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection ID

        Args:
            id: NFT collection ID. *refers to /reference/nfts-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT collection data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.nfts_id(id=id, request_options=request_options).unwrap()

    def nfts_list(
        self,
        *,
        order: Order7OrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[NftsList]:
        """To query all supported NFTs with ID, contract address, name, asset platform ID and symbol on CoinGecko

        Args:
            order: Sort order of responses.
            per_page: Total results per page. Valid values: 1...250
            page: Page through results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported NFTs

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.nfts_list(
            order=order, per_page=per_page, page=page, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NftsWithRawResponse:
        return self._with_raw_response


class AsyncNfts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNftsWithRawResponse(client, server, auth)

    async def nfts_contract_address(
        self,
        *,
        asset_platform_id: str = "ethereum",
        contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
        request_options: RequestOptionsOrDict | None = None,
    ) -> Nftdata:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection contract address
        and respective asset platform

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: Contract address of the NFT collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT collection data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.nfts_contract_address(
                asset_platform_id=asset_platform_id, contract_address=contract_address, request_options=request_options
            )
        ).unwrap()

    async def nfts_id(
        self, *, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None
    ) -> Nftdata:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection ID

        Args:
            id: NFT collection ID. *refers to /reference/nfts-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            NFT collection data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.nfts_id(id=id, request_options=request_options)).unwrap()

    async def nfts_list(
        self,
        *,
        order: Order7OrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[NftsList]:
        """To query all supported NFTs with ID, contract address, name, asset platform ID and symbol on CoinGecko

        Args:
            order: Sort order of responses.
            per_page: Total results per page. Valid values: 1...250
            page: Page through results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported NFTs

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.nfts_list(
                order=order, per_page=per_page, page=page, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNftsWithRawResponse:
        return self._with_raw_response


class NftsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfts_contract_address(
        self,
        *,
        asset_platform_id: str = "ethereum",
        contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Nftdata, RawError]:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection contract address
        and respective asset platform

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: Contract address of the NFT collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/{asset_platform_id}/contract/{contract_address}"),
            path_params=[
                param[str]("asset_platform_id", asset_platform_id), param[str]("contract_address", contract_address)
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Nftdata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def nfts_id(
        self, *, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Nftdata, RawError]:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection ID

        Args:
            id: NFT collection ID. *refers to /reference/nfts-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Nftdata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def nfts_list(
        self,
        *,
        order: Order7OrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[NftsList], RawError]:
        """To query all supported NFTs with ID, contract address, name, asset platform ID and symbol on CoinGecko

        Args:
            order: Sort order of responses.
            per_page: Total results per page. Valid values: 1...250
            page: Page through results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/list"),
            query_params=[
                param[Order7OrStr | None]("order", order),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[NftsList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNftsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfts_contract_address(
        self,
        *,
        asset_platform_id: str = "ethereum",
        contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Nftdata, RawError]:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection contract address
        and respective asset platform

        Args:
            asset_platform_id: Asset platform ID. *refers to /reference/asset-platforms-list.
            contract_address: Contract address of the NFT collection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/{asset_platform_id}/contract/{contract_address}"),
            path_params=[
                param[str]("asset_platform_id", asset_platform_id), param[str]("contract_address", contract_address)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Nftdata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def nfts_id(
        self, *, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Nftdata, RawError]:
        """To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection ID

        Args:
            id: NFT collection ID. *refers to /reference/nfts-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Nftdata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def nfts_list(
        self,
        *,
        order: Order7OrStr | None = None,
        per_page: int | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[NftsList], RawError]:
        """To query all supported NFTs with ID, contract address, name, asset platform ID and symbol on CoinGecko

        Args:
            order: Sort order of responses.
            per_page: Total results per page. Valid values: 1...250
            page: Page through results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nfts/list"),
            query_params=[
                param[Order7OrStr | None]("order", order),
                param[int | None]("per_page", per_page),
                param[int | None]("page", page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[list[NftsList]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
