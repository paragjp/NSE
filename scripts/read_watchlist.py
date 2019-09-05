import os
import sys
import pandas as pd
pd.set_option('display.max_columns', 51)

def read_watchlist(read) :
    wdf1 = pd.read_excel('C:\\NSE\\inputs\\watchlist.xlsx', sheet_name='Sheet2')
    wdf1.columns = \
        wdf1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')','')
    script = read[0]
    script = script.upper().strip().replace(" ","")
    wdf2 = wdf1[wdf1['column1.symbol'] == script]
    wdf2_total_rows = wdf2.shape[0]
    if wdf2_total_rows == 0:
       print("SCRIPT : ", script)
       sys.exit("No Data Found in Watchlist")

# calculate difference
    ltp = round(float(wdf2['column1.ltp'].values), 2)
    change = round(float(ltp - read[1]),2)

    if abs(change) >= abs(read[3]) :
        if ltp > float(read[1]):
           remarks = "UP than base strike"
        else :
           remarks = "DOWN than base Strike"
    else:
        remarks = "No change compare to baseline difference"

    return(script, ltp, change, remarks)



