




import mysql.connector as mysql
conn = mysql.connect(user='root', password='scott',host='127.0.0.1')
c=conn.cursor()
c.execute("use fyit_b")
#c.execute("alter table employee add primary key(eno)")
c.execute("alter table employee drop primary key")
conn.commit()
conn.close()
