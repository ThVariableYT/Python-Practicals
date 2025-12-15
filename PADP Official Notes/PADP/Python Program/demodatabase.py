import mysql.connector as mysql
conn=mysql.connect(user='root', password='scott', host='127.0.0.1')
c=conn.cursor()
#c.execute("create database fyit_b")
#print("Database created")
c.execute("show databases")
#print(c.fetchall())
for i in c:
    print(i)
conn.close()
