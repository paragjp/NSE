import os
import pandas as pd
import os

import pandas as pd

pd.set_option('display.max_columns', 21)

#reading baseline file for reading strike price and % of change
def read_baseline() :
    filename = "C:\\NSE\\inputs\\newbasefile.txt"
    if os.path.isfile(filename):
        f = open("C:\\NSE\\inputs\\newbasefile.txt", "r")
    else:
        f = open("C:\\NSE\\inputs\\basefile.txt", "r")

    l=f.readlines()
#   reading original strike price
#    f_base_strike = float(l[2])
    f_base_strike = float(l[4])
    f_base_change = float(l[3])
    f_check_strike=0
#    if f_check_strike == (f_base_strike%50) :
    f.close()
#    else :
#       raise ValueError("Base Strike Price Not divisible by 50 :", f_base_strike)

    return (f_base_strike, f_base_change)
