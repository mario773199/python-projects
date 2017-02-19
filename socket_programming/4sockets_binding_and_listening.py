import socket
import sys

host = ' '
#listen on port 5555
port = 5555

#AF_INET for address family, SOCK_STREAM for internet and not EDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#if there is a binding error, then print the socket.error to the screen
try:
    s.bind((host, port))

except socket.error as e:
    print(str(e))

#queue of how many incoming connections before we turn away
s.listen(5)

conn, addr = s.accept()

print('conencted to: ' + addr[0] + ':' + str(addr[1]))

