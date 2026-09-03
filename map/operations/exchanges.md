<!-- Generated file — do not edit; regenerated with the SDK. -->

# Exchanges — operations

Accessor: `client.exchanges` · Source: `coin_gecko_demo_api/apis/exchanges.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.exchanges.exchange_rates

- **Route**: `GET /exchange_rates`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def exchange_rates(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ExchangeRates`
- **Returns (raw)**: `ApiResult[ExchangeRates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ExchangeRates` | `coin_gecko_demo_api/models/exchange_rates.py` |

### client.exchanges.exchanges

- **Route**: `GET /exchanges`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def exchanges(*, per_page: float | None = None, page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `per_page` — query · `page` — query
- **Returns (parsed)**: `list[Exchange1]`
- **Returns (raw)**: `ApiResult[list[Exchange1], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Exchange1` | `coin_gecko_demo_api/models/exchange1.py` |

### client.exchanges.exchanges_id

- **Route**: `GET /exchanges/{id}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def exchanges_id(*, id: str = "binance", dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `dex_pair_format` — query
- **Returns (parsed)**: `ExchangesId`
- **Returns (raw)**: `ApiResult[ExchangesId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DexPairFormatOrStr` | `coin_gecko_demo_api/models/enums/dex_pair_format.py` |
| `ExchangesId` | `coin_gecko_demo_api/models/exchanges_id.py` |

### client.exchanges.exchanges_id_tickers

- **Route**: `GET /exchanges/{id}/tickers`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def exchanges_id_tickers(*, id: str = "binance", coin_ids: str | None = None, include_exchange_logo: bool | None = None, page: float | None = None, depth: bool | None = None, order: Order3OrStr | None = None, dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `coin_ids` — query · `include_exchange_logo` — query · `page` — query · `depth` — query · `order` — query · `dex_pair_format` — query
- **Returns (parsed)**: `CoinsIdTickers`
- **Returns (raw)**: `ApiResult[CoinsIdTickers, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order3OrStr` | `coin_gecko_demo_api/models/enums/order3.py` |
| `DexPairFormatOrStr` | `coin_gecko_demo_api/models/enums/dex_pair_format.py` |
| `CoinsIdTickers` | `coin_gecko_demo_api/models/coins_id_tickers.py` |

### client.exchanges.exchanges_id_volume_chart

- **Route**: `GET /exchanges/{id}/volume_chart`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def exchanges_id_volume_chart(days: DaysOrStr, *, id: str = "binance", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `days`
- **Params**: `id` — path · `days` — query
- **Returns (parsed)**: `list[list[ExchangeVolumeChart]]`
- **Returns (raw)**: `ApiResult[list[list[ExchangeVolumeChart]], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DaysOrStr` | `coin_gecko_demo_api/models/enums/days.py` |
| `ExchangeVolumeChart` | `coin_gecko_demo_api/models/unions/exchange_volume_chart.py` |

### client.exchanges.exchanges_list

- **Route**: `GET /exchanges/list`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def exchanges_list(*, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query
- **Returns (parsed)**: `list[ExchangesList]`
- **Returns (raw)**: `ApiResult[list[ExchangesList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatusOrStr` | `coin_gecko_demo_api/models/enums/status.py` |
| `ExchangesList` | `coin_gecko_demo_api/models/exchanges_list.py` |

