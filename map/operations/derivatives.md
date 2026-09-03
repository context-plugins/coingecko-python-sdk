<!-- Generated file — do not edit; regenerated with the SDK. -->

# Derivatives — operations

Accessor: `client.derivatives` · Source: `coin_gecko_demo_api/apis/derivatives.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.derivatives.derivatives_exchanges

- **Route**: `GET /derivatives/exchanges`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def derivatives_exchanges(*, order: Order4OrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `order` — query · `per_page` — query · `page` — query
- **Returns (parsed)**: `list[DerivativesExchange]`
- **Returns (raw)**: `ApiResult[list[DerivativesExchange], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order4OrStr` | `coin_gecko_demo_api/models/enums/order4.py` |
| `DerivativesExchange` | `coin_gecko_demo_api/models/derivatives_exchange.py` |

### client.derivatives.derivatives_exchanges_id

- **Route**: `GET /derivatives/exchanges/{id}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def derivatives_exchanges_id(*, id: str = "binance_futures", include_tickers: IncludeTickersOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `include_tickers` — query
- **Returns (parsed)**: `DerivativesExchangesId`
- **Returns (raw)**: `ApiResult[DerivativesExchangesId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeTickersOrStr` | `coin_gecko_demo_api/models/enums/include_tickers.py` |
| `DerivativesExchangesId` | `coin_gecko_demo_api/models/derivatives_exchanges_id.py` |

### client.derivatives.derivatives_exchanges_list

- **Route**: `GET /derivatives/exchanges/list`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def derivatives_exchanges_list(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[DerivativesExchangesList]`
- **Returns (raw)**: `ApiResult[list[DerivativesExchangesList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DerivativesExchangesList` | `coin_gecko_demo_api/models/derivatives_exchanges_list.py` |

### client.derivatives.derivatives_tickers

- **Route**: `GET /derivatives`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def derivatives_tickers(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[DerivativesTicker]`
- **Returns (raw)**: `ApiResult[list[DerivativesTicker], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DerivativesTicker` | `coin_gecko_demo_api/models/derivatives_ticker.py` |

