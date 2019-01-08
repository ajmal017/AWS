import redis
import pandas as pd
import json
r = redis.Redis(host="localhost", port=6379, charset="utf-8", decode_responses=True,db=1)

data = r.lrange('Ticks-LTP',0,-1)
l=[]
for i in data:
    l.append(json.loads(i))
df = pd.DataFrame(l)
df.to_pickle('raw-54290183.pkl')
df['timestamp']= pd.to_datetime(df['timestamp'],infer_datetime_format=False)
df.set_index(df['timestamp'],inplace=True,drop=True)
data = df['2019-01-08 09:15:00':'2019-01-08 15:30:00']
data = data[['average_price', 'buy_quantity', 'change',
       'last_price', 'last_quantity', 'oi',
       'oi_day_high', 'oi_day_low', 'sell_quantity', 'volume']]
data.drop_duplicates(['last_price','volume'],keep= 'last').iloc[::-1]
data.to_pickle('54290183.pkl')
