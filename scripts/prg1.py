import pandas as pd
import os

import pandas as pd

pd.set_option('display.max_columns', 21)

from read_baseline import read_baseline
from read_nifty50 import read_nifty50
from get_datetime import get_datetime
from first_order import first_order
from normal_orders import normal_orders
from refresh_excel import refresh_excel
from format_masters import format_masters

#reading baseline file for reading strike price and % of change
basestrike, basechange=read_baseline()

#reading NIFTY file for getting current nifty file
current_nifty, current_change=read_nifty50()

#Get date and time
param='A'
dt1, time1, week_thursday, last_thursday, abr_month,dt_yyyymmd,time_hh24mise =get_datetime('A')

remarks="NA"

# execute first order if newbasefile.txt is not exists
filename="C:\\NSE\\inputs\\newbasefile.txt"

#refresh Excel
# refresh_excel()
#returns True if File exists
if os.path.isfile(filename):
    #   shutil.copyfile('C:\\NSE\\inputs\\newbasefile.txt', 'C:\\NSE\\inputs\\basefile.txt')
    normal_orders(dt1, time1, current_nifty, week_thursday, last_thursday, abr_month, dt_yyyymmd, time_hh24mise)
else :
    first_order(dt1, time1,current_nifty,week_thursday, last_thursday, abr_month,dt_yyyymmd,time_hh24mise)

format_masters()