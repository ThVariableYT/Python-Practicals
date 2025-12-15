import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   conn = mysql.connector.connect(host='localhost',  database='bank',
                                  user='root', password='scott')

   conn.autocommit = True
   cursor = conn.cursor()
   cursor.execute("select * from account_a where id=1")
   a=cursor.fetchall()
   for res in a:
      bal=res[1]
   if bal==0:
      print("check the balance")
   elif bal>0:
   # withdraw from account A 
      cursor.execute("Update account_A set balance = balance-500 where id = 1")
   # Deposit to account B 
      cursor.execute("Update account_B set balance = balance+500 where id = 3")
      print ("Record Updated successfully ")
   #Commit your changes
      #conn.commit()
except mysql.connector.Error as error :
    print("Failed to update record to database rollback: {}".format(error))
    #reverting changes because of exception
    conn.rollback()
finally:
    #closing database connection.
    if(conn.is_connected()):
        #cursor.close()
        conn.close()
        print("connection is closed")



