def calculate_change(f_basestrike, f_current_nifty, ):
    if f_basestrike >= f_current_nifty:
       f_current_change = round(float(f_basestrike) - float(f_current_nifty),2)
    else:
        f_current_change = round( float(f_current_nifty)- float(f_basestrike) , 2)
    return(f_current_change)