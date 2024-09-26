import tkinter
from tkinter import *

windows= tkinter.Tk()
windows.title("FIrst GUI window")
windows.minsize(600,300)
label=tkinter.Label(windows,text="Welcom to my Window",font=("Arial",24,"bold"))
label.pack()
windows.mainloop()