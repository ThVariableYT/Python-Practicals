import tkinter as tk
from tkinter import messagebox

def add_appointment():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    location = entry_location.get()
    time = entry_time.get()
    phone = entry_phone.get()

    # Basic check: require at least name and phone
    if not name or not phone:
        messagebox.showwarning("Missing data",
                               "Please enter at least patient's name and phone number.")
        return

    messagebox.showinfo(
        "Success",
        f"Appointment for {name} has been created"
    )

# Main window
root = tk.Tk()
root.title("ABC Hospital Appointments")
root.geometry("900x400")

# Background color
root.configure(bg="#8fd38f")   # light green

# Title label
title_lbl = tk.Label(
    root,
    text="ABC Hospital Appointments",
    font=("Helvetica", 32, "bold"),
    bg="#8fd38f"
)
title_lbl.grid(row=0, column=0, columnspan=2, pady=(20, 30), padx=20, sticky="w")

label_font = ("Helvetica", 18, "bold")
entry_font = ("Helvetica", 16)

# Patient's Name
lbl_name = tk.Label(root, text="Patient's Name", font=label_font, bg="#8fd38f")
lbl_name.grid(row=1, column=0, sticky="w", padx=20, pady=5)
entry_name = tk.Entry(root, width=30, font=entry_font)
entry_name.grid(row=1, column=1, pady=5, padx=10, sticky="w")

# Age
lbl_age = tk.Label(root, text="Age", font=label_font, bg="#8fd38f")
lbl_age.grid(row=2, column=0, sticky="w", padx=20, pady=5)
entry_age = tk.Entry(root, width=30, font=entry_font)
entry_age.grid(row=2, column=1, pady=5, padx=10, sticky="w")

# Gender
lbl_gender = tk.Label(root, text="Gender", font=label_font, bg="#8fd38f")
lbl_gender.grid(row=3, column=0, sticky="w", padx=20, pady=5)
entry_gender = tk.Entry(root, width=30, font=entry_font)
entry_gender.grid(row=3, column=1, pady=5, padx=10, sticky="w")

# Location
lbl_location = tk.Label(root, text="Location", font=label_font, bg="#8fd38f")
lbl_location.grid(row=4, column=0, sticky="w", padx=20, pady=5)
entry_location = tk.Entry(root, width=30, font=entry_font)
entry_location.grid(row=4, column=1, pady=5, padx=10, sticky="w")

# Appointment Time
lbl_time = tk.Label(root, text="Appointment Time", font=label_font, bg="#8fd38f")
lbl_time.grid(row=5, column=0, sticky="w", padx=20, pady=5)
entry_time = tk.Entry(root, width=30, font=entry_font)
entry_time.grid(row=5, column=1, pady=5, padx=10, sticky="w")

# Phone Number
lbl_phone = tk.Label(root, text="Phone Number", font=label_font, bg="#8fd38f")
lbl_phone.grid(row=6, column=0, sticky="w", padx=20, pady=5)
entry_phone = tk.Entry(root, width=30, font=entry_font)
entry_phone.grid(row=6, column=1, pady=5, padx=10, sticky="w")

# Add Appointment button
btn_add = tk.Button(
    root,
    text="Add Appointment",
    font=("Helvetica", 16, "bold"),
    bg="#337ab7",
    fg="white",
    width=20,
    command=add_appointment
)
btn_add.grid(row=7, column=0, columnspan=2, pady=30)

root.mainloop()
