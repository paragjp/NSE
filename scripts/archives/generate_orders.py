import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', 51)

from first_order1 import first_order1

def generate_orders(wdf2_total_rows, wd2_up_down, r1_script, r1_strike,wd2_ltp, r1_diff, wd2_change, r1_qty):

    dt1 = dt.datetime.now().strftime("%Y%m%d")
    time1= dt.datetime.now().strftime("%H%M%S")

    order_executed = "Y"
    lower_band = 0.00
    upper_band = 0.00
    call_price = 0.00
    put_price = 0.00
    amt = 0.00

    #checking it is first order or not
    if wdf2_total_rows < 3:
        remarks = "First CALL Order"
        data1 = [dt1, time1, r1_script, r1_strike, wd2_ltp, r1_diff, wd2_change, r1_qty, "CALL", "S",
                call_price, put_price, amt, order_executed, remarks, lower_band, upper_band]

        first_order1(data1)
        remarks = "First PUT Order"
        data2 = [dt1, time1, r1_script, r1_strike, wd2_ltp, r1_diff, wd2_change, r1_qty, "PUT", "S",
                call_price, put_price, amt, order_executed, remarks, lower_band, upper_band]

        df_excel = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
        df_excel.columns = \
            df_excel.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
        df_excel = df_excel[df_excel['remarks'] != 'Average']
        new = pd.DataFrame([data1,data2],columns=['date', 'time', 'script', 'base_strike', 'current_nifty',
                                            'base_change', 'current_change', 'qty', 'call_put', 'buy_sell',
                                            'call_price',
                                            'put_price', 'amt', 'executed', 'remarks',
                                            'lower_band', 'upper_band'])

        new = df_excel.append(new, sort=False)
        new.to_excel("C:\\NSE\\OUTPUTS\\Masters.xlsx", index=False)
    else:
        print("No Orders")
