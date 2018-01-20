import socket
import sys

host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))

except socket.error as e:
    print str(e)

s.listen(5)

conn,addr = s.accept()

print 'Connected to:',addr[0],':',addr[1]
