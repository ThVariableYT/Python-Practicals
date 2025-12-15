import tkinter as tk
win=tk.Tk()
win.minsize(400,300)
photo =tk.PhotoImage(file="download.png")
label =tk.Label(image=photo)
label.pack()
button=tk.Button(win,text="OK",activebackground="red",activeforeground="yellow",bd=6)
button.pack()
win.mainloop()
