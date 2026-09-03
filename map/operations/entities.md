<!-- Generated file — do not edit; regenerated with the SDK. -->

# Entities — operations

Accessor: `client.entities` · Source: `coin_gecko_demo_api/apis/entities.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.entities.companies_public_treasury

- **Route**: `GET /{entity}/public_treasury/{coin_id}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def companies_public_treasury(entity: EntityOrStr, *, coin_id: str = "bitcoin", per_page: int | None = None, page: int | None = None, order: Order5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `entity`
- **Params**: `entity` — path · `coin_id` — path · `per_page` — query · `page` — query · `order` — query
- **Returns (parsed)**: `PublicTreasury`
- **Returns (raw)**: `ApiResult[PublicTreasury, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EntityOrStr` | `coin_gecko_demo_api/models/enums/entity.py` |
| `Order5OrStr` | `coin_gecko_demo_api/models/enums/order5.py` |
| `PublicTreasury` | `coin_gecko_demo_api/models/unions/public_treasury.py` |

### client.entities.entities_list

- **Route**: `GET /entities/list`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def entities_list(*, entity_type: EntityTypeOrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_type` — query · `per_page` — query · `page` — query
- **Returns (parsed)**: `list[EntitiesList]`
- **Returns (raw)**: `ApiResult[list[EntitiesList], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EntityTypeOrStr` | `coin_gecko_demo_api/models/enums/entity_type.py` |
| `EntitiesList` | `coin_gecko_demo_api/models/entities_list.py` |

