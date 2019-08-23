import pandas as pd

pd.set_option('display.max_columns', 21)

def read_niftyoptions(basestrike):
    df1 = pd.read_excel('C:\\NSE\\inputs\\NIFTYOptions.xlsm', sheet_name='OC')
    df2 = (df1.loc[df1['Strike Price'] == basestrike])
    df2.columns = df2.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    f_c1 = round(float(df2['calls_ltp'].values),2)
    f_p1 = round(float(df2['puts_ltp'].values),2)
    f_calls_bid_price = round(float(df2['calls_bid_price'].values),2)
    f_puts_bid_price = round(float(df2['puts_bid_price'].values),2)
    return(f_c1,f_p1, f_calls_bid_price, f_puts_bid_price)

