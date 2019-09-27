import threading
from disp_message import disp_message

msg =" This is a test message"
msgtype = 1

t1 = threading.Thread(target=disp_message, args=(msg,msgtype,))
t1.start()
t1.join()

for i in range(100000):
    print(i)
disp_message(msg,msgtype)
print("Done!")