def myround(f_basestrike, base):
    f_order_strike = f_basestrike
    f_base = base
    return(f_base * round(f_order_strike/f_base))