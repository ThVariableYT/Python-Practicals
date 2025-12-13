from operator import mul
import tkinter as tk
win=tk.Tk() 
win.minsize (200,200)

def add(): 
    e3.delete (0,10) 
    num1=int (el.get()) 
    num2=int (e2.get()) 
    ans=num1+num2
    e3.insert (0, ans)

def sub ():
    e3.delete (0,10)
    num1=int (el.get())
    num2=int (e2.get())
    ans=num1-num2
    e3.insert (0, ans)

cal=tk.Label(win, text="Calculator", font=("Arial", 30))
cal.grid(row=1, column=3)
ln1=tk.Label (win, text="Type Value 1:")
ln1.grid(row=2, column=2)
el=tk.Entry(win, width=20)
el.grid(row=2, column=3)

ln2=tk.Label (win, text="Type Value 2:")
ln2.grid(row=3, column=2) 
e2=tk.Entry(win, width=20) 
e2.grid(row=3, column=3)

f=tk.Frame (win)
b1=tk.Button(f, text="+", bg="green", fg="white", command=add)
b1.grid(row=1, column=1, padx=5)
b2=tk.Button(f, text="-", bg="green", fg="white", command=sub)
b2.grid(row=1, column=2, padx=5)
b3=tk.Button(f, text="*", bg="green", fg="white", command=lambda: e3.insert(0, mul(int(el.get()), int(e2.get()))))
b3.grid(row=1, column=3, padx=5)
b4=tk.Button(f, text="/", bg="green", fg="white", command=lambda: e3.insert(0, int(el.get()) / int(e2.get())))
b4.grid(row=1, column=4, padx=5)
f.grid(row=4, column= 3)

lans=tk.Label (win, text="Result:") 
lans.grid(row=5,column=2) 
e3=tk.Entry (win, width=20) 
e3.grid(row=5,column=3)
win.mainloop()