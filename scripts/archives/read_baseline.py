import pandas as pd

pd.set_option('display.max_columns', 21)

#reading baseline file for reading strike price and % of change
def read_baseline() :

    f = open("C:\\NSE\\inputs\\basefile.txt", "r")
    f_base_strike = int(f.readline())
    f_check_strike=0
    if f_check_strike == (f_base_strike%50) :
       f_base_change = int(f.readline())
       f.close()
    else :
       raise ValueError("Base Strike Price Not divisible by 50 :", f_base_strike)

    return (f_base_strike, f_base_change)
