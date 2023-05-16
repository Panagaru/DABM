import socket

s = socket.socket()
port = 6000

s.connect(("10.16.9.231",port))

while True:
    mensaje = input("#>")
    s.send(mensaje.encode("utf-8"))
    if mensaje == "salir":
        break

print("Adiós")
s.close()
