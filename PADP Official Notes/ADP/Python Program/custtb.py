import mysql.connector as mysql
conn=mysql.connect(user='root',password='scott',host='localhost',database='python')
c=conn.cursor()
#c.execute("create table customer(custid int(9) primary key, custname varchar(30), phoneno int(10))")
#print("Customer table created")
c.execute("describe customer")
print(c.fetchall())
conn.close()
