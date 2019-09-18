import os
import pandas as pd
pd.set_option('display.max_columns', 51)
import numpy as np

#reading baseline file for reading strike price and % of change
def read_baseline() :
    r1 = pd.read_excel('C:\\NSE\\inputs\\basefile.xlsx')
    r1.columns = \
            r1.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    for index, row in r1.iterrows():
        read1=[]
        r_script = row[0]
        r_strike = row[1]
        r_qty = row[2]
        r_diff = row[3]
        r_expirydt = row[4]
        r_fo_script= row[5]
        r_lot_size = row[6]
        r_orig_strike = row[7]
        r_round = row[8]
        read1 = [r_script, r_strike, r_qty, r_diff, r_expirydt, r_fo_script, r_lot_size, r_orig_strike,r_round]
        if len(read1) == 0 :
            print("Reading Baseline File is complted")
            sys.exit("program completed")
    return(read1)
