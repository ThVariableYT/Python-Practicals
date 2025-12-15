import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
from mysql.connector import errorcode
global roll
global name
def ok():
 try:
  db = mysql.connector.connect(host="localhost",user="root",password="scott",database="college")
  mycursor = db.cursor()
  messagebox.showinfo("Status", "Hello")
  roll=rollno.get()
  print(roll)
  name=stuname.get()
  print(name)
  sql = "insert into student(rollno,name) values (%s,%s)"
  val=(roll,name)
  mycursor.execute(sql, val)
  db.commit()
  print("inserted")
  messagebox.showinfo("Status", "Student Registered")
 except mysql.connector.Error as error :
    print("Failed to update record to database: {}".format(error))

window = tk.Tk()
window.title("Student Registration Page")
tk.Label(window, text = "Roll No : ",bg="red",fg="yellow").grid(row=0,column=0)
rollno=tk.Entry(window)
rollno.grid(row = 0, column = 4,padx=25)
tk.Label(window, text = "Name ",bg="green",fg ="yellow").grid(row=0,column=8,padx=10)
stuname=tk.Entry(window)
stuname.grid(row=0,column=9,padx=25,pady=25)
button3=tk.Button(window, text = "Click",bg="red",fg="yellow",command=ok).grid(row=0,column=12)
window.mainloop()
