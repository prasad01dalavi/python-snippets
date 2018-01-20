import socket
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientName = socket.gethostname()
print 'Client Name:',clientName 
clientIP = socket.gethostbyname(clientName)
print "Client IP:",clientIP 

port = 65535                         #communication with server through port 80
print 'Client Port:',port

address = ('localhost',port)
print 'Client is connected to',clientIP,',',port
print

while True:
    client = socket.socket()
    client.connect(('13.126.145.90',port)) #IP address of server
    client.send('Hello from Client!')
    serverData = client.recv(1024)
    print serverData
    time.sleep(5)
