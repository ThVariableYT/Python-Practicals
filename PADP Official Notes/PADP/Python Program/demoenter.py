import tkinter as tk

top = tk.Tk()
top.minsize(500,500)
L1 = tk.Label(top, text="User Name")
L1.pack()
E1 = tk.Entry(top, bd =5)
E1.pack()
L2=tk.Label(top)
L2.pack(side="left")

def displayname():
    username=E1.get()
    L2.config(text=username)
    #L2=tk.Label(top, text=username)
    #L2.pack(side="left")

def removename():
    L2.config(text="")
    
b1=tk.Button(top,text="Submit" ,command=displayname)
b1.pack()

b2=tk.Button(top,text="Clear" ,command=removename)
b2.pack()
top.mainloop()
