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
from ..models.dexes_list import DexesList
from ..models.enums.currency import CurrencyOrStr
from ..models.enums.duration import DurationOrStr
from ..models.enums.include import IncludeOrStr
from ..models.enums.include2 import Include2OrStr
from ..models.enums.include3 import Include3OrStr
from ..models.enums.sort import SortOrStr
from ..models.enums.sort2 import Sort2OrStr
from ..models.enums.timeframe import TimeframeOrStr
from ..models.multi_pool_address_data import MultiPoolAddressData
from ..models.multi_token_data import MultiTokenData
from ..models.networks_list import NetworksList
from ..models.ohlcv import Ohlcv
from ..models.onchain_simple_price import OnchainSimplePrice
from ..models.pool import Pool
from ..models.pool_address_data import PoolAddressData
from ..models.pool_search import PoolSearch
from ..models.pool_tokens_info import PoolTokensInfo
from ..models.token_data import TokenData
from ..models.token_info import TokenInfo
from ..models.token_info_recently_updated import TokenInfoRecentlyUpdated
from ..models.trades import Trades
from ..server.server import Server


class Onchain:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnchainWithRawResponse(client, server, auth)

    def dexes_list(
        self, *, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DexesList:
        """To query all the supported decentralized exchanges (DEXs) based on the provided network on GeckoTerminal

        Args:
            network: Network ID. *refers to /reference/networks-list.
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported DEXs on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dexes_list(network=network, page=page, request_options=request_options).unwrap()

    def latest_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the latest pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Latest pools across all networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.latest_pools_list(
            include=include,
            page=page,
            include_gt_community_data=include_gt_community_data,
            request_options=request_options,
        ).unwrap()

    def latest_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the latest pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Latest pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.latest_pools_network(
            network=network,
            include=include,
            page=page,
            include_gt_community_data=include_gt_community_data,
            request_options=request_options,
        ).unwrap()

    def networks_list(
        self, *, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NetworksList:
        """To retrieve a list of all supported networks on GeckoTerminal

        Args:
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.networks_list(page=page, request_options=request_options).unwrap()

    def onchain_simple_price(
        self,
        *,
        network: str = "eth",
        addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        include_market_cap: bool | None = None,
        mcap_fdv_fallback: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_price_change: bool | None = None,
        include_total_reserve_in_usd: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnchainSimplePrice:
        """To get token price based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include_market_cap: Include market capitalization. Default: ``false``
            mcap_fdv_fallback: Return FDV if market cap is not available. Default: ``false``
            include_24hr_vol: Include 24hr volume. Default: ``false``
            include_24hr_price_change: Include 24hr price change. Default: ``false``
            include_total_reserve_in_usd: Include total reserve in USD. Default: ``false``
            include_inactive_source: Include token price data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token price data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.onchain_simple_price(
            network=network,
            addresses=addresses,
            include_market_cap=include_market_cap,
            mcap_fdv_fallback=mcap_fdv_fallback,
            include_24hr_vol=include_24hr_vol,
            include_24hr_price_change=include_24hr_price_change,
            include_total_reserve_in_usd=include_total_reserve_in_usd,
            include_inactive_source=include_inactive_source,
            request_options=request_options,
        ).unwrap()

    def pool_address(
        self,
        *,
        network: str = "eth",
        address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolAddressData:
        """To query the specific pool based on the provided network and pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Pool address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Specific pool data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pool_address(
            network=network,
            address=address,
            include=include,
            include_volume_breakdown=include_volume_breakdown,
            include_composition=include_composition,
            request_options=request_options,
        ).unwrap()

    def pool_ohlcv_contract_address(
        self,
        timeframe: TimeframeOrStr,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        aggregate: str | None = None,
        before_timestamp: int | None = None,
        limit: int | None = None,
        currency: CurrencyOrStr | None = None,
        token: str | None = None,
        include_empty_intervals: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Ohlcv:
        """To get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a
        network

        Args:
            timeframe: Timeframe of the OHLCV chart.
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            aggregate: Time period to aggregate each OHLCV. Available values (day): ``1`` Available values (hour):
                ``1``, ``4``, ``12`` Available values (minute): ``1``, ``5``, ``15`` Default value: 1
            before_timestamp: Return OHLCV data before this timestamp (integer seconds since epoch).
            limit: Number of OHLCV results to return, maximum 1000. Default value: 100
            currency: Return OHLCV in USD or quote token. Default: ``usd``
            token: Return OHLCV for token, use this to invert the chart. Available values: ``base``, ``quote``, or token
                address. Default: ``base``
            include_empty_intervals: Include empty intervals with no trade data. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool OHLCV chart data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pool_ohlcv_contract_address(
            timeframe,
            network=network,
            pool_address=pool_address,
            aggregate=aggregate,
            before_timestamp=before_timestamp,
            limit=limit,
            currency=currency,
            token=token,
            include_empty_intervals=include_empty_intervals,
            request_options=request_options,
        ).unwrap()

    def pool_token_info_contract_address(
        self,
        *,
        network: str = "solana",
        pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt",
        include: Include2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolTokensInfo:
        """To query pool metadata (base and quote token details, image, socials, websites, description, contract
        address, etc.) based on a provided pool contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            include: Attributes to include.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool tokens info data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pool_token_info_contract_address(
            network=network, pool_address=pool_address, include=include, request_options=request_options
        ).unwrap()

    def pool_trades_contract_address(
        self,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        trade_volume_in_usd_greater_than: float | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Trades:
        """To query the last 300 trades in the past 24 hours based on the provided pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            trade_volume_in_usd_greater_than: Filter trades by trade volume in USD greater than this value. Default
                value: 0
            token: Return trades for token, use this to invert the chart. Available values: ``base``, ``quote``, or
                token address. Default: ``base``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Last 300 trades in past 24 hours from a pool

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pool_trades_contract_address(
            network=network,
            pool_address=pool_address,
            trade_volume_in_usd_greater_than=trade_volume_in_usd_greater_than,
            token=token,
            request_options=request_options,
        ).unwrap()

    def pools_addresses(
        self,
        *,
        network: str = "eth",
        addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiPoolAddressData:
        """To query multiple pools based on the provided network and pool addresses

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Pool contract address, comma-separated if more than one pool contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multiple pools data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pools_addresses(
            network=network,
            addresses=addresses,
            include=include,
            include_volume_breakdown=include_volume_breakdown,
            include_composition=include_composition,
            request_options=request_options,
        ).unwrap()

    def search_pools(
        self,
        *,
        query: str | None = "weth",
        network: str | None = None,
        include: str | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolSearch:
        """To search for pools across all networks by pool address, token name, token symbol, or token contract address

        Args:
            query: Search query: pool contract address, token name, token symbol, or token contract address.
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool search results

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_pools(
            query=query, network=network, include=include, page=page, request_options=request_options
        ).unwrap()

    def token_data_contract_address(
        self,
        *,
        network: str = "eth",
        address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenData:
        """To query specific token data based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include token data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.token_data_contract_address(
            network=network,
            address=address,
            include=include,
            include_composition=include_composition,
            include_inactive_source=include_inactive_source,
            request_options=request_options,
        ).unwrap()

    def token_info_contract_address(
        self,
        *,
        network: str = "solana",
        address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump",
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenInfo:
        """To query token metadata (name, symbol, CoinGecko ID, image, socials, websites, description, etc.) based on a
        provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token info data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.token_info_contract_address(
            network=network, address=address, request_options=request_options
        ).unwrap()

    def tokens_data_contract_addresses(
        self,
        *,
        network: str = "solana",
        addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiTokenData:
        """To query multiple tokens data based on the provided token contract addresses on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multiple tokens data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.tokens_data_contract_addresses(
            network=network,
            addresses=addresses,
            include=include,
            include_composition=include_composition,
            include_inactive_source=include_inactive_source,
            request_options=request_options,
        ).unwrap()

    def tokens_info_recent_updated(
        self,
        *,
        include: Include3OrStr | None = None,
        network: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenInfoRecentlyUpdated:
        """To query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal

        Args:
            include: Attributes for related resources to include.
            network: Filter tokens by provided network. *refers to /reference/networks-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Most recently updated tokens info

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.tokens_info_recent_updated(
            include=include, network=network, request_options=request_options
        ).unwrap()

    def top_pools_contract_address(
        self,
        *,
        network: str = "eth",
        token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: str | None = None,
        include_inactive_source: bool | None = None,
        page: int | None = None,
        sort: Sort2OrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query top pools based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            token_address: Token contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_volume_usd_liquidity_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools for a token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.top_pools_contract_address(
            network=network,
            token_address=token_address,
            include=include,
            include_inactive_source=include_inactive_source,
            page=page,
            sort=sort,
            include_gt_community_data=include_gt_community_data,
            request_options=request_options,
        ).unwrap()

    def top_pools_dex(
        self,
        *,
        network: str = "eth",
        dex: str = "sushiswap",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the top pools based on the provided network and decentralized exchange (DEX)

        Args:
            network: Network ID. *refers to /reference/networks-list.
            dex: DEX ID. *refers to /reference/dexes-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools on a network's DEX

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.top_pools_dex(
            network=network,
            dex=dex,
            include=include,
            page=page,
            sort=sort,
            include_gt_community_data=include_gt_community_data,
            request_options=request_options,
        ).unwrap()

    def top_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the top pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.top_pools_network(
            network=network,
            include=include,
            page=page,
            sort=sort,
            include_gt_community_data=include_gt_community_data,
            request_options=request_options,
        ).unwrap()

    def trending_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the trending pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trending pools across all networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.trending_pools_list(
            include=include,
            page=page,
            duration=duration,
            include_gt_community_data=include_gt_community_data,
            request_options=request_options,
        ).unwrap()

    def trending_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query the trending pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trending pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.trending_pools_network(
            network=network,
            include=include,
            page=page,
            duration=duration,
            include_gt_community_data=include_gt_community_data,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> OnchainWithRawResponse:
        return self._with_raw_response


class AsyncOnchain:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnchainWithRawResponse(client, server, auth)

    async def dexes_list(
        self, *, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DexesList:
        """To query all the supported decentralized exchanges (DEXs) based on the provided network on GeckoTerminal

        Args:
            network: Network ID. *refers to /reference/networks-list.
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported DEXs on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dexes_list(network=network, page=page, request_options=request_options)
        ).unwrap()

    async def latest_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the latest pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Latest pools across all networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.latest_pools_list(
                include=include,
                page=page,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def latest_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the latest pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Latest pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.latest_pools_network(
                network=network,
                include=include,
                page=page,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def networks_list(
        self, *, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NetworksList:
        """To retrieve a list of all supported networks on GeckoTerminal

        Args:
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of supported networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.networks_list(page=page, request_options=request_options)).unwrap()

    async def onchain_simple_price(
        self,
        *,
        network: str = "eth",
        addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        include_market_cap: bool | None = None,
        mcap_fdv_fallback: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_price_change: bool | None = None,
        include_total_reserve_in_usd: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnchainSimplePrice:
        """To get token price based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include_market_cap: Include market capitalization. Default: ``false``
            mcap_fdv_fallback: Return FDV if market cap is not available. Default: ``false``
            include_24hr_vol: Include 24hr volume. Default: ``false``
            include_24hr_price_change: Include 24hr price change. Default: ``false``
            include_total_reserve_in_usd: Include total reserve in USD. Default: ``false``
            include_inactive_source: Include token price data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token price data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.onchain_simple_price(
                network=network,
                addresses=addresses,
                include_market_cap=include_market_cap,
                mcap_fdv_fallback=mcap_fdv_fallback,
                include_24hr_vol=include_24hr_vol,
                include_24hr_price_change=include_24hr_price_change,
                include_total_reserve_in_usd=include_total_reserve_in_usd,
                include_inactive_source=include_inactive_source,
                request_options=request_options,
            )
        ).unwrap()

    async def pool_address(
        self,
        *,
        network: str = "eth",
        address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolAddressData:
        """To query the specific pool based on the provided network and pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Pool address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Specific pool data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pool_address(
                network=network,
                address=address,
                include=include,
                include_volume_breakdown=include_volume_breakdown,
                include_composition=include_composition,
                request_options=request_options,
            )
        ).unwrap()

    async def pool_ohlcv_contract_address(
        self,
        timeframe: TimeframeOrStr,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        aggregate: str | None = None,
        before_timestamp: int | None = None,
        limit: int | None = None,
        currency: CurrencyOrStr | None = None,
        token: str | None = None,
        include_empty_intervals: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Ohlcv:
        """To get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a
        network

        Args:
            timeframe: Timeframe of the OHLCV chart.
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            aggregate: Time period to aggregate each OHLCV. Available values (day): ``1`` Available values (hour):
                ``1``, ``4``, ``12`` Available values (minute): ``1``, ``5``, ``15`` Default value: 1
            before_timestamp: Return OHLCV data before this timestamp (integer seconds since epoch).
            limit: Number of OHLCV results to return, maximum 1000. Default value: 100
            currency: Return OHLCV in USD or quote token. Default: ``usd``
            token: Return OHLCV for token, use this to invert the chart. Available values: ``base``, ``quote``, or token
                address. Default: ``base``
            include_empty_intervals: Include empty intervals with no trade data. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool OHLCV chart data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pool_ohlcv_contract_address(
                timeframe,
                network=network,
                pool_address=pool_address,
                aggregate=aggregate,
                before_timestamp=before_timestamp,
                limit=limit,
                currency=currency,
                token=token,
                include_empty_intervals=include_empty_intervals,
                request_options=request_options,
            )
        ).unwrap()

    async def pool_token_info_contract_address(
        self,
        *,
        network: str = "solana",
        pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt",
        include: Include2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolTokensInfo:
        """To query pool metadata (base and quote token details, image, socials, websites, description, contract
        address, etc.) based on a provided pool contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            include: Attributes to include.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool tokens info data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pool_token_info_contract_address(
                network=network, pool_address=pool_address, include=include, request_options=request_options
            )
        ).unwrap()

    async def pool_trades_contract_address(
        self,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        trade_volume_in_usd_greater_than: float | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Trades:
        """To query the last 300 trades in the past 24 hours based on the provided pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            trade_volume_in_usd_greater_than: Filter trades by trade volume in USD greater than this value. Default
                value: 0
            token: Return trades for token, use this to invert the chart. Available values: ``base``, ``quote``, or
                token address. Default: ``base``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Last 300 trades in past 24 hours from a pool

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pool_trades_contract_address(
                network=network,
                pool_address=pool_address,
                trade_volume_in_usd_greater_than=trade_volume_in_usd_greater_than,
                token=token,
                request_options=request_options,
            )
        ).unwrap()

    async def pools_addresses(
        self,
        *,
        network: str = "eth",
        addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiPoolAddressData:
        """To query multiple pools based on the provided network and pool addresses

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Pool contract address, comma-separated if more than one pool contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multiple pools data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pools_addresses(
                network=network,
                addresses=addresses,
                include=include,
                include_volume_breakdown=include_volume_breakdown,
                include_composition=include_composition,
                request_options=request_options,
            )
        ).unwrap()

    async def search_pools(
        self,
        *,
        query: str | None = "weth",
        network: str | None = None,
        include: str | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PoolSearch:
        """To search for pools across all networks by pool address, token name, token symbol, or token contract address

        Args:
            query: Search query: pool contract address, token name, token symbol, or token contract address.
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Pool search results

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_pools(
                query=query, network=network, include=include, page=page, request_options=request_options
            )
        ).unwrap()

    async def token_data_contract_address(
        self,
        *,
        network: str = "eth",
        address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenData:
        """To query specific token data based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include token data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.token_data_contract_address(
                network=network,
                address=address,
                include=include,
                include_composition=include_composition,
                include_inactive_source=include_inactive_source,
                request_options=request_options,
            )
        ).unwrap()

    async def token_info_contract_address(
        self,
        *,
        network: str = "solana",
        address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump",
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenInfo:
        """To query token metadata (name, symbol, CoinGecko ID, image, socials, websites, description, etc.) based on a
        provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token info data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.token_info_contract_address(
                network=network, address=address, request_options=request_options
            )
        ).unwrap()

    async def tokens_data_contract_addresses(
        self,
        *,
        network: str = "solana",
        addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiTokenData:
        """To query multiple tokens data based on the provided token contract addresses on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Multiple tokens data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.tokens_data_contract_addresses(
                network=network,
                addresses=addresses,
                include=include,
                include_composition=include_composition,
                include_inactive_source=include_inactive_source,
                request_options=request_options,
            )
        ).unwrap()

    async def tokens_info_recent_updated(
        self,
        *,
        include: Include3OrStr | None = None,
        network: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenInfoRecentlyUpdated:
        """To query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal

        Args:
            include: Attributes for related resources to include.
            network: Filter tokens by provided network. *refers to /reference/networks-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Most recently updated tokens info

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.tokens_info_recent_updated(
                include=include, network=network, request_options=request_options
            )
        ).unwrap()

    async def top_pools_contract_address(
        self,
        *,
        network: str = "eth",
        token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: str | None = None,
        include_inactive_source: bool | None = None,
        page: int | None = None,
        sort: Sort2OrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query top pools based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            token_address: Token contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_volume_usd_liquidity_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools for a token

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.top_pools_contract_address(
                network=network,
                token_address=token_address,
                include=include,
                include_inactive_source=include_inactive_source,
                page=page,
                sort=sort,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def top_pools_dex(
        self,
        *,
        network: str = "eth",
        dex: str = "sushiswap",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the top pools based on the provided network and decentralized exchange (DEX)

        Args:
            network: Network ID. *refers to /reference/networks-list.
            dex: DEX ID. *refers to /reference/dexes-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools on a network's DEX

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.top_pools_dex(
                network=network,
                dex=dex,
                include=include,
                page=page,
                sort=sort,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def top_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the top pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Top pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.top_pools_network(
                network=network,
                include=include,
                page=page,
                sort=sort,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def trending_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query all the trending pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trending pools across all networks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.trending_pools_list(
                include=include,
                page=page,
                duration=duration,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    async def trending_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Pool:
        """To query the trending pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trending pools on a network

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.trending_pools_network(
                network=network,
                include=include,
                page=page,
                duration=duration,
                include_gt_community_data=include_gt_community_data,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOnchainWithRawResponse:
        return self._with_raw_response


class OnchainWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def dexes_list(
        self, *, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DexesList, RawError]:
        """To query all the supported decentralized exchanges (DEXs) based on the provided network on GeckoTerminal

        Args:
            network: Network ID. *refers to /reference/networks-list.
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/dexes"),
            path_params=[param[str]("network", network)],
            query_params=[param[int | None]("page", page)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[DexesList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def latest_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the latest pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/new_pools"),
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def latest_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the latest pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/new_pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def networks_list(
        self, *, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NetworksList, RawError]:
        """To retrieve a list of all supported networks on GeckoTerminal

        Args:
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks"),
            query_params=[param[int | None]("page", page)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[NetworksList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def onchain_simple_price(
        self,
        *,
        network: str = "eth",
        addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        include_market_cap: bool | None = None,
        mcap_fdv_fallback: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_price_change: bool | None = None,
        include_total_reserve_in_usd: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnchainSimplePrice, RawError]:
        """To get token price based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include_market_cap: Include market capitalization. Default: ``false``
            mcap_fdv_fallback: Return FDV if market cap is not available. Default: ``false``
            include_24hr_vol: Include 24hr volume. Default: ``false``
            include_24hr_price_change: Include 24hr price change. Default: ``false``
            include_total_reserve_in_usd: Include total reserve in USD. Default: ``false``
            include_inactive_source: Include token price data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/simple/networks/{network}/token_price/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[bool | None]("include_market_cap", include_market_cap),
                param[bool | None]("mcap_fdv_fallback", mcap_fdv_fallback),
                param[bool | None]("include_24hr_vol", include_24hr_vol),
                param[bool | None]("include_24hr_price_change", include_24hr_price_change),
                param[bool | None]("include_total_reserve_in_usd", include_total_reserve_in_usd),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[OnchainSimplePrice],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pool_address(
        self,
        *,
        network: str = "eth",
        address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolAddressData, RawError]:
        """To query the specific pool based on the provided network and pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Pool address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{address}"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_volume_breakdown", include_volume_breakdown),
                param[bool | None]("include_composition", include_composition),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolAddressData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pool_ohlcv_contract_address(
        self,
        timeframe: TimeframeOrStr,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        aggregate: str | None = None,
        before_timestamp: int | None = None,
        limit: int | None = None,
        currency: CurrencyOrStr | None = None,
        token: str | None = None,
        include_empty_intervals: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Ohlcv, RawError]:
        """To get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a
        network

        Args:
            timeframe: Timeframe of the OHLCV chart.
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            aggregate: Time period to aggregate each OHLCV. Available values (day): ``1`` Available values (hour):
                ``1``, ``4``, ``12`` Available values (minute): ``1``, ``5``, ``15`` Default value: 1
            before_timestamp: Return OHLCV data before this timestamp (integer seconds since epoch).
            limit: Number of OHLCV results to return, maximum 1000. Default value: 100
            currency: Return OHLCV in USD or quote token. Default: ``usd``
            token: Return OHLCV for token, use this to invert the chart. Available values: ``base``, ``quote``, or token
                address. Default: ``base``
            include_empty_intervals: Include empty intervals with no trade data. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}"),
            path_params=[
                param[str]("network", network),
                param[str]("pool_address", pool_address),
                param[TimeframeOrStr]("timeframe", timeframe),
            ],
            query_params=[
                param[str | None]("aggregate", aggregate),
                param[int | None]("before_timestamp", before_timestamp),
                param[int | None]("limit", limit),
                param[CurrencyOrStr | None]("currency", currency),
                param[str | None]("token", token),
                param[bool | None]("include_empty_intervals", include_empty_intervals),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Ohlcv],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pool_token_info_contract_address(
        self,
        *,
        network: str = "solana",
        pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt",
        include: Include2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolTokensInfo, RawError]:
        """To query pool metadata (base and quote token details, image, socials, websites, description, contract
        address, etc.) based on a provided pool contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            include: Attributes to include.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/info"),
            path_params=[param[str]("network", network), param[str]("pool_address", pool_address)],
            query_params=[param[Include2OrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolTokensInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pool_trades_contract_address(
        self,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        trade_volume_in_usd_greater_than: float | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Trades, RawError]:
        """To query the last 300 trades in the past 24 hours based on the provided pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            trade_volume_in_usd_greater_than: Filter trades by trade volume in USD greater than this value. Default
                value: 0
            token: Return trades for token, use this to invert the chart. Available values: ``base``, ``quote``, or
                token address. Default: ``base``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/trades"),
            path_params=[param[str]("network", network), param[str]("pool_address", pool_address)],
            query_params=[
                param[float | None]("trade_volume_in_usd_greater_than", trade_volume_in_usd_greater_than),
                param[str | None]("token", token),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Trades],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pools_addresses(
        self,
        *,
        network: str = "eth",
        addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiPoolAddressData, RawError]:
        """To query multiple pools based on the provided network and pool addresses

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Pool contract address, comma-separated if more than one pool contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/multi/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_volume_breakdown", include_volume_breakdown),
                param[bool | None]("include_composition", include_composition),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[MultiPoolAddressData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_pools(
        self,
        *,
        query: str | None = "weth",
        network: str | None = None,
        include: str | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolSearch, RawError]:
        """To search for pools across all networks by pool address, token name, token symbol, or token contract address

        Args:
            query: Search query: pool contract address, token name, token symbol, or token contract address.
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/search/pools"),
            query_params=[
                param[str | None]("query", query),
                param[str | None]("network", network),
                param[str | None]("include", include),
                param[int | None]("page", page),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolSearch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def token_data_contract_address(
        self,
        *,
        network: str = "eth",
        address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenData, RawError]:
        """To query specific token data based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include token data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{address}"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            query_params=[
                param[IncludeOrStr | None]("include", include),
                param[bool | None]("include_composition", include_composition),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def token_info_contract_address(
        self,
        *,
        network: str = "solana",
        address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenInfo, RawError]:
        """To query token metadata (name, symbol, CoinGecko ID, image, socials, websites, description, etc.) based on a
        provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{address}/info"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def tokens_data_contract_addresses(
        self,
        *,
        network: str = "solana",
        addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiTokenData, RawError]:
        """To query multiple tokens data based on the provided token contract addresses on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/multi/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[IncludeOrStr | None]("include", include),
                param[bool | None]("include_composition", include_composition),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[MultiTokenData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def tokens_info_recent_updated(
        self,
        *,
        include: Include3OrStr | None = None,
        network: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenInfoRecentlyUpdated, RawError]:
        """To query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal

        Args:
            include: Attributes for related resources to include.
            network: Filter tokens by provided network. *refers to /reference/networks-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/tokens/info_recently_updated"),
            query_params=[param[Include3OrStr | None]("include", include), param[str | None]("network", network)],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenInfoRecentlyUpdated],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def top_pools_contract_address(
        self,
        *,
        network: str = "eth",
        token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: str | None = None,
        include_inactive_source: bool | None = None,
        page: int | None = None,
        sort: Sort2OrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query top pools based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            token_address: Token contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_volume_usd_liquidity_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{token_address}/pools"),
            path_params=[param[str]("network", network), param[str]("token_address", token_address)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_inactive_source", include_inactive_source),
                param[int | None]("page", page),
                param[Sort2OrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def top_pools_dex(
        self,
        *,
        network: str = "eth",
        dex: str = "sushiswap",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the top pools based on the provided network and decentralized exchange (DEX)

        Args:
            network: Network ID. *refers to /reference/networks-list.
            dex: DEX ID. *refers to /reference/dexes-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/dexes/{dex}/pools"),
            path_params=[param[str]("network", network), param[str]("dex", dex)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[SortOrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def top_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the top pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[SortOrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def trending_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the trending pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/trending_pools"),
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[DurationOrStr | None]("duration", duration),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def trending_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query the trending pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/trending_pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[DurationOrStr | None]("duration", duration),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncOnchainWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def dexes_list(
        self, *, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DexesList, RawError]:
        """To query all the supported decentralized exchanges (DEXs) based on the provided network on GeckoTerminal

        Args:
            network: Network ID. *refers to /reference/networks-list.
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/dexes"),
            path_params=[param[str]("network", network)],
            query_params=[param[int | None]("page", page)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[DexesList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def latest_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the latest pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/new_pools"),
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def latest_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the latest pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/new_pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def networks_list(
        self, *, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NetworksList, RawError]:
        """To retrieve a list of all supported networks on GeckoTerminal

        Args:
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks"),
            query_params=[param[int | None]("page", page)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[NetworksList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def onchain_simple_price(
        self,
        *,
        network: str = "eth",
        addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        include_market_cap: bool | None = None,
        mcap_fdv_fallback: bool | None = None,
        include_24hr_vol: bool | None = None,
        include_24hr_price_change: bool | None = None,
        include_total_reserve_in_usd: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnchainSimplePrice, RawError]:
        """To get token price based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include_market_cap: Include market capitalization. Default: ``false``
            mcap_fdv_fallback: Return FDV if market cap is not available. Default: ``false``
            include_24hr_vol: Include 24hr volume. Default: ``false``
            include_24hr_price_change: Include 24hr price change. Default: ``false``
            include_total_reserve_in_usd: Include total reserve in USD. Default: ``false``
            include_inactive_source: Include token price data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/simple/networks/{network}/token_price/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[bool | None]("include_market_cap", include_market_cap),
                param[bool | None]("mcap_fdv_fallback", mcap_fdv_fallback),
                param[bool | None]("include_24hr_vol", include_24hr_vol),
                param[bool | None]("include_24hr_price_change", include_24hr_price_change),
                param[bool | None]("include_total_reserve_in_usd", include_total_reserve_in_usd),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[OnchainSimplePrice],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pool_address(
        self,
        *,
        network: str = "eth",
        address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolAddressData, RawError]:
        """To query the specific pool based on the provided network and pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Pool address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{address}"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_volume_breakdown", include_volume_breakdown),
                param[bool | None]("include_composition", include_composition),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolAddressData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pool_ohlcv_contract_address(
        self,
        timeframe: TimeframeOrStr,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        aggregate: str | None = None,
        before_timestamp: int | None = None,
        limit: int | None = None,
        currency: CurrencyOrStr | None = None,
        token: str | None = None,
        include_empty_intervals: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Ohlcv, RawError]:
        """To get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a
        network

        Args:
            timeframe: Timeframe of the OHLCV chart.
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            aggregate: Time period to aggregate each OHLCV. Available values (day): ``1`` Available values (hour):
                ``1``, ``4``, ``12`` Available values (minute): ``1``, ``5``, ``15`` Default value: 1
            before_timestamp: Return OHLCV data before this timestamp (integer seconds since epoch).
            limit: Number of OHLCV results to return, maximum 1000. Default value: 100
            currency: Return OHLCV in USD or quote token. Default: ``usd``
            token: Return OHLCV for token, use this to invert the chart. Available values: ``base``, ``quote``, or token
                address. Default: ``base``
            include_empty_intervals: Include empty intervals with no trade data. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}"),
            path_params=[
                param[str]("network", network),
                param[str]("pool_address", pool_address),
                param[TimeframeOrStr]("timeframe", timeframe),
            ],
            query_params=[
                param[str | None]("aggregate", aggregate),
                param[int | None]("before_timestamp", before_timestamp),
                param[int | None]("limit", limit),
                param[CurrencyOrStr | None]("currency", currency),
                param[str | None]("token", token),
                param[bool | None]("include_empty_intervals", include_empty_intervals),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Ohlcv],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pool_token_info_contract_address(
        self,
        *,
        network: str = "solana",
        pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt",
        include: Include2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolTokensInfo, RawError]:
        """To query pool metadata (base and quote token details, image, socials, websites, description, contract
        address, etc.) based on a provided pool contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            include: Attributes to include.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/info"),
            path_params=[param[str]("network", network), param[str]("pool_address", pool_address)],
            query_params=[param[Include2OrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolTokensInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pool_trades_contract_address(
        self,
        *,
        network: str = "eth",
        pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553",
        trade_volume_in_usd_greater_than: float | None = None,
        token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Trades, RawError]:
        """To query the last 300 trades in the past 24 hours based on the provided pool address

        Args:
            network: Network ID. *refers to /reference/networks-list.
            pool_address: Pool contract address.
            trade_volume_in_usd_greater_than: Filter trades by trade volume in USD greater than this value. Default
                value: 0
            token: Return trades for token, use this to invert the chart. Available values: ``base``, ``quote``, or
                token address. Default: ``base``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/{pool_address}/trades"),
            path_params=[param[str]("network", network), param[str]("pool_address", pool_address)],
            query_params=[
                param[float | None]("trade_volume_in_usd_greater_than", trade_volume_in_usd_greater_than),
                param[str | None]("token", token),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Trades],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pools_addresses(
        self,
        *,
        network: str = "eth",
        addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        include: str | None = None,
        include_volume_breakdown: bool | None = None,
        include_composition: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiPoolAddressData, RawError]:
        """To query multiple pools based on the provided network and pool addresses

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Pool contract address, comma-separated if more than one pool contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_volume_breakdown: Include volume breakdown. Default: ``false``
            include_composition: Include pool composition. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools/multi/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_volume_breakdown", include_volume_breakdown),
                param[bool | None]("include_composition", include_composition),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[MultiPoolAddressData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_pools(
        self,
        *,
        query: str | None = "weth",
        network: str | None = None,
        include: str | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PoolSearch, RawError]:
        """To search for pools across all networks by pool address, token name, token symbol, or token contract address

        Args:
            query: Search query: pool contract address, token name, token symbol, or token contract address.
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/search/pools"),
            query_params=[
                param[str | None]("query", query),
                param[str | None]("network", network),
                param[str | None]("include", include),
                param[int | None]("page", page),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[PoolSearch],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def token_data_contract_address(
        self,
        *,
        network: str = "eth",
        address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenData, RawError]:
        """To query specific token data based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include token data from inactive pools using the most recent swap. Default:
                ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{address}"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            query_params=[
                param[IncludeOrStr | None]("include", include),
                param[bool | None]("include_composition", include_composition),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def token_info_contract_address(
        self,
        *,
        network: str = "solana",
        address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenInfo, RawError]:
        """To query token metadata (name, symbol, CoinGecko ID, image, socials, websites, description, etc.) based on a
        provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            address: Token contract address.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{address}/info"),
            path_params=[param[str]("network", network), param[str]("address", address)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def tokens_data_contract_addresses(
        self,
        *,
        network: str = "solana",
        addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump",
        include: IncludeOrStr | None = None,
        include_composition: bool | None = None,
        include_inactive_source: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiTokenData, RawError]:
        """To query multiple tokens data based on the provided token contract addresses on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            addresses: Token contract address, comma-separated if more than one token contract address.
            include: Attributes to include.
            include_composition: Include pool composition. Default: ``false``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/multi/{addresses}"),
            path_params=[param[str]("network", network), param[str]("addresses", addresses)],
            query_params=[
                param[IncludeOrStr | None]("include", include),
                param[bool | None]("include_composition", include_composition),
                param[bool | None]("include_inactive_source", include_inactive_source),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[MultiTokenData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def tokens_info_recent_updated(
        self,
        *,
        include: Include3OrStr | None = None,
        network: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenInfoRecentlyUpdated, RawError]:
        """To query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal

        Args:
            include: Attributes for related resources to include.
            network: Filter tokens by provided network. *refers to /reference/networks-list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/tokens/info_recently_updated"),
            query_params=[param[Include3OrStr | None]("include", include), param[str | None]("network", network)],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[TokenInfoRecentlyUpdated],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def top_pools_contract_address(
        self,
        *,
        network: str = "eth",
        token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7",
        include: str | None = None,
        include_inactive_source: bool | None = None,
        page: int | None = None,
        sort: Sort2OrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query top pools based on the provided token contract address on a network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            token_address: Token contract address.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            include_inactive_source: Include tokens from inactive pools using the most recent swap. Default: ``false``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_volume_usd_liquidity_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/tokens/{token_address}/pools"),
            path_params=[param[str]("network", network), param[str]("token_address", token_address)],
            query_params=[
                param[str | None]("include", include),
                param[bool | None]("include_inactive_source", include_inactive_source),
                param[int | None]("page", page),
                param[Sort2OrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def top_pools_dex(
        self,
        *,
        network: str = "eth",
        dex: str = "sushiswap",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the top pools based on the provided network and decentralized exchange (DEX)

        Args:
            network: Network ID. *refers to /reference/networks-list.
            dex: DEX ID. *refers to /reference/dexes-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/dexes/{dex}/pools"),
            path_params=[param[str]("network", network), param[str]("dex", dex)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[SortOrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def top_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        sort: SortOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the top pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            sort: Sort the pools by field. Default: ``h24_tx_count_desc``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[SortOrStr | None]("sort", sort),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def trending_pools_list(
        self,
        *,
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query all the trending pools across all networks on GeckoTerminal

        Args:
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``, ``network``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/trending_pools"),
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[DurationOrStr | None]("duration", duration),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def trending_pools_network(
        self,
        *,
        network: str = "eth",
        include: str | None = None,
        page: int | None = None,
        duration: DurationOrStr | None = None,
        include_gt_community_data: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Pool, RawError]:
        """To query the trending pools based on the provided network

        Args:
            network: Network ID. *refers to /reference/networks-list.
            include: Attributes to include, comma-separated if more than one. Available values: ``base_token``,
                ``quote_token``, ``dex``
            page: Page through results. Default value: 1
            duration: Duration to sort trending list by. Default: ``24h``
            include_gt_community_data: Include GeckoTerminal community data (sentiment votes, suspicious reports).
                Default: ``false``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/onchain/networks/{network}/trending_pools"),
            path_params=[param[str]("network", network)],
            query_params=[
                param[str | None]("include", include),
                param[int | None]("page", page),
                param[DurationOrStr | None]("duration", duration),
                param[bool | None]("include_gt_community_data", include_gt_community_data),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.header_auth, self._auth.query_auth),
            decoder=json_decoder[Pool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
