import mysql.connector 
conn=mysql.connector.connect(user='root',password='scott',host='localhost',database="python")


mycursor=conn.cursor()
mycursor.execute("create table emp(id int(5),name varchar(20))")
print("Table created")
mycursor.execute("show tables")
print(mycursor.fetchall())
conn.close()
