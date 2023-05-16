import socket

s = socket.socket()
port = 6000

s.connect(("localhost",port))

dato = s.recv(1024).decode()
print(dato)
