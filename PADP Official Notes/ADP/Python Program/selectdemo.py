import mysql.connector
cnx = mysql.connector.MySQLConnection(user='root',password="scott", database='test')
print(cnx)