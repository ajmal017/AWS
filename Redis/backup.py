while r4.llen(instrument_token):
    data = r4.lpop(instrument_token)
    r4.lpush("instrument_token1", data)
    r4.lpush("instrument_token2", data)
    

while r4.llen('instrument_token2'): 
    data = r4.lpop('instrument_token2')
    r4.lpush("10504450", data)
