import pandas as pd
import os

import pandas as pd

pd.set_option('display.max_columns', 50)

from get_datetime import get_datetime

filename = "C:\\NSE\\OUTPUTS\\OILog.xlsx"
if os.path.isfile(filename):
    os.remove(filename)

# creating base OI Log File
df1 = pd.read_excel('C:\\NSE\\inputs\\NIFTYOptions.xlsm', index_col=None)
df1.columns=df1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df1=df1[['strike_price','calls_oi']]
df1.to_excel("C:\\NSE\\OUTPUTS\\OILog.xlsx", index=False)