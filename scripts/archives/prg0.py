# Create blank Masterfile for recording ALL changes after particular duration
import pandas as pd
from openpyxl.workbook import Workbook

#heading = [" MASTERS File " + dttime[:11]]
filename = 'C:\\NSE\\outputs\\MASTERS.xlsx'
# Create blank Masterfile for recording ALL changes after particular duration

wb = Workbook()
ws = wb.active
ws.title = "Masters"
wb.save(filename='C:\\NSE\\outputs\Masters.xlsx')
print("Masters Excel File created in C:\\NSE\\outputs")

masterdf = pd.DataFrame(columns = ['Date', 'Time', 'Base Stike', 'Base Change','Current NIFTY',
                                   'Change','CALL Price', 'Put Price', 'Remarks'])

masterdf.to_excel("C:\\NSE\\outputs\Masters.xlsx", startrow = 0,index = False)
