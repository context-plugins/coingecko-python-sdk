<!-- Generated file — do not edit; regenerated with the SDK. -->

# GlobalApi — operations

Accessor: `client.global_api` · Source: `coin_gecko/apis/global_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.global_api.crypto_global

- **Route**: `GET /global`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def crypto_global(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `GlobalModel`
- **Returns (raw)**: `ApiResult[GlobalModel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GlobalModel` | `coin_gecko/models/global_model.py` |

### client.global_api.global_defi

- **Route**: `GET /global/decentralized_finance_defi`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def global_defi(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `GlobalDeFi`
- **Returns (raw)**: `ApiResult[GlobalDeFi, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GlobalDeFi` | `coin_gecko/models/global_de_fi.py` |

