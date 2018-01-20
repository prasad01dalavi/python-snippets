import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = 'livingmindtech.com'

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print ('Port',port,'is open!')            
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        protscan(worker)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,101):  #checking first 100 ports
    q.put(worker)

q.join()

    
    
