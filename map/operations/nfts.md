<!-- Generated file — do not edit; regenerated with the SDK. -->

# Nfts — operations

Accessor: `client.nfts` · Source: `coin_gecko_demo_api/apis/nfts.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfts.nfts_contract_address

- **Route**: `GET /nfts/{asset_platform_id}/contract/{contract_address}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def nfts_contract_address(*, asset_platform_id: str = "ethereum", contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `asset_platform_id` — path · `contract_address` — path
- **Returns (parsed)**: `Nftdata`
- **Returns (raw)**: `ApiResult[Nftdata, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Nftdata` | `coin_gecko_demo_api/models/nftdata.py` |

### client.nfts.nfts_id

- **Route**: `GET /nfts/{id}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def nfts_id(*, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `id` — path
- **Returns (parsed)**: `Nftdata`
- **Returns (raw)**: `ApiResult[Nftdata, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Nftdata` | `coin_gecko_demo_api/models/nftdata.py` |

### client.nfts.nfts_list

- **Route**: `GET /nfts/list`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def nfts_list(*, order: Order7OrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `order` — query · `per_page` — query · `page` — query
- **Returns (parsed)**: `list[NftsList]`
- **Returns (raw)**: `ApiResult[list[NftsList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order7OrStr` | `coin_gecko_demo_api/models/enums/order7.py` |
| `NftsList` | `coin_gecko_demo_api/models/nfts_list.py` |

