import tkinter as tk
from tkinter import messagebox

def add_appointment():
    name = e_name.get()
    if not name or not e_phone.get():
        messagebox.showwarning("Missing data",
                               "Enter patient's name and phone number.")
        return
    messagebox.showinfo("Success",
                        f"Appointment for {name} has been created")

root = tk.Tk()
root.title("ABC Hospital Appointments")
root.configure(bg="#8fd38f")

# Title
tk.Label(root, text="ABC Hospital Appointments",
         font=("Helvetica", 28, "bold"), bg="#8fd38f").grid(
    row=0, column=0, columnspan=2, pady=20, padx=20, sticky="w"
)

labels = [
    "Patient's Name", "Age", "Gender",
    "Location", "Appointment Time", "Phone Number"
]

entries = []
for i, text in enumerate(labels, start=1):
    tk.Label(root, text=text, font=("Helvetica", 16, "bold"),
             bg="#8fd38f").grid(row=i, column=0, padx=20, pady=5, sticky="w")
    ent = tk.Entry(root, font=("Helvetica", 14), width=30)
    ent.grid(row=i, column=1, padx=10, pady=5, sticky="w")
    entries.append(ent)

e_name, e_age, e_gender, e_location, e_time, e_phone = entries

tk.Button(root, text="Add Appointment", font=("Helvetica", 14, "bold"),
          bg="#337ab7", fg="white", width=20,
          command=add_appointment).grid(
    row=7, column=0, columnspan=2, pady=25
)

root.mainloop()
