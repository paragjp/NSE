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

def first_order(dt1, time1,current_nifty,week_thursday,last_thursday,abr_month,dt_yyyymmd,time_hh24mise):
    print("First Orders Generation")
    # reading baseline file
    f_basestrike, f_basechange = read_baseline()

    # getting basestrike to nearest fifty for order strike price
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
    file.write(str(f_basestrike)+"\n")
    file.close()


    # Getting Difference between basenifty strike price and current nifty
    f_current_change = calculate_change(float(f_basestrike),float(f_current_nifty))

    f_executed = "Y"

    f_call_put = "CALL"
    f_buy_sell = "S"
    f_remarks = "First CALL Order"
#    f_lower_band = float(f_order_strike - f_calls_bid_price)
#    f_upper_band = float(f_order_strike + f_calls_bid_price)
    f_lower_band = 0.00
    f_upper_band = 0.00

    data = [dt1, f_time1, f_basestrike, f_current_nifty, f_current_change, f_order_strike,
            f_calls_bid_price, 0.00, f_call_put, f_buy_sell, f_executed, f_remarks, f_lower_band, f_upper_band]

    order_generation(f_order_strike, f_call_put, f_buy_sell, f_calls_bid_price, f_puts_bid_price,
                     week_thursday, last_thursday, abr_month,dt_yyyymmd,time_hh24mise)
    # append to masters excel
    append_to_excel(data)

    f_call_put = "PUT"
    f_buy_sell = "S"
    f_remarks = "First PUT Order"
    #f_lower_band = float(f_order_strike - f_puts_bid_price)
    f_lower_band = 0.00
    f_upper_band = 0.00
    f_upper_band =  float(f_order_strike + f_puts_bid_price)
    data = [dt1, f_time1, f_basestrike, f_current_nifty, f_current_change, f_order_strike,
            0.00, f_puts_bid_price, f_call_put, f_buy_sell, f_executed, f_remarks, f_lower_band, f_upper_band]
    # append to masters excel
    append_to_excel(data)

    # calculate Lower and Upper Band and calculate total average
    calculate_band()
    write_last_row()
    # orders generation
    order_generation(f_order_strike, f_call_put, f_buy_sell, f_calls_bid_price, f_puts_bid_price,
                     week_thursday, last_thursday, abr_month, dt_yyyymmd, time_hh24mise)


