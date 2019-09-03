import datetime as dt

from dateutil.relativedelta import relativedelta, TH


def get_datetime(param) :
    f_param = param
    if f_param == 'A':
        f_dt = dt.datetime.now().strftime("%d-%b-%Y")
        f_time = dt.datetime.now().strftime("%H%M%S")

# if 4 <= day <= 20 or 24 <= day <= 30:
    #     suffix = "th"
    # else:
    #     suffix = ["st", "nd", "rd"][day % 10 - 1]

# Get last Thursday of a month
    end_of_month = dt.datetime.today() + relativedelta(day=31)
    f_week_thursday = (dt.datetime.today() + relativedelta(weekday=TH(1)))
    f_last_thursday = (end_of_month + relativedelta(weekday=TH(-1))).strftime('%d')
    f_time = dt.datetime.now().strftime("%H:%M:%S")
    f_abr_month = dt.datetime.now().strftime("%b").upper()


# Get date and time for writing orders files

    f_dt_yyyymmd=dt.datetime.now().strftime("%Y""%m""%d")
    f_time_hh24mise=dt.datetime.now().strftime('%H%M%S')

    return (f_dt, f_time, f_week_thursday, f_last_thursday, f_abr_month,f_dt_yyyymmd,f_time_hh24mise)