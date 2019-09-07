import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

pd.set_option('display.max_columns', 51)

def lower_upper(read):
    df=[]
    df = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df.columns = \
        df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    #    df = df[df['remarks'] != 'Average']
    df['total_premium'] = df['call_price'] + df['put_price']
    df['cumm_premium'] = df.groupby(['script'])['total_premium'].transform(lambda x: x.expanding().sum())
    df['amt'] = df.total_premium * df.qty
    df['kount'] = df.groupby(['script', 'call_put']).cumcount() + 1
    df['sum_amt'] = df.groupby(['script', 'call_put'])['amt'].transform(lambda x: x.expanding().sum())
    df['sum_qty'] = df.groupby(['script', 'call_put'])['qty'].transform(lambda x: x.expanding().sum())
    df['qty_strike'] = df['base_strike'] * df['qty']
    df['cum_qty_strike'] = df.groupby(['script', 'call_put'])['qty_strike'].transform(lambda x: x.expanding().sum())
    df['arrived_strike'] = df['cum_qty_strike'] / df['sum_qty']
    df['call_kount']=\
     df.loc[df["total_premium"]> 0].groupby(["script"])['call_put'].apply(lambda x: np.cumsum(x == 'CALL')).replace(0,1)
    df['put_kount']=\
     df.loc[df["total_premium"] > 0].groupby(["script"])['call_put'].apply(lambda x: np.cumsum(x == 'PUT')).replace(0,1)

    df['lower_band'] = df.arrived_strike - (df.cumm_premium / df.put_kount)
    df['upper_band'] = df.arrived_strike + (df.cumm_premium / df.call_kount)

    df['lower_band'] = df['lower_band'].replace(to_replace=0, method='ffill')
    df['upper_band'] = df['upper_band'].replace(to_replace=0, method='ffill')
    df.loc[df['total_premium'] == 0, ['lower_band', 'upper_band']] = 'NA'
    df.drop(['call_kount', 'put_kount'], axis=1, inplace=True)
    df.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)
