import socket
s = socket.socket()
port = 6000

s.connect(("localhost", port))
s.send("Hola server !!!".encode('utf-8'))

with open('recibido.csv','wb') as f:
    print("Archivo abierto")

    while True:
        print("Recibido datos ...")
        data = s.recv(1024)
        print("Data=", data)
        if not data:
            break

        f.write(data)

print("Archivo recibido")
s.close()