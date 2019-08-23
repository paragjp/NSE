import datetime as dt
import pandas as pd
from refresh_oi import refresh_oi
from format_oi import format_oi

df1=pd.read_excel('C:\\NSE\\OUTPUTS\\OILog.xlsx', index_col=None)
df1.columns = df1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df4="Hello"

refresh_oi()

df2 = pd.read_excel('C:\\NSE\\inputs\\NIFTYOptions.xlsm', index_col=None)
df2.columns=df2.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

df3=df2[['strike_price','calls_oi','puts_oi']]
df3.head()

df4=pd.merge(df1, df3, on='strike_price')
# Finding out the difference
l=len(df4.columns)


time1=dt.datetime.now().strftime("%H:%M:%S")
if l == 5 :
    header1="CALL"+time1
    df4[header1]=df4.iloc[:-1,-2] - df4.iloc[:-1,-4]
    header1="PUT"+time1
    df4[header1]=df4.iloc[:-1,-2] - df4.iloc[:-1,-4]
else:
    header1="CALL"+time1
    df4[header1]=df4.iloc[:-1,-2] - df4.iloc[:-1,-6]
    header1="PUT"+time1
    df4[header1]=df4.iloc[:-1,-2] - df4.iloc[:-1,-6]

df4.to_excel("C:\\NSE\\OUTPUTS\\OILog.xlsx", index=False)
format_oi()