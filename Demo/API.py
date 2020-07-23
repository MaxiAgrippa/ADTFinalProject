# yfinance Demo:

from pprint import pprint
# import yfinance as yf
# data = yf.download("SPY AAPL", start="2019-04-01", end="2019-04-30")
# print(data)

# Yahoo Financial Demo:
import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"

querystring = {"frequency": "1d", "filter": "history", "period1": "1546448400", "period2": "1562086800", "symbol": "AMRN"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "c2829536e9msh4b1be8fae335bf0p141362jsnc364d462c0ad"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
