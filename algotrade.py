import pandas as pd 
import pandas_datareader.data as pdr 
from datetime import datetime
import matplotlib.pyplot as pyplot

import json
import requests 

start = datetime(2010,10,1)
end = datetime(2020,4,30)

inflation = pdr.DataReader('T5YIE','fred',start,end)
inflation.plot(), pyplot.show();