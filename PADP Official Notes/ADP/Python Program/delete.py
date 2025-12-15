import mysql.connector as mysql
conn = mysql.connect(user='root', password='scott',host='127.0.0.1',
                     database='python')
c=conn.cursor()
c.execute("select * from customer")
print(c.fetchall())
#custid = rows[0][0]
#print(custid)
c.execute("delete from customer where custid=2")
conn.commit()
print(c.rowcount,"records deleted")
conn.close()
