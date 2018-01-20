import socket
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientName = socket.gethostname()
print 'Client Name:', clientName
clientIP = socket.gethostbyname(clientName)
print "Client IP:", clientIP

port = 50545  # communication with server through port 80
# print 'Client Port:',port


while True:
    client = socket.socket()
    print 'Connecting to server...'
    client.connect(('148.72.232.160', port))  # IP address of server
    print 'Connected to server !'
    client.send('Hello from local Client!')
# serverData = client.recv(1024)
# print serverData
    time.sleep(5)
