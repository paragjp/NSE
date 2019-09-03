import pandas as pd

pd.set_option('display.max_columns', 25)

from read_baseline import read_baseline
from read_niftyoptions import read_niftyoptions
from append_to_excel import append_to_excel
from calculate_change import calculate_change
from myround import myround
from order_generation import order_generation
from write_last_row import write_last_row
from calculate_band import calculate_band

def normal_orders(dt1, time1, current_nifty, week_thursday, last_thursday, abr_month, dt_yyyymmd, time_hh24mise):
    # reading baseline file
    f_basestrike, f_basechange = read_baseline()

    # getting basestrike to nearest fifty for orders
    base = 50
#    f_order_strike = myround(current_nifty,base)
    f_order_strike = f_basestrike

    #getting bid price for CALL and PUT
    f_callltp, f_putltp, f_calls_bid_price, f_puts_bid_price = read_niftyoptions(f_order_strike)

    #Converting inputs to function specific variables
    f_dt1, f_time1, f_current_nifty = dt1, time1, current_nifty

    file = open("C:\\NSE\\inputs\\newbasefile.txt", "w+")
    file.write(f_dt1+"\n")
    file.write(f_time1+"\n")
    file.write(str(f_current_nifty)+"\n")
    file.write(str(f_basechange)+"\n")
    file.write(str(f_basestrike) + "\n")
    file.close()

    # Getting Difference between basenifty strike price and current nifty
    f_current_change = calculate_change(float(f_basestrike),float(f_current_nifty))

    f_executed = "Y"

    if abs(f_current_change) >= abs(f_basechange):
        if float(f_current_nifty) >= float(f_basestrike):
            f_call_put = "PUT"
            f_buy_sell = "S"
            f_remarks = "NIFTY is UP"
            f_calls_bid_price = 0.00
        elif float(f_current_nifty) <= float(f_basestrike):
            f_call_put = "CALL"
            f_buy_sell = "S"
            f_remarks = "NIFTY is DOWN"
            f_puts_bid_price = 0.00
    else:
        f_call_put = "NA"
        f_buy_sell = "N"
        f_executed = "N"
        f_remarks = "No change"

#    f_calls_bid_price=0.00
#    f_puts_bid_price=80.00

    if f_executed == "Y":
        f_lower_band = 0.00
        f_upper_band = 0.00

        data = [dt1, f_time1, f_basestrike, f_current_nifty, f_current_change, f_order_strike,
                f_calls_bid_price, f_puts_bid_price, f_call_put, f_buy_sell, f_executed, f_remarks,
                f_lower_band, f_upper_band]

        # append to masters excel
        append_to_excel(data)

        # calculate Lower and Upper Band and calculate total average
        calculate_band()
        write_last_row()

        order_generation(f_order_strike, f_call_put, f_buy_sell, f_calls_bid_price, f_puts_bid_price,
                         week_thursday, last_thursday, abr_month,dt_yyyymmd,time_hh24mise)
