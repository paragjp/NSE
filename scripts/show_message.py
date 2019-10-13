import tkinter as tk

def show_message(type1, msg1, msg2, msg3):
    root = tk.Tk()
    if type1 == "L":
        h1 = "LOSS Notifications"
        tk.Label(root, text=msg1, fg="red", bg="yellow", font="Verdana 14 bold").pack()
        tk.Label(root, text=msg2, fg="red", bg="yellow", font="Verdana 14 bold").pack()
        tk.Label(root, text=msg3, fg="black", bg="orange", font="Verdana 14 bold").pack()
    elif type1 == "P":
        h1 = "Profit Notifications"
        tk.Label(root, text=msg1, fg="yellow", bg="blue", font="Verdana 14 bold").pack()
        tk.Label(root, text=msg2, fg="yellow", bg="blue", font="Verdana 14 bold").pack()
        tk.Label(root, text=msg3, fg="white", bg="green", font="Verdana 14 bold").pack()
    elif type1 == "N":
        h1 = "No Loss No Profit Notifications"
        tk.Label(root, text=msg1, fg="black", bg="white", font="Verdana 14 bold").pack()
        tk.Label(root, text=msg2, fg="black", bg="white", font="Verdana 14 bold").pack()
        tk.Label(root, text=msg3, fg="black", bg="white", font="Verdana 14 bold").pack()
    root.title(h1)
    root.bell()
    root.update()
#    tk.mainloop()
