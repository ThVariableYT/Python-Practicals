import tkinter as tk
import tkinter.font as font
win=tk.Tk()
win.resizable(0,0)
win.minsize(300,200)
win.title("Label Demo")
myFont=font.Font(family='gg sans', size=20, weight='bold')
label=tk.Label(win, text="FYBSc IT/CS", font=myFont, bg="red", fg="yellow")
label.pack()
label2=tk.Label(win, text="SYBSc IT/CS", font=myFont, bg="blue", fg="yellow")
label2.pack()
win.mainloop()