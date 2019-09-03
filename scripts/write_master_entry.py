import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

from lower_upper import lower_upper

def write_master_entry(dt1, dt2, time, time1, read, ltp, change, remarks, first_order):
    df_master= pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df_master.columns = \
        df_master.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    if first_order == "Y" :
        call_put= "CALL"
        buy_sell= "SELL"
        call_price = 0.00
        put_price = 0.00
        executed = "Y"
        remarks = "First CALL Order"
        master1=[dt2, time1, read[0], read[1], ltp, read[3], change, read[2], call_put,
                buy_sell, call_price, put_price, 0.00, 0.00, 0.00, executed, remarks, 0.00, 0.00, 0.00, 0.00,
                0.00, 0.00, 0.00, 0.00]

        call_put = "PUT"
        buy_sell = "SELL"
        call_price = 0.00
        put_price = 0.00
        executed = "Y"
        remarks = "First PUT Order"
        master2=[dt2, time1, read[0],read[1], ltp, read[3], change,read[2],call_put,
                buy_sell, call_price, put_price, 0.00, 0.00, 0.00, executed, remarks, 0.00, 0.00, 0.00, 0.00,
                0.00, 0.00, 0.00, 0.00]

        master=[]
        master= pd.DataFrame([master1,master2], columns =
                                ['date', 'time', 'script','base_strike','ltp',
                                 'base_change', 'current_change', 'qty',
                                 'call_put','buy_sell','call_price',
                                 'put_price', 'total_premium', 'cumm_premium', 'amt', 'executed', 'remarks',
                                 'kount', 'sum_amt', 'sum_qty', 'qty_strike',
                                 'cum_qty_strike','arrived_strike', 'lower_band','upper_band'])
        master.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)

    if first_order == "N" :
       call_put = ""
       buy_sell = "SELL"
       call_price = 0.00
       put_price = 0.00
       executed = "Y"
       maxster=[]
       new=[]
       df_excel=[]
       if  float(ltp) >= float(read[1]) and abs(change) >= float(read[3]) :
            remarks = "PUT Order"
            call_put = "PUT"
            master  = [dt2, time1, read[0], read[1], ltp, read[3], change, read[2], call_put,
                       buy_sell, call_price, put_price, 0.00, 0.00, 0.00, executed, remarks, 0.00, 0.00, 0.00, 0.00,
                       0.00, 0.00, 0.00, 0.00]
       elif float(ltp) <= float(read[1]) and abs(change) >= float(read[3]) :
            remarks = "CALL Order"
            call_put = "CALL"
            master  = [dt2, time1, read[0], read[1], ltp, read[3], change, read[2], call_put,
                       buy_sell, call_price, put_price, 0.00, 0.00, 0.00, executed, remarks, 0.00, 0.00, 0.00, 0.00,
                       0.00, 0.00, 0.00, 0.00]

       df_excel = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
       df_excel.columns = \
                    df_excel.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
       df_excel = df_excel[df_excel['remarks'] != 'Average']

       result=[]
       new = pd.DataFrame([master], columns =
                                    ['date', 'time', 'script','base_strike','ltp',
                                     'base_change', 'current_change', 'qty',
                                     'call_put','buy_sell','call_price',
                                     'put_price', 'total_premium', 'cumm_premium', 'amt', 'executed', 'remarks',
                                     'kount', 'sum_amt', 'sum_qty', 'qty_strike',
                                     'cum_qty_strike','arrived_strike', 'lower_band','upper_band'])
       result = df_excel.append(new, sort=False)
       result.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)

       lower_upper()

