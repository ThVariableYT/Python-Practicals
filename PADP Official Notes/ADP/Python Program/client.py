        # This is client.py file
import socket
# create a socket object
s = socket.socket() 
# get local machine name
host = socket.gethostname()
print(host)
port = 12345
# connection to hostname on the port.
s.connect((host, port))                               
# Receive no more than 1024 bytes
msg = s.recv(1024)                                     
s.close()
print (msg.decode('ascii'))


