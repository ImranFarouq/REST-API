import datetime as dt

from typing import Optional, List
# from pydantic import BaseModel, Field

from fastapi import FastAPI,HTTPException
from schemas import Trade
import uuid

app = FastAPI()

# Dummy data 

trades_db = [
    {
        "tradeId": 1,
        "assetClass": "FX",
        "counterparty": "Wells Fargo,",
        "instrumentId": "EUR/USD",
        "instrumentName": "Euro/US Dollar",
        "tradeDateTime": "2023-06-04 11:00:00",
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 5.20,
            "quantity": 50
        },
        "trader": "Praveen"
    },
    {
        "tradeId": 2,
        "assetClass": "Bond",
        "counterparty": "Deutsche Bank",
        "instrumentId": "NFLX",
        "instrumentName": "Netflix  Inc.",
        "tradeDateTime": "2023-01-14 13:00:00",
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 2000.0,
            "quantity": 100
        },
        "trader": "Vicky"
    },
     {
        "tradeId": 3,
        "assetClass": "Equity",
        "counterparty": "JP Morgan",
        "instrumentId": "AAPL",
        "instrumentName": "Apple Inc.",
        "tradeDateTime": "2023-06-01 09:30:00",
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 150.0,
            "quantity": 200
        },
        "trader": "Yuvraj"
    }
]



# Endpoint to fetch a list of trades

@app.get("/trades", response_model=List[Trade])

async def list_trades(
    search: Optional[str] = None,   # default values are set to None for all Query Parameters
    assetClass: Optional[str] = None,
    start: Optional[dt.datetime] = None,
    end: Optional[dt.datetime] = None,
    minPrice: Optional[float] = None,
    maxPrice: Optional[float] = None,
    tradeType: Optional[str] = None
) -> List[Trade]:
    """Get all trades or Search a particular trade."""  
    trades = trades_db
    
    # Searching/Retreiving trades by the provided search term
    if search:
        trades = [trade for trade in trades if search.lower() in str(trade).lower()]
    
    # Filtering the trades by provided parameters
    if assetClass:
        trades = [trade for trade in trades if str(trade["assetClass"]).lower() == str(assetClass).lower()]

    if start:
        trades = [trade for trade in trades if dt.datetime.fromisoformat(trade["tradeDateTime"]) >= start]
   
    if end:
        trades = [trade for trade in trades if dt.datetime.fromisoformat(trade["tradeDateTime"]) <= end]

    if minPrice:  # minprice inclusive
        trades = [trade for trade in trades if trade["tradeDetails"]["price"] >= minPrice]
   
    if maxPrice: # maxprice inclusive
        trades = [trade for trade in trades if trade["tradeDetails"]["price"] <= maxPrice]
   
    if tradeType:
        trades = [trade for trade in trades if str(trade["tradeDetails"]["buySellIndicator"]).lower() == str(tradeType).lower()]

    # if no such trade exists will retun 404
    if not trades:
        raise HTTPException(status_code=404, detail="Trade not found")  

    return trades



# Endpoint to create a Trade 
@app.post("/trades", response_model=Trade)
async def create_trade( trade: Trade ) -> Trade:                             
    """Create a new trade."""
    trades_db.append(trade)
    return trade


# Endpoint to fetch a Trade by its tradeId
# we are using here Path Parameter
@app.get("/trades/{tradeId}", response_model=Trade)
async def get_trade_by_id(tradeId: str) -> Trade:
    """Get a trade by its tradeId."""
    for trade in trades_db:
        if trade["tradeId"] == int(tradeId):   
            return trade      
    raise HTTPException(status_code=404, detail="Trade not found")  


@app.put("/trades/{trade_id}", response_model=Trade)
async def update_trade(trade_id: str, trade: Trade) -> Trade:
    """Updating a existing trade."""
    for t in trades_db:
        if t["tradeId"] == int(trade_id):
            trades_db.remove(t)
            trades_db.append(trade)
            return trade
    raise HTTPException(status_code=404, detail="Trade not found")

# Endpoint to delete a Trade by its tradeId
# we are using here Path Parameter
@app.delete("/trades/{tradeId}")
async def delete_trade(tradeId: str):
    """Deleting a trade."""
    for trade in trades_db:
        if trade["tradeId"] == int(tradeId):
            trades_db.remove(trade)    
            return {"message": "Trade deleted successfully"}
    raise HTTPException(status_code=404, detail="Trade not found")

