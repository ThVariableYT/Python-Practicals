from tkinter import*
root=Tk()
def display():
  if (ent1.get()==""):
    print("Please Enter Name")
  else: 
      print("Name:"+ent1.get())
      ent1.focus()
l1=Label(root,text="Enter Name")

frame=Frame(root)
l1.grid(row=0,column=0)
frame.grid(row=0,column=1)

ent1=Entry(frame)
b=Button(frame,text="Submit",command=display)
ent1.grid(row=0,column=0)
b.grid(row=0,column=1)
