import pandas as pd
pd.set_option('display.max_columns', 21)

data=[111,21,31,4,5,6,7,8, 9]
df_excel = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
print("Excel Df")
print(df_excel)
new=pd.DataFrame([data], columns = ['Date', 'Time', 'Base Stike', 'Base Change','Current NIFTY', 'Change',
                                             'CALL Price', 'Put Price', 'Remarks'])
result = df_excel.append(new)
print(result)
result.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)
