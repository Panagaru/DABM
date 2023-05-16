import socket

s = socket.socket()
port = 6000

s.bind(("10.16.8.2",port))

s.listen(0) # máximo 5 conexiones al servidor

c,addr = s.accept()
print("Conexión obtenida de ...", addr)

while True:
    datos = c.recv(1024)
    if (datos.decode() == "salir"):
        break

    print("Recibí:", datos.decode())
    c.send(datos)

print("Adiós")
s.close()
