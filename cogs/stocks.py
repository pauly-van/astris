import yfinance as yf

async def getStock(ticker):
    stock = yf.Ticker(ticker)
    return stock.info

