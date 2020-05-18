import yfinance as yf

ticker = yf.Ticker("TCS.NS")
print(ticker)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
print(ticker.info)

print(ticker.info['fiftyTwoWeekLow'])


"""
returns:
{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'ticker'
}
"""

# get historical market data
print(ticker.history(period="max"))
"""
returns:
              Open    High    Low    Close      Volume  Dividends  Splits
Date
1986-03-13    0.06    0.07    0.06    0.07  1031788800        0.0     0.0
1986-03-14    0.07    0.07    0.07    0.07   308160000        0.0     0.0
...
2019-04-15  120.94  121.58  120.57  121.05    15792600        0.0     0.0
2019-04-16  121.64  121.65  120.10  120.77    14059700        0.0     0.0
"""

# show actions (dividends, splits)
print(ticker.actions)
"""
returns:
            Dividends  Splits
Date
1987-09-21       0.00     2.0
1990-04-16       0.00     2.0
...
2018-11-14       0.46     0.0
2019-02-20       0.46     0.0
"""

# show dividends
print(ticker.dividends)
"""
returns:
Date
2003-02-19    0.08
2003-10-15    0.16
...
2018-11-14    0.46
2019-02-20    0.46
"""

# show splits
print(ticker.splits)