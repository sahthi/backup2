#!/usr/bin/python
from socket import *
HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)
tcpclisock=socket(AF_INET,SOCK_STREAM)
tcpclisock.connect(ADDR)
while 1:
     data=raw_input(">")
     if not data:
          break
     tcpclisock.send(data)
     data=tcpclisock.recv(1024)
     if not data:
          break
     print data
tcpclisock.close()

     
	

