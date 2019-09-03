import pandas as pd

def order_generation(f_order_strike, f_call_put, f_buy_sell, f_calls_bid_price, f_puts_bid_price,
                     week_thursday, last_thursday, abr_month,dt_yyyymmd,time_hh24mise):

    f_order_strike1=int(f_order_strike)
    f_call_put1=f_call_put
    f_buy_sell1=f_buy_sell
    f_calls_bid_price1=f_calls_bid_price
    f_week_thursday = week_thursday
    f_last_thursday = last_thursday
    f_abr_month = abr_month
    f_dt_yyyymmd1= dt_yyyymmd
    f_time_hh24mise1=time_hh24mise

    if f_call_put1 == "CALL":
        f_instrument = "CE"
        f_limit_price = f_calls_bid_price
    else:
        f_instrument = "PE"
        f_limit_price = f_puts_bid_price

    if f_buy_sell1 == "S":
        f_order_sell_buy = "SELL"
    else:
        f_order_sell_buy = "BUY"

    dt1 = ["NSE", "NIFTY" + f_abr_month + str(f_order_strike1) + f_instrument, 1, f_order_sell_buy, 'LIMIT',
           f_limit_price, 0, 'Regular', 0, 0, 'NRML', 0]

    orderdf = pd.DataFrame([dt1], columns=["Exchange", "Trading Symbol",
                                           "Quantity", "Buy/Sell", "Order Type",
                                           "Limit Price", "Trigger Price", "Complexity",
                                           "Target Points", "Stoploss Points", "Intraday / Delivery",
                                           "Trailing Stoploss"])

    fname = f_call_put1 + "-" + f_order_sell_buy + "-" + f_dt_yyyymmd1 + "-" + f_time_hh24mise1 + ".xlsx"
    orderdf.to_excel('C:\\NSE\\outputs\\' + fname, index=False)


