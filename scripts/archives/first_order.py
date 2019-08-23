import pandas as pd

pd.set_option('display.max_columns', 25)

from read_baseline import read_baseline
from read_niftyoptions import read_niftyoptions

# reading baseline file
basestrike, basechange = read_baseline()

#getting bid price for CALL and PUT

callltp, putltp, calls_bid_price, puts_bid_price = read_niftyoptions(basestrike)

print(calls_bid_price, puts_bid_price)