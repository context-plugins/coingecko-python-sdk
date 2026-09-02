<!-- Generated file — do not edit; regenerated with the SDK. -->

# SearchApi — operations

Accessor: `client.search_api` · Source: `coin_gecko/apis/search_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.search_api.search_data

- **Route**: `GET /search`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def search_data(query: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query`
- **Params**: `query` — query
- **Returns (parsed)**: `Search`
- **Returns (raw)**: `ApiResult[Search, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Search` | `coin_gecko/models/search.py` |

### client.search_api.trending_search

- **Route**: `GET /search/trending`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def trending_search(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TrendingSearch`
- **Returns (raw)**: `ApiResult[TrendingSearch, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TrendingSearch` | `coin_gecko/models/trending_search.py` |

