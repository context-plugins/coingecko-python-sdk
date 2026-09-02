<!-- Generated file — do not edit; regenerated with the SDK. -->

# Coins — operations

Accessor: `client.coins` · Source: `coin_gecko/apis/coins.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.coins.coins_categories

- **Route**: `GET /coins/categories`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_categories(*, order: Order2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `order` — query
- **Returns (parsed)**: `list[Category1]`
- **Returns (raw)**: `ApiResult[list[Category1], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order2OrStr` | `coin_gecko/models/enums/order2.py` |
| `Category1` | `coin_gecko/models/category1.py` |

### client.coins.coins_categories_list

- **Route**: `GET /coins/categories/list`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_categories_list(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[CategoriesList]`
- **Returns (raw)**: `ApiResult[list[CategoriesList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CategoriesList` | `coin_gecko/models/categories_list.py` |

### client.coins.coins_contract_address

- **Route**: `GET /coins/{id}/contract/{contract_address}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_contract_address(*, id: str = "ethereum", contract_address: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `contract_address` — path
- **Returns (parsed)**: `CoinsContractAddress`
- **Returns (raw)**: `ApiResult[CoinsContractAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CoinsContractAddress` | `coin_gecko/models/coins_contract_address.py` |

### client.coins.coins_id

- **Route**: `GET /coins/{id}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_id(*, id: str = "bitcoin", localization: bool | None = None, tickers: bool | None = None, market_data: bool | None = None, community_data: bool | None = None, developer_data: bool | None = None, sparkline: bool | None = None, include_categories_details: bool | None = None, dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `localization` — query · `tickers` — query · `market_data` — query · `community_data` — query · `developer_data` — query · `sparkline` — query · `include_categories_details` — query · `dex_pair_format` — query
- **Returns (parsed)**: `CoinsId`
- **Returns (raw)**: `ApiResult[CoinsId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DexPairFormatOrStr` | `coin_gecko/models/enums/dex_pair_format.py` |
| `CoinsId` | `coin_gecko/models/coins_id.py` |

### client.coins.coins_id_history

- **Route**: `GET /coins/{id}/history`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_id_history(*, id: str = "bitcoin", date: str = "30-12-2025", localization: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `date` — query · `localization` — query
- **Returns (parsed)**: `CoinsIdHistory`
- **Returns (raw)**: `ApiResult[CoinsIdHistory, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CoinsIdHistory` | `coin_gecko/models/coins_id_history.py` |

### client.coins.coins_id_market_chart

- **Route**: `GET /coins/{id}/market_chart`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_id_market_chart(*, id: str = "bitcoin", vs_currency: str = "usd", days: str = "1", interval: IntervalOrStr | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `vs_currency` — query · `days` — query · `interval` — query · `precision` — query
- **Returns (parsed)**: `CoinsMarketChart`
- **Returns (raw)**: `ApiResult[CoinsMarketChart, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IntervalOrStr` | `coin_gecko/models/enums/interval.py` |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `CoinsMarketChart` | `coin_gecko/models/coins_market_chart.py` |

### client.coins.coins_id_market_chart_range

- **Route**: `GET /coins/{id}/market_chart/range`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_id_market_chart_range(*, id: str = "bitcoin", vs_currency: str = "usd", from_: int = 1767024000, to: int = 1777564800, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `vs_currency` — query · `from_` — query `from` · `to` — query · `precision` — query
- **Returns (parsed)**: `CoinsMarketChart`
- **Returns (raw)**: `ApiResult[CoinsMarketChart, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `CoinsMarketChart` | `coin_gecko/models/coins_market_chart.py` |

### client.coins.coins_id_ohlc

- **Route**: `GET /coins/{id}/ohlc`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_id_ohlc(days: DaysOrStr, *, id: str = "bitcoin", vs_currency: str = "usd", precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `days`
- **Params**: `id` — path · `vs_currency` — query · `days` — query · `precision` — query
- **Returns (parsed)**: `list[list[float]]`
- **Returns (raw)**: `ApiResult[list[list[float]], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DaysOrStr` | `coin_gecko/models/enums/days.py` |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |

### client.coins.coins_id_tickers

- **Route**: `GET /coins/{id}/tickers`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_id_tickers(*, id: str = "bitcoin", exchange_ids: str | None = None, include_exchange_logo: bool | None = None, page: int | None = None, order: Order1OrStr | None = None, depth: bool | None = None, dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `exchange_ids` — query · `include_exchange_logo` — query · `page` — query · `order` — query · `depth` — query · `dex_pair_format` — query
- **Returns (parsed)**: `CoinsIdTickers`
- **Returns (raw)**: `ApiResult[CoinsIdTickers, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order1OrStr` | `coin_gecko/models/enums/order1.py` |
| `DexPairFormatOrStr` | `coin_gecko/models/enums/dex_pair_format.py` |
| `CoinsIdTickers` | `coin_gecko/models/coins_id_tickers.py` |

### client.coins.coins_list

- **Route**: `GET /coins/list`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_list(*, include_platform: bool | None = None, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include_platform` — query · `status` — query
- **Returns (parsed)**: `list[CoinsList]`
- **Returns (raw)**: `ApiResult[list[CoinsList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatusOrStr` | `coin_gecko/models/enums/status.py` |
| `CoinsList` | `coin_gecko/models/coins_list.py` |

### client.coins.coins_markets

- **Route**: `GET /coins/markets`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def coins_markets(*, vs_currency: str = "usd", ids: str | None = "bitcoin", names: str | None = "Bitcoin", symbols: str | None = "btc", include_tokens: IncludeTokensOrStr | None = None, category: str | None = None, order: OrderOrStr | None = None, per_page: int | None = None, page: int | None = None, sparkline: bool | None = None, price_change_percentage: str | None = None, locale: LocaleOrStr | None = None, precision: PrecisionOrStr | None = None, include_rehypothecated: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `vs_currency` — query · `ids` — query · `names` — query · `symbols` — query · `include_tokens` — query · `category` — query · `order` — query · `per_page` — query · `page` — query · `sparkline` — query · `price_change_percentage` — query · `locale` — query · `precision` — query · `include_rehypothecated` — query
- **Returns (parsed)**: `list[CoinsMarket]`
- **Returns (raw)**: `ApiResult[list[CoinsMarket], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeTokensOrStr` | `coin_gecko/models/enums/include_tokens.py` |
| `OrderOrStr` | `coin_gecko/models/enums/order.py` |
| `LocaleOrStr` | `coin_gecko/models/enums/locale.py` |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `CoinsMarket` | `coin_gecko/models/coins_market.py` |

### client.coins.contract_address_market_chart

- **Route**: `GET /coins/{id}/contract/{contract_address}/market_chart`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def contract_address_market_chart(*, id: str = "ethereum", contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", vs_currency: str = "usd", days: str = "1", interval: IntervalOrStr | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `contract_address` — path · `vs_currency` — query · `days` — query · `interval` — query · `precision` — query
- **Returns (parsed)**: `CoinsMarketChart`
- **Returns (raw)**: `ApiResult[CoinsMarketChart, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IntervalOrStr` | `coin_gecko/models/enums/interval.py` |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `CoinsMarketChart` | `coin_gecko/models/coins_market_chart.py` |

### client.coins.contract_address_market_chart_range

- **Route**: `GET /coins/{id}/contract/{contract_address}/market_chart/range`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def contract_address_market_chart_range(*, id: str = "ethereum", contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", vs_currency: str = "usd", from_: int = 1767024000, to: int = 1777564800, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `contract_address` — path · `vs_currency` — query · `from_` — query `from` · `to` — query · `precision` — query
- **Returns (parsed)**: `CoinsMarketChart`
- **Returns (raw)**: `ApiResult[CoinsMarketChart, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `CoinsMarketChart` | `coin_gecko/models/coins_market_chart.py` |

