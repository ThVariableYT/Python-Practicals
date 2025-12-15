from tkinter import *   
top = Tk()    
top.minsize(200,200)  

def fetchval():
    mylbl.config(text=spin.get())

#names=("imran","rajesh","pooja","prit") 
spin = Spinbox(top, from_=1,to=10 ,font=("Arial",20))
#for text write values=names
spin.pack()  
mybtn=Button(top,text="Submit",command=fetchval)
mybtn.pack()
mylbl=Label(top,text="")
mylbl.pack()
top.mainloop()
