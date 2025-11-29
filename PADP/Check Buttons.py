from tkinter import *
win=Tk()

def btnclk():
    print(i.get())
    print(j.get())
    
i=StringVar()
j=StringVar()
chk1=Checkbutton(win,text="Option 1",variable=i,onvalue="Option 1 Checked",offvalue="Option 1 Unchecked")
chk1.pack()
chk1.deselect()
chk2=Checkbutton(win,text="Option 2",variable=j,onvalue="Option 2 Checked",offvalue="Option 2 Unchecked")
chk2.pack()
chk2.deselect()
btn=Button(win,text="Click Me!" ,command=btnclk)
btn.pack()
win.mainloop()