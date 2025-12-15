#This is server.py file
import socket                                    
# get local machine name
host = socket.gethostname()
print(host)
port = 12345
# create a socket object
serversocket = socket.socket() 
# bind to the port
serversocket.bind((host, port))                                  
# queue up to 5 requests
serversocket.listen(5)                                           
while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      
   print("Got a connection from %s" % str(addr))
   msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
clientsocket.close()
