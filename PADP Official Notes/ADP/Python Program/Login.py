from tkinter import *
import tkinter.messagebox
import mysql.connector


#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",password="scott",database="LoginDB")
cursordb = connectiondb.cursor()


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")

    global username_verification
    global password_verification
    Label(root2, text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_verification).pack()
    Label(root2, text="")


def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    #sql = "select * from user where username = %s and password = %s"
    sql="insert into user values(%s,%s)";
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    connectiondb.commit()
    print(cursordb.rowcount,"Record inserted successfully")
    #results = cursordb.fetchall()
    #if results:
     #   for i in results:
      #      logged()
       #     break
    #else:
     #   failed()

def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
    return

def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")
    Label(root,text='Welcome to Log In System', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",command=login).pack()
    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",command=Exit).pack()
    Label(root,text="").pack()  

main_display()
root.mainloop()
