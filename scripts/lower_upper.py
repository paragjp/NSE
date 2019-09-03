import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

pd.set_option('display.max_columns', 51)

def lower_upper():
    df=[]
    df = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df.columns = \
        df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    #    df = df[df['remarks'] != 'Average']
    df['total_premium'] = df['call_price'] + df['put_price']
    df['cumm_premium'] = df.groupby(['script'])['total_premium'].transform(lambda x: x.expanding().sum())
    #   total_premium = 0
    #   total_premium = df.total_premium.iat[-1]

    #    if total_premium > 0:
    df['amt'] = df.total_premium * df.qty
    df['kount'] = df.groupby(['script', 'call_put']).cumcount() + 1

    # df['mean_amt']=df.groupby(['script','call_put'])['amt'].transform(lambda x: x.expanding().mean())

    df['sum_amt'] = df.groupby(['script', 'call_put'])['amt'].transform(lambda x: x.expanding().sum())
    df['sum_qty'] = df.groupby(['script', 'call_put'])['qty'].transform(lambda x: x.expanding().sum())
    df['qty_strike'] = df['base_strike'] * df['qty']

    # df['sum_strike']=df.groupby(['script','call_put'])['strike'].transform(lambda x: x.expanding().sum())
    # df['mean_strike']=df['qty_strike'] / df['sum_qty']

    df['cum_qty_strike'] = df.groupby(['script', 'call_put'])['qty_strike'].transform(lambda x: x.expanding().sum())
    df['arrived_strike'] = df['cum_qty_strike'] / df['sum_qty']
    df['lower_band'] = ((df.arrived_strike - (df.cumm_premium / df.kount)).where(df.call_put == 'PUT', 0))
    df['upper_band'] = ((df.arrived_strike + (df.cumm_premium / df.kount)).where(df.call_put == 'CALL', 0))
    df['lower_band'] = df['lower_band'].replace(to_replace=0, method='ffill')
    df['upper_band'] = df['upper_band'].replace(to_replace=0, method='ffill')
    df.loc[df['total_premium'] == 0, ['lower_band', 'upper_band']] = 'NA'
    df.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)
