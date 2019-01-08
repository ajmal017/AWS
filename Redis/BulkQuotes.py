import  helperpgm as m
import pandas as pd
import json
import requests
h = m.helperclass()

## LTP
df = pd.DataFrame()
data = requests.get("https://api.kite.trade/quote/ltp?api_key={}&access_token={}&i=NSE:WIPRO&i=NSE:INFY&i=BSE:SENSEX&i=NSE:NIFTY+50".format(h.kite.api_key,h.kite.access_token)) 
if data.status_code == 200:    
    df = pd.DataFrame(list(json.loads(data.content.decode('utf-8'))['data'].values()))
elif data.status_code == 403:
    print("403 Error")
else:
    print("Error Getting Quote")
if not df.empty:
    print(df)

## OHLC

df = pd.DataFrame()
data = requests.get("https://api.kite.trade/quote/ohlc?api_key={}&access_token={}&i=NSE:WIPRO&i=NSE:INFY&i=BSE:SENSEX&i=NSE:NIFTY+50".format(h.kite.api_key,h.kite.access_token)) 
if data.status_code == 200:
    df = pd.DataFrame(list(json.loads(data.content.decode('utf-8'))['data'].values()))
    df= df.merge(pd.DataFrame(list(df['ohlc'])),left_index=True,right_index=True)[['instrument_token', 'last_price','close', 'high', 'low','open']]
elif data.status_code == 403:
    print("403 Error")
else:
    print("Error Getting Quote")
if not df.empty:
    print(df)
