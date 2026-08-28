<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `coin_gecko/client.py` · 61 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.asset_platforms_list

- **Route**: `GET /asset_platforms`
- **Signature**: `def asset_platforms_list(*, filter: FilterOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `filter` — query
- **Returns (parsed)**: `list[AssetPlatform]`
- **Returns (raw)**: `ApiResult[list[AssetPlatform], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FilterOrStr` | `coin_gecko/models/enums/filter.py` |
| `AssetPlatform` | `coin_gecko/models/asset_platform.py` |

### client.coins_categories

- **Route**: `GET /coins/categories`
- **Signature**: `def coins_categories(*, order: Order2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `order` — query
- **Returns (parsed)**: `list[Category1]`
- **Returns (raw)**: `ApiResult[list[Category1], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order2OrStr` | `coin_gecko/models/enums/order2.py` |
| `Category1` | `coin_gecko/models/category1.py` |

### client.coins_categories_list

- **Route**: `GET /coins/categories/list`
- **Signature**: `def coins_categories_list(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[CategoriesList]`
- **Returns (raw)**: `ApiResult[list[CategoriesList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CategoriesList` | `coin_gecko/models/categories_list.py` |

### client.coins_contract_address

- **Route**: `GET /coins/{id}/contract/{contract_address}`
- **Signature**: `def coins_contract_address(*, id: str = "ethereum", contract_address: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `contract_address` — path
- **Returns (parsed)**: `CoinsContractAddress`
- **Returns (raw)**: `ApiResult[CoinsContractAddress, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CoinsContractAddress` | `coin_gecko/models/coins_contract_address.py` |

### client.coins_id

- **Route**: `GET /coins/{id}`
- **Signature**: `def coins_id(*, id: str = "bitcoin", localization: bool | None = None, tickers: bool | None = None, market_data: bool | None = None, community_data: bool | None = None, developer_data: bool | None = None, sparkline: bool | None = None, include_categories_details: bool | None = None, dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `localization` — query · `tickers` — query · `market_data` — query · `community_data` — query · `developer_data` — query · `sparkline` — query · `include_categories_details` — query · `dex_pair_format` — query
- **Returns (parsed)**: `CoinsId`
- **Returns (raw)**: `ApiResult[CoinsId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DexPairFormatOrStr` | `coin_gecko/models/enums/dex_pair_format.py` |
| `CoinsId` | `coin_gecko/models/coins_id.py` |

### client.coins_id_history

- **Route**: `GET /coins/{id}/history`
- **Signature**: `def coins_id_history(*, id: str = "bitcoin", date: str = "30-12-2025", localization: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `date` — query · `localization` — query
- **Returns (parsed)**: `CoinsIdHistory`
- **Returns (raw)**: `ApiResult[CoinsIdHistory, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CoinsIdHistory` | `coin_gecko/models/coins_id_history.py` |

### client.coins_id_market_chart

- **Route**: `GET /coins/{id}/market_chart`
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

### client.coins_id_market_chart_range

- **Route**: `GET /coins/{id}/market_chart/range`
- **Signature**: `def coins_id_market_chart_range(*, id: str = "bitcoin", vs_currency: str = "usd", from_: int = 1767024000, to: int = 1777564800, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `vs_currency` — query · `from_` — query `from` · `to` — query · `precision` — query
- **Returns (parsed)**: `CoinsMarketChart`
- **Returns (raw)**: `ApiResult[CoinsMarketChart, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `CoinsMarketChart` | `coin_gecko/models/coins_market_chart.py` |

### client.coins_id_ohlc

- **Route**: `GET /coins/{id}/ohlc`
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

### client.coins_id_tickers

- **Route**: `GET /coins/{id}/tickers`
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

### client.coins_list

- **Route**: `GET /coins/list`
- **Signature**: `def coins_list(*, include_platform: bool | None = None, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include_platform` — query · `status` — query
- **Returns (parsed)**: `list[CoinsList]`
- **Returns (raw)**: `ApiResult[list[CoinsList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatusOrStr` | `coin_gecko/models/enums/status.py` |
| `CoinsList` | `coin_gecko/models/coins_list.py` |

### client.coins_markets

- **Route**: `GET /coins/markets`
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

### client.companies_public_treasury

- **Route**: `GET /{entity}/public_treasury/{coin_id}`
- **Signature**: `def companies_public_treasury(entity: EntityOrStr, *, coin_id: str = "bitcoin", per_page: int | None = None, page: int | None = None, order: Order5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `entity`
- **Params**: `entity` — path · `coin_id` — path · `per_page` — query · `page` — query · `order` — query
- **Returns (parsed)**: `PublicTreasury`
- **Returns (raw)**: `ApiResult[PublicTreasury, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EntityOrStr` | `coin_gecko/models/enums/entity.py` |
| `Order5OrStr` | `coin_gecko/models/enums/order5.py` |
| `PublicTreasury` | `coin_gecko/models/unions/public_treasury.py` |

### client.contract_address_market_chart

- **Route**: `GET /coins/{id}/contract/{contract_address}/market_chart`
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

### client.contract_address_market_chart_range

- **Route**: `GET /coins/{id}/contract/{contract_address}/market_chart/range`
- **Signature**: `def contract_address_market_chart_range(*, id: str = "ethereum", contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", vs_currency: str = "usd", from_: int = 1767024000, to: int = 1777564800, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `contract_address` — path · `vs_currency` — query · `from_` — query `from` · `to` — query · `precision` — query
- **Returns (parsed)**: `CoinsMarketChart`
- **Returns (raw)**: `ApiResult[CoinsMarketChart, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `CoinsMarketChart` | `coin_gecko/models/coins_market_chart.py` |

### client.crypto_global

- **Route**: `GET /global`
- **Signature**: `def crypto_global(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `GlobalModel`
- **Returns (raw)**: `ApiResult[GlobalModel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GlobalModel` | `coin_gecko/models/global_model.py` |

### client.derivatives_exchanges

- **Route**: `GET /derivatives/exchanges`
- **Signature**: `def derivatives_exchanges(*, order: Order4OrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `order` — query · `per_page` — query · `page` — query
- **Returns (parsed)**: `list[DerivativesExchange]`
- **Returns (raw)**: `ApiResult[list[DerivativesExchange], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order4OrStr` | `coin_gecko/models/enums/order4.py` |
| `DerivativesExchange` | `coin_gecko/models/derivatives_exchange.py` |

### client.derivatives_exchanges_id

- **Route**: `GET /derivatives/exchanges/{id}`
- **Signature**: `def derivatives_exchanges_id(*, id: str = "binance_futures", include_tickers: IncludeTickersOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `include_tickers` — query
- **Returns (parsed)**: `DerivativesExchangesId`
- **Returns (raw)**: `ApiResult[DerivativesExchangesId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeTickersOrStr` | `coin_gecko/models/enums/include_tickers.py` |
| `DerivativesExchangesId` | `coin_gecko/models/derivatives_exchanges_id.py` |

### client.derivatives_exchanges_list

- **Route**: `GET /derivatives/exchanges/list`
- **Signature**: `def derivatives_exchanges_list(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[DerivativesExchangesList]`
- **Returns (raw)**: `ApiResult[list[DerivativesExchangesList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DerivativesExchangesList` | `coin_gecko/models/derivatives_exchanges_list.py` |

### client.derivatives_tickers

- **Route**: `GET /derivatives`
- **Signature**: `def derivatives_tickers(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[DerivativesTicker]`
- **Returns (raw)**: `ApiResult[list[DerivativesTicker], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DerivativesTicker` | `coin_gecko/models/derivatives_ticker.py` |

### client.dexes_list

- **Route**: `GET /onchain/networks/{network}/dexes`
- **Signature**: `def dexes_list(*, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `page` — query
- **Returns (parsed)**: `DexesList`
- **Returns (raw)**: `ApiResult[DexesList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DexesList` | `coin_gecko/models/dexes_list.py` |

### client.entities_list

- **Route**: `GET /entities/list`
- **Signature**: `def entities_list(*, entity_type: EntityTypeOrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_type` — query · `per_page` — query · `page` — query
- **Returns (parsed)**: `list[EntitiesList]`
- **Returns (raw)**: `ApiResult[list[EntitiesList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EntityTypeOrStr` | `coin_gecko/models/enums/entity_type.py` |
| `EntitiesList` | `coin_gecko/models/entities_list.py` |

### client.exchange_rates

- **Route**: `GET /exchange_rates`
- **Signature**: `def exchange_rates(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ExchangeRates`
- **Returns (raw)**: `ApiResult[ExchangeRates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ExchangeRates` | `coin_gecko/models/exchange_rates.py` |

### client.exchanges

- **Route**: `GET /exchanges`
- **Signature**: `def exchanges(*, per_page: float | None = None, page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `per_page` — query · `page` — query
- **Returns (parsed)**: `list[Exchange1]`
- **Returns (raw)**: `ApiResult[list[Exchange1], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Exchange1` | `coin_gecko/models/exchange1.py` |

### client.exchanges_id

- **Route**: `GET /exchanges/{id}`
- **Signature**: `def exchanges_id(*, id: str = "binance", dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `dex_pair_format` — query
- **Returns (parsed)**: `ExchangesId`
- **Returns (raw)**: `ApiResult[ExchangesId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DexPairFormatOrStr` | `coin_gecko/models/enums/dex_pair_format.py` |
| `ExchangesId` | `coin_gecko/models/exchanges_id.py` |

### client.exchanges_id_tickers

- **Route**: `GET /exchanges/{id}/tickers`
- **Signature**: `def exchanges_id_tickers(*, id: str = "binance", coin_ids: str | None = None, include_exchange_logo: bool | None = None, page: float | None = None, depth: bool | None = None, order: Order3OrStr | None = None, dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `coin_ids` — query · `include_exchange_logo` — query · `page` — query · `depth` — query · `order` — query · `dex_pair_format` — query
- **Returns (parsed)**: `CoinsIdTickers`
- **Returns (raw)**: `ApiResult[CoinsIdTickers, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order3OrStr` | `coin_gecko/models/enums/order3.py` |
| `DexPairFormatOrStr` | `coin_gecko/models/enums/dex_pair_format.py` |
| `CoinsIdTickers` | `coin_gecko/models/coins_id_tickers.py` |

### client.exchanges_id_volume_chart

- **Route**: `GET /exchanges/{id}/volume_chart`
- **Signature**: `def exchanges_id_volume_chart(days: DaysOrStr, *, id: str = "binance", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `days`
- **Params**: `id` — path · `days` — query
- **Returns (parsed)**: `list[list[ExchangeVolumeChart]]`
- **Returns (raw)**: `ApiResult[list[list[ExchangeVolumeChart]], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DaysOrStr` | `coin_gecko/models/enums/days.py` |
| `ExchangeVolumeChart` | `coin_gecko/models/unions/exchange_volume_chart.py` |

### client.exchanges_list

- **Route**: `GET /exchanges/list`
- **Signature**: `def exchanges_list(*, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query
- **Returns (parsed)**: `list[ExchangesList]`
- **Returns (raw)**: `ApiResult[list[ExchangesList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatusOrStr` | `coin_gecko/models/enums/status.py` |
| `ExchangesList` | `coin_gecko/models/exchanges_list.py` |

### client.global_defi

- **Route**: `GET /global/decentralized_finance_defi`
- **Signature**: `def global_defi(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `GlobalDeFi`
- **Returns (raw)**: `ApiResult[GlobalDeFi, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GlobalDeFi` | `coin_gecko/models/global_de_fi.py` |

### client.latest_pools_list

- **Route**: `GET /onchain/networks/new_pools`
- **Signature**: `def latest_pools_list(*, include: str | None = None, page: int | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include` — query · `page` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Pool` | `coin_gecko/models/pool.py` |

### client.latest_pools_network

- **Route**: `GET /onchain/networks/{network}/new_pools`
- **Signature**: `def latest_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `include` — query · `page` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Pool` | `coin_gecko/models/pool.py` |

### client.networks_list

- **Route**: `GET /onchain/networks`
- **Signature**: `def networks_list(*, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query
- **Returns (parsed)**: `NetworksList`
- **Returns (raw)**: `ApiResult[NetworksList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NetworksList` | `coin_gecko/models/networks_list.py` |

### client.nfts_contract_address

- **Route**: `GET /nfts/{asset_platform_id}/contract/{contract_address}`
- **Signature**: `def nfts_contract_address(*, asset_platform_id: str = "ethereum", contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `asset_platform_id` — path · `contract_address` — path
- **Returns (parsed)**: `Nftdata`
- **Returns (raw)**: `ApiResult[Nftdata, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Nftdata` | `coin_gecko/models/nftdata.py` |

### client.nfts_id

- **Route**: `GET /nfts/{id}`
- **Signature**: `def nfts_id(*, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path
- **Returns (parsed)**: `Nftdata`
- **Returns (raw)**: `ApiResult[Nftdata, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Nftdata` | `coin_gecko/models/nftdata.py` |

### client.nfts_list

- **Route**: `GET /nfts/list`
- **Signature**: `def nfts_list(*, order: Order7OrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `order` — query · `per_page` — query · `page` — query
- **Returns (parsed)**: `list[NftsList]`
- **Returns (raw)**: `ApiResult[list[NftsList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order7OrStr` | `coin_gecko/models/enums/order7.py` |
| `NftsList` | `coin_gecko/models/nfts_list.py` |

### client.onchain_simple_price

- **Route**: `GET /onchain/simple/networks/{network}/token_price/{addresses}`
- **Signature**: `def onchain_simple_price(*, network: str = "eth", addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", include_market_cap: bool | None = None, mcap_fdv_fallback: bool | None = None, include_24hr_vol: bool | None = None, include_24hr_price_change: bool | None = None, include_total_reserve_in_usd: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `addresses` — path · `include_market_cap` — query · `mcap_fdv_fallback` — query · `include_24hr_vol` — query · `include_24hr_price_change` — query · `include_total_reserve_in_usd` — query · `include_inactive_source` — query
- **Returns (parsed)**: `OnchainSimplePrice`
- **Returns (raw)**: `ApiResult[OnchainSimplePrice, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OnchainSimplePrice` | `coin_gecko/models/onchain_simple_price.py` |

### client.ping_server

- **Route**: `GET /ping`
- **Signature**: `def ping_server(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `PingServer`
- **Returns (raw)**: `ApiResult[PingServer, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PingServer` | `coin_gecko/models/ping_server.py` |

### client.pool_address

- **Route**: `GET /onchain/networks/{network}/pools/{address}`
- **Signature**: `def pool_address(*, network: str = "eth", address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", include: str | None = None, include_volume_breakdown: bool | None = None, include_composition: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `address` — path · `include` — query · `include_volume_breakdown` — query · `include_composition` — query
- **Returns (parsed)**: `PoolAddressData`
- **Returns (raw)**: `ApiResult[PoolAddressData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PoolAddressData` | `coin_gecko/models/pool_address_data.py` |

### client.pool_ohlcv_contract_address

- **Route**: `GET /onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}`
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

### client.pool_token_info_contract_address

- **Route**: `GET /onchain/networks/{network}/pools/{pool_address}/info`
- **Signature**: `def pool_token_info_contract_address(*, network: str = "solana", pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt", include: Include2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `pool_address` — path · `include` — query
- **Returns (parsed)**: `PoolTokensInfo`
- **Returns (raw)**: `ApiResult[PoolTokensInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Include2OrStr` | `coin_gecko/models/enums/include2.py` |
| `PoolTokensInfo` | `coin_gecko/models/pool_tokens_info.py` |

### client.pool_trades_contract_address

- **Route**: `GET /onchain/networks/{network}/pools/{pool_address}/trades`
- **Signature**: `def pool_trades_contract_address(*, network: str = "eth", pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553", trade_volume_in_usd_greater_than: float | None = None, token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `pool_address` — path · `trade_volume_in_usd_greater_than` — query · `token` — query
- **Returns (parsed)**: `Trades`
- **Returns (raw)**: `ApiResult[Trades, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Trades` | `coin_gecko/models/trades.py` |

### client.pools_addresses

- **Route**: `GET /onchain/networks/{network}/pools/multi/{addresses}`
- **Signature**: `def pools_addresses(*, network: str = "eth", addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", include: str | None = None, include_volume_breakdown: bool | None = None, include_composition: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `addresses` — path · `include` — query · `include_volume_breakdown` — query · `include_composition` — query
- **Returns (parsed)**: `MultiPoolAddressData`
- **Returns (raw)**: `ApiResult[MultiPoolAddressData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MultiPoolAddressData` | `coin_gecko/models/multi_pool_address_data.py` |

### client.public_treasury_entity

- **Route**: `GET /public_treasury/{entity_id}`
- **Signature**: `def public_treasury_entity(*, entity_id: str = "strategy", holding_amount_change: str | None = None, holding_change_percentage: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_id` — path · `holding_amount_change` — query · `holding_change_percentage` — query
- **Returns (parsed)**: `PublicTreasuryEntity`
- **Returns (raw)**: `ApiResult[PublicTreasuryEntity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PublicTreasuryEntity` | `coin_gecko/models/public_treasury_entity.py` |

### client.public_treasury_entity_chart

- **Route**: `GET /public_treasury/{entity_id}/{coin_id}/holding_chart`
- **Signature**: `def public_treasury_entity_chart(*, entity_id: str = "strategy", coin_id: str = "bitcoin", days: str = "365", include_empty_intervals: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_id` — path · `coin_id` — path · `days` — query · `include_empty_intervals` — query
- **Returns (parsed)**: `PublicTreasuryEntityChart`
- **Returns (raw)**: `ApiResult[PublicTreasuryEntityChart, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PublicTreasuryEntityChart` | `coin_gecko/models/public_treasury_entity_chart.py` |

### client.public_treasury_transaction_history

- **Route**: `GET /public_treasury/{entity_id}/transaction_history`
- **Signature**: `def public_treasury_transaction_history(*, entity_id: str = "strategy", per_page: int | None = None, page: int | None = None, order: Order6OrStr | None = None, coin_ids: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_id` — path · `per_page` — query · `page` — query · `order` — query · `coin_ids` — query
- **Returns (parsed)**: `PublicTreasuryTransactionHistory`
- **Returns (raw)**: `ApiResult[PublicTreasuryTransactionHistory, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order6OrStr` | `coin_gecko/models/enums/order6.py` |
| `PublicTreasuryTransactionHistory` | `coin_gecko/models/public_treasury_transaction_history.py` |

### client.search_data

- **Route**: `GET /search`
- **Signature**: `def search_data(query: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query`
- **Params**: `query` — query
- **Returns (parsed)**: `Search`
- **Returns (raw)**: `ApiResult[Search, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Search` | `coin_gecko/models/search.py` |

### client.search_pools

- **Route**: `GET /onchain/search/pools`
- **Signature**: `def search_pools(*, query: str | None = "weth", network: str | None = None, include: str | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `query` — query · `network` — query · `include` — query · `page` — query
- **Returns (parsed)**: `PoolSearch`
- **Returns (raw)**: `ApiResult[PoolSearch, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PoolSearch` | `coin_gecko/models/pool_search.py` |

### client.simple_price

- **Route**: `GET /simple/price`
- **Signature**: `def simple_price(*, vs_currencies: str = "usd", ids: str | None = "bitcoin", names: str | None = "Bitcoin", symbols: str | None = "btc", include_tokens: IncludeTokensOrStr | None = None, include_market_cap: bool | None = None, include_24hr_vol: bool | None = None, include_24hr_change: bool | None = None, include_last_updated_at: bool | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `vs_currencies` — query · `ids` — query · `names` — query · `symbols` — query · `include_tokens` — query · `include_market_cap` — query · `include_24hr_vol` — query · `include_24hr_change` — query · `include_last_updated_at` — query · `precision` — query
- **Returns (parsed)**: `dict[str, SimplePrice]`
- **Returns (raw)**: `ApiResult[dict[str, SimplePrice], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeTokensOrStr` | `coin_gecko/models/enums/include_tokens.py` |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `SimplePrice` | `coin_gecko/models/simple_price.py` |

### client.simple_supported_currencies

- **Route**: `GET /simple/supported_vs_currencies`
- **Signature**: `def simple_supported_currencies(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[str]`
- **Returns (raw)**: `ApiResult[list[str], RawError]`
- **Error**: `RawError` — **Case B**

### client.simple_token_price

- **Route**: `GET /simple/token_price/{id}`
- **Signature**: `def simple_token_price(*, id: str = "ethereum", contract_addresses: str = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599", vs_currencies: str = "usd", include_market_cap: bool | None = None, include_24hr_vol: bool | None = None, include_24hr_change: bool | None = None, include_last_updated_at: bool | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `contract_addresses` — query · `vs_currencies` — query · `include_market_cap` — query · `include_24hr_vol` — query · `include_24hr_change` — query · `include_last_updated_at` — query · `precision` — query
- **Returns (parsed)**: `dict[str, SimplePrice]`
- **Returns (raw)**: `ApiResult[dict[str, SimplePrice], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `SimplePrice` | `coin_gecko/models/simple_price.py` |

### client.token_data_contract_address

- **Route**: `GET /onchain/networks/{network}/tokens/{address}`
- **Signature**: `def token_data_contract_address(*, network: str = "eth", address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7", include: IncludeOrStr | None = None, include_composition: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `address` — path · `include` — query · `include_composition` — query · `include_inactive_source` — query
- **Returns (parsed)**: `TokenData`
- **Returns (raw)**: `ApiResult[TokenData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeOrStr` | `coin_gecko/models/enums/include.py` |
| `TokenData` | `coin_gecko/models/token_data.py` |

### client.token_info_contract_address

- **Route**: `GET /onchain/networks/{network}/tokens/{address}/info`
- **Signature**: `def token_info_contract_address(*, network: str = "solana", address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `address` — path
- **Returns (parsed)**: `TokenInfo`
- **Returns (raw)**: `ApiResult[TokenInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TokenInfo` | `coin_gecko/models/token_info.py` |

### client.token_lists

- **Route**: `GET /token_lists/{asset_platform_id}/all.json`
- **Signature**: `def token_lists(*, asset_platform_id: str = "ethereum", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `asset_platform_id` — path
- **Returns (parsed)**: `TokenLists`
- **Returns (raw)**: `ApiResult[TokenLists, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TokenLists` | `coin_gecko/models/token_lists.py` |

### client.tokens_data_contract_addresses

- **Route**: `GET /onchain/networks/{network}/tokens/multi/{addresses}`
- **Signature**: `def tokens_data_contract_addresses(*, network: str = "solana", addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump", include: IncludeOrStr | None = None, include_composition: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `addresses` — path · `include` — query · `include_composition` — query · `include_inactive_source` — query
- **Returns (parsed)**: `MultiTokenData`
- **Returns (raw)**: `ApiResult[MultiTokenData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeOrStr` | `coin_gecko/models/enums/include.py` |
| `MultiTokenData` | `coin_gecko/models/multi_token_data.py` |

### client.tokens_info_recent_updated

- **Route**: `GET /onchain/tokens/info_recently_updated`
- **Signature**: `def tokens_info_recent_updated(*, include: Include3OrStr | None = None, network: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include` — query · `network` — query
- **Returns (parsed)**: `TokenInfoRecentlyUpdated`
- **Returns (raw)**: `ApiResult[TokenInfoRecentlyUpdated, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Include3OrStr` | `coin_gecko/models/enums/include3.py` |
| `TokenInfoRecentlyUpdated` | `coin_gecko/models/token_info_recently_updated.py` |

### client.top_pools_contract_address

- **Route**: `GET /onchain/networks/{network}/tokens/{token_address}/pools`
- **Signature**: `def top_pools_contract_address(*, network: str = "eth", token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7", include: str | None = None, include_inactive_source: bool | None = None, page: int | None = None, sort: Sort2OrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `token_address` — path · `include` — query · `include_inactive_source` — query · `page` — query · `sort` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Sort2OrStr` | `coin_gecko/models/enums/sort2.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.top_pools_dex

- **Route**: `GET /onchain/networks/{network}/dexes/{dex}/pools`
- **Signature**: `def top_pools_dex(*, network: str = "eth", dex: str = "sushiswap", include: str | None = None, page: int | None = None, sort: SortOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `dex` — path · `include` — query · `page` — query · `sort` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrStr` | `coin_gecko/models/enums/sort.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.top_pools_network

- **Route**: `GET /onchain/networks/{network}/pools`
- **Signature**: `def top_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, sort: SortOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `include` — query · `page` — query · `sort` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrStr` | `coin_gecko/models/enums/sort.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.trending_pools_list

- **Route**: `GET /onchain/networks/trending_pools`
- **Signature**: `def trending_pools_list(*, include: str | None = None, page: int | None = None, duration: DurationOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include` — query · `page` — query · `duration` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DurationOrStr` | `coin_gecko/models/enums/duration.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.trending_pools_network

- **Route**: `GET /onchain/networks/{network}/trending_pools`
- **Signature**: `def trending_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, duration: DurationOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `network` — path · `include` — query · `page` — query · `duration` — query · `include_gt_community_data` — query
- **Returns (parsed)**: `Pool`
- **Returns (raw)**: `ApiResult[Pool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DurationOrStr` | `coin_gecko/models/enums/duration.py` |
| `Pool` | `coin_gecko/models/pool.py` |

### client.trending_search

- **Route**: `GET /search/trending`
- **Signature**: `def trending_search(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TrendingSearch`
- **Returns (raw)**: `ApiResult[TrendingSearch, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrendingSearch` | `coin_gecko/models/trending_search.py` |

