import yfinance as yf
import json
import pandas as pd


tick = "TCS.NS"

pb = 1.0

ticker = yf.Ticker(tick)
print(ticker)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""


# get stock info print(ticker.info)
if  ticker.info['priceToBook'] >= pb :
    data = {'tick':[tick],
         'fiftyTwoWeekLow':ticker.info['fiftyTwoWeekLow'],
         'regularMarketOpen': ticker.info['regularMarketOpen'],
         'bookValue': ticker.info['bookValue'],
         'priceToBook': ticker.info['priceToBook'],
         'dividendRate':ticker.info['dividendRate']}
    print(data)
    df = pd.DataFrame(data)
    print(df)