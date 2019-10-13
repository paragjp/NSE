import os
import sys
import pandas as pd
import datetime as dt
import numpy as np

from lower_upper import lower_upper
from myround import myround
from cal_profit_loss import cal_profit_loss

def write_master_entry(dt1, dt2, time, time1, read, ltp, change, remarks, first_order):
    df_excel= pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df_excel.columns = \
        df_excel.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    if first_order == "Y" :
        call_put= "CALL"
        buy_sell= "SELL"
        call_price = 0.00
        put_price = 0.00
        executed = "Y"
        type1="O"
        remarks = "First CALL Order"
        qty=qty = read[2]*read[6]
        master1=[dt2,time1,read[0],read[1],ltp,read[3],change,qty,
                 type1,call_put,buy_sell,call_price,put_price,0.00,0.00,0.00,
                 executed, remarks,1.00,0.00,0.00,0.00,0.00,0.00,0.00]

        call_put = "PUT"
        buy_sell = "SELL"
        call_price = 0.00
        put_price = 0.00
        executed = "Y"
        remarks = "First PUT Order"
        master2=[dt2,time1,read[0],read[1],ltp,read[3],change,qty,
                 type,call_put,buy_sell,call_price,put_price,0.00,0.00,0.00,
                 executed,remarks,1.00,0.00,0.00,0.00,0.00,0.00,0.00]

        master=[]
        master= pd.DataFrame([master1,master2], columns =
                                ['date','time','script','base_strike','ltp','base_change','current_change','qty',
                                 'type','call_put','buy_sell','call_price','put_price','total_premium','cumm_premium',
                                 'amt','executed','remarks','kount','profit','loss',
                                 'arrived_call_strike','arrived_put_strike','upper_band','lower_band'])

        result = df_excel.append(master, sort=False)
        result.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)


    if first_order == "N" :
       call_put = ""
       buy_sell = "SELL"
       call_price = 0.00
       put_price = 0.00
       type1="O"
       executed = "Y"
       master=[]
       new=[]
       df_excel=[]
       qty = read[2]*read[6]
       new_strike=0
       read1=[]

       #new_strike = myround(float(ltp), int(read[8]))
       new_strike = round(float(ltp),2)
       r1 = pd.read_excel('C:\\NSE\\inputs\\basefile.xlsx')
       r1.columns = \
           r1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
       read1=read
       read1[1]= new_strike
       r1.loc[(r1['script'] == read[0])] = read1
       r1.to_excel('C:\\NSE\\inputs\\basefile.xlsx', index=False)


       if  float(ltp) >= float(read[1]) and abs(change) >= float(read[3]) :
            remarks = "PUT Order"
            call_put = "PUT"
            master  = [dt2, time1,read[0],read[1],ltp,read[3],change,qty,type1,
                       call_put,buy_sell,call_price,put_price,0.00,0.00,0.00,
                       executed, remarks,0.00,0.00,0.00,0.00,0.00,0.00,
                       0.00]


       elif float(ltp) <= float(read[1]) and abs(change) >= float(read[3]) :
            remarks = "CALL Order"
            call_put = "CALL"
            master  = [dt2,time1,read[0],read[1],ltp,read[3],change,qty,type1,
                       call_put,buy_sell,call_price,put_price,0.00,0.00,0.00,
                       executed,remarks,0.00,0.00,0.00,0.00,0.00,0.00,
                       0.00]

       else :
           print("SCRIPT : ", read[0])
           sys.exit("Changes are less than defined in a basefile")

       df_excel = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
       df_excel.columns = \
                    df_excel.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
       df_excel = df_excel[df_excel['remarks'] != 'Average']

       result=[]
       result1=[]
       new = pd.DataFrame([master], columns =
                                       ['date','time','script','base_strike','ltp','base_change','current_change','qty',
                                        'type1','call_put','buy_sell','call_price','put_price','total_premium','cumm_premium',
                                        'amt','executed','remarks','kount','profit','loss','arrived_call_strike',
                                        'arrived_put_strike','upper_band','lower_band'])
       result = df_excel.append(new, sort=False)
       result['kount'] = result.groupby(['script', 'call_put']).cumcount() + 1
       print("XXXXXXXXXXXXX")
       result1=cal_profit_loss(result,type1)
       print("yyyyyyyyyyyyyy")
       result.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)
       lower_upper()


