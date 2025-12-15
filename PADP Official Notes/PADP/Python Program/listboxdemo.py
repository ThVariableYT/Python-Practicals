from tkinter import *
top = Tk()
def click():
    #x=Lb1.get(Lb1.curselection())
    x=[Lb1.get(i) for i in Lb1.curselection()]
    output.config(text=x)

lbl=Label(top,text="Programming Languages")
lbl.pack()
Lb1 = Listbox(top, activestyle="dotbox", selectmode="multiple")
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()
b1 = Button(top, text='print selection', width=15, height=2, command=click)
b1.pack()
output=Label(top)
output.pack()
top.mainloop()
