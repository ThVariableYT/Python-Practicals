from tkinter import *
from tkinter import Canvas
win=Tk()
win.title("Canvas Shapes")
canvas=Canvas(win)

canvas.create_oval(60, 60, 120, 120, outline="#f11", fill="green", width=4)
canvas.create_oval(110, 10, 210, 80, outline="#f11",fill="#1f1", width=2)
canvas.create_rectangle(230, 10, 290, 60, outline="#f11", fill="#1f1", width=2)
canvas.create_arc(30, 200, 90, 100, start=0,extent=210, outline="#f11", fill="#1f1", width=2)
points = [150, 100, 200, 120, 240, 180, 210,200, 150, 150, 100, 200]
canvas.create_polygon(points, outline='#f11', fill='#1f1', width=2)
canvas.create_line(50,230,70,200,width=2,fill="green")
canvas.create_line(50,230,80,230,width=2,fill="green")
canvas.create_line(70,200,80,230,width=2,fill="green")
canvas.pack(fill=BOTH, expand=True)
win.mainloop()
