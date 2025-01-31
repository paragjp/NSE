import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

pd.set_option('display.max_columns', 51)
def update_excels(script,dt2,time1,totalcost,celtp,peltp,msg3):
    df = pd.read_excel('C:\\NSE\\inputs\\cepebasefile.xlsx', index_col=None)
    df.columns = \
        df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    #df['date'] = df['date'].dt.strftime('%d-%b-%y')
    #df['date']
    #df['expiry_date']
    #  df['expiry_date'] = df['expiry_date'].dt.strftime('%d-%b-%y')
    print(script)

    df['total'] = np.select(
                           [df['script'] == script],
                           [
                           totalcost
                           ],
                           default=df['total']
                           )


    df['upddt'] = np.select(
        [df['script'] == script],
        [
            dt2
        ],
        default=df['upddt']
    )

    df['updtime'] = np.select(
        [df['script'] == script],
        [
            time1
        ],
        default=df['updtime']
    )
    df['lastce'] = np.select(
        [df['script'] == script],
        [
            celtp
        ],
        default=df['lastce']
    )
    df['lastpe'] = np.select(
        [df['script'] == script],
        [
            peltp
        ],
        default=df['lastpe']
    )
    df['last_total'] = np.select(
        [df['script'] == script],
        [
            celtp+peltp
        ],
        default=df['last_total']
    )
    df['loss_profit'] = np.select(
        [df['script'] == script],
        [
            df['total'] - df['lastce'] - df['lastpe']
        ],
        default=df['loss_profit']
    )
    df['percentage'] = np.select(
        [df['script'] == script],
        [
            df['loss_profit'] / df['total'] * 100
        ],
        default=df['percentage']
    )
    df['remarks'] = np.select(
        [df['script'] == script],
        [
            msg3
        ],
        default=df['remarks']
    )
    # df.style.format({'percentage': '{:,.2%}'.format})

    df2 = pd.read_excel('C:\\NSE\\inputs\\watchlist.xlsx', index_col=None)
    df2.columns = \
        df2.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df3 = pd.merge(df, df2[['column1.symbol', 'column1.ltp']], how='left', left_on=['script'],
                   right_on=['column1.symbol'])
    df3['ltp'] = df3['column1.ltp']
    df3.drop(['column1.symbol', 'column1.ltp'], inplace=True, axis=1)
    df = df3

    df=df.round({"spot":2, "call": 2, "put": 2, "total": 2, "ltp":2, "celtp": 2, "lastce":2, "lastpe":2, "last_total":2,"loss_profit":2, "percentage":2})

    df1= pd.DataFrame(df, columns=['date','script','expiry_date','spot','cestrike','call','pestrike','put','total',
                                  'loss','profit','upddt','updtime', 'ltp','lastce','lastpe','last_total','loss_profit','percentage','remarks'])
    df1.sort_values(by=['script'], ascending=[True], inplace=True)
    df1.to_excel('C:\\NSE\\inputs\\cepebasefile.xlsx', index=False)


