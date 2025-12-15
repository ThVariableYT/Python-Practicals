from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("150x100")
def hello():
  message=e1.get();
  messagebox.showinfo("Information", 'Welcome, {}'.format(message))
  '''messagebox.showinfo("Information","Hello world")#1
  messagebox.showwarning("Warning", "Hello World") #2
  messagebox.showerror("Error", "Hello World") #3
  messagebox.askquestion("Question", "Are you sure?") #4
  messagebox.askyesno("Say Hello", "Hello world") #5
  messagebox.askretrycancel("Retry", "Want to retry") #6
  messagebox.askyesnocancel("Ask", "Are you sure?") #7 extra
  messagebox.askokcancel("Confirm","Do you want to confirm?")#8'''
e1=Entry(top,width=20)
e1.place(x=25,y=30)
B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()
