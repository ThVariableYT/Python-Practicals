


import mysql.connector as mysql
conn= mysql.connect(username="root", password="scott",
                           host="127.0.0.1", database="python")
c=conn.cursor()
c.execute("select * from customer where phoneno like '%58%'")
print(c.fetchall())
conn.close()
