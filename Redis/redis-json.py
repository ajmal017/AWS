import redis,datetime,json
r = redis.Redis(host="localhost", port=6379, charset="utf-8", decode_responses=True,db=2)
r.flushdb()

ticks = [{'tradable': True, 'mode': 'full', 'instrument_token': 779521, 'last_price': 296.3, 'last_quantity': 25, 'average_price': 298.25, 'volume': 14579399, 'buy_quantity': 0, 'sell_quantity': 25227, 'ohlc': {'open': 301.05, 'high': 301.5, 'low': 295.2, 'close': 297.65}, 'change': -0.453552830505616, 'last_trade_time': datetime.datetime(2019, 1, 7, 15, 58, 39), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 1, 7, 16, 19, 53), 'depth': {'buy': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 25227, 'price': 296.3, 'orders': 74}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}]

data = json.dumps(ticks[0], indent=4, sort_keys=True, default=str)

json.loads(data)
####################################################################################################################################################################################
import redis,json
import datetime
r = redis.Redis(host="localhost", port=6379, charset="utf-8", decode_responses=True,db=2)
r.flushdb()

ticks = [{'tradable': True, 'mode': 'full', 'instrument_token': 779521, 'last_price': 296.3, 'last_quantity': 25, 'average_price': 298.25, 'volume': 14579399, 'buy_quantity': 0, 'sell_quantity': 25227, 'ohlc': {'open': 301.05, 'high': 301.5, 'low': 295.2, 'close': 297.65}, 'change': -0.453552830505616, 'last_trade_time': datetime.datetime(2019, 1, 7, 15, 58, 39), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 1, 7, 16, 19, 53), 'depth': {'buy': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 25227, 'price': 296.3, 'orders': 74}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}]
ticks[0]['tradable'] = str(ticks[0]['tradable'])
ticks[0]['timestamp'] = str(ticks[0]['timestamp'])
ticks[0]['last_trade_time'] = str(ticks[0]['last_trade_time'])

r.lpush('ticks',str(ticks))

data = r.lrange('ticks',0,0)
data = data[0].strip('[]').replace("\'", "\"")
json.loads(data)

####################################################################################################################################################################################
import datetime
import redis,json
r = redis.Redis(host="localhost", port=6379, charset="utf-8", decode_responses=True,db=3)
ticks = [{'tradable': True, 'mode': 'full', 'instrument_token': 779521, 'last_price': 296.3, 'last_quantity': 25, 'average_price': 298.25, 'volume': 14579399, 'buy_quantity': 0, 'sell_quantity': 25227, 'ohlc': {'open': 301.05, 'high': 301.5, 'low': 295.2, 'close': 297.65}, 'change': -0.453552830505616, 'last_trade_time': datetime.datetime(2019, 1, 7, 15, 58, 39), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 1, 7, 16, 19, 53), 'depth': {'buy': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 25227, 'price': 296.3, 'orders': 74}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}]

#json.loads(json.dumps(ticks[0], indent=4, sort_keys=True, default=str))


r.lpush("Ticks-JSON",json.dumps(ticks[0],default=str))

json.loads(r.lrange("Ticks-JSON",0,0)[0])

####################################################################################################################################################################################
