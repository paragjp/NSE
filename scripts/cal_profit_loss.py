import os
import sys
import pandas as pd
import datetime as dt
import numpy as np
pd.set_option('display.max_columns', 51)

def cal_profit_loss(result, type1):
    result1=result
    df = []
    df = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df.columns = \
        df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    print("Calculating Profit ...")
    df['profit'] = np.select(
        [
            (df['type1'] == "O") & (df['call_put'] == "CALL") & (df['buy_sell'] == "SELL"),
            (df['type1'] == "O") & (df['call_put'] == "CALL") & (df['buy_sell'] == "BUY"),
            (df['type1'] == "O") & (df['call_put'] == "PUT") & (df['buy_sell'] == "SELL"),
            (df['type1'] == "O") & (df['call_put'] == "PUT") & (df['buy_sell'] == "BUY")

        ],
        [
            df['qty'].mul(df['call_price']),
            df['ltp'].sub(df['base_strike']).mul(df['qty']).clip(lower=0),
            df['qty'].mul(df['put_price']),
            0
        ],
        default=df['profit']

    )
    print("Calculating Loss ...")
    df['loss'] = np.select(
        [
            (df['type1'] == "O") & (df['call_put'] == "CALL") & (df['buy_sell'] == "SELL"),
            (df['type1'] == "O") & (df['call_put'] == "CALL") & (df['buy_sell'] == "BUY"),
            (df['type1'] == "O") & (df['call_put'] == "PUT") & (df['buy_sell'] == "SELL"),
            (df['type1'] == "O") & (df['call_put'] == "PUT") & (df['buy_sell'] == "BUY")

        ],
        [
            df['ltp'].sub(df['base_strike']).mul(df['qty']).clip(lower=0) * -1,
            df['qty'].mul(df['call_price']) * -1,
            df['base_strike'].sub(df['ltp']).mul(df['qty']).clip(lower=0) * -1,
            df['qty'].mul(df['put_price']) * -1,
        ],
        default=df['loss']

    )
    print("returning DF")
    return (df)
