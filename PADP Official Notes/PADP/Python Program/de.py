import mysql.connector as mysql
conn= mysql.connect(user="root", password="scott", host="localhost", database="customer")
mycursor=conn.cursor()
#mycursor.execute("create database Practical_3")
mycursor.execute("use Practical_3")
#mycursor.execute("create table bike(bikeid int primary key, bikename varchar(20), bikecost int, prdt date)")
mycursor.execute("insert into bike values(1,'Honda',70000,'2003-03-12')")
conn.commit()
conn.close()

