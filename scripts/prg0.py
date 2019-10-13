# Create blank Masterfile for recording ALL changes after particular duration
import os
import pandas as pd
import datetime as dt
from disp_message import disp_message

filename='C:\\NSE\\outputs\Masters.xlsx'
if os.path.isfile(filename):
    os.remove(filename)

filename = "C:\\NSE\\OUTPUTS\\Masters.xlsx"
if os.path.isfile(filename):
    os.remove(filename)

masterdf = pd.DataFrame(columns=['date', 'time', 'script','base_strike','ltp',
                                 'base_change', 'current_change', 'qty','type',
                                 'call_put','buy_sell','call_price',
                                 'put_price', 'total_premium', 'cumm_premium', 'amt', 'executed', 'remarks',
                                 'kount','profit', 'loss', 'arrived_call_strike','arrived_put_strike','upper_band','lower_band'])
masterdf.to_excel("C:\\NSE\\outputs\Masters.xlsx", startrow=0, index=False)

x1=dt.datetime.now().strftime("%d %b %Y %H:%M:%S")
msg="Master File Initiated at "+x1
msgtype=1
disp_message(msg,msgtype)


filename = "C:\\NSE\\inputs\\newbasefile.txt"
if os.path.isfile(filename):
    os.remove(filename)
