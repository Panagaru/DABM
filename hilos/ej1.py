import threading
#como se crea un hilo
def worker():
    print("Hilo ejecutandose")
    return

#lista de hilos

threads = []

for i in range(0,5):
    t = threading.Thread(target=worker) #instrucciones que s evan a ejecutar en ese hilo
    threads.append(t)
    t.start() #como se inicia un hilo
