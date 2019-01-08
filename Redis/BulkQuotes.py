import  helperpgm as m
import pandas as pd
import json
import requests
h = m.helperclass()

data = requests.get("https://api.kite.trade/quote/ltp?api_key={}&access_token={}&i=NSE:WIPRO&i=NSE:INFY&i=BSE:SENSEX&i=NSE:NIFTY+50".format(h.kite.api_key,h.kite.access_token)) 
if data.status_code == 200:
    d = json.loads(data.content.decode('utf-8'))
    df = pd.DataFrame(list(d['data'].values()))
df
