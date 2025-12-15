from tkinter import *
root=Tk()
display=""
def cancel():
  global display
  display=""
  #display=display[:-1]
  ent1.config(text=display)
def evaluation(value):
  global display
  display+=value
  ent1.delete(0,END)
  ent1.insert(0,display)
  #ent1.config(display)
  #ent1.config(text=display)
def total():
  try:
    global display
    display=eval(str(display))
    ent1.delete(0,END)
    ent1.insert(0,display)
    #ent1.config(text=display)
    display=""
  except:
    display="error!"
    ent1.delete(0,END)
    ent1.insert(0,display)
    #ent1.config(text=display)
    display=""
str1=StringVar()
ent1=Entry(root,text="",textvariable=str1)
btnCancel=Button(root,text="C",command=lambda:cancel())
btnDiv=Button(root,text="/",command=lambda:evaluation("/"))
ent1.grid(row=0,column=0,columnspan=4,sticky=N+S+E+W)
btnCancel.grid(row=1,column=0,columnspan=3,sticky=N+S+E+W)
btnDiv.grid(row=1,column=3,sticky=N+S+E+W)

btnSeven=Button(root,text="7",command=lambda:evaluation("7"))
btnEight=Button(root,text="8",command=lambda:evaluation("8"))
btnNine=Button(root,text="9",command=lambda:evaluation("9"))
btnMul=Button(root,text="*",command=lambda:evaluation("*"))
btnSeven.grid(row=2,column=0,sticky=N+S+E+W)
btnEight.grid(row=2,column=1,sticky=N+S+E+W)
btnNine.grid(row=2,column=2,sticky=N+S+E+W)
btnMul.grid(row=2,column=3,sticky=N+S+E+W)

btnFour=Button(root,text="4",command=lambda:evaluation("4"))
btnFive=Button(root,text="5",command=lambda:evaluation("5"))
btnSix=Button(root,text="6",command=lambda:evaluation("6"))
btnMinus=Button(root,text="-",command=lambda:evaluation("-"))
btnFour.grid(row=3,column=0,sticky=N+S+E+W)
btnFive.grid(row=3,column=1,sticky=N+S+E+W)
btnSix.grid(row=3,column=2,sticky=N+S+E+W)
btnMinus.grid(row=3,column=3,sticky=N+S+E+W)

btnOne=Button(root,text="1",command=lambda:evaluation("1"))
btnTwo=Button(root,text="2",command=lambda:evaluation("2"))
btnThree=Button(root,text="3",command=lambda:evaluation("3"))
btnPlus=Button(root,text="+",command=lambda:evaluation("+"))
btnOne.grid(row=4,column=0,sticky=N+S+E+W)
btnTwo.grid(row=4,column=1,sticky=N+S+E+W)
btnThree.grid(row=4,column=2,sticky=N+S+E+W)
btnPlus.grid(row=4,column=3,sticky=N+S+E+W)

btnZero=Button(root,text="0",command=lambda:evaluation("0"))
btnPeriod=Button(root,text=".",command=lambda:evaluation("."))
btnEqual=Button(root,text="=",command=lambda:total())
btnZero.grid(row=5,column=0,columnspan="2",sticky=N+S+E+W)
btnPeriod.grid(row=5,column=2,sticky=N+S+E+W)
btnEqual.grid(row=5,column=3,sticky=N+S+E+W)















