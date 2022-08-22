#-*- coding: UTF-8 -*- 

import socket
 

try:

    s = socket.socket()
     

    s.connect(('127.0.0.1', 7000))

except:
   input("hgh:")



s.send('{"protocol":123,"username":true,"password":"123456"}|#|'.encode())
print (s.recv(1024))



print (s.recv(1024))

input()




