import tkinter as tk
#from tkinter import messagebox

window = tk.Tk()
window.title("GUI")
window.minsize(200,200)
# creating a function called say_hi()
def say_hi():
    tk.Label(window, text = "Hi").pack()
    #messagebox.showinfo("HI","Welcome,vishakha")

tk.Button(window, text = "Click Me!", command = say_hi).pack()
# 'command' is executed when you click the button
# in this above case we're calling the function 'say_hi'.
window.mainloop()
