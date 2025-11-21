
import tkinter as tk
window=tk.Tk()
window.title("GUI")
window.minsize(200,200)
label=tk.Label(window)
label.pack()
# creating a function called say_hi()
def say_hi():
    #tk.Label(window, text = "Hi").pack()
    label.config(text="Hi")
b=tk.Button(window,text ="Click Me!",command = say_hi)
b.pack()
# 'command' is executed when you click the button
# in the above case we're calling the function 'say hi'
window.mainloop()
