import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

myServer = 'www.livingmindtech.com'
# This is my server to scan the available open port
# This method for scanning the open ports is very slow
# I should go with threaded port scanner for faster results


def port_scanner(port):
    try:
        s.connect((myServer, port))
        return True
    except:
        return False


for portNumber in range(1, 26):  # Scanning ports from 1 to 25
    if port_scanner(portNumber):
        print 'Port', portNumber, 'is Opened !'
    else:
        print 'Port', portNumber, 'is Closed !'
