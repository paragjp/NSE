import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

pd.set_option('display.max_columns', 51)

def write_order(read,dt1,dt2,time,time1,ltp,change):
    script = read[5]
    buy_sell = "S"
    strike=read[1]
    lot = read[6]
    normal_order=[]
    order=[]
    if float(ltp) >= float(read[1]) and abs(float(change)) >= float(read[3]):
       symbol= script+str(strike)+"PE"
       fname = "PUT"+"-"+dt1+"-"+time+".xlsx"
    elif float(ltp) <= float(read[1]) and abs(float(change)) >= float(read[3]):
       symbol = script + str(strike) + "CE"
       fname = "CALL" + "-" + str(dt1) + "-" + str(time) + ".xlsx"

    order = ["NSE", symbol, lot, 'SELL', 'LIMIT', 0, 0, 'Regular', 0, 0, 'NRML', 0]

    normal_order = pd.DataFrame([order], columns=["Exchange", "Trading Symbol",
                                           "Quantity", "Buy/Sell", "Order Type",
                                           "Limit Price", "Trigger Price", "Complexity",
                                           "Target Points", "Stoploss Points", "Intraday / Delivery",
                                           "Trailing Stoploss"])
    normal_order.to_excel('C:\\NSE\\outputs\\' + fname, index=False)
