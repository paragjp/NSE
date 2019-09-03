import pandas as pd

pd.set_option('display.max_columns', 21)

#reading NIFTY50 file for reading current NIFTY level
def read_nifty50() :

    nifty1 = pd.read_excel('C:\\NSE\\inputs\\NIFTY50.xlsm', sheet_name='Sheet2')
# removing column spaces special characters and converting into smaller case
    nifty1.columns = \
        nifty1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')','')
    f_current_nifty=nifty1.loc[4, 'value']
    if isinstance(f_current_nifty,str) == True:
        f_current_nifty = float(nifty1.loc[4, 'value'].replace(',', ''))
    else:
        f_current_nifty = float(f_current_nifty)

    f_current_change = float(nifty1.loc[6, 'value'])

    return(f_current_nifty,f_current_change)