import socket
import time

name = socket.gethostname()
print 'Client Name:', name    # Computer Name

clientIP = socket.gethostbyname(name)
print 'Client IP Address:', clientIP   # Private(Local) IP Address of the PC

while True:
    client = socket.socket()

    client.connect(('192.168.0.100', 1234))
    # IP address of server and the port on client will connect to server
    client.send('Hello from Client!')  # Client will send the data to server
    print 'Data sent!'

    serverData = client.recv(1024)
    # Client can also receive the data from server (1025 bytes of data)
    print 'Data from server', serverData
    time.sleep(5)

