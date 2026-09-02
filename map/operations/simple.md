<!-- Generated file — do not edit; regenerated with the SDK. -->

# Simple — operations

Accessor: `client.simple` · Source: `coin_gecko/apis/simple.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.simple.simple_price

- **Route**: `GET /simple/price`
- **Auth**: `header_auth` OR `query_auth`
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

### client.simple.simple_supported_currencies

- **Route**: `GET /simple/supported_vs_currencies`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def simple_supported_currencies(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[str]`
- **Returns (raw)**: `ApiResult[list[str], RawError]`
- **Error**: `RawError` — **Case B**

### client.simple.simple_token_price

- **Route**: `GET /simple/token_price/{id}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def simple_token_price(*, id: str = "ethereum", contract_addresses: str = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599", vs_currencies: str = "usd", include_market_cap: bool | None = None, include_24hr_vol: bool | None = None, include_24hr_change: bool | None = None, include_last_updated_at: bool | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path · `contract_addresses` — query · `vs_currencies` — query · `include_market_cap` — query · `include_24hr_vol` — query · `include_24hr_change` — query · `include_last_updated_at` — query · `precision` — query
- **Returns (parsed)**: `dict[str, SimplePrice]`
- **Returns (raw)**: `ApiResult[dict[str, SimplePrice], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PrecisionOrStr` | `coin_gecko/models/enums/precision.py` |
| `SimplePrice` | `coin_gecko/models/simple_price.py` |

