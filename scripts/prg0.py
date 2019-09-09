# Create blank Masterfile for recording ALL changes after particular duration
import os
import pandas as pd

filename='C:\\NSE\\outputs\Masters.xlsx'
if os.path.isfile(filename):
    os.remove(filename)

filename = "C:\\NSE\\OUTPUTS\\Masters.xlsx"
if os.path.isfile(filename):
    os.remove(filename)

masterdf = pd.DataFrame(columns=['date', 'time', 'script','base_strike','ltp',
                                 'base_change', 'current_change', 'qty',
                                 'call_put','buy_sell','call_price',
                                 'put_price', 'total_premium', 'cumm_premium', 'amt', 'executed', 'remarks',
                                 'kount', 'arrived_strike','lower_band','upper_band' ])
masterdf.to_excel("C:\\NSE\\outputs\Masters.xlsx", startrow=0, index=False)


filename = "C:\\NSE\\inputs\\newbasefile.txt"
if os.path.isfile(filename):
    os.remove(filename)
