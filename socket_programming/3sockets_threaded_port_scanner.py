#!/usr/bin/python3
import socket
import threading
from Queue import Queue

print_lock = threading.Lock()

target = 'mariogsalazar.com'

def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #for tcp stream
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port,'is open!')
        con.close()
    except:
        pass

#Threading stuff that I don't know yet :>) -----------
def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,101):
    q.put(worker)

q.join()

