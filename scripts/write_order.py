import os
import sys
import pandas as pd
import datetime as dt
import numpy as np
from disp_message import disp_message

pd.set_option('display.max_columns', 51)

def write_order(read,dt1,dt2,time,time1,ltp,change):
    script = read[5]
    script = script.upper().strip().replace(" ", "")
    buy_sell = "S"
    strike=read[1]
    qty = read[2]*read[6]
    normal_order=[]
    order=[]
    if float(ltp) >= float(read[1]) and abs(float(change)) >= float(read[3]):
       symbol= script+str(strike)+"PE"
       fname = script+"-"+"PUT"+"-"+dt1+"-"+time+".xlsx"
    elif float(ltp) <= float(read[1]) and abs(float(change)) >= float(read[3]):
       symbol = script + str(strike) + "CE"
       fname = script+"-"+"CALL" + "-" + str(dt1) + "-" + str(time) + ".xlsx"
    else:
        dt1 = dt.datetime.now().strftime("%Y""%m""%d")
        time1 = dt.datetime.now().strftime('%H:%M:%S')
        dt2 = dt1 + time1
        t1 = dt.datetime.strptime(dt2, '%Y%m%d%H:%M:%S')
        dt_time = t1.strftime("%d %b %Y %H:%M:%S")
        msg = str(dt_time)+ " "+ script.upper() + "NO Order Generated in NSE as change is not significant" + " Pl check"
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
