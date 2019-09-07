import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', 51)

def first_order1(read, dt1, dt2, time, time1):
    script = read[5]
    script = script.upper().strip().replace(" ", "")
    buy_sell = "S"
    strike=read[1]
    qty = read[2]
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

