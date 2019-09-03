import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

pd.set_option('display.max_columns', 51)
from read_watchlist import read_watchlist
from refresh_excel import refresh_excel
from first_order1 import first_order1
from write_master_entry import write_master_entry
from write_order import write_order
from format_masters import format_masters

r1 = pd.read_csv('C:\\NSE\\inputs\\basefile.csv')
r1.columns = \
    r1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
for index, row in r1.iterrows():
    read = []
    r_script = row[0]
    r_strike = row[1]
    r_qty = row[2]
    r_diff = row[3]
    r_expirydt = row[4]
    r_fo_script = row[5]
    r_lot_size = row[6]
    read = [r_script, r_strike, r_qty, r_diff, r_expirydt, r_fo_script, r_lot_size]
    if len(read) == 0:
        print("Reading Baseline File is completed")
        sys.exit("program completed")
    print(read)

    today = dt.datetime.now().strftime("%Y%m%d").upper()

    if int(today) > int(read[4]):
        print("SCRIPT : ", read[0])
        print("Expiry Date :", read[4])
        sys.exit("Expiry Date is over for above script")

    refresh_excel()
    dt1 = dt.datetime.now().strftime("%Y""%m""%d")
    dt2 = dt.datetime.now().strftime("%d-%b-%Y")

    time1 = dt.datetime.now().strftime('%H:%M:%S')
    time = time1.replace(':','')

    df_master= pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df_master.columns = \
        df_master.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    ltp, change, remarks = read_watchlist(read)
    if df_master.empty :
       first_order = "Y"
       first_order1(read, dt1, dt2, time, time1)
    elif abs(change) > float(read[3]):
         first_order = "N"
         write_order(read,dt1,dt2,time,time1,ltp,change)

    write_master_entry(dt1, dt2, time, time1, read, ltp, change, remarks, first_order)

    format_masters()

print("Program Finished ...")

#format_masters()