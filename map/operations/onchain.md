<!-- Generated file — do not edit; regenerated with the SDK. -->

# Onchain — operations

Accessor: `client.onchain` · Source: `coin_gecko/apis/onchain.py` · 20 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.onchain.dexes_list

- **Route**: `GET /onchain/networks/{network}/dexes`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def dexes_list(*, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `page` — query
- **Returns (parsed)**: `DexesList`
- **Returns (raw)**: `ApiResult[DexesList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DexesList` | `coin_gecko/models/dexes_list.py` |

### client.onchain.latest_pools_list

- **Route**: `GET /onchain/networks/new_pools`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def latest_pools_list(*, include: str | None = None, page: int | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include` — query · `page` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Pool` | `coin_gecko/models/pool.py` |

### client.onchain.latest_pools_network

- **Route**: `GET /onchain/networks/{network}/new_pools`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def latest_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `include` — query · `page` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Pool` | `coin_gecko/models/pool.py` |

### client.onchain.networks_list

- **Route**: `GET /onchain/networks`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def networks_list(*, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query
- **Returns (parsed)**: `NetworksList`
- **Returns (raw)**: `ApiResult[NetworksList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NetworksList` | `coin_gecko/models/networks_list.py` |

### client.onchain.onchain_simple_price

- **Route**: `GET /onchain/simple/networks/{network}/token_price/{addresses}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def onchain_simple_price(*, network: str = "eth", addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", include_market_cap: bool | None = None, mcap_fdv_fallback: bool | None = None, include_24hr_vol: bool | None = None, include_24hr_price_change: bool | None = None, include_total_reserve_in_usd: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `addresses` — path · `include_market_cap` — query · `mcap_fdv_fallback` — query · `include_24hr_vol` — query · `include_24hr_price_change` — query · `include_total_reserve_in_usd` — query · `include_inactive_source` — query
- **Returns (parsed)**: `OnchainSimplePrice`
- **Returns (raw)**: `ApiResult[OnchainSimplePrice, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OnchainSimplePrice` | `coin_gecko/models/onchain_simple_price.py` |

### client.onchain.pool_address

- **Route**: `GET /onchain/networks/{network}/pools/{address}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def pool_address(*, network: str = "eth", address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", include: str | None = None, include_volume_breakdown: bool | None = None, include_composition: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `address` — path · `include` — query · `include_volume_breakdown` — query · `include_composition` — query
- **Returns (parsed)**: `PoolAddressData`
- **Returns (raw)**: `ApiResult[PoolAddressData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PoolAddressData` | `coin_gecko/models/pool_address_data.py` |

### client.onchain.pool_ohlcv_contract_address

- **Route**: `GET /onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def pool_ohlcv_contract_address(timeframe: TimeframeOrStr, *, network: str = "eth", pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553", aggregate: str | None = None, before_timestamp: int | None = None, limit: int | None = None, currency: CurrencyOrStr | None = None, token: str | None = None, include_empty_intervals: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `timeframe`
- **Params**: `network` — path · `pool_address` — path · `timeframe` — path · `aggregate` — query · `before_timestamp` — query · `limit` — query · `currency` — query · `token` — query · `include_empty_intervals` — query
- **Returns (parsed)**: `Ohlcv`
- **Returns (raw)**: `ApiResult[Ohlcv, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TimeframeOrStr` | `coin_gecko/models/enums/timeframe.py` |
| `CurrencyOrStr` | `coin_gecko/models/enums/currency.py` |
| `Ohlcv` | `coin_gecko/models/ohlcv.py` |

### client.onchain.pool_token_info_contract_address

- **Route**: `GET /onchain/networks/{network}/pools/{pool_address}/info`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def pool_token_info_contract_address(*, network: str = "solana", pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt", include: Include2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `pool_address` — path · `include` — query
- **Returns (parsed)**: `PoolTokensInfo`
- **Returns (raw)**: `ApiResult[PoolTokensInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Include2OrStr` | `coin_gecko/models/enums/include2.py` |
| `PoolTokensInfo` | `coin_gecko/models/pool_tokens_info.py` |

### client.onchain.pool_trades_contract_address

- **Route**: `GET /onchain/networks/{network}/pools/{pool_address}/trades`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def pool_trades_contract_address(*, network: str = "eth", pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553", trade_volume_in_usd_greater_than: float | None = None, token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `pool_address` — path · `trade_volume_in_usd_greater_than` — query · `token` — query
- **Returns (parsed)**: `Trades`
- **Returns (raw)**: `ApiResult[Trades, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Trades` | `coin_gecko/models/trades.py` |

### client.onchain.pools_addresses

- **Route**: `GET /onchain/networks/{network}/pools/multi/{addresses}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def pools_addresses(*, network: str = "eth", addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", include: str | None = None, include_volume_breakdown: bool | None = None, include_composition: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `addresses` — path · `include` — query · `include_volume_breakdown` — query · `include_composition` — query
- **Returns (parsed)**: `MultiPoolAddressData`
- **Returns (raw)**: `ApiResult[MultiPoolAddressData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MultiPoolAddressData` | `coin_gecko/models/multi_pool_address_data.py` |

### client.onchain.search_pools

- **Route**: `GET /onchain/search/pools`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def search_pools(*, query: str | None = "weth", network: str | None = None, include: str | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `query` — query · `network` — query · `include` — query · `page` — query
- **Returns (parsed)**: `PoolSearch`
- **Returns (raw)**: `ApiResult[PoolSearch, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PoolSearch` | `coin_gecko/models/pool_search.py` |

### client.onchain.token_data_contract_address

- **Route**: `GET /onchain/networks/{network}/tokens/{address}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def token_data_contract_address(*, network: str = "eth", address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7", include: IncludeOrStr | None = None, include_composition: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `address` — path · `include` — query · `include_composition` — query · `include_inactive_source` — query
- **Returns (parsed)**: `TokenData`
- **Returns (raw)**: `ApiResult[TokenData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeOrStr` | `coin_gecko/models/enums/include.py` |
| `TokenData` | `coin_gecko/models/token_data.py` |

### client.onchain.token_info_contract_address

- **Route**: `GET /onchain/networks/{network}/tokens/{address}/info`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def token_info_contract_address(*, network: str = "solana", address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `address` — path
- **Returns (parsed)**: `TokenInfo`
- **Returns (raw)**: `ApiResult[TokenInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TokenInfo` | `coin_gecko/models/token_info.py` |

### client.onchain.tokens_data_contract_addresses

- **Route**: `GET /onchain/networks/{network}/tokens/multi/{addresses}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def tokens_data_contract_addresses(*, network: str = "solana", addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump", include: IncludeOrStr | None = None, include_composition: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `addresses` — path · `include` — query · `include_composition` — query · `include_inactive_source` — query
- **Returns (parsed)**: `MultiTokenData`
- **Returns (raw)**: `ApiResult[MultiTokenData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeOrStr` | `coin_gecko/models/enums/include.py` |
| `MultiTokenData` | `coin_gecko/models/multi_token_data.py` |

### client.onchain.tokens_info_recent_updated

- **Route**: `GET /onchain/tokens/info_recently_updated`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def tokens_info_recent_updated(*, include: Include3OrStr | None = None, network: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include` — query · `network` — query
- **Returns (parsed)**: `TokenInfoRecentlyUpdated`
- **Returns (raw)**: `ApiResult[TokenInfoRecentlyUpdated, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Include3OrStr` | `coin_gecko/models/enums/include3.py` |
| `TokenInfoRecentlyUpdated` | `coin_gecko/models/token_info_recently_updated.py` |

### client.onchain.top_pools_contract_address

- **Route**: `GET /onchain/networks/{network}/tokens/{token_address}/pools`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def top_pools_contract_address(*, network: str = "eth", token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7", include: str | None = None, include_inactive_source: bool | None = None, page: int | None = None, sort: Sort2OrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `token_address` — path · `include` — query · `include_inactive_source` — query · `page` — query · `sort` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Sort2OrStr` | `coin_gecko/models/enums/sort2.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.onchain.top_pools_dex

- **Route**: `GET /onchain/networks/{network}/dexes/{dex}/pools`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def top_pools_dex(*, network: str = "eth", dex: str = "sushiswap", include: str | None = None, page: int | None = None, sort: SortOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `dex` — path · `include` — query · `page` — query · `sort` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrStr` | `coin_gecko/models/enums/sort.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.onchain.top_pools_network

- **Route**: `GET /onchain/networks/{network}/pools`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def top_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, sort: SortOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `include` — query · `page` — query · `sort` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrStr` | `coin_gecko/models/enums/sort.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.onchain.trending_pools_list

- **Route**: `GET /onchain/networks/trending_pools`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def trending_pools_list(*, include: str | None = None, page: int | None = None, duration: DurationOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include` — query · `page` — query · `duration` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DurationOrStr` | `coin_gecko/models/enums/duration.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.onchain.trending_pools_network

- **Route**: `GET /onchain/networks/{network}/trending_pools`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def trending_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, duration: DurationOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `include` — query · `page` — query · `duration` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DurationOrStr` | `coin_gecko/models/enums/duration.py` |
| `Pool` | `coin_gecko/models/pool.py` |

