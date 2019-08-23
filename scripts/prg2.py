import datetime as dt

import pandas as pd

pd.set_option('display.max_columns', 21)

f = open("C:\\NSE\\inputs\\basefile.txt", "r")
basestrike = int(f.readline())
basechange = int(f.readline())
print(basestrike)
print(basechange)
f.close()

nifty1=pd.read_excel('C:\\NSE\\inputs\\NIFTY50.xlsm', sheet_name='Sheet2')
nifty1.columns = nifty1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
print(nifty1.columns)


current_nifty=float(nifty1.loc[4, 'value'].replace(',',''))

current_change = float(nifty1.loc[6, 'value'])
df1 = pd.read_excel('C:\\NSE\\inputs\\NSEOptions.xlsm', sheet_name='OC')

df2 = (df1.loc[df1['Strike Price'] == basestrike])
df2.columns = df2.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
c1 = round(float(df2['calls_ltp'].values),2)
p1 = round(float(df2['puts_ltp'].values),2)

dt1 = dt.datetime.now().strftime("%d-%b-%Y")
time1 = dt.datetime.now().strftime("%H:%M:%S")

if basestrike >= float(current_nifty) and int(round(basestrike/float(current_nifty)*100 > basechange)) :
    dt1 = dt.datetime.now().strftime("%d-%b-%Y")
    time1 = dt.datetime.now().strftime("%H:%M:%S")
    current_change=round(float(basestrike/float(current_nifty)*100),2)
    callltp = c1
    putltp = p1
    remarks = "Order Generated NIFTY Down"
    data = [dt1, time1, basestrike, basechange, current_nifty, current_change, c1, p1, remarks]
elif basestrike<= float(current_nifty) and int(round(float(current_nifty)/basestrike*100 > basechange)) :
    dt1 = dt.datetime.now().strftime("%d-%b-%Y")
    time1 = dt.datetime.now().strftime("%H:%M:%S")
    print(basestrike, current_nifty, basechange)
    current_change = round(float(basestrike / float(current_nifty) * 100),2)
    print(current_change)
    callltp = c1
    putltp = p1
    remarks = "Order Generated NIFTY Up"
    data = [dt1, time1, basestrike, basechange, current_nifty, current_change, c1, p1,remarks]
else :
    dt1 = dt.datetime.now().strftime("%d-%b-%Y")
    time1 = dt.datetime.now().strftime("%H:%M:%S")
    callltp = c1
    putltp = p1
    if basechange <= float(current_nifty) :
        current_change = round(float(basestrike / float(current_nifty) * 100),2)
    else :
        current_change = (round(basestrike / float(current_nifty) * 100 > basechange),2)
        remarks = "Order NOT Generated"
        data = [dt1, time1, basestrike, basechange, current_nifty, current_change, c1, p1, remarks]


#masterdf = pd.DataFrame([data], columns = ['Date', 'Time', 'Base Stike', 'Base Change','Current NIFTY', 'Change',
                                             'CALL Price', 'Put Price', 'Remarks'])

masterdf.to_excel("C:\\NSE\\outputs\Masters.xlsx", startrow = 0,index = False)