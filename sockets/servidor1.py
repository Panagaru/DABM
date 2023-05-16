import socket

s = socket.socket()
port = 6000

s.bind(("localhost",port))

s.listen(5) # máximo 5 conexiones al servidor

while True:
    c,addr = s.accept()
    print("Conexión obtenida de ...", addr)
    c.send("Gracias por conectarse.".encode("utf-8"))
    c.close()
