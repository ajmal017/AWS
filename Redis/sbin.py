import redis
import pandas as pd 

r4 = redis.StrictRedis(host="localhost", port=6379, charset="utf-8", decode_responses=True,db=4)

data = r4.lrange("11709442",0,-1)

i=0;k=0
my_dict={}
cols=["instrument_token","date","ltp","volume"]
while i < r4.llen("11709442"):
    tick = data[i].split(";")
    d=dict(zip(cols,tick ))
    my_dict[k]=d
    k+=1; i+=1   
    
df=pd.DataFrame.from_dict(my_dict,'index')    
print(df)
    
