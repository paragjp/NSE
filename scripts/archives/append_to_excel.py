import pandas as pd
pd.set_option('display.max_columns', 21)

def append_to_excel(data):
    df_excel = pd.read_excel('C:\\NSE\\outputs\Masters.xlsx', index_col=None)
    df_excel.columns = \
        df_excel.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df_excel = df_excel[df_excel['remarks'] != 'Average']
    new = pd.DataFrame([data], columns=['date', 'time', 'base_strike','current_nifty',
                                        'change', 'order_strike','call_price', 'put_price', 'call_put', 'buy_sell',
                                        "executed", 'remarks', 'lower_band', 'upper_band'])
    result = df_excel.append(new, sort=False)
#    print(result)

#    result_sort=result.sort_values(by=["Date", "Time"], ascending=[False, False])
#    result_sort.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)
    result.to_excel('C:\\NSE\\outputs\Masters.xlsx', index=False)

