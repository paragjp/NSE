import datetime as dt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Information")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="OK", command = popup.destroy)
    B1.pack()
    popup.mainloop()

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)


msg="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
popupmsg(msg)

