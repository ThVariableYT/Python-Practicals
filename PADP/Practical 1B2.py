import tkinter as tk
from tkinter import messagebox

def register():
    user_id = entry_id.get()
    name = entry_name.get()
    gender = gender_var.get()
    address = entry_address.get()
    contact = entry_contact.get()

    # You can add validation or saving to file/database here
    info = (
        f"ID: {user_id}\n"
        f"Name: {name}\n"
        f"Gender: {gender}\n"
        f"Address: {address}\n"
        f"Contact: {contact}"
    )
    messagebox.showinfo("Registration Details", info)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Registration Form")

# Main frame (for a neat border-like look)
frame = tk.Frame(root, padx=20, pady=20, relief=tk.GROOVE, borderwidth=2)
frame.pack(padx=10, pady=10)

# Title label
title_label = tk.Label(frame, text="Registration Form", font=("Arial", 12, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# ID
label_id = tk.Label(frame, text="ID")
label_id.grid(row=1, column=0, sticky="w", pady=2)
entry_id = tk.Entry(frame, width=30)
entry_id.grid(row=1, column=1, pady=2)

# Name
label_name = tk.Label(frame, text="Name")
label_name.grid(row=2, column=0, sticky="w", pady=2)
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=2, column=1, pady=2)

# Gender
label_gender = tk.Label(frame, text="Gender")
label_gender.grid(row=3, column=0, sticky="w", pady=2)

gender_var = tk.StringVar(value="Male")
radio_male = tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male")
radio_female = tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female")
radio_male.grid(row=3, column=1, sticky="w", pady=2)
radio_female.grid(row=3, column=1, sticky="w", padx=70, pady=2)

# Address
label_address = tk.Label(frame, text="Address")
label_address.grid(row=4, column=0, sticky="w", pady=2)
entry_address = tk.Entry(frame, width=30)
entry_address.grid(row=4, column=1, pady=2)

# Contact
label_contact = tk.Label(frame, text="Contact")
label_contact.grid(row=5, column=0, sticky="w", pady=2)
entry_contact = tk.Entry(frame, width=30)
entry_contact.grid(row=5, column=1, pady=2)

# Buttons
button_exit = tk.Button(frame, text="Exit", width=10, command=exit_app)
button_register = tk.Button(frame, text="Register", width=10, command=register)
button_exit.grid(row=6, column=0, pady=(10, 0))
button_register.grid(row=6, column=1, pady=(10, 0), sticky="e")

root.mainloop()
