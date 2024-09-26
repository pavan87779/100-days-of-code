import tkinter
from tkinter import *
root=tkinter.Tk()
root.title("Demo")
root.minsize(400,300)
mylabel=tkinter.Label(text="New Text",font=("Arial",24,"bold"))
mylabel.pack()
def button1():
    print("clicked me")
    new_text=input.get()
    mylabel.config(text=new_text)

button=tkinter.Button(text="Click Me",command= button1)
button.pack()
input=Entry(width=15)
input.pack()
print(input.get())




root.mainloop()