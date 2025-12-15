from tkinter import *
import sys
root=Tk()
root.minsize(200,200)
def singleclk(event):
    print("Button-1 single click")
    #btn.configure(bg="red")
def doubleclk(event):
    print("Button double click exit")
    sys.exit()
    #btn.configure(bg="yellow")
btn=Button(root,text="Mouse click event", cursor="cross", relief=GROOVE)
btn.pack()
btn.bind('<Button-1>',singleclk)
btn.bind('<Double-Button-1>',doubleclk)
#btn.bind('<Enter>',singleclk)
#btn.bind('<Leave>',doubleclk)
root.mainloop()
