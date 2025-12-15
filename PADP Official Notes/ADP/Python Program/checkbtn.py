from tkinter import *
win=Tk()

def btnclk():
    print(i.get())
    print(j.get())

i=StringVar()
j=StringVar()
chk1=Checkbutton(win,text="Option1",variable=i,onvalue="Option1 checked",
                 offvalue="Option1 unchecked")
chk1.pack()
chk1.deselect()
chk2=Checkbutton(win,text="Option2",variable=j,onvalue="Option2 checked",
                 offvalue="Option2 unchecked")
chk2.pack()
chk2.deselect()
btn=Button(win,text="Click me!" ,command=btnclk)
btn.pack()
win.mainloop()
