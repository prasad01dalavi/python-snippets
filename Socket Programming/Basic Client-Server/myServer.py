import socket
import time

#Create a socket at server to receive data from client through that socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'My Server Name:',socket.gethostname()

myServerIP = socket.gethostbyname(socket.gethostname())
print "My Server IP:",myServerIP  

port = 1234
print 'My Port for Communication:',port

##address = ('localhost',port)
address = ('localhost',port)
print 'My complete address:',address

server.bind(address)
server.listen(1)
print 'My Server has started listening to client...'

##client,addr = server.accept()
##print 'Got a connection from',addr[0],':',addr[1]

while True:
    client,addr = server.accept()    #server socket is accepting the data from the client
    print addr
    data = client.recv(1024)
    print 'Received data at the Server:',data
    client.send('Reply from server')
    
    
