from tkinter import *
from tkinter import messagebox

def disp_message(msg,msgtype):
    top = Tk()
    top.withdraw()
    if msgtype==1:
        messagebox.showwarning("Warning",msg)
    elif msgtype==2:
         messagebox.showinfo("information",msg)
    else:
        messagebox.showerror("Error",msg)