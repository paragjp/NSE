import datetime as dt
def get_datetime() :
    f_dt = dt.datetime.now().strftime("%d-%b-%Y")
    f_time = dt.datetime.now().strftime("%H:%M:%S")
    return(f_dt,f_time)