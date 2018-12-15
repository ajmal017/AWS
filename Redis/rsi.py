
[https://stockcharts.com](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:relative_strength_index_rsi)


import numpy as np
import helperpgm as h
import pandas as pd 
m = h.helperclass()
#pd.set_option('max_rows', 7)
#pd.set_eng_float_format(accuracy=2, use_eng_prefix=True)
pd.set_option('precision', 2)
pd.set_option('display.max_rows',1000)
pd.set_option('display.column_space',12)

df = m.Get_Historical_data(779521,"2018-12-12","2018-12-13","minute")

#df = pd.read_excel("C:/Users/Administrator/Downloads/cs-rsi.xls")
#df.reset_index(inplace=True,drop=True)
df = df[['Date','Close']]
df['Change'] = df.Close.values - df.Close.shift(1).values
df['Gain'] = np.where(df.Change >=0, df.Change,0)
df['Loss'] = np.where(df.Change <0, df.Change,0)
df['Avg-Gain'] = df.Gain.rolling(window=n, min_periods=n).mean()
df['Avg-Loss'] = abs(df.Loss.rolling(window=n, min_periods=n).mean())
df.at[n,'RS'] = df.at[n,'Avg-Gain'] / df.at[n,'Avg-Loss']
df.at[n,'RSI'] = 100-(100/(1+(df.at[n,'Avg-Gain'] / df.at[n,'Avg-Loss'])))
dff = df[:n]
df = df[n:]
df.reset_index(inplace=True,drop=True)
flag=False
for i,j in df.iterrows():
    if flag == False:
        flag =True
        continue
    df.at[i,'Avg-Gain'] = ((df.at[(i-1),'Avg-Gain']*(n-1)) + df.at[i,'Gain'])/n
    df.at[i,'Avg-Loss'] = ((df.at[(i-1),'Avg-Loss']*(n-1)) + abs(df.at[i,'Loss']))/n
    df.at[i,'RS'] = (((df.at[(i-1),'Avg-Gain']*(n-1)) + df.at[i,'Gain'])/n)/(((df.at[(i-1),'Avg-Loss']*(n-1)) + abs(df.at[i,'Loss']))/n)
    df.at[i,'RSI'] = 100-(100/(1+((((df.at[(i-1),'Avg-Gain']*(n-1)) + df.at[i,'Gain'])/n)/(((df.at[(i-1),'Avg-Loss']*(n-1)) + abs(df.at[i,'Loss']))/n))))
dff = dff.append(df,ignore_index=True)
