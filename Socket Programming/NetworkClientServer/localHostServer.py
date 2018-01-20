# first of all import the socket library
import socket               

# next create a socket object
serverSocket = socket.socket()  #Socket at server side

serverName = 'localhost'
print 'Server Name:',serverName
serverIP = socket.gethostbyname(serverName)
print 'Server IP:',serverIP

port = 21421                    #Give any random port
print 'Server Port:',port
#Next bind to the port
#coming from other computers on the network

serverSocket.bind(('localhost', port))   #Bind the IP of local host to the server      
print "Server is binded to",serverIP,',',port

# put the socket into listening mode
serverSocket.listen(5)     
print "Server is Listening..."            
print

while True:
   # Establish connection with client.
   client, addr = serverSocket.accept() #addr argument is a server address (127.0.0.1)
   #clinet is an object to receive the data
   clientData = client.recv(1024)
   print clientData

   # send a reply message to the client. 
   client.send('Hello from Server!')
   # Close the connection with the client
   client.close()   
