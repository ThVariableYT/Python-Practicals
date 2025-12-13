from tkinter import * #import tkinter as tk
top=Tk()
top.minsize(200, 200)

def fetchval():
    mylbl.config(text=spin.get())

names=("imran","rajesh","pooja", "prit")
spin = Spinbox(top, values=names, font=("Arial", 20))
#for text write values=names
spin.pack()
mybtn=Button (top, text="Submit", command=fetchval)
mybtn.pack()
mylbl=Label (top,text="")
mylbl.pack()
top.mainloop()