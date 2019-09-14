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
from disp_message import disp_message
from lower_upper import lower_upper
from write_to_html_file import write_to_html_file


r1 = pd.read_csv('C:\\NSE\\inputs\\basefile.csv')
r1.columns = \
    r1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
for index, row in r1.iterrows():
    read = list(row)

    if len(read) == 0:
        print("Reading Baseline File is completed")
        sys.exit("program completed")

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


    script, ltp, change, remarks = read_watchlist(read)
    y = int(df_master.query('script == @script')['script'].count())
    if y > 0:
        first_order = "N"
    else:
        first_order = "Y"

    print(read)

    if first_order == "Y" :
       first_order1(read, dt1, dt2, time, time1)
    elif abs(change) >= float(read[3]):
         write_order(read,dt1,dt2,time,time1,ltp,change)
    else:
        lower_upper()
        format_masters()
        write_to_html_file
        dt1 = dt.datetime.now().strftime("%Y""%m""%d")
        time1 = dt.datetime.now().strftime('%H:%M:%S')
        dt2 = dt1 + time1
        t1 = dt.datetime.strptime(dt2, '%Y%m%d%H:%M:%S')
        dt_time = t1.strftime("%d %b %Y %H:%M:%S")
        msg = str(dt_time)+ " NO Order Generated as change is not significant for "+script.upper()+" LTP:"+\
              str(ltp)+" Base Strike:"+str(read[1])+" Change:"+str(change)+ " Pl check"
        msgtype = 3
        disp_message(msg, msgtype)
        sys.exit("No Order is generated")

    write_master_entry(dt1, dt2, time, time1, read, ltp, change, remarks, first_order)
    format_masters()
    write_to_html_file

print("Program Finished ...")

#format_masters()