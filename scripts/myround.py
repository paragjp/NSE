import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', 51)

def myround(x, base=5):
    return int(base * round(float(x) / base))

