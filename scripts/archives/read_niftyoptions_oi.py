import pandas as pd

pd.set_option('display.max_columns', 21)

def read_niftyoptionsoi():
    df1 = pd.read_excel('C:\\NSE\\inputs\\NIFTYOptions.xlsm', sheet_name='OC')
    df2.columns = df2.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df3 = df1[['calls_oi']]