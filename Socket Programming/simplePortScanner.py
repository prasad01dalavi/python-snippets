import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

myServer = 'livingmindtech.com'  #This is my server

def portScanner(port):
    try:
        s.connect((myServer,port))
        return True
    except:
        return False

for portNumber in range(1,26):  #Scanning ports from 1 to 25
    if portScanner(portNumber):
        print 'Port',portNumber,'is Opened !'
    else:
        print 'Port',portNumber,'is Closed !'

