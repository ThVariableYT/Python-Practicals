import tkinter as tk
top = tk.Tk()#window
top.minsize(200,200)
top.resizable(0,0)
B = tk.Button(top, text ="Hello", activebackground="red",activeforeground="blue",bd=5)
B.pack( side="right" )
top.mainloop()
