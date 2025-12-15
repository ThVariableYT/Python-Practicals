import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.minsize(300,300)
image = Image.open("download.jpg")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()
root.mainloop()
