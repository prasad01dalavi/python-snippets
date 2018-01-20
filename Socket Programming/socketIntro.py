import socket
import time

socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Object:',socketObject

myWebSite = 'livingmindtech.com'  #This is my server
port = 80            #communication with server through port 80

myWebSiteIP = socket.gethostbyname(myWebSite)
print "My Website IP:",myWebSiteIP  #or I can ping livingmindtech.com to get the IP


request = "GET / HTTP/1.1\nHost: "+myWebSite+"\n\n"

socketObject.connect((myWebSite,port))  #Can also write: nsocketObject.connect(('43.255.154.112',port))
socketObject.send(request.encode())
result = socketObject.recv(1024)
print result

