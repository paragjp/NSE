import os
import sys
import pandas as pd
import datetime as dt
import time as dttime
import numpy as np

pd.set_option('display.max_columns', 51)
from refresh_excel_oi import refresh_excel_oi
from read_cepe import read_cepe
from first_order1 import first_order1
from show_message import show_message
from update_excels import update_excels
from format_excels_cepe import format_excels_cepe
from append_excels import append_excels
from refresh_excel import refresh_excel
from df_to_html import df_to_html

refresh_excel()
r1 = pd.read_excel('C:\\NSE\\inputs\\cepebasefile.xlsx')
r1.columns = \
    r1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
for index, row in r1.iterrows():
    read = list(row)

    if len(read) == 0:
        print("Reading Baseline File is completed")
        sys.exit("Program completed ...")

    today = dt.datetime.now().strftime("%Y%m%d").upper()
    print(read[2])

    if int(today) > int(read[2]):
        print("SCRIPT : ", read[0])
        print("Expiry Date :", read[2])
        sys.exit("Expiry Date is over for above script check CEPEbasefile.xlsx")

    # refresh_excel_oi()
    dt1 = dt.datetime.now().strftime("%Y""%m""%d")
    dt2 = dt.datetime.now().strftime("%d-%b-%Y")

    time1 = dt.datetime.now().strftime('%H:%M:%S')
    time = time1.replace(':','')

    r2= pd.read_excel('C:\\NSE\\inputs\\OI.xlsx', index_col=None)
    r2.columns = \
        r2.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    script,celtp,peltp,loss,profit,totalcost,totalltp = read_cepe(read)

    msg1 = dt1 + " " + time1 + " " + script.upper() + " Total Cost is: " + str(round(totalcost,2))  + \
           " Loss Limit:" + str(loss) + " Profit Limit:" + str(profit) + "\n"
    msg2= "Current CALL Premium :"+ str(celtp) + " PUT Premium :" + str(peltp) + " Total LTP: " \
           + str(round(totalltp,2))
    if abs(totalcost-totalltp) >=loss :
       print("Reached loss limit of ", loss)
       type1="L"
       msg3 = "!! LOSS !! Difference between Total Cost & Total LTP is: " + str(round(abs(totalcost-totalltp),2))+"\n"
    elif abs(totalltp-totalcost) >= profit:
        print("Reached max profit limit", profit)
        type1="P"
        msg3 = "** PROFIT ** Difference between Total Cost & Total LTP is: " + str(round(abs(totalltp-totalcost),2)) + "\n"
    else:
        type1="N"
        msg3 = "No PROFIT or Loss ** Difference between Total Cost & Total LTP is: " + str(round(abs(totalcost-totalltp),2)) + "\n"

    show_message(type1,msg1,msg2,msg3)
    update_excels(script,dt2,time1,totalcost,celtp,peltp,msg3)

append_excels(script,dt2,time1,totalcost,celtp,peltp)
#
format_excels_cepe()
dttime.sleep(3)
df_to_html()
print("Program Finished ...")

#format_masters()