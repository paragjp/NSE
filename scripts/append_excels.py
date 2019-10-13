import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

pd.set_option('display.max_columns', 51)
def append_excels(script,dt2,time1,totalcost,celtp,peltp):

    df1 = pd.read_excel('C:\\NSE\\inputs\\cepebasefile.xlsx', index_col=None)
    df1.columns = \
        df1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    df2 = pd.read_excel('C:\\NSE\\outputs\\CEPElog.xlsx', index_col=None)
    df2.columns = \
        df2.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df2 = df2.round(
        {"call": 2, "put": 2, "total": 2, "celtp": 2, "lastce": 2, "lastpe": 2, "last_total": 2, "loss_profit": 2,
         "percentage": 2})

    df3 = df2.append(df1, ignore_index=True)


    df3 = pd.DataFrame(df3, columns=['date', 'script', 'expiry_date', 'cestrike', 'call', 'pestrike', 'put', 'total',
                                     'loss', 'profit', 'upddt', 'updtime', 'lastce', 'lastpe', 'last_total',
                                     'loss_profit', 'percentage','remarks'])
    df3.sort_values(by=['script', 'upddt', 'updtime'], ascending=[True, False, False], inplace=True)
    df3 = df3.reset_index(drop=True)
    df3.to_excel('C:\\NSE\\outputs\\CEPElog.xlsx', index=False)


