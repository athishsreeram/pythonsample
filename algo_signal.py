import yfinance as yf
import json

ticker = yf.Ticker("TCS.NS")
print(ticker)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
print(ticker.info)

print(ticker.info['fiftyTwoWeekLow'])


parsed = json.loads(str(ticker.info))

print(json.dumps(parsed, indent=2, sort_keys=True))