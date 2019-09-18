import os
import sys
import pandas as pd
import datetime as dt
import numpy as np
from disp_message import disp_message
from format_masters import format_masters
from disp_message import disp_message
from lower_upper import lower_upper
import write_to_html_file


pd.set_option('display.max_columns', 51)

def write_order(read,dt1,dt2,time,time1,ltp,change):
    script = read[5]
    script = script.upper().strip().replace(" ", "")
    buy_sell = "S"
    strike=read[1]
    qty = read[2]*read[6]
    prevdiff=read[7]
    normal_order=[]
    order=[]
    previous_call_change = 0
    previous_put_change = 0
    # calculate previous change is greater than 1 Rs
    df = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df.columns = \
        df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df = df[df['remarks'] != 'Average']
#    previous_call_change=df[(df.script == script)].set_index('current_change')['call_put'].eq('CALL')[::-1].idxmax()+prevdiff
#    previous_put_change=df[(df.script == script)].set_index('current_change')['call_put'].eq('PUT')[::-1].idxmax()+prevdiff

#    if float(ltp) >= float(read[1]) and abs(float(change)) >= float(read[3]) and  abs(float(change)) >= float(previous_put_change):
    if float(ltp) >= float(read[1]) and abs(float(change)) >= float(read[3]):
       symbol= script+str(strike)+"PE"
       fname = script+"-"+"PUT"+"-"+dt1+"-"+time+".xlsx"
#    elif float(ltp) <= float(read[1]) and abs(float(change)) >= float(read[3]) and abs(float(change)) >= float(previous_call_change):
    elif float(ltp) <= float(read[1]) and abs(float(change)) >= float(read[3]):
       symbol = script + str(strike) + "CE"
       fname = script+"-"+"CALL" + "-" + str(dt1) + "-" + str(time) + ".xlsx"
    else:
        lower_upper()
        format_masters()
        write_to_html_file
        dt1 = dt.datetime.now().strftime("%Y""%m""%d")
        time1 = dt.datetime.now().strftime('%H:%M:%S')
        dt2 = dt1 + time1
        t1 = dt.datetime.strptime(dt2, '%Y%m%d%H:%M:%S')
        dt_time = t1.strftime("%d %b %Y %H:%M:%S")
        msg = str(dt_time)+ " "+script.upper()+" NO Order Generated in NSE as change is not significant"\
              +" Pl check"+" Current Change :"+str(change)+" New Strike :"+str(read[1])
        msgtype = 3
        disp_message(msg, msgtype)
        sys.exit("No Order is generated")

    order = ["NSE", symbol, qty, 'SELL', 'LIMIT', 0, 0, 'Regular', 0, 0, 'NRML', 0]

    normal_order = pd.DataFrame([order], columns=["Exchange", "Trading Symbol",
                                           "Quantity", "Buy/Sell", "Order Type",
                                           "Limit Price", "Trigger Price", "Complexity",
                                           "Target Points", "Stoploss Points", "Intraday / Delivery",
                                           "Trailing Stoploss"])
    normal_order.to_excel('C:\\NSE\\outputs\\' + fname, index=False)

    dt1 = dt.datetime.now().strftime("%Y""%m""%d")
    time1 = dt.datetime.now().strftime('%H:%M:%S')
    dt2 = dt1 + time1
    t1 = dt.datetime.strptime(dt2, '%Y%m%d%H:%M:%S')
    dt_time = t1.strftime("%d %b %Y %H:%M:%S")
    msg = str(dt_time) + " " + script.upper()+" Order Generated in NSE for Qty "+str(qty)+" at Strike Price "+str(strike)+ " Pl check"
    msgtype = 2
    disp_message(msg, msgtype)
