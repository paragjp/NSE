# Create blank Masterfile for recording ALL changes after particular duration
import os

import pandas as pd
from openpyxl.workbook import Workbook

# Create blank Masterfile for recording ALL changes after particular duration
# heading = [" MASTERS File " + dttime[:11]]
# Remove Masters Excel file
filename='C:\\NSE\\outputs\Masters.xlsx'
if os.path.isfile(filename):
    os.remove(filename)

#filename = 'C:\\NSE\\outputs\\MASTERS.xlsx'

#wb = Workbook()
#ws = wb.active
#ws.title = "Masters"
#wb.save(filename='C:\\NSE\\outputs\Masters.xlsx')
#print("Masters Excel File  created in C:\\NSE\\outputs")

masterdf = pd.DataFrame(columns=['date', 'time', 'base_strike','current_nifty',
                                        'change', 'order_strike','call_price', 'put_price', 'call_put', 'buy_sell',
                                        "executed", 'remarks', 'lower_band', 'upper_band'])
masterdf.to_excel("C:\\NSE\\outputs\Masters.xlsx", startrow=0, index=False)


filename = "C:\\NSE\\inputs\\newbasefile.txt"
if os.path.isfile(filename):
    os.remove(filename)
