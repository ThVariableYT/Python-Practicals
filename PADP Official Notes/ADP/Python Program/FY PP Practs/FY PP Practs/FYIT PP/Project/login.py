from tkinter import *
root=Tk()
def checkLogin():
  window = Toplevel(root)
  window.title("Register")
  lblName=Label(window,text="Enter Name")
  lblName.pack()

  
lbl1=Label(root,text="Enter Username")
lbl2=Label(root,text="Enter Password")
ent1=Entry(root)
ent2=Entry(root)
lbl1.grid(row=0,column=0)
ent1.grid(row=0,column=1)
lbl2.grid(row=1,column=0)
ent2.grid(row=1,column=1)
b1=Button(root,text="Login",command=checkLogin)
b1.grid(row=2,column=1,sticky=N+S+E+W,padx=5,pady=5)

