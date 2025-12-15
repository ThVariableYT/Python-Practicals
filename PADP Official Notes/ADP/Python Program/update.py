import mysql.connector as mysql
conn = mysql.connect(user='root', password='scott',host='127.0.0.1',
                     database='python')
c=conn.cursor()
c.execute("alter table customer add occupation varchar(30)")
c.execute("describe customer")
#c.execute("alter table customer add primary key(custid)")
#c.execute("update customer set phoneno=64586686 where custid=2")
#c.execute("update cust set savings=20000")
#conn.commit()
#.execute("select * from customer")
print(c.fetchall())
conn.close()
