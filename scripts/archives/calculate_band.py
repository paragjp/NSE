import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

def calculate_band():
    df = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df.columns = \
            df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df=df[df['remarks'] != 'Average']
    dfband=df[['call_price','put_price']].cumsum()
    dfband['total'] = dfband['call_price'] + dfband['put_price']
    df['lower_band']= df['order_strike'] - dfband['total']
    df['upper_band'] = df['order_strike'] + dfband['total']
    df.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)