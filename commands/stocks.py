import yfinance as yf
from bs4 import BeautifulSoup
from requests import get

def scrapeYahooStock(ticker):
#    stock = ticker.content.split(' ')[1]
    url = "https://finance.yahoo.com/quote/"
    full_url = url + ticker
    response = get(full_url).content
    soup = BeautifulSoup(response, 'html.parser')
    stock_price = soup.findAll(class_ = "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")[0].text
#    return stock, stock_price
    return stock_price
