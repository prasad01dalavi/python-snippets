##import socket
##client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##ip = socket.gethostbyname('www.google.com')
##print 'Google IP:',ip
##port = 80 
##address = (ip,port)
##client.connect(address)
##print 'Connection Successful!'
##response = client.send('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
##print 'Response =',response
##print client.recv(1024)

#-------------End of client Programming--------------------#

#---------------Server Programming-------------------------#
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myIP = socket.gethostbyname(socket.gethostbyname())
port = 1234
address = (myIP, port)
server.bind(address)
server.listen(1)   #Only one client can listen

print "Started Listening..."
client,addr = server.accept()
print "Got a connection from",addr[0]
while True:
    data = client.recv(1024)
    print "Data from client:"data
    print "Processing the data..."
    if(data = "Hello Server"):
        client.send("Hello Client!")
        print "Processing has been completed!"
    elif(data == "Disconnect!"):
        client.send("GoodBye!")
        client.close()
        break
    else:
        client.send("Invalid Data!")
        print "Invalid Data!"
