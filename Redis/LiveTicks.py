import selenium3 as s
import logging
from kiteconnect import KiteTicker
from kiteconnect import KiteConnect
import pandas as pd
import redis
from datetime import datetime
from dateutil import tz
import kiteconnect.exceptions as ex
from selenium import webdriver

r = redis.Redis(host='127.0.0.1',port=6379,db=1)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

## Get the Insrument Tokens
df = pd.read_pickle("E:/Trading Programs/00 Main Programs/pkl/NSE_FUT.pkl")
df1 = pd.read_pickle("E:/Trading Programs/00 Main Programs/pkl/NSE_BANKNIFTY_OPT.pkl")
Bank_Nifty_Tokens= df1.instrument_token.tolist()
Fut_Tokens= df.instrument_token.tolist()
tokens = Bank_Nifty_Tokens + Fut_Tokens


## Login to Kite
try:
    df = pd.read_pickle('access_token_and_date.pkl')    
    kite = KiteConnect(api_key=df[0].api_key)
    kite.set_access_token(df[0].access_token)
    access_token = df[0].access_token
    apikey = df[0].api_key
    kite.holdings()    
except ex.TokenException as token_error:
    print(token_error, "Retrying")
    try:
        chrome_path = r"H:\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(chrome_path)
        driver.get(
            "https://kite.trade/connect/login?v=3&api_key=" + df[0].api_key)
        Request_token = input('Enter the Request Token: ')
        data = kite.generate_session(
            Request_token, api_secret=df[0].secret_key)
        kite.set_access_token(data["access_token"])
        d1 = {'access_token': data["access_token"],
              'api_key': df[0].api_key, 'secret_key': df[0].secret_key}
        df = pd.DataFrame.from_dict(d1, "index")
        df.to_pickle('access_token_and_date.pkl')
        kite = KiteConnect(api_key=df[0].api_key)
        kite.set_access_token(data["access_token"])        
        access_token = data["access_token"]
    except Exception as e:
        raise e

except Exception as e:
    print("Authentication failed", str(e))

    
    
# Initialise.
kws = KiteTicker(apikey, access_token, debug=False)

def on_ticks(ws, ticks):
    r.lpush("Ticks-Full",ticks)
    #print(ticks)
    
def on_connect(ws, response):
    logging.debug("on connect: {}".format(response))
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL, tokens)


def on_close(ws, code, reason):
    logging.error("closed connection on close: {} {}".format(code, reason))
    #ws.stop()


def on_error(ws, code, reason):
    logging.error("closed connection on error: {} {}".format(code, reason))


def on_noreconnect(ws):
    logging.error("Reconnecting the websocket failed")


def on_reconnect(ws, attempt_count):
    logging.debug("Reconnecting the websocket: {}".format(attempt_count))


def on_order_update(ws, data):
    print("order update: ", data)

print("Starting Live Ticker")
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
kws.on_error = on_error
kws.on_noreconnect = on_noreconnect
kws.on_reconnect = on_reconnect
kws.on_order_update = on_order_update


kws.connect(threaded=True)

import datetime
r4 = s.redis_conn(4)
r4.flushdb()
print("Starting Ticker Processor")
while True:
    data_str = r.lpop('Ticks-Full')
    if data_str != None:
        data_list = eval(data_str)
        for ticks in data_list:        
            r4.lpush(ticks.get('instrument_token'),str(ticks.get('instrument_token')) + str(';') + str(ticks.get('timestamp')) + str(';') + str(ticks.get('last_price')) + str(';') + str(ticks.get('volume')))            