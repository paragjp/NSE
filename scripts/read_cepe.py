import os
import sys
import pandas as pd
pd.set_option('display.max_columns', 51)



def read_cepe(read) :
    print("Reading Script :"+read[1].upper())

    wdf1 = pd.read_excel('C:\\NSE\\inputs\\OI.xlsx', sheet_name=read[1].upper())
    wdf1.columns = \
        wdf1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    script = read[1]
    cestrike = round(float(read[4]),2)
    pestrike = round(float(read[6]),2)
    totalcost = round(float(read[5]+read[7]),2)
    loss=round(float(read[9]),2)
    profit=round(float(read[10]),2)
    wdf2 = wdf1.loc[wdf1['strike_price'].isin([cestrike])]
    wdf2_total_rows = wdf2.shape[0]
    if wdf2_total_rows != 1:
        print("SCRIPT : ", script)
        print("strike :"+str(cestrike))
        sys.exit("No CALL Data Found in OI File")

    wdf3 = wdf1.loc[wdf1['strike_price'].isin([pestrike])]
    wdf3_total_rows = wdf3.shape[0]
    if wdf3_total_rows != 1:
        print("SCRIPT : ", script)
        print("strike :" + str(pestrike))
        sys.exit("No PUT Data Found in OI File")

# Get current CALL & PUT Premium
    celtp= round(float(wdf2['calls_ltp'].values), 2)
    peltp= round(float(wdf3['puts_ltp'].values), 2)
    totalltp = round(float(celtp+peltp),2)

    return(script,celtp,peltp,loss,profit,totalcost,totalltp)



