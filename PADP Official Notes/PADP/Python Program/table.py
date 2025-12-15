import tkinter as tk
import tkinter.font as font
win = tk.Tk()
win.minsize(300,200)
def tablefinder():
        enter = 0
        limit = 0
        m = 0
    
#                 # enter = int(enter)
#                 limit = enter*10+1
                m=1
            for i in range(enter,limit,enter):
                            tk.Label(win,enter , " × " ,m, " = " , i)
                            m += 1
            enter = tk.Entry(win,bd=10)
            enter.place(x=0,y=50)
            tk.Button(win,text="Calculate",command=tablefinder).pack()
