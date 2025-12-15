from tkinter import*
root=Tk()
def var_states():
  print("Hobby1:%d,\n Hobby2:%d"%(var1.get(),var2.get()))
var1=IntVar()
c1=Checkbutton(root,text="Hobby1",variable=var1)
var2=IntVar()
c2=Checkbutton(root,text="Hobby2",variable=var2)
b=Button(root,text="Show",command=var_states)
c1.pack(side=LEFT)
c2.pack(side=LEFT)
b.pack(side=LEFT)
        
