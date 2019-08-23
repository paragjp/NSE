import pandas as pd
pd.set_option('display.max_columns', 21)

from read_baseline import read_baseline
from read_nifty50 import read_nifty50
from read_niftyoptions import read_niftyoptions
from get_datetime import get_datetime
from append_to_excel import append_to_excel

#reading baseline file for reading strike price and % of change
basestrike, basechange=read_baseline()

#reading NIFTY file for getting current nifty file
current_nifty, current_change=read_nifty50()

#reading NIFTY Option change Analysis File
callltp, putltp = read_niftyoptions(basestrike)

#Get date and time
dt1, time1=get_datetime()
remarks="test"

if float(basestrike) >= float(current_nifty) and \
    abs(round((float(current_nifty)*100/basestrike) -100,2)) >= abs(round(basechange,2)):
    current_change = round((float(current_nifty) *100 / basestrike ) - 100, 2)
    remarks = "PUT Sell Order Generated NIFTY Down"

elif basestrike<= float(current_nifty) and \
    abs(round(100 -(float(basestrike*100/current_nifty)),2)) >= abs(round(basechange,2)) :
    current_change = round((100 - float( basestrike * 100)/current_nifty), 2)
    remarks = "CALL Sell Order Generated NIFTY Up"
else :
    if  float(basestrike) >= float(current_nifty) :
       current_change = round((float(current_nifty) *100 / basestrike ) - 100, 2)
    else :
        current_change = round((100 - float( basestrike * 100)/current_nifty), 2)

    remarks = "Order NOT Generated No change compare to basechange"



data=[dt1, time1, basestrike, basechange, current_nifty,current_change,callltp, putltp, remarks]
print(data)

#append to masters excel
append_to_excel(data)
#format_excel()