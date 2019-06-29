
#s = requests.get("https://api.kite.trade/instruments").content
#df = pd.read_csv(io.StringIO(s.decode('utf-8')))
#df = df.loc[(df['instrument_type'] == "EQ") & (df['segment'] == "BSE") & (df['exchange'] == "BSE") & (df['tick_size'] == 0.05) & (df['lot_size'] == 1)].reset_index(drop=True)

## BSE Stocks
BSE_Stocks = df.loc[(df['instrument_type'] == "EQ") & (df['segment'] == "BSE") & (df['exchange'] == "BSE") & (df['tick_size'] == 0.05) & (df['lot_size'] == 1)]

## NSE Futures 
df['expiry'] = pd.to_datetime(df['expiry'])
NSE_FUT = df.loc[((df.expiry.dt.month == pd.datetime.now().month)|(df.expiry.dt.month == pd.datetime.now().month+1)) & (df.expiry.dt.year == pd.datetime.now().year) & (df.segment == 'NFO-FUT')]
NSE_FUT.loc[NSE_FUT.exchange=="NFO"][['tradingsymbol','expiry','lot_size','exchange']].reset_index(drop=True)

## MCX tokens in List
MCX = df.loc[df['exchange'] == "MCX"].reset_index(drop=True)
MCX[["instrument_token","tradingsymbol"]].values.tolist()

NSE_OPT = df.loc[(df.expiry.dt.month == pd.datetime.now().month) &(df.expiry.dt.year == pd.datetime.now().year) & (df.segment == 'NFO-OPT') & (df.exchange =='NFO') &  (df.tradingsymbol.str.contains('NIFTY')) & (~df.tradingsymbol.str.contains('BANK'))].reset_index(drop=True)
if NSE_OPT.empty:
    NSE_OPT = df.loc[(df.expiry.dt.month == pd.datetime.now().month+1) &(df.expiry.dt.year == pd.datetime.now().year) & (df.segment == 'NFO-OPT') & (df.exchange =='NFO') &  (df.tradingsymbol.str.contains('NIFTY')) & (~df.tradingsymbol.str.contains('BANK'))].reset_index(drop=True)
NSE_OPT    

BANK_NIFTY_OPT = df.loc[((df.expiry.dt.month == pd.datetime.now().month)|(df.expiry.dt.month == pd.datetime.now().month+1)) & (df.segment == 'NFO-OPT') & (df.exchange =='NFO') &  (df.tradingsymbol.str.contains('BANKNIFTY'))].reset_index(drop=True)
BANK_NIFTY_OPT

## ITM ATM OTM
price = 10806.5
fprice = int(math.floor(price / 100.0)) * 100
if (price - fprice) >= 50:
    fprice += 50

ATM = [fprice]
x= fprice

ITM =[]
for i in range(20):
    x = x -50
    ITM.append(x)

    x= fprice
OTM =[]
for i in range(20):
    x = x + 50
    OTM.append(x)

########    
    
def Nifty_Options():
    NSE_OPT = df.loc[(df.expiry.dt.month == pd.datetime.now().month) &(df.expiry.dt.year == pd.datetime.now().year) & (df.segment == 'NFO-OPT') & (df.exchange =='NFO') &  (df.tradingsymbol.str.contains('NIFTY')) & (~df.tradingsymbol.str.contains('BANK'))].reset_index(drop=True)
    month_abbr = calendar.month_abbr[pd.datetime.now().month].upper()
    if NSE_OPT.empty:
        NSE_OPT = df.loc[(df.expiry.dt.month == pd.datetime.now().month+1) &(df.expiry.dt.year == pd.datetime.now().year) & (df.segment == 'NFO-OPT') & (df.exchange =='NFO') &  (df.tradingsymbol.str.contains('NIFTY')) & (~df.tradingsymbol.str.contains('BANK'))].reset_index(drop=True)
        month_abbr = calendar.month_abbr[pd.datetime.now().month + 1].upper()
    return [NSE_OPT ,month_abbr]
df = Nifty_Options()
month_abbr = df[1]
df = df[0]

########    

def Options(price=11788.85):
    ## ITM ATM OTM
        
    fprice = int(math.floor(price / 100.0)) * 100
    if (price - fprice) >= 50:
        fprice = fprice + 50

    ## ATM
    ATM = [fprice]
    x= fprice

    ##ITM
    ITM =[]
    for i in range(20):
        x = x -50
        ITM.append(x)

    x= fprice

    ##OTM
    OTM =[]
    for i in range(20):
        x = x + 50
        OTM.append(x)
        
    return [ITM, ATM,OTM]

def print_Options():
    opt = Options()

    print("*** ITM **\n\n")
    for j in opt[0]:        
        print(df.loc[(df.strike == j) & (df.instrument_type == "CE")  & df.tradingsymbol.str.contains(month_abbr)])

    print("\n\n*** ATM **\n\n")
    for j in opt[1]:        
        print(df.loc[(df.strike == j) & (df.instrument_type == "CE")  & df.tradingsymbol.str.contains(month_abbr)])


    print("\n\n*** OTM **\n\n")
    for j in opt[2]:        
        print(df.loc[(df.strike == j) & (df.instrument_type == "CE")  & df.tradingsymbol.str.contains(month_abbr)])
print_Options()

########    

def Get_Nifty_500():
    s = requests.get("https://www.nseindia.com/content/indices/ind_nifty500list.csv").content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))

df= Get_Nifty_500()
print(df.Industry.unique().tolist())
l = []
for i in df.Industry.unique().tolist():
    l.append(df.loc[df.Industry == i].values)
print(l)    

########    

from nsepy import get_history
from datetime import date
data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
print(data)

########    

import pandas as pd
import requests
import io
from io import BytesIO
import time
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta
from zipfile import ZipFile
import smtplib


def Get_FnO():   
    s = requests.get("https://www.nseindia.com/content/fo/fo_mktlots.csv").content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))


def Get_Nifty_500():
    s = requests.get("https://www.nseindia.com/content/indices/ind_nifty500list.csv").content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))


def NSE_ban_securities():
    download_date = datetime.now()
    try:
        url = "https://www.nseindia.com/archives/fo/sec_ban/fo_secban_" + \
            download_date.strftime('%d%m%Y') + ".csv"        
        s = requests.get(url).content
        df = pd.read_csv(io.StringIO(s.decode('utf-8')))
        if not df.empty:
            return [j for i in df.values.tolist() for j in i]
        else:
            return "No Securities in Ban Period for {}".format(download_date.strftime('%d-%m-%Y'))
    except:
        print("404 - Page not Found")


def Get_BSE_Bhav_copy():
    download_date = datetime.now()# - timedelta(days=1)
    bse_url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ' + \
        download_date.strftime("%d%m%y") + '_CSV.ZIP'
    content = requests.get(bse_url)
    zf = ZipFile(BytesIO(content.content))    
    match = [s for s in zf.namelist() if ".CSV" in s][0]    
    return pd.read_csv(zf.open(match), low_memory=False, skiprows=[0])


def Get_NSE_Bhav_copy():
    download_date = datetime.now() # - timedelta(days=1)
    var1 = "fo" + download_date.strftime("%d") + download_date.strftime("%b").upper() + \
        download_date.strftime("%Y") + "bhav.csv.zip"
    NSE_url = "https://www.nseindia.com/content/historical/DERIVATIVES/" + \
        download_date.strftime("%Y") + "/" + download_date.strftime("%b").upper() + "/" + var1
    print("Link - \t", NSE_url)    
    content = requests.get(NSE_url)
    zf = ZipFile(BytesIO(content.content))    
    match = [s for s in zf.namelist() if ".csv" in s][0]    
    return pd.read_csv(zf.open(match), low_memory=False, skiprows=[0])


def Get_Stock_List_from_Nifty():
    url = "https://www.nseindia.com/content/equities/EQUITY_L.csv"
    s = pd.read_csv(io.BytesIO(requests.get(url).content),
                    encoding="ISO-8859-1", engine='python')
    stocklist = s.SYMBOL.tolist()
    return stocklist


def Get_Indian_Time():
    #d1 = datetime.now() - timedelta(hours=5, minutes=30)
    #d1.strftime("%Y-%m-%d  %I:%M:%S.%f")
    return pd.to_datetime((datetime.utcnow() - timedelta(hours=-5, minutes=-30)).strftime("%Y-%m-%d  %I:%M:%S.%f")) 


def Send_Email(subject, body):
    gmail_user = 'girishsanchetix@gmail.com'
    gmail_pwd = ''
    recipient = 'girish400@gmail.com'
    FROM = gmail_user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()
        server_ssl.login(gmail_user, gmail_pwd)
        server_ssl.sendmail(FROM, TO, message)
        server_ssl.close()
    except smtplib.SMTPException as email_error:
        print(email_error)


def NSE_Open_Interest():
    download_date = datetime.now()# - timedelta(days=1)
    bse_url = "https://nseindia.com/archives/nsccl/mwpl/nseoi_" + download_date.strftime('%d%m%Y') + ".zip"
    content = requests.get(bse_url)
    zf = ZipFile(BytesIO(content.content))    
    match = [s for s in zf.namelist() if ".csv" in s][0]    
    return pd.read_csv(zf.open(match), header=None, low_memory=False, skiprows=[0])


def NSE_Daily_Volatility():
    download_date = datetime.now()# - timedelta(days=1)
    s = requests.get("https://nseindia.com/archives/nsccl/volt/FOVOLT_" + download_date.strftime('%d%m%Y') + ".csv").content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))


def NSE_Exposure_Limit():
    download_date = datetime.now()# - timedelta(days=1)
    s = requests.get("https://nseindia.com/archives/exp_lim/ael_" + download_date.strftime('%d%m%Y') + ".csv").content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))


def fao_participant_vol():
    download_date = datetime.now()# - timedelta(days=1)
    s = requests.get("https://nseindia.com/content/nsccl/fao_participant_vol_" + download_date.strftime('%d%m%Y') + ".csv").content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))    
