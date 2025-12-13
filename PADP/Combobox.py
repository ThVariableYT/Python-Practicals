from cProfile import label
import tkinter as tk
from tkinter import ttk
# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry ('500x250')

def fetchval():
    lbl.config (text='Month choosen'+monthchoosen.get ())

# label
tk.Label (window, text="Select the Month:", font=("Times New Roman", 10)).grid (column=0, row=5, padx=10, pady=25)

# Combobox creation
months=("Jan","Feb", "Mar")
n = tk.StringVar()
monthchoosen= ttk.Combobox(window, width = 27, textvariable=n, values=months)
monthchoosen.grid (column = 1, row = 5)
monthchoosen.current (0) #to display default month 
tk.Button (window, text="Submit", command=fetchval).grid(column=1, row=7) 
lbl=tk.Label (window, text="") 
lbl.grid(column=1,row=9)
window.mainloop()