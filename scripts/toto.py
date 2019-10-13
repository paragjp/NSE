import datetime as dt
## program to generate a simple toast notifier
from win10Toast import ToastNotifier
## instantiating the class
dt1 = dt.datetime.now().strftime("%Y""%m""%d")
dt2 = dt.datetime.now().strftime("%d-%b-%Y")

time1 = dt.datetime.now().strftime('%H:%M:%S')
time = time1.replace(':','')
n = ToastNotifier()
n.show_toast("Test Message","Notification body"+dt1+" "+time1,duration=15)