import tkinter as tk
win=tk.Tk()
win.minsize(400,300)
photo =tk.PhotoImage(file="download.png")
label =tk.Label(image=photo)
label.pack()
win.mainloop()
