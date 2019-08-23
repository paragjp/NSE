import pandas as pd
pd.set_option('display.max_columns', 21)


def calculate_change(basestrike, current_nifty):
    if  float(basestrike) >= float(current_nifty) :
       f_current_change = round((float(current_nifty) *100 / basestrike ) - 100, 2)
    else :
        f_current_change = round((100 - float( basestrike * 100)/current_nifty), 2)

    return(f_current_change)