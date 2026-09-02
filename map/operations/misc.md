<!-- Generated file — do not edit; regenerated with the SDK. -->

# Misc — operations

Accessor: `client.misc` · Source: `coin_gecko/apis/misc.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.misc.asset_platforms_list

- **Route**: `GET /asset_platforms`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def asset_platforms_list(*, filter: FilterOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `filter` — query
- **Returns (parsed)**: `list[AssetPlatform]`
- **Returns (raw)**: `ApiResult[list[AssetPlatform], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FilterOrStr` | `coin_gecko/models/enums/filter.py` |
| `AssetPlatform` | `coin_gecko/models/asset_platform.py` |

### client.misc.ping_server

- **Route**: `GET /ping`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def ping_server(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `PingServer`
- **Returns (raw)**: `ApiResult[PingServer, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PingServer` | `coin_gecko/models/ping_server.py` |

### client.misc.token_lists

- **Route**: `GET /token_lists/{asset_platform_id}/all.json`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def token_lists(*, asset_platform_id: str = "ethereum", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `asset_platform_id` — path
- **Returns (parsed)**: `TokenLists`
- **Returns (raw)**: `ApiResult[TokenLists, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TokenLists` | `coin_gecko/models/token_lists.py` |

