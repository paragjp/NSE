import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', 51)
from disp_message import disp_message


def first_order1(read, dt1, dt2, time, time1,ltp):
    msg=""
    script = read[5]
    script = script.upper().strip().replace(" ", "")
    buy_sell = "S"
    strike=read[1]
    qty = read[2]*read[6]

    symbol= script+str(strike)+"CE"
    order1 = ["NSE", symbol, qty, 'SELL', 'LIMIT', 0, 0, 'Regular', 0, 0, 'NRML', 0]


    fname = script+"-"+"FIRST"+"-"+str(dt1)+"-"+str(time)+".xlsx"

    symbol = script + str(strike) + "PE"
    order2 = ["NSE", symbol, qty, 'SELL', 'LIMIT', 0, 0, 'Regular', 0, 0, 'NRML', 0]
    first_order = pd.DataFrame([order1, order2], columns=["Exchange", "Trading Symbol",
                                           "Quantity", "Buy/Sell", "Order Type",
                                           "Limit Price", "Trigger Price", "Complexity",
                                           "Target Points", "Stoploss Points", "Intraday / Delivery",
                                           "Trailing Stoploss"])
    first_order.to_excel('C:\\NSE\\outputs\\' + fname, index=False)

    r1 = pd.read_excel('C:\\NSE\\inputs\\basefile.xlsx')
    r1.columns = \
        r1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    r1['strike']=round(float(ltp),2)
    r1['lastupd_dt']=dt2
    r1['lastupd_time']=time1
    r1.to_excel('C:\\NSE\\inputs\\basefile.xlsx', index=False)

    dt1 = dt.datetime.now().strftime("%Y""%m""%d")
    time1 = dt.datetime.now().strftime('%H:%M:%S')
    dt2 = dt1 + time1
    t1 = dt.datetime.strptime(dt2, '%Y%m%d%H:%M:%S')
    dt_time = t1.strftime("%d %b %Y %H:%M:%S")
    msg = str(dt_time)+" "+script.upper()+" FIRST "+"Order Generated in NSE for Qty "+str(qty)+" at Strike Price "+str(strike)+" Pl check"
    msgtype=2
    disp_message(msg,msgtype)

