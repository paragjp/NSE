import pandas as pd

def write_last_row():
# reading excel and deleting row having Average value and appending last average row
    lastdf = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    lastdf.columns = \
            lastdf.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    lastdf1 = lastdf[lastdf['remarks'] != 'Average']
    f_lower_bandavg=round(float(lastdf1['lower_band'].mean(axis=0)),2)
    f_upper_bandavg=round(float(lastdf1['upper_band'].mean(axis=0)),2)
    last=['Average',f_lower_bandavg, f_upper_bandavg]
    last_rows=pd.DataFrame([last], columns =['remarks', 'lower_band', 'upper_band'])
    lastdf=lastdf1.append(last_rows, sort=False).fillna(' ')
    lastdf.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)

#lastdf1 = lastdf[lastdf['Remarks'] != 'Average']
#f_lower_bandavg = round(float(lastdf1['Lower Band'].mean(axis=0)), 2)
#f_upper_bandavg = round(float(lastdf1['Upper Band'].mean(axis=0)), 2)
#last = ['Average', f_lower_bandavg, f_upper_bandavg]
#last_rows = pd.DataFrame([last], columns=['Remarks', 'Lower Band', 'Upper Band'])
#lastdf = lastdf1.append(last_rows, sort=False).fillna(' ')
#lastdf.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)
