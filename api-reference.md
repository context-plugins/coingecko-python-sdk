# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [CoinGeckoClient](coin_gecko/client.py)

<details>
<summary><code>def asset_platforms_list(*, filter: FilterOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> list[AssetPlatform]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported asset platforms (blockchain networks) on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_platforms_list()
    # TODO: Handle 'response' of type list[AssetPlatform]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_platforms_list()
    # TODO: Handle 'response' of type list[AssetPlatform]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>filter</code> | <code>[FilterOrStr](coin_gecko/models/enums/filter.py) \| None</code> | Apply relevant filters to results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AssetPlatform](coin_gecko/models/asset_platform.py)&#93;</code> -- List of asset platforms

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_categories(*, order: Order2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Category1]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the coins categories with market data (market cap, volume, etc.) on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_categories()
    # TODO: Handle 'response' of type list[Category1]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_categories()
    # TODO: Handle 'response' of type list[Category1]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order</code> | <code>[Order2OrStr](coin_gecko/models/enums/order2.py) \| None</code> | Sort results by field. <br>Default: `market_cap_desc`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Category1](coin_gecko/models/category1.py)&#93;</code> -- List of coin categories with market data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_categories_list(*, request_options: RequestOptionsOrDict | None = None) -> list[CategoriesList]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported coins categories on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_categories_list()
    # TODO: Handle 'response' of type list[CategoriesList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_categories_list()
    # TODO: Handle 'response' of type list[CategoriesList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[CategoriesList](coin_gecko/models/categories_list.py)&#93;</code> -- List of coin categories

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_contract_address(*, id: str = "ethereum", contract_address: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", request_options: RequestOptionsOrDict | None = None) -> CoinsContractAddress</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.) of a coin based on an asset platform and a particular token contract address

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_contract_address()
    # TODO: Handle 'response' of type CoinsContractAddress
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_contract_address()
    # TODO: Handle 'response' of type CoinsContractAddress
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Asset platform ID. <br>*refers to /reference/asset-platforms-list.<br>**Default**: <code>"ethereum"</code> |
| <code>contract_address</code> | <code>str</code> | The contract address of token.<br>**Default**: <code>"0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsContractAddress](coin_gecko/models/coins_contract_address.py)</code> -- Coin data by token contract address

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_id(*, id: str = "bitcoin", localization: bool | None = None, tickers: bool | None = None, market_data: bool | None = None, community_data: bool | None = None, developer_data: bool | None = None, sparkline: bool | None = None, include_categories_details: bool | None = None, dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CoinsId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.) of a coin based on a particular coin ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_id()
    # TODO: Handle 'response' of type CoinsId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_id()
    # TODO: Handle 'response' of type CoinsId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Coin ID. <br>*refers to /reference/coins-list<br>**Default**: <code>"bitcoin"</code> |
| <code>localization</code> | <code>bool \| None</code> | Include all localized languages in the response. <br>Default: true<br>**Default**: <code>None</code> |
| <code>tickers</code> | <code>bool \| None</code> | Include tickers data. <br>Default: true<br>**Default**: <code>None</code> |
| <code>market_data</code> | <code>bool \| None</code> | Include market data. <br>Default: true<br>**Default**: <code>None</code> |
| <code>community_data</code> | <code>bool \| None</code> | Include community data. <br>Default: true<br>**Default**: <code>None</code> |
| <code>developer_data</code> | <code>bool \| None</code> | Include developer data. <br>Default: true<br>**Default**: <code>None</code> |
| <code>sparkline</code> | <code>bool \| None</code> | Include sparkline 7-day data. <br>Default: false<br>**Default**: <code>None</code> |
| <code>include_categories_details</code> | <code>bool \| None</code> | Include categories details. <br>Default: false<br>**Default**: <code>None</code> |
| <code>dex_pair_format</code> | <code>[DexPairFormatOrStr](coin_gecko/models/enums/dex_pair_format.py) \| None</code> | Set to `symbol` to display DEX pair base and target as symbols. <br>Default: `contract_address`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsId](coin_gecko/models/coins_id.py)</code> -- Coin data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_id_history(*, id: str = "bitcoin", date: str = "30-12-2025", localization: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> CoinsIdHistory</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query the historical data (price, market cap, 24hrs volume, etc.) at a given date for a coin based on a particular coin ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_id_history()
    # TODO: Handle 'response' of type CoinsIdHistory
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_id_history()
    # TODO: Handle 'response' of type CoinsIdHistory
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Coin ID. <br>*refers to /reference/coins-list.<br>**Default**: <code>"bitcoin"</code> |
| <code>date</code> | <code>str</code> | The date of data snapshot. <br>Format: `dd-mm-yyyy`<br>**Default**: <code>"30-12-2025"</code> |
| <code>localization</code> | <code>bool \| None</code> | Include all the localized languages in response. <br>Default: true<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsIdHistory](coin_gecko/models/coins_id_history.py)</code> -- Coin historical data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_id_market_chart(*, id: str = "bitcoin", vs_currency: str = "usd", days: str = "1", interval: IntervalOrStr | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CoinsMarketChart</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get the historical chart data of a coin including time in UNIX, price, market cap and 24hrs volume based on particular coin ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_id_market_chart()
    # TODO: Handle 'response' of type CoinsMarketChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_id_market_chart()
    # TODO: Handle 'response' of type CoinsMarketChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Coin ID. <br>*refers to /reference/coins-list.<br>**Default**: <code>"bitcoin"</code> |
| <code>vs_currency</code> | <code>str</code> | Target currency of market data. <br>*refers to /reference/simple-supported-currencies.<br>**Default**: <code>"usd"</code> |
| <code>days</code> | <code>str</code> | Data up to number of days ago. <br>You may use any integer or `max` for number of days.<br>**Default**: <code>"1"</code> |
| <code>interval</code> | <code>[IntervalOrStr](coin_gecko/models/enums/interval.py) \| None</code> | Data interval, leave empty for auto granularity.<br>**Default**: <code>None</code> |
| <code>precision</code> | <code>[PrecisionOrStr](coin_gecko/models/enums/precision.py) \| None</code> | Decimal place for currency price value.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsMarketChart](coin_gecko/models/coins_market_chart.py)</code> -- Coin historical chart data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_id_market_chart_range(*, id: str = "bitcoin", vs_currency: str = "usd", from_: int = 1767024000, to: int = 1777564800, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CoinsMarketChart</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get the historical chart data of a coin within certain time range in UNIX along with price, market cap and 24hrs volume based on particular coin ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_id_market_chart_range()
    # TODO: Handle 'response' of type CoinsMarketChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_id_market_chart_range()
    # TODO: Handle 'response' of type CoinsMarketChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Coin ID. <br>*refers to /reference/coins-list.<br>**Default**: <code>"bitcoin"</code> |
| <code>vs_currency</code> | <code>str</code> | Target currency of market data. <br>*refers to /reference/simple-supported-currencies.<br>**Default**: <code>"usd"</code> |
| <code>from_</code> | <code>int</code> | Starting date in UNIX timestamp.<br>**Default**: <code>1767024000</code> |
| <code>to</code> | <code>int</code> | Ending date in UNIX timestamp.<br>**Default**: <code>1777564800</code> |
| <code>precision</code> | <code>[PrecisionOrStr](coin_gecko/models/enums/precision.py) \| None</code> | Decimal place for currency price value.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsMarketChart](coin_gecko/models/coins_market_chart.py)</code> -- Coin historical chart data within time range

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_id_ohlc(days: DaysOrStr, *, id: str = "bitcoin", vs_currency: str = "usd", precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> list[list[float]]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_id_ohlc(days)
    # TODO: Handle 'response' of type list[list[float]]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_id_ohlc(days)
    # TODO: Handle 'response' of type list[list[float]]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>days</code> | <code>[DaysOrStr](coin_gecko/models/enums/days.py)</code> | Data up to number of days ago. |
| <code>id</code> | <code>str</code> | Coin ID. <br>*refers to /reference/coins-list.<br>**Default**: <code>"bitcoin"</code> |
| <code>vs_currency</code> | <code>str</code> | Target currency of price data. <br>*refers to /reference/simple-supported-currencies.<br>**Default**: <code>"usd"</code> |
| <code>precision</code> | <code>[PrecisionOrStr](coin_gecko/models/enums/precision.py) \| None</code> | Decimal place for currency price value.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;list&#91;float&#93;&#93;</code> -- Coin OHLC chart data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_id_tickers(*, id: str = "bitcoin", exchange_ids: str | None = None, include_exchange_logo: bool | None = None, page: int | None = None, order: Order1OrStr | None = None, depth: bool | None = None, dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CoinsIdTickers</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query the coin tickers on both centralized exchange (CEX) and decentralized exchange (DEX) based on a particular coin ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_id_tickers()
    # TODO: Handle 'response' of type CoinsIdTickers
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_id_tickers()
    # TODO: Handle 'response' of type CoinsIdTickers
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Coin ID. <br>*refers to /reference/coins-list<br>**Default**: <code>"bitcoin"</code> |
| <code>exchange_ids</code> | <code>str \| None</code> | Exchange ID. <br>*refers to /reference/exchanges-list<br>**Default**: <code>None</code> |
| <code>include_exchange_logo</code> | <code>bool \| None</code> | Include exchange logo. <br>Default: false<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results<br>**Default**: <code>None</code> |
| <code>order</code> | <code>[Order1OrStr](coin_gecko/models/enums/order1.py) \| None</code> | Sort the order of responses. <br>Default: trust_score_desc<br>**Default**: <code>None</code> |
| <code>depth</code> | <code>bool \| None</code> | Include 2% orderbook depth, i.e. `cost_to_move_up_usd` and `cost_to_move_down_usd`. <br>Default: false<br>**Default**: <code>None</code> |
| <code>dex_pair_format</code> | <code>[DexPairFormatOrStr](coin_gecko/models/enums/dex_pair_format.py) \| None</code> | Set to `symbol` to display DEX pair base and target as symbols. <br>Default: `contract_address`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsIdTickers](coin_gecko/models/coins_id_tickers.py)</code> -- Coin tickers

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_list(*, include_platform: bool | None = None, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> list[CoinsList]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported coins on CoinGecko with coin ID, name and symbol

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_list()
    # TODO: Handle 'response' of type list[CoinsList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_list()
    # TODO: Handle 'response' of type list[CoinsList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include_platform</code> | <code>bool \| None</code> | Include platform and token's contract addresses. <br>Default: false<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[StatusOrStr](coin_gecko/models/enums/status.py) \| None</code> | Filter by status of coins. <br>Default: active<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[CoinsList](coin_gecko/models/coins_list.py)&#93;</code> -- List of coins

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def coins_markets(*, vs_currency: str = "usd", ids: str | None = "bitcoin", names: str | None = "Bitcoin", symbols: str | None = "btc", include_tokens: IncludeTokensOrStr | None = None, category: str | None = None, order: OrderOrStr | None = None, per_page: int | None = None, page: int | None = None, sparkline: bool | None = None, price_change_percentage: str | None = None, locale: LocaleOrStr | None = None, precision: PrecisionOrStr | None = None, include_rehypothecated: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> list[CoinsMarket]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported coins with price, market cap, volume and market related data

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coins_markets()
    # TODO: Handle 'response' of type list[CoinsMarket]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coins_markets()
    # TODO: Handle 'response' of type list[CoinsMarket]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vs_currency</code> | <code>str</code> | Target currency of coins and market data. <br>*refers to /reference/simple-supported-currencies<br>**Default**: <code>"usd"</code> |
| <code>ids</code> | <code>str \| None</code> | Coins' IDs, comma-separated if querying more than 1 coin. <br>*refers to /reference/coins-list<br>**Default**: <code>"bitcoin"</code> |
| <code>names</code> | <code>str \| None</code> | Coins' names, comma-separated if querying more than 1 coin.<br>**Default**: <code>"Bitcoin"</code> |
| <code>symbols</code> | <code>str \| None</code> | Coins' symbols, comma-separated if querying more than 1 coin.<br>**Default**: <code>"btc"</code> |
| <code>include_tokens</code> | <code>[IncludeTokensOrStr](coin_gecko/models/enums/include_tokens.py) \| None</code> | For `symbols` lookups, specify `all` to include all matching tokens. <br>Default `top` returns top-ranked tokens by market cap or volume.<br>**Default**: <code>None</code> |
| <code>category</code> | <code>str \| None</code> | Filter based on coins' category. <br>*refers to /reference/coins-categories-list<br>**Default**: <code>None</code> |
| <code>order</code> | <code>[OrderOrStr](coin_gecko/models/enums/order.py) \| None</code> | Sort result by field. <br>Default: market_cap_desc<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Total results per page. <br>Default: 100 <br>Valid values: 1...250<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default: 1<br>**Default**: <code>None</code> |
| <code>sparkline</code> | <code>bool \| None</code> | Include sparkline 7-day data. <br>Default: false<br>**Default**: <code>None</code> |
| <code>price_change_percentage</code> | <code>str \| None</code> | Include price change percentage timeframe, comma-separated if querying more than 1 timeframe. <br>Valid values: `1h`, `24h`, `7d`, `14d`, `30d`, `200d`, `1y`<br>**Default**: <code>None</code> |
| <code>locale</code> | <code>[LocaleOrStr](coin_gecko/models/enums/locale.py) \| None</code> | Language background. <br>Default: en<br>**Default**: <code>None</code> |
| <code>precision</code> | <code>[PrecisionOrStr](coin_gecko/models/enums/precision.py) \| None</code> | Decimal places for currency price value<br>**Default**: <code>None</code> |
| <code>include_rehypothecated</code> | <code>bool \| None</code> | Include rehypothecated tokens in results. When true, returns `market_cap_rank_with_rehypothecated` field. <br>Default: false<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[CoinsMarket](coin_gecko/models/coins_market.py)&#93;</code> -- List of coins with market data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def companies_public_treasury(entity: EntityOrStr, *, coin_id: str = "bitcoin", per_page: int | None = None, page: int | None = None, order: Order5OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> PublicTreasury</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query public companies' and governments' cryptocurrency holdings by coin ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.companies_public_treasury(entity)
    # TODO: Handle 'response' of type PublicTreasury
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.companies_public_treasury(entity)
    # TODO: Handle 'response' of type PublicTreasury
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity</code> | <code>[EntityOrStr](coin_gecko/models/enums/entity.py)</code> | Public company or government entity. |
| <code>coin_id</code> | <code>str</code> | Coin ID. <br>e.g. `bitcoin`, `ethereum`, `solana`, `binancecoin`<br>**Default**: <code>"bitcoin"</code> |
| <code>per_page</code> | <code>int \| None</code> | Total results per page. <br>Default value: 250 <br>Valid values: 1...250<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>order</code> | <code>[Order5OrStr](coin_gecko/models/enums/order5.py) \| None</code> | Sort order for results. <br>Default: `total_holdings_usd_desc`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PublicTreasury](coin_gecko/models/unions/public_treasury.py)</code> -- Public companies or governments crypto treasury holdings data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def contract_address_market_chart(*, id: str = "ethereum", contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", vs_currency: str = "usd", days: str = "1", interval: IntervalOrStr | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CoinsMarketChart</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get the historical chart data including time in UNIX, price, market cap and 24hrs volume based on asset platform and particular token contract address

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.contract_address_market_chart()
    # TODO: Handle 'response' of type CoinsMarketChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.contract_address_market_chart()
    # TODO: Handle 'response' of type CoinsMarketChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Asset platform ID. <br>*refers to /reference/asset-platforms-list.<br>**Default**: <code>"ethereum"</code> |
| <code>contract_address</code> | <code>str</code> | The contract address of token.<br>**Default**: <code>"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"</code> |
| <code>vs_currency</code> | <code>str</code> | Target currency of market data. <br>*refers to /reference/simple-supported-currencies.<br>**Default**: <code>"usd"</code> |
| <code>days</code> | <code>str</code> | Data up to number of days ago. <br>You may use any integer or `max` for number of days.<br>**Default**: <code>"1"</code> |
| <code>interval</code> | <code>[IntervalOrStr](coin_gecko/models/enums/interval.py) \| None</code> | Data interval, leave empty for auto granularity.<br>**Default**: <code>None</code> |
| <code>precision</code> | <code>[PrecisionOrStr](coin_gecko/models/enums/precision.py) \| None</code> | Decimal place for currency price value.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsMarketChart](coin_gecko/models/coins_market_chart.py)</code> -- Coin historical chart data by token address

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def contract_address_market_chart_range(*, id: str = "ethereum", contract_address: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", vs_currency: str = "usd", from_: int = 1767024000, to: int = 1777564800, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CoinsMarketChart</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get the historical chart data within certain time range in UNIX along with price, market cap and 24hrs volume based on asset platform and particular token contract address

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.contract_address_market_chart_range()
    # TODO: Handle 'response' of type CoinsMarketChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.contract_address_market_chart_range()
    # TODO: Handle 'response' of type CoinsMarketChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Asset platform ID. <br>*refers to /reference/asset-platforms-list.<br>**Default**: <code>"ethereum"</code> |
| <code>contract_address</code> | <code>str</code> | The contract address of token.<br>**Default**: <code>"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"</code> |
| <code>vs_currency</code> | <code>str</code> | Target currency of market data. <br>*refers to /reference/simple-supported-currencies.<br>**Default**: <code>"usd"</code> |
| <code>from_</code> | <code>int</code> | Starting date in UNIX timestamp.<br>**Default**: <code>1767024000</code> |
| <code>to</code> | <code>int</code> | Ending date in UNIX timestamp.<br>**Default**: <code>1777564800</code> |
| <code>precision</code> | <code>[PrecisionOrStr](coin_gecko/models/enums/precision.py) \| None</code> | Decimal place for currency price value.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsMarketChart](coin_gecko/models/coins_market_chart.py)</code> -- Coin historical chart data within time range by token address

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crypto_global(*, request_options: RequestOptionsOrDict | None = None) -> GlobalModel</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query cryptocurrency global data including active cryptocurrencies, markets, total crypto market cap and etc

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crypto_global()
    # TODO: Handle 'response' of type GlobalModel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.crypto_global()
    # TODO: Handle 'response' of type GlobalModel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GlobalModel](coin_gecko/models/global_model.py)</code> -- Cryptocurrency global market data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def derivatives_exchanges(*, order: Order4OrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[DerivativesExchange]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the derivatives exchanges with related data (ID, name, open interest, ...) on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.derivatives_exchanges()
    # TODO: Handle 'response' of type list[DerivativesExchange]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.derivatives_exchanges()
    # TODO: Handle 'response' of type list[DerivativesExchange]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order</code> | <code>[Order4OrStr](coin_gecko/models/enums/order4.py) \| None</code> | Sort order of responses. <br>Default: `open_interest_btc_desc`<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Total results per page.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[DerivativesExchange](coin_gecko/models/derivatives_exchange.py)&#93;</code> -- List of derivative exchanges with data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def derivatives_exchanges_id(*, id: str = "binance_futures", include_tickers: IncludeTickersOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> DerivativesExchangesId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query the derivatives exchange's related data (name, open interest, trade volume, ...) based on the exchange's ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.derivatives_exchanges_id()
    # TODO: Handle 'response' of type DerivativesExchangesId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.derivatives_exchanges_id()
    # TODO: Handle 'response' of type DerivativesExchangesId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Derivative exchange ID. <br>*refers to /reference/derivatives-exchanges-list.<br>**Default**: <code>"binance_futures"</code> |
| <code>include_tickers</code> | <code>[IncludeTickersOrStr](coin_gecko/models/enums/include_tickers.py) \| None</code> | Include tickers data. <br>Default: tickers data is not included.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DerivativesExchangesId](coin_gecko/models/derivatives_exchanges_id.py)</code> -- Derivative exchange data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def derivatives_exchanges_list(*, request_options: RequestOptionsOrDict | None = None) -> list[DerivativesExchangesList]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported derivatives exchanges with ID and name on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.derivatives_exchanges_list()
    # TODO: Handle 'response' of type list[DerivativesExchangesList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.derivatives_exchanges_list()
    # TODO: Handle 'response' of type list[DerivativesExchangesList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[DerivativesExchangesList](coin_gecko/models/derivatives_exchanges_list.py)&#93;</code> -- List of derivative exchange identifiers and names

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def derivatives_tickers(*, request_options: RequestOptionsOrDict | None = None) -> list[DerivativesTicker]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the tickers from derivatives exchanges on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.derivatives_tickers()
    # TODO: Handle 'response' of type list[DerivativesTicker]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.derivatives_tickers()
    # TODO: Handle 'response' of type list[DerivativesTicker]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[DerivativesTicker](coin_gecko/models/derivatives_ticker.py)&#93;</code> -- List of derivative tickers

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dexes_list(*, network: str = "eth", page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> DexesList</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported decentralized exchanges (DEXs) based on the provided network on GeckoTerminal

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dexes_list()
    # TODO: Handle 'response' of type DexesList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dexes_list()
    # TODO: Handle 'response' of type DexesList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DexesList](coin_gecko/models/dexes_list.py)</code> -- List of supported DEXs on a network

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def entities_list(*, entity_type: EntityTypeOrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[EntitiesList]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported entities on CoinGecko with entity ID, name, symbol, and country

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.entities_list()
    # TODO: Handle 'response' of type list[EntitiesList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.entities_list()
    # TODO: Handle 'response' of type list[EntitiesList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_type</code> | <code>[EntityTypeOrStr](coin_gecko/models/enums/entity_type.py) \| None</code> | Filter by entity type.<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Total results per page. <br>Default value: 100 <br>Valid values: 1...250<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[EntitiesList](coin_gecko/models/entities_list.py)&#93;</code> -- List of entities with ID, name, symbol, and country

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exchange_rates(*, request_options: RequestOptionsOrDict | None = None) -> ExchangeRates</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query BTC exchange rates with other currencies

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.exchange_rates()
    # TODO: Handle 'response' of type ExchangeRates
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exchange_rates()
    # TODO: Handle 'response' of type ExchangeRates
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ExchangeRates](coin_gecko/models/exchange_rates.py)</code> -- BTC exchange rates with other currencies

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exchanges(*, per_page: float | None = None, page: float | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Exchange1]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported exchanges with exchanges' data (ID, name, country, etc.) that have active trading volumes on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.exchanges()
    # TODO: Handle 'response' of type list[Exchange1]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exchanges()
    # TODO: Handle 'response' of type list[Exchange1]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>per_page</code> | <code>float \| None</code> | Total results per page. <br>Default: 100. <br>Valid values: 1...250<br>**Default**: <code>None</code> |
| <code>page</code> | <code>float \| None</code> | Page through results. <br>Default: 1<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Exchange1](coin_gecko/models/exchange1.py)&#93;</code> -- List of exchanges with data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exchanges_id(*, id: str = "binance", dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ExchangesId</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query exchange's data (name, year established, country, etc.), exchange volume in BTC and top 100 tickers based on exchange's ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.exchanges_id()
    # TODO: Handle 'response' of type ExchangesId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exchanges_id()
    # TODO: Handle 'response' of type ExchangesId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Exchange ID. <br>*refers to /reference/exchanges-list.<br>**Default**: <code>"binance"</code> |
| <code>dex_pair_format</code> | <code>[DexPairFormatOrStr](coin_gecko/models/enums/dex_pair_format.py) \| None</code> | Set to `symbol` to display DEX pair base and target as symbols. <br>Default: `contract_address`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ExchangesId](coin_gecko/models/exchanges_id.py)</code> -- Exchange data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exchanges_id_tickers(*, id: str = "binance", coin_ids: str | None = None, include_exchange_logo: bool | None = None, page: float | None = None, depth: bool | None = None, order: Order3OrStr | None = None, dex_pair_format: DexPairFormatOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CoinsIdTickers</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query exchange's tickers based on exchange's ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.exchanges_id_tickers()
    # TODO: Handle 'response' of type CoinsIdTickers
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exchanges_id_tickers()
    # TODO: Handle 'response' of type CoinsIdTickers
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Exchange ID. <br>*refers to /reference/exchanges-list.<br>**Default**: <code>"binance"</code> |
| <code>coin_ids</code> | <code>str \| None</code> | Filter tickers by coin IDs, comma-separated if querying more than 1 coin. <br>*refers to /reference/coins-list.<br>**Default**: <code>None</code> |
| <code>include_exchange_logo</code> | <code>bool \| None</code> | Include exchange logo. <br>Default: false<br>**Default**: <code>None</code> |
| <code>page</code> | <code>float \| None</code> | Page through results.<br>**Default**: <code>None</code> |
| <code>depth</code> | <code>bool \| None</code> | Include 2% orderbook depth (cost_to_move_up_usd and cost_to_move_down_usd). <br>Default: false<br>**Default**: <code>None</code> |
| <code>order</code> | <code>[Order3OrStr](coin_gecko/models/enums/order3.py) \| None</code> | Sort the order of responses. <br>Default: `trust_score_desc`<br>**Default**: <code>None</code> |
| <code>dex_pair_format</code> | <code>[DexPairFormatOrStr](coin_gecko/models/enums/dex_pair_format.py) \| None</code> | Set to `symbol` to display DEX pair base and target as symbols. <br>Default: `contract_address`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CoinsIdTickers](coin_gecko/models/coins_id_tickers.py)</code> -- Exchange tickers

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exchanges_id_volume_chart(days: DaysOrStr, *, id: str = "binance", request_options: RequestOptionsOrDict | None = None) -> list[list[ExchangeVolumeChart]]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query the historical volume chart data with time in UNIX and trading volume data in BTC based on exchange's ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.exchanges_id_volume_chart(days)
    # TODO: Handle 'response' of type list[list[ExchangeVolumeChart]]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exchanges_id_volume_chart(days)
    # TODO: Handle 'response' of type list[list[ExchangeVolumeChart]]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>days</code> | <code>[DaysOrStr](coin_gecko/models/enums/days.py)</code> | Data up to number of days ago. |
| <code>id</code> | <code>str</code> | Exchange ID or derivative exchange ID. <br>*refers to /reference/exchanges-list or /reference/derivatives-exchanges-list.<br>**Default**: <code>"binance"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;list&#91;[ExchangeVolumeChart](coin_gecko/models/unions/exchange_volume_chart.py)&#93;&#93;</code> -- Exchange volume chart data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exchanges_list(*, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ExchangesList]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported exchanges with ID and name

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.exchanges_list()
    # TODO: Handle 'response' of type list[ExchangesList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exchanges_list()
    # TODO: Handle 'response' of type list[ExchangesList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>status</code> | <code>[StatusOrStr](coin_gecko/models/enums/status.py) \| None</code> | Filter by status of exchanges. <br>Default: `active`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ExchangesList](coin_gecko/models/exchanges_list.py)&#93;</code> -- List of exchanges

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def global_defi(*, request_options: RequestOptionsOrDict | None = None) -> GlobalDeFi</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query top 100 cryptocurrency global decentralized finance (DeFi) data including DeFi market cap, trading volume

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.global_defi()
    # TODO: Handle 'response' of type GlobalDeFi
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.global_defi()
    # TODO: Handle 'response' of type GlobalDeFi
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GlobalDeFi](coin_gecko/models/global_de_fi.py)</code> -- Global decentralized finance (DeFi) market data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def latest_pools_list(*, include: str | None = None, page: int | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Pool</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the latest pools across all networks on GeckoTerminal

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.latest_pools_list()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.latest_pools_list()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`, `network`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>include_gt_community_data</code> | <code>bool \| None</code> | Include GeckoTerminal community data (sentiment votes, suspicious reports). <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Pool](coin_gecko/models/pool.py)</code> -- Latest pools across all networks

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def latest_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Pool</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the latest pools based on the provided network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.latest_pools_network()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.latest_pools_network()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>include_gt_community_data</code> | <code>bool \| None</code> | Include GeckoTerminal community data (sentiment votes, suspicious reports). <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Pool](coin_gecko/models/pool.py)</code> -- Latest pools on a network

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def networks_list(*, page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> NetworksList</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To retrieve a list of all supported networks on GeckoTerminal

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.networks_list()
    # TODO: Handle 'response' of type NetworksList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.networks_list()
    # TODO: Handle 'response' of type NetworksList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[NetworksList](coin_gecko/models/networks_list.py)</code> -- List of supported networks

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def nfts_contract_address(*, asset_platform_id: str = "ethereum", contract_address: str = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8", request_options: RequestOptionsOrDict | None = None) -> Nftdata</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection contract address and respective asset platform

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.nfts_contract_address()
    # TODO: Handle 'response' of type Nftdata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.nfts_contract_address()
    # TODO: Handle 'response' of type Nftdata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset_platform_id</code> | <code>str</code> | Asset platform ID. <br>*refers to /reference/asset-platforms-list.<br>**Default**: <code>"ethereum"</code> |
| <code>contract_address</code> | <code>str</code> | Contract address of the NFT collection.<br>**Default**: <code>"0xBd3531dA5CF5857e7CfAA92426877b022e612cf8"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Nftdata](coin_gecko/models/nftdata.py)</code> -- NFT collection data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def nfts_id(*, id: str = "pudgy-penguins", request_options: RequestOptionsOrDict | None = None) -> Nftdata</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the NFT data (name, floor price, 24hr volume, ...) based on the NFT collection ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.nfts_id()
    # TODO: Handle 'response' of type Nftdata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.nfts_id()
    # TODO: Handle 'response' of type Nftdata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | NFT collection ID. <br>*refers to /reference/nfts-list.<br>**Default**: <code>"pudgy-penguins"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Nftdata](coin_gecko/models/nftdata.py)</code> -- NFT collection data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def nfts_list(*, order: Order7OrStr | None = None, per_page: int | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[NftsList]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all supported NFTs with ID, contract address, name, asset platform ID and symbol on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.nfts_list()
    # TODO: Handle 'response' of type list[NftsList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.nfts_list()
    # TODO: Handle 'response' of type list[NftsList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order</code> | <code>[Order7OrStr](coin_gecko/models/enums/order7.py) \| None</code> | Sort order of responses.<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Total results per page. <br>Valid values: 1...250<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[NftsList](coin_gecko/models/nfts_list.py)&#93;</code> -- List of supported NFTs

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def onchain_simple_price(*, network: str = "eth", addresses: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", include_market_cap: bool | None = None, mcap_fdv_fallback: bool | None = None, include_24hr_vol: bool | None = None, include_24hr_price_change: bool | None = None, include_total_reserve_in_usd: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> OnchainSimplePrice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get token price based on the provided token contract address on a network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.onchain_simple_price()
    # TODO: Handle 'response' of type OnchainSimplePrice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.onchain_simple_price()
    # TODO: Handle 'response' of type OnchainSimplePrice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>addresses</code> | <code>str</code> | Token contract address, comma-separated if more than one token contract address.<br>**Default**: <code>"0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"</code> |
| <code>include_market_cap</code> | <code>bool \| None</code> | Include market capitalization. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>mcap_fdv_fallback</code> | <code>bool \| None</code> | Return FDV if market cap is not available. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>include_24hr_vol</code> | <code>bool \| None</code> | Include 24hr volume. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>include_24hr_price_change</code> | <code>bool \| None</code> | Include 24hr price change. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>include_total_reserve_in_usd</code> | <code>bool \| None</code> | Include total reserve in USD. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>include_inactive_source</code> | <code>bool \| None</code> | Include token price data from inactive pools using the most recent swap. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OnchainSimplePrice](coin_gecko/models/onchain_simple_price.py)</code> -- Token price data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ping_server(*, request_options: RequestOptionsOrDict | None = None) -> PingServer</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To check the API server status

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.ping_server()
    # TODO: Handle 'response' of type PingServer
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.ping_server()
    # TODO: Handle 'response' of type PingServer
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PingServer](coin_gecko/models/ping_server.py)</code> -- Server status

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pool_address(*, network: str = "eth", address: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", include: str | None = None, include_volume_breakdown: bool | None = None, include_composition: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> PoolAddressData</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query the specific pool based on the provided network and pool address

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pool_address()
    # TODO: Handle 'response' of type PoolAddressData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pool_address()
    # TODO: Handle 'response' of type PoolAddressData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>address</code> | <code>str</code> | Pool address.<br>**Default**: <code>"0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640"</code> |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`<br>**Default**: <code>None</code> |
| <code>include_volume_breakdown</code> | <code>bool \| None</code> | Include volume breakdown. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>include_composition</code> | <code>bool \| None</code> | Include pool composition. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PoolAddressData](coin_gecko/models/pool_address_data.py)</code> -- Specific pool data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pool_ohlcv_contract_address(timeframe: TimeframeOrStr, *, network: str = "eth", pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553", aggregate: str | None = None, before_timestamp: int | None = None, limit: int | None = None, currency: CurrencyOrStr | None = None, token: str | None = None, include_empty_intervals: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Ohlcv</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pool_ohlcv_contract_address(timeframe)
    # TODO: Handle 'response' of type Ohlcv
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pool_ohlcv_contract_address(timeframe)
    # TODO: Handle 'response' of type Ohlcv
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>timeframe</code> | <code>[TimeframeOrStr](coin_gecko/models/enums/timeframe.py)</code> | Timeframe of the OHLCV chart. |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>pool_address</code> | <code>str</code> | Pool contract address.<br>**Default**: <code>"0x06da0fd433c1a5d7a4faa01111c044910a184553"</code> |
| <code>aggregate</code> | <code>str \| None</code> | Time period to aggregate each OHLCV. <br>Available values (day): `1` <br>Available values (hour): `1`, `4`, `12` <br>Available values (minute): `1`, `5`, `15` <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>before_timestamp</code> | <code>int \| None</code> | Return OHLCV data before this timestamp (integer seconds since epoch).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Number of OHLCV results to return, maximum 1000. <br>Default value: 100<br>**Default**: <code>None</code> |
| <code>currency</code> | <code>[CurrencyOrStr](coin_gecko/models/enums/currency.py) \| None</code> | Return OHLCV in USD or quote token. <br>Default: `usd`<br>**Default**: <code>None</code> |
| <code>token</code> | <code>str \| None</code> | Return OHLCV for token, use this to invert the chart. <br>Available values: `base`, `quote`, or token address. <br>Default: `base`<br>**Default**: <code>None</code> |
| <code>include_empty_intervals</code> | <code>bool \| None</code> | Include empty intervals with no trade data. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Ohlcv](coin_gecko/models/ohlcv.py)</code> -- Pool OHLCV chart data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pool_token_info_contract_address(*, network: str = "solana", pool_address: str = "8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt", include: Include2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> PoolTokensInfo</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query pool metadata (base and quote token details, image, socials, websites, description, contract address, etc.) based on a provided pool contract address on a network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pool_token_info_contract_address()
    # TODO: Handle 'response' of type PoolTokensInfo
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pool_token_info_contract_address()
    # TODO: Handle 'response' of type PoolTokensInfo
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"solana"</code> |
| <code>pool_address</code> | <code>str</code> | Pool contract address.<br>**Default**: <code>"8WwcNqdZjCY5Pt7AkhupAFknV2txca9sq6YBkGzLbvdt"</code> |
| <code>include</code> | <code>[Include2OrStr](coin_gecko/models/enums/include2.py) \| None</code> | Attributes to include.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PoolTokensInfo](coin_gecko/models/pool_tokens_info.py)</code> -- Pool tokens info data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pool_trades_contract_address(*, network: str = "eth", pool_address: str = "0x06da0fd433c1a5d7a4faa01111c044910a184553", trade_volume_in_usd_greater_than: float | None = None, token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Trades</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query the last 300 trades in the past 24 hours based on the provided pool address

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pool_trades_contract_address()
    # TODO: Handle 'response' of type Trades
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pool_trades_contract_address()
    # TODO: Handle 'response' of type Trades
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>pool_address</code> | <code>str</code> | Pool contract address.<br>**Default**: <code>"0x06da0fd433c1a5d7a4faa01111c044910a184553"</code> |
| <code>trade_volume_in_usd_greater_than</code> | <code>float \| None</code> | Filter trades by trade volume in USD greater than this value. <br>Default value: 0<br>**Default**: <code>None</code> |
| <code>token</code> | <code>str \| None</code> | Return trades for token, use this to invert the chart. <br>Available values: `base`, `quote`, or token address. <br>Default: `base`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Trades](coin_gecko/models/trades.py)</code> -- Last 300 trades in past 24 hours from a pool

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pools_addresses(*, network: str = "eth", addresses: str = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", include: str | None = None, include_volume_breakdown: bool | None = None, include_composition: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> MultiPoolAddressData</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query multiple pools based on the provided network and pool addresses

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pools_addresses()
    # TODO: Handle 'response' of type MultiPoolAddressData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pools_addresses()
    # TODO: Handle 'response' of type MultiPoolAddressData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>addresses</code> | <code>str</code> | Pool contract address, comma-separated if more than one pool contract address.<br>**Default**: <code>"0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640"</code> |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`<br>**Default**: <code>None</code> |
| <code>include_volume_breakdown</code> | <code>bool \| None</code> | Include volume breakdown. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>include_composition</code> | <code>bool \| None</code> | Include pool composition. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MultiPoolAddressData](coin_gecko/models/multi_pool_address_data.py)</code> -- Multiple pools data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def public_treasury_entity(*, entity_id: str = "strategy", holding_amount_change: str | None = None, holding_change_percentage: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PublicTreasuryEntity</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query public companies' and governments' cryptocurrency holdings by entity ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.public_treasury_entity()
    # TODO: Handle 'response' of type PublicTreasuryEntity
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.public_treasury_entity()
    # TODO: Handle 'response' of type PublicTreasuryEntity
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_id</code> | <code>str</code> | Public company or government entity ID. <br>*refers to /reference/entities-list.<br>**Default**: <code>"strategy"</code> |
| <code>holding_amount_change</code> | <code>str \| None</code> | Include holding amount change for specified timeframes, comma-separated if querying more than 1 timeframe. <br>Valid values: `7d`, `14d`, `30d`, `90d`, `1y`, `ytd`<br>**Default**: <code>None</code> |
| <code>holding_change_percentage</code> | <code>str \| None</code> | Include holding change percentage for specified timeframes, comma-separated if querying more than 1 timeframe. <br>Valid values: `7d`, `14d`, `30d`, `90d`, `1y`, `ytd`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PublicTreasuryEntity](coin_gecko/models/public_treasury_entity.py)</code> -- Public company or government crypto treasury holdings data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def public_treasury_entity_chart(*, entity_id: str = "strategy", coin_id: str = "bitcoin", days: str = "365", include_empty_intervals: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> PublicTreasuryEntityChart</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query historical cryptocurrency holdings chart of public companies and governments by entity ID and coin ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.public_treasury_entity_chart()
    # TODO: Handle 'response' of type PublicTreasuryEntityChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.public_treasury_entity_chart()
    # TODO: Handle 'response' of type PublicTreasuryEntityChart
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_id</code> | <code>str</code> | Public company or government entity ID. <br>*refers to /reference/entities-list.<br>**Default**: <code>"strategy"</code> |
| <code>coin_id</code> | <code>str</code> | Coin ID. <br>e.g. `bitcoin`, `ethereum`, `solana`, `binancecoin`<br>**Default**: <code>"bitcoin"</code> |
| <code>days</code> | <code>str</code> | Data up to number of days ago. <br>Valid values: `7`, `14`, `30`, `90`, `180`, `365`<br>**Default**: <code>"365"</code> |
| <code>include_empty_intervals</code> | <code>bool \| None</code> | Include empty intervals with no transaction data. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PublicTreasuryEntityChart](coin_gecko/models/public_treasury_entity_chart.py)</code> -- Crypto treasury holdings historical chart data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def public_treasury_transaction_history(*, entity_id: str = "strategy", per_page: int | None = None, page: int | None = None, order: Order6OrStr | None = None, coin_ids: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PublicTreasuryTransactionHistory</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query public companies' and governments' cryptocurrency transaction history by entity ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.public_treasury_transaction_history()
    # TODO: Handle 'response' of type PublicTreasuryTransactionHistory
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.public_treasury_transaction_history()
    # TODO: Handle 'response' of type PublicTreasuryTransactionHistory
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_id</code> | <code>str</code> | Public company or government entity ID. <br>*refers to /reference/entities-list.<br>**Default**: <code>"strategy"</code> |
| <code>per_page</code> | <code>int \| None</code> | Total results per page. <br>Default value: 100 <br>Valid values: 1...250<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>order</code> | <code>[Order6OrStr](coin_gecko/models/enums/order6.py) \| None</code> | Sort order of transactions. <br>Default: `date_desc`<br>**Default**: <code>None</code> |
| <code>coin_ids</code> | <code>str \| None</code> | Filter transactions by coin IDs, comma-separated if querying more than 1 coin. <br>*refers to /reference/coins-list.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PublicTreasuryTransactionHistory](coin_gecko/models/public_treasury_transaction_history.py)</code> -- Crypto treasury transaction history data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_data(query: str, *, request_options: RequestOptionsOrDict | None = None) -> Search</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To search for coins, categories and markets listed on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.search_data(query)
    # TODO: Handle 'response' of type Search
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.search_data(query)
    # TODO: Handle 'response' of type Search
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query</code> | <code>str</code> | Search query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Search](coin_gecko/models/search.py)</code> -- Search results

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_pools(*, query: str | None = "weth", network: str | None = None, include: str | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> PoolSearch</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To search for pools across all networks by pool address, token name, token symbol, or token contract address

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.search_pools()
    # TODO: Handle 'response' of type PoolSearch
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.search_pools()
    # TODO: Handle 'response' of type PoolSearch
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query</code> | <code>str \| None</code> | Search query: pool contract address, token name, token symbol, or token contract address.<br>**Default**: <code>"weth"</code> |
| <code>network</code> | <code>str \| None</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>None</code> |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PoolSearch](coin_gecko/models/pool_search.py)</code> -- Pool search results

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def simple_price(*, vs_currencies: str = "usd", ids: str | None = "bitcoin", names: str | None = "Bitcoin", symbols: str | None = "btc", include_tokens: IncludeTokensOrStr | None = None, include_market_cap: bool | None = None, include_24hr_vol: bool | None = None, include_24hr_change: bool | None = None, include_last_updated_at: bool | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> dict[str, SimplePrice]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query the prices of one or more coins by using their unique Coin API IDs, symbols, or names

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_price()
    # TODO: Handle 'response' of type dict[str, SimplePrice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.simple_price()
    # TODO: Handle 'response' of type dict[str, SimplePrice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vs_currencies</code> | <code>str</code> | Target currency of coins, comma-separated if querying more than 1 currency. <br>*refers to /reference/simple-supported-currencies<br>**Default**: <code>"usd"</code> |
| <code>ids</code> | <code>str \| None</code> | Coins' IDs, comma-separated if querying more than 1 coin. <br>*refers to /reference/coins-list<br>**Default**: <code>"bitcoin"</code> |
| <code>names</code> | <code>str \| None</code> | Coins' names, comma-separated if querying more than 1 coin.<br>**Default**: <code>"Bitcoin"</code> |
| <code>symbols</code> | <code>str \| None</code> | Coins' symbols, comma-separated if querying more than 1 coin.<br>**Default**: <code>"btc"</code> |
| <code>include_tokens</code> | <code>[IncludeTokensOrStr](coin_gecko/models/enums/include_tokens.py) \| None</code> | For `symbols` lookups, specify `all` to include all matching tokens. <br>Default `top` returns top-ranked tokens by market cap or volume.<br>**Default**: <code>None</code> |
| <code>include_market_cap</code> | <code>bool \| None</code> | Include market capitalization. <br>Default: false<br>**Default**: <code>None</code> |
| <code>include_24hr_vol</code> | <code>bool \| None</code> | Include 24-hour trading volume. <br>Default: false<br>**Default**: <code>None</code> |
| <code>include_24hr_change</code> | <code>bool \| None</code> | Include 24-hour change percentage. <br>Default: false<br>**Default**: <code>None</code> |
| <code>include_last_updated_at</code> | <code>bool \| None</code> | Include last updated price time as a UNIX timestamp. <br>Default: false<br>**Default**: <code>None</code> |
| <code>precision</code> | <code>[PrecisionOrStr](coin_gecko/models/enums/precision.py) \| None</code> | Decimal places for currency price value<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>dict&#91;str, [SimplePrice](coin_gecko/models/simple_price.py)&#93;</code> -- Coin prices

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def simple_supported_currencies(*, request_options: RequestOptionsOrDict | None = None) -> list[str]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the supported currencies on CoinGecko

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_supported_currencies()
    # TODO: Handle 'response' of type list[str]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.simple_supported_currencies()
    # TODO: Handle 'response' of type list[str]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;str&#93;</code> -- List of supported currencies

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def simple_token_price(*, id: str = "ethereum", contract_addresses: str = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599", vs_currencies: str = "usd", include_market_cap: bool | None = None, include_24hr_vol: bool | None = None, include_24hr_change: bool | None = None, include_last_updated_at: bool | None = None, precision: PrecisionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> dict[str, SimplePrice]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query one or more token prices by using their token contract addresses

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.simple_token_price()
    # TODO: Handle 'response' of type dict[str, SimplePrice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.simple_token_price()
    # TODO: Handle 'response' of type dict[str, SimplePrice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Asset platform's ID. <br>*refers to /reference/asset-platforms-list<br>**Default**: <code>"ethereum"</code> |
| <code>contract_addresses</code> | <code>str</code> | Token contract addresses, comma-separated if querying more than 1 token<br>**Default**: <code>"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"</code> |
| <code>vs_currencies</code> | <code>str</code> | Target currency of coins, comma-separated if querying more than 1 currency. <br>*refers to /reference/simple-supported-currencies<br>**Default**: <code>"usd"</code> |
| <code>include_market_cap</code> | <code>bool \| None</code> | Include market capitalization. <br>Default: false<br>**Default**: <code>None</code> |
| <code>include_24hr_vol</code> | <code>bool \| None</code> | Include 24-hour trading volume. <br>Default: false<br>**Default**: <code>None</code> |
| <code>include_24hr_change</code> | <code>bool \| None</code> | Include 24-hour change percentage. <br>Default: false<br>**Default**: <code>None</code> |
| <code>include_last_updated_at</code> | <code>bool \| None</code> | Include last updated price time as a UNIX timestamp. <br>Default: false<br>**Default**: <code>None</code> |
| <code>precision</code> | <code>[PrecisionOrStr](coin_gecko/models/enums/precision.py) \| None</code> | Decimal places for currency price value<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>dict&#91;str, [SimplePrice](coin_gecko/models/simple_price.py)&#93;</code> -- Token prices

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def token_data_contract_address(*, network: str = "eth", address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7", include: IncludeOrStr | None = None, include_composition: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> TokenData</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query specific token data based on the provided token contract address on a network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.token_data_contract_address()
    # TODO: Handle 'response' of type TokenData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.token_data_contract_address()
    # TODO: Handle 'response' of type TokenData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>address</code> | <code>str</code> | Token contract address.<br>**Default**: <code>"0xdac17f958d2ee523a2206206994597c13d831ec7"</code> |
| <code>include</code> | <code>[IncludeOrStr](coin_gecko/models/enums/include.py) \| None</code> | Attributes to include.<br>**Default**: <code>None</code> |
| <code>include_composition</code> | <code>bool \| None</code> | Include pool composition. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>include_inactive_source</code> | <code>bool \| None</code> | Include token data from inactive pools using the most recent swap. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TokenData](coin_gecko/models/token_data.py)</code> -- Token data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def token_info_contract_address(*, network: str = "solana", address: str = "Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump", request_options: RequestOptionsOrDict | None = None) -> TokenInfo</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query token metadata (name, symbol, CoinGecko ID, image, socials, websites, description, etc.) based on a provided token contract address on a network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.token_info_contract_address()
    # TODO: Handle 'response' of type TokenInfo
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.token_info_contract_address()
    # TODO: Handle 'response' of type TokenInfo
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"solana"</code> |
| <code>address</code> | <code>str</code> | Token contract address.<br>**Default**: <code>"Dfh5DzRgSvvCFDoYc2ciTkMrbDfRKybA4SoFbPmApump"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TokenInfo](coin_gecko/models/token_info.py)</code> -- Token info data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def token_lists(*, asset_platform_id: str = "ethereum", request_options: RequestOptionsOrDict | None = None) -> TokenLists</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To get full list of tokens of a blockchain network (asset platform) that is supported by [Ethereum token list standard](https://tokenlists.org/)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.token_lists()
    # TODO: Handle 'response' of type TokenLists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.token_lists()
    # TODO: Handle 'response' of type TokenLists
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asset_platform_id</code> | <code>str</code> | Asset platform ID. <br>*refers to /reference/asset-platforms-list.<br>**Default**: <code>"ethereum"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TokenLists](coin_gecko/models/token_lists.py)</code> -- Token list by asset platform

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def tokens_data_contract_addresses(*, network: str = "solana", addresses: str = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump", include: IncludeOrStr | None = None, include_composition: bool | None = None, include_inactive_source: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> MultiTokenData</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query multiple tokens data based on the provided token contract addresses on a network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tokens_data_contract_addresses()
    # TODO: Handle 'response' of type MultiTokenData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.tokens_data_contract_addresses()
    # TODO: Handle 'response' of type MultiTokenData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"solana"</code> |
| <code>addresses</code> | <code>str</code> | Token contract address, comma-separated if more than one token contract address.<br>**Default**: <code>"6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump"</code> |
| <code>include</code> | <code>[IncludeOrStr](coin_gecko/models/enums/include.py) \| None</code> | Attributes to include.<br>**Default**: <code>None</code> |
| <code>include_composition</code> | <code>bool \| None</code> | Include pool composition. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>include_inactive_source</code> | <code>bool \| None</code> | Include tokens from inactive pools using the most recent swap. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MultiTokenData](coin_gecko/models/multi_token_data.py)</code> -- Multiple tokens data

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def tokens_info_recent_updated(*, include: Include3OrStr | None = None, network: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TokenInfoRecentlyUpdated</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tokens_info_recent_updated()
    # TODO: Handle 'response' of type TokenInfoRecentlyUpdated
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.tokens_info_recent_updated()
    # TODO: Handle 'response' of type TokenInfoRecentlyUpdated
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include</code> | <code>[Include3OrStr](coin_gecko/models/enums/include3.py) \| None</code> | Attributes for related resources to include.<br>**Default**: <code>None</code> |
| <code>network</code> | <code>str \| None</code> | Filter tokens by provided network. <br>*refers to /reference/networks-list.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TokenInfoRecentlyUpdated](coin_gecko/models/token_info_recently_updated.py)</code> -- Most recently updated tokens info

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def top_pools_contract_address(*, network: str = "eth", token_address: str = "0xdac17f958d2ee523a2206206994597c13d831ec7", include: str | None = None, include_inactive_source: bool | None = None, page: int | None = None, sort: Sort2OrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Pool</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query top pools based on the provided token contract address on a network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.top_pools_contract_address()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.top_pools_contract_address()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>token_address</code> | <code>str</code> | Token contract address.<br>**Default**: <code>"0xdac17f958d2ee523a2206206994597c13d831ec7"</code> |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`<br>**Default**: <code>None</code> |
| <code>include_inactive_source</code> | <code>bool \| None</code> | Include tokens from inactive pools using the most recent swap. <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[Sort2OrStr](coin_gecko/models/enums/sort2.py) \| None</code> | Sort the pools by field. <br>Default: `h24_volume_usd_liquidity_desc`<br>**Default**: <code>None</code> |
| <code>include_gt_community_data</code> | <code>bool \| None</code> | Include GeckoTerminal community data (sentiment votes, suspicious reports). <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Pool](coin_gecko/models/pool.py)</code> -- Top pools for a token

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def top_pools_dex(*, network: str = "eth", dex: str = "sushiswap", include: str | None = None, page: int | None = None, sort: SortOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Pool</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the top pools based on the provided network and decentralized exchange (DEX)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.top_pools_dex()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.top_pools_dex()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>dex</code> | <code>str</code> | DEX ID. <br>*refers to /reference/dexes-list.<br>**Default**: <code>"sushiswap"</code> |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[SortOrStr](coin_gecko/models/enums/sort.py) \| None</code> | Sort the pools by field. <br>Default: `h24_tx_count_desc`<br>**Default**: <code>None</code> |
| <code>include_gt_community_data</code> | <code>bool \| None</code> | Include GeckoTerminal community data (sentiment votes, suspicious reports). <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Pool](coin_gecko/models/pool.py)</code> -- Top pools on a network's DEX

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def top_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, sort: SortOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Pool</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the top pools based on the provided network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.top_pools_network()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.top_pools_network()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[SortOrStr](coin_gecko/models/enums/sort.py) \| None</code> | Sort the pools by field. <br>Default: `h24_tx_count_desc`<br>**Default**: <code>None</code> |
| <code>include_gt_community_data</code> | <code>bool \| None</code> | Include GeckoTerminal community data (sentiment votes, suspicious reports). <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Pool](coin_gecko/models/pool.py)</code> -- Top pools on a network

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def trending_pools_list(*, include: str | None = None, page: int | None = None, duration: DurationOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Pool</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query all the trending pools across all networks on GeckoTerminal

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trending_pools_list()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.trending_pools_list()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`, `network`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>duration</code> | <code>[DurationOrStr](coin_gecko/models/enums/duration.py) \| None</code> | Duration to sort trending list by. <br>Default: `24h`<br>**Default**: <code>None</code> |
| <code>include_gt_community_data</code> | <code>bool \| None</code> | Include GeckoTerminal community data (sentiment votes, suspicious reports). <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Pool](coin_gecko/models/pool.py)</code> -- Trending pools across all networks

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def trending_pools_network(*, network: str = "eth", include: str | None = None, page: int | None = None, duration: DurationOrStr | None = None, include_gt_community_data: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Pool</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query the trending pools based on the provided network

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trending_pools_network()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.trending_pools_network()
    # TODO: Handle 'response' of type Pool
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>network</code> | <code>str</code> | Network ID. <br>*refers to /reference/networks-list.<br>**Default**: <code>"eth"</code> |
| <code>include</code> | <code>str \| None</code> | Attributes to include, comma-separated if more than one. <br>Available values: `base_token`, `quote_token`, `dex`<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page through results. <br>Default value: 1<br>**Default**: <code>None</code> |
| <code>duration</code> | <code>[DurationOrStr](coin_gecko/models/enums/duration.py) \| None</code> | Duration to sort trending list by. <br>Default: `24h`<br>**Default**: <code>None</code> |
| <code>include_gt_community_data</code> | <code>bool \| None</code> | Include GeckoTerminal community data (sentiment votes, suspicious reports). <br>Default: `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Pool](coin_gecko/models/pool.py)</code> -- Trending pools on a network

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def trending_search(*, request_options: RequestOptionsOrDict | None = None) -> TrendingSearch</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

To query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.trending_search()
    # TODO: Handle 'response' of type TrendingSearch
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.trending_search()
    # TODO: Handle 'response' of type TrendingSearch
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](coin_gecko/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TrendingSearch](coin_gecko/models/trending_search.py)</code> -- Trending search coins, NFTs and categories

**OnError**: <code>[ApiError](coin_gecko/core/exceptions.py)&#91;[RawError](coin_gecko/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

