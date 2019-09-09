import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

pd.set_option('display.max_columns', 51)

def lower_upper():
    df=[]
    df1=[]
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
    df['total_qty'] = df.groupby(['script'])['qty'].transform(lambda x: x.expanding().sum())
    df['qty_x_strike'] = df['base_strike'] * df['qty']
    df['cumm_qty_x_strike'] = df.groupby(['script', 'call_put'])['qty_x_strike'].transform(
        lambda x: x.expanding().sum())
    df['cumm_call_qty'] = df['qty'].mul(df['call_put'].eq('CALL')).groupby(df['script']).cumsum()
    df['cumm_put_qty'] = df['qty'].mul(df['call_put'].eq('PUT')).groupby(df['script']).cumsum()
    df['cumm_call_qty'] = df['cumm_call_qty'].replace(0, df['cumm_put_qty'])
    df['cumm_put_qty'] = df['cumm_put_qty'].replace(0, df['cumm_call_qty'])

    df['arrived_call_strike'] = df['cumm_qty_x_strike'] / df['cumm_call_qty'].where(df['call_put'] == "CALL")
    df['arrived_put_strike'] = df['cumm_qty_x_strike'] / df['cumm_put_qty'].where(df['call_put'] == "PUT")

    # df['arrived_put_strike'] = df['arrived_put_strike'].replace(0, df['arrived_call_strike'])
    # df['arrived_call_strike'] = df['arrived_call_strike'].replace(0, df['arrived_put_strike'])
    df['arrived_call_strike'] = df['arrived_call_strike'].fillna(method='ffill')
    df['arrived_put_strike'] = df['arrived_put_strike'].fillna(method='ffill')
    # df['arrived_call_strike'] = df['arrived_put_strike'].fillna(df['arrived_call_strike'])
    # df['arrived_put_strike'] = df['arrived_put_strike'].fillna(df['arrived_call_strike'])
    df['cumm_amt'] = df.groupby(['script'])['amt'].transform(lambda x: x.expanding().sum())
    df['upper_band'] = df['arrived_call_strike'] + (df['cumm_amt'] / df['cumm_call_qty'])
    df['lower_band'] = df['arrived_put_strike'] - (df['cumm_amt'] / df['cumm_put_qty'])
    df = df.fillna('NA')

    df.loc[df['total_premium'] == 0, ['cumm_premium', 'amt', 'arrived_call_strike', 'arrived_put_strike',
                                       'lower_band', 'upper_band']] = 'NA'
    df1 = df[['date', 'time', 'script', 'base_strike', 'ltp', 'base_change', 'current_change', 'qty',
               'call_put', 'buy_sell', 'call_price', 'put_price', 'total_premium', 'cumm_premium', 'amt',
               'executed', 'remarks', 'kount', 'arrived_call_strike', 'arrived_put_strike', 'upper_band',
               'lower_band']]
    #df1.loc[df['total_premium']==0,['cumm_premium','amt','arrived_call_strike','arrived_put_strike',
    #                              'lower_band', 'upper_band']] = 'NA'
    # df.drop(['call_kount','put_kount','ct','x','y','c1','p1'], axis=1, inplace=True)
    df1.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)
