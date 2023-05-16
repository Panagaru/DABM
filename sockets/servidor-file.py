import socket

s = socket.socket()
port = 6000
s.bind(("localhost", port))
s.listen(1)

print("servidor escuchando ...")

while True:
    c,addr = s.accept()
    print("Conexión obtenida de ...", addr)
    data = c.recv(1024)
    print("Recibí:", data.decode())

    file = "sockets\ejemplo.csv"
    f = open(file,'rb') # rb = lectura modo binario
    l = f.read(1024)

    while (l):
        c.send(l)
        print("Enviando ...", l)
        l = f.read(1024)

    f.close()
    print("Archivo enviado")
    c.close()