<!-- Generated file — do not edit; regenerated with the SDK. -->

# PublicTreasuryApi — operations

Accessor: `client.public_treasury_api` · Source: `coin_gecko_demo_api/apis/public_treasury_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.public_treasury_api.public_treasury_entity

- **Route**: `GET /public_treasury/{entity_id}`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def public_treasury_entity(*, entity_id: str = "strategy", holding_amount_change: str | None = None, holding_change_percentage: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_id` — path · `holding_amount_change` — query · `holding_change_percentage` — query
- **Returns (parsed)**: `PublicTreasuryEntity`
- **Returns (raw)**: `ApiResult[PublicTreasuryEntity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PublicTreasuryEntity` | `coin_gecko_demo_api/models/public_treasury_entity.py` |

### client.public_treasury_api.public_treasury_entity_chart

- **Route**: `GET /public_treasury/{entity_id}/{coin_id}/holding_chart`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def public_treasury_entity_chart(*, entity_id: str = "strategy", coin_id: str = "bitcoin", days: str = "365", include_empty_intervals: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_id` — path · `coin_id` — path · `days` — query · `include_empty_intervals` — query
- **Returns (parsed)**: `PublicTreasuryEntityChart`
- **Returns (raw)**: `ApiResult[PublicTreasuryEntityChart, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PublicTreasuryEntityChart` | `coin_gecko_demo_api/models/public_treasury_entity_chart.py` |

### client.public_treasury_api.public_treasury_transaction_history

- **Route**: `GET /public_treasury/{entity_id}/transaction_history`
- **Auth**: `header_auth` OR `query_auth`
- **Signature**: `def public_treasury_transaction_history(*, entity_id: str = "strategy", per_page: int | None = None, page: int | None = None, order: Order6OrStr | None = None, coin_ids: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_id` — path · `per_page` — query · `page` — query · `order` — query · `coin_ids` — query
- **Returns (parsed)**: `PublicTreasuryTransactionHistory`
- **Returns (raw)**: `ApiResult[PublicTreasuryTransactionHistory, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order6OrStr` | `coin_gecko_demo_api/models/enums/order6.py` |
| `PublicTreasuryTransactionHistory` | `coin_gecko_demo_api/models/public_treasury_transaction_history.py` |

