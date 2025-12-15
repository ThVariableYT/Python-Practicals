import tkinter as tk
import tkinter.font as font
win=tk.Tk()
#win.resizable(0,0)
win.title("Label demo")
myFont=font.Font(family='Helvetica', size=20, weight='bold')
l1=tk.Label(win, text="FYBSc IT/CS", font=myFont,bg="red", fg="yellow")
l1.pack()
l2=tk.Label(win,text="SYBSc IT/CS", font=myFont,bg="blue",fg="yellow")
l2.pack(pady=10)
win.mainloop()
