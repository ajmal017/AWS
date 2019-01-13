import  helperpgm as m
import pandas as pd
import numpy as np
import requests
h = m.helperclass()

## Get Nifty 500
nifty500 = h.Get_Nifty_500()
nifty500 = nifty500.astype(dtype={"Kite_Token": "int"})
nifty500.set_index('Kite_Token',inplace=True,drop=True)
#nifty500.groupby('Industry').count()['Company Name']
l = list(nifty500['Symbol'].values)
l = np.array_split(l,3)

## Get The String
s1=[]
for i in l:   
    s = "https://api.kite.trade/quote/ohlc?api_key={}&access_token={}".format(h.kite.api_key, h.kite.access_token)
    for j in i:
        s = s + "&i=NSE:{}".format(j)        
    s1.append(s)

df1= pd.DataFrame()
for i in s1:    
    data = requests.get(i)
    df = pd.DataFrame(
        list(json.loads(data.content.decode('utf-8'))['data'].values()))
    df = df.merge(pd.DataFrame(list(df['ohlc'])), left_index=True, right_index=True)[
        ['instrument_token', 'last_price', 'close', 'high', 'low', 'open']]
    #df.columns = [['Kite_Token', 'last_price', 'close', 'high', 'low', 'open']]
    df.set_index('instrument_token',inplace=True,drop=True)
    df = df.merge(nifty500,how='inner',left_index=True, right_index=True)
    df1 = df1.append(df,ignore_index=True)


df1[["last_price","close"]]

df1['posneg'] = df1["last_price"] - df1["close"]
#print("Percentage Positive:",sum(n > 0 for n in df1.pos_neg.values)/df1.pos_neg.count()*100)
df1.head()

df1.columns

df1['Up_Down'] = np.where(df1.pos_neg > 0, "Up","Down")
df1[['last_price', 'close', 'high', 'low', 'open', 'Company Name',
       'Industry', 'Symbol', 'Series', 'pos_neg']]

tdf = df1.groupby(['Industry','Up_Down']).size().unstack()
tdf['sum1'] = tdf['Up'] + tdf['Down']
tdf['up_percentage']  = tdf['Up']*100 / tdf['sum1']
tdf['down_percentage']  = tdf['Down']*100 / tdf['sum1']
