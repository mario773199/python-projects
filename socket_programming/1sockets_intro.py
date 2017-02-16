#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #for tcp stream

print(s)

server = 'mariogsalazar.com'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server, port))
s.send(request.encode())
result = s.recv(1024)
#print(result)
while(len(result) > 0):
    print(result)
    result = s.recv(1024)

