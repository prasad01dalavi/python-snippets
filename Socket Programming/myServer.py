import socket

# Create a socket at server to receive data from client through that socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET => IPv4 Protocol
# socket.SOCK_STREAM => TCP Protocol

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# This will allow windows to use the same port when we re-run the code

print 'My Server Name:', socket.gethostname()
# Computer Host Machine name

myServerIP = socket.gethostbyname(socket.gethostname())
print "My Server IP:", myServerIP  # IP address of the server

port = 1234
print 'My Port for Communication:', port

address = ('192.168.0.100', port)
# Declare server address to which client will communicate
print 'Server address:', address    # Server address: ('192.168.0.100', 1234)
# Note: address = ('', port) specifies that the socket is reachable
# by any address the machine happens to have.

server.bind(address)
# Bind the server to that address
# Bind it tightly !!

server.listen(1)  # Server can accept the connection from 1 client

while True:
    client, addr = server.accept()
    print client  # <socket._socketobject object at 0x0000000001E44938>
    print addr    # ('192.168.0.100', 52215)
    # where first element of tuple is IP of client and 2nd element is port

    data = client.recv(1024)   # Take 1024 bytes from client data
    print 'Received data at the Server:', data
    client.send('Reply from server')
