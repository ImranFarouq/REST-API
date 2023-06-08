# SteelEye-API-Developer-Assignment

Built a REST API using FastAPI with endpoints serving CRUD functionallity for Trade data. 
Here I have used a dummy data list of dict containing trade details (as per provided schema). 

Pydantic: 
Data validation and settings management using Python type annotations.
pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.

This API uses a Pydantic lib to define the data model for Trade object( by inheriting the Base Model from Pydantic).

Uvicorn:

Uvicorn is an ASGI(Asynchronous Server Gateway Interface) web server implementation for Python.
The ASGI specification fills this gap, and it enables us to build a common set of tooling usable across all async frameworks.
Uvicorn currently supports HTTP/1.1 and WebSockets.

This API has 4 endpoints:

1. GET ('/trades'): Returns a list of all trades and it has advance filtering operations by search term, asset class, trade date range, price range(Max and Min both inclusive) and trade type .

2. GET ('/trades/{'tradeID'}): To get a Trade by its TradeID

3. POST ('/trades'): To Create a new trade.

4. PUT ('/trades/{'tradeID'}): To Update an existing trade by its TradeId.

5. DELETE ('/trades/{'tradeID'}): To Delete an existing trade by its TradeId.

## Advanced filtering
<p>The users would have the ability to filter trades. The endpoint fetching a list of trades will support filtering using the following optional query parameters:</p>

<table role="table">
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>assetClass</code></td>
<td>Asset class of the trade.</td>
</tr>
<tr>
<td><code>end</code></td>
<td>The maximum date for the <code>tradeDateTime</code> field.</td>
</tr>
<tr>
<td><code>maxPrice</code></td>
<td>The maximum value for the <code>tradeDetails.price</code> field.</td>
</tr>
<tr>
<td><code>minPrice</code></td>
<td>The minimum value for the <code>tradeDetails.price</code> field.</td>
</tr>
<tr>
<td><code>start</code></td>
<td>The minimum date for the <code>tradeDateTime</code> field.</td>
</tr>
<tr>
<td><code>tradeType</code></td>
<td>The <code>tradeDetails.buySellIndicator</code> is a <code>BUY</code> or <code>SELL</code>
</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
