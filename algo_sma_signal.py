import sys
import os

from pandas_datareader import data as pdr
import matplotlib.pyplot as pyplot
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

x = (sys.argv[1])

print("The script has the name %s" % x)

yf.pdr_override() # <== that's all it takes :-)

# download dataframe using pandas_datareader
data = pdr.get_data_yahoo(x, start="2019-06-01", end="2020-12-18")


df = pd.DataFrame(data)

df = df.reset_index()

print(df.columns)


#df.plot(kind='line',x='Date',y='Close',color='red')
#pyplot.show()

#for i in range(0,df.shape[0]-2):
#    df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)

# buy when 20 sma > 50 sma
# sell when 20 sma < 50 sma

df['pandas_SMA_20'] = df.iloc[:,4].rolling(window=20).mean()
df['pandas_SMA_50'] = df.iloc[:,4].rolling(window=50).mean()

df['Buy'] = df['pandas_SMA_20'] < df['pandas_SMA_50']
df['Trigger'] = df['pandas_SMA_20'] == df['pandas_SMA_50']

pyplot.figure(figsize=[15,10])
pyplot.title('SMA 20 VS 50 %s' %x)
pyplot.grid(True)
pyplot.plot(df['Close'],label='Price')
pyplot.plot(df['pandas_SMA_20'],label='SMA 20 DAYS')
pyplot.plot(df['pandas_SMA_50'],label='SMA 50 DAYS')
pyplot.legend(loc=2)
#pyplot.show()

try:
    # Create target Directory
    os.mkdir(today)
    print("Directory " , today ,  " Created ") 
except FileExistsError:
    print("Directory " , today ,  " already exists")

filename = x+'_20vs50_'+today+'.png' 

pyplot.savefig(os.path.join(today,filename))

#print(df.loc[df['Buy'] == True ])


print(df.tail(1))